"""Génère docs/Guide_Prompts_QA_Workflow.pdf à partir des prompts du dépôt.

Usage : pip install reportlab && python scripts/build_pdf.py
"""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, Preformatted, KeepTogether, NextPageTemplate)
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon

OUT = sys.argv[1] if len(sys.argv) > 1 else "docs/Guide_Prompts_QA_Workflow.pdf"
W, H = A4
INK = colors.HexColor("#0f172a"); MUTED = colors.HexColor("#475569")
ACC = colors.HexColor("#d97757"); NAVY = colors.HexColor("#1e1b4b")
BLUE = colors.HexColor("#2563eb"); GREEN = colors.HexColor("#16a34a"); PURPLE = colors.HexColor("#7c3aed")
BOX = colors.HexColor("#f1f5f9"); LINE = colors.HexColor("#cbd5e1")

st = {
 "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=NAVY, spaceAfter=4),
 "tag": ParagraphStyle("tag", fontName="Helvetica", fontSize=9.5, leading=13, textColor=MUTED, spaceAfter=8),
 "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11.5, leading=15, textColor=ACC, spaceBefore=10, spaceAfter=4),
 "p": ParagraphStyle("p", fontName="Helvetica", fontSize=10, leading=14.5, textColor=INK, spaceAfter=4),
 "li": ParagraphStyle("li", fontName="Helvetica", fontSize=10, leading=14, textColor=INK, leftIndent=14, bulletIndent=4, spaceAfter=2),
 "code": ParagraphStyle("code", fontName="Courier", fontSize=8.8, leading=12, textColor=INK),
 "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=9, leading=12, textColor=INK),
 "cellb": ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=colors.white),
}

def P(t, s="p"): return Paragraph(t, st[s])
def bullets(items): return [Paragraph(i, st["li"], bulletText="-") for i in items]

def codebox(text):
    pre = Preformatted(text.strip("\n"), st["code"])
    t = Table([[pre]], colWidths=[W - 40*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), BOX), ("BOX", (0,0), (-1,-1), 0.6, LINE),
        ("LINEBEFORE", (0,0), (0,-1), 3, ACC), ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8)]))
    return t

def table(rows, widths):
    data = [[Paragraph(c, st["cellb"]) for c in rows[0]]] + [[Paragraph(c, st["cell"]) for c in r] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), NAVY),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, BOX]),
        ("GRID", (0,0), (-1,-1), 0.4, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4)]))
    return t

def header(num, title, role, mcp):
    return [P(f'<font color="#d97757">{num}</font>  {title}', "h1"),
            P(f"<b>Rôle :</b> {role}   |   <b>MCP :</b> {mcp}", "tag")]

def flow():
    d = Drawing(W - 40*mm, 120)
    steps = [("Spécification", MUTED), ("Ticket Jira", BLUE), ("Scénarios\nGherkin", GREEN),
             ("Exécution\nSelenium", GREEN), ("Mise à jour\nJira", BLUE), ("Ticket BUG", ACC)]
    bw, gap = 66, 13.5; y = 60
    for i, (lab, c) in enumerate(steps):
        x = i * (bw + gap)
        d.add(Rect(x, y, bw, 44, rx=6, ry=6, fillColor=c, strokeColor=None))
        lines = lab.split("\n")
        for j, ln in enumerate(lines):
            d.add(String(x + bw/2, y + 26 - (j*11) + (5 if len(lines) == 2 else 0) - 3, ln, fontName="Helvetica-Bold",
                         fontSize=8.5, fillColor=colors.white, textAnchor="middle"))
        if i < len(steps) - 1:
            ax = x + bw + 2; d.add(Line(ax, y + 22, ax + gap - 5, y + 22, strokeColor=INK, strokeWidth=1))
            d.add(Polygon([ax + gap - 4, y + 22, ax + gap - 9, y + 25, ax + gap - 9, y + 19], fillColor=INK, strokeColor=None))
        d.add(String(x + bw/2, y - 14, f"Étape {['--','01','02','03','03','05'][i]}" if i else "Entrée",
                     fontName="Helvetica", fontSize=8, fillColor=MUTED, textAnchor="middle"))
    d.add(String(0, 12, "Claude orchestre chaque étape via le Model Context Protocol (MCP) : Jira pour les tickets, Selenium pour le navigateur.",
                 fontName="Helvetica-Oblique", fontSize=8.5, fillColor=MUTED))
    return d

def on_page(c, doc):
    c.saveState()
    c.setFillColor(ACC); c.rect(0, H - 6, W, 6, stroke=0, fill=1)
    c.setFont("Helvetica", 8); c.setFillColor(MUTED)
    c.drawString(20*mm, 12*mm, "Guide Stratégique de Prompts QA Automation  |  Claude x MCP")
    c.drawRightString(W - 20*mm, 12*mm, f"Page {doc.page}")
    c.restoreState()

def on_cover(c, doc):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0, H - 115*mm, W, 115*mm, stroke=0, fill=1)
    c.setFillColor(ACC); c.rect(20*mm, H - 40*mm, 18*mm, 2.2*mm, stroke=0, fill=1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 30)
    c.drawString(20*mm, H - 58*mm, "Guide Stratégique de Prompts")
    c.drawString(20*mm, H - 71*mm, "QA Automation")
    c.setFont("Helvetica", 13); c.setFillColor(colors.HexColor("#c7d2fe"))
    c.drawString(20*mm, H - 85*mm, "Workflow piloté par Claude via MCP : Jira, Gherkin & Selenium")
    x = 20*mm
    for lab, col in [("Claude", ACC), ("MCP", PURPLE), ("Jira", BLUE), ("Selenium", GREEN), ("Cucumber / BDD", GREEN)]:
        w = c.stringWidth(lab, "Helvetica-Bold", 10) + 14
        c.setFillColor(col); c.roundRect(x, H - 102*mm, w, 7*mm, 3.5*mm, stroke=0, fill=1)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 10); c.drawCentredString(x + w/2, H - 99.6*mm, lab)
        x += w + 6
    c.setFillColor(MUTED); c.setFont("Helvetica", 9)
    c.drawString(20*mm, 20*mm, "Adam Chouk  |  github.com/adama007/claude-mcp-qa-automation")
    c.drawRightString(W - 20*mm, 20*mm, "Version 2.0  |  Octobre 2026")
    c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=20*mm,
                      title="Guide de Prompts QA Automation - Claude MCP", author="Adam Chouk",
                      subject="Prompts QA: Jira, Gherkin, Selenium", creator="Claude")
fr = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
cover_fr = Frame(doc.leftMargin, doc.bottomMargin + 10*mm, doc.width, H - 125*mm - doc.bottomMargin, id="c")
doc.addPageTemplates([PageTemplate("cover", [cover_fr], onPage=on_cover), PageTemplate("body", [fr], onPage=on_page)])

E = [P("Ce guide réunit les prompts utilisés pour automatiser le cycle de vie des tests avec <b>Claude</b>, "
       "connecté à <b>Jira</b> et <b>Selenium</b> grâce au <b>Model Context Protocol (MCP)</b>."),
     P("Après la configuration des deux serveurs MCP, un workflow simple couvre trois actions : "
       "<b>la création des scénarios</b>, <b>l'exécution en temps réel</b> et <b>la déclaration de bug</b> après l'exécution."),
     Spacer(1, 8), P("Vue d'ensemble", "h3"),
     table([["#", "Prompt", "MCP", "Sortie"],
            ["00", "Connexion à Jira", "Jira", "Liste des projets"],
            ["01", "Initialisation & ticket Jira", "Jira", "Ticket QA en To Do (KAN-20)"],
            ["02", "Conception BDD (Gherkin)", "-", "Fichier login.feature"],
            ["03", "Exécution Selenium & synchronisation", "Selenium + Jira", "KAN-20 -&gt; Done, rapport"],
            ["04", "Workflow amélioration & reporting", "Selenium + Jira", "KAN-21 -&gt; In Progress"],
            ["05", "Gestion des anomalies", "Jira", "Bug KAN-22 lié à KAN-21"]],
           [12*mm, 62*mm, 32*mm, 64*mm]),
     NextPageTemplate("body"), PageBreak()]

E += [P("Le workflow en un coup d'oeil", "h1"), P("De la spécification au rapport de bug, chaque étape correspond à un prompt.", "tag"),
      Spacer(1, 6), flow(), Spacer(1, 10), P("Prérequis", "h3")]
E += bullets(["Claude Desktop avec les serveurs MCP <b>Atlassian (Jira)</b> et <b>Selenium</b> configurés.",
              "Un projet Jira (dans la démo : <b>My Software Team</b>, clé <b>KAN</b>).",
              "Une spécification du module à tester, jointe dans la conversation (ex. <i>Login</i>).",
              "Application testée : <b>https://www.saucedemo.com/</b>"])
E += [P("Variables à remplacer", "h3"),
      table([["Variable", "Description"],
             ["&lt;EMAIL_TESTEUR&gt;", "Email Atlassian du testeur à qui assigner les tickets"],
             ["My Software Team", "Nom de votre projet Jira"],
             ["KAN-20, KAN-21", "Clés de vos tickets"]], [50*mm, 120*mm]),
      P("Connexion à Jira", "h3"), P("<b>00</b> - Vérifier que le MCP Atlassian fonctionne avant de lancer le workflow :"),
      codebox("Connecte-toi à Jira et donne-moi la liste des projets existants."),
      PageBreak()]

E += header("01", "Initialisation & ticket Jira", "Expert QA &amp; Jira", "Atlassian (Jira)")
E += [P("Prompt", "h3"), codebox("""
Tu es un expert QA et Jira.
Lis seulement le fichier « Login » fourni en contexte.
Crée un ticket Jira de type "TODO" pour un testeur QA dans le projet
"My Software Team".

Contexte :
- Testeur assigné : <EMAIL_TESTEUR>
- Module : Login
- Objectif : automatiser les tests du module login

Le ticket doit contenir :
- Titre clair
- Description détaillée
- Objectif du test
- Périmètre (login valide / invalide / lock user / performance user etc.)
- Critères d'acceptation
- Definition of Done
- Tags (QA, automation, login, regression)

Format attendu : prêt à copier dans Jira."""), P("Résultat obtenu", "h3")]
E += bullets(["Claude lit la spécification et retrouve l'identifiant Jira du testeur.",
              "Ticket <b>KAN-20</b> créé en <b>To Do</b>, priorité Medium, labels <i>QA, automation, login, regression</i>."])
E += [Spacer(1, 10)] + header("02", "Conception BDD (Gherkin)", "Expert QA Automation", "aucun (génération)")
E += [P("Prompt", "h3"), codebox("""
Tu es un expert QA Automation.
Lis le document de spécification du module Login.

Actions requises :
1. Identifie toutes les fonctionnalités du login.
2. Génère tous les scénarios possibles de test (positifs, négatifs,
   edge cases).
3. Transforme ces scénarios en format Cucumber (Gherkin).

Format attendu :
Feature: Login
Scenario: [Nom du scénario]
Inclure : Given / When / Then, cas utilisateur valide/invalide/bloqué,
mot de passe incorrect, champs vides et comportement UI attendu."""), PageBreak()]

E += [P("Exemple de scénario généré", "h3"), codebox("""
@smoke @regression
Scenario: Connexion réussie avec l'utilisateur standard
  Given je suis sur la page de connexion "https://www.saucedemo.com/"
  When je saisis le username "standard_user"
  And je saisis le password "secret_sauce"
  And je clique sur le bouton "Login"
  Then je suis redirigé vers la page d'inventaire "/inventory.html"
  And le titre de la page est "Swag Labs\""""), Spacer(1, 6),
      P("Le fichier complet couvre les cas positifs, négatifs, edge cases, session, sécurité et performance "
        "(<i>features/login.feature</i> dans le dépôt GitHub)."), Spacer(1, 10)]
E += header("03", "Exécution & synchronisation", "Exécutant QA Automation", "Selenium + Atlassian (Jira)")
E += [P("Prompt", "h3"), codebox("""
Fais l'exécution avec Selenium de ce scénario :
Scenario: Connexion réussie avec l'utilisateur standard

Workflow post-exécution :
1. Change le statut du ticket "QA Login" sur Jira.
2. Ajoute un commentaire détaillant le résultat du test au ticket KAN-20."""),
      P("Résultat obtenu", "h3"),
      table([["Indicateur", "Valeur"], ["Étapes réussies", "8 / 8"], ["Taux de réussite", "100 %"],
             ["Durée d'exécution", "~3 secondes"], ["Navigateur", "Chrome (Selenium WebDriver)"],
             ["Ticket KAN-20", "To Do -&gt; Done, rapport complet en commentaire"]], [55*mm, 115*mm]),
      PageBreak()]

E += [P('<font color="#d97757">04</font>  Workflows avancés', "h1"),
      P("Deux prompts qui enchaînent tout le cycle et gèrent automatiquement les échecs.", "tag"),
      P("4.1  Amélioration &amp; reporting", "h3"), codebox("""
Tu es un QA Automation Engineer expert en Jira, Cucumber et Selenium.
Objectif : lire uniquement le fichier « Amélioration » fourni et
automatiser tout le workflow QA autour de cette amélioration.

Étape 1 - Analyse du fichier d'amélioration.
Étape 2 - Création du ticket Jira TODO
          (Labels : QA, Automation, Login, Enhancement
           | Assigné à : <EMAIL_TESTEUR>).
Étape 3 - Génération d'un seul scénario Gherkin d'acceptation.
Étape 4 - Exécution du test Selenium.
Étape 5 - Mise à jour Jira :
          - Commentaire de reporting.
          - Si succès -> DONE.
          - Si échec  -> IN PROGRESS."""),
      P("Résultat obtenu", "h3"),
      table([["Étape", "Résultat"],
             ["1 - Analyse", "Ajout de l'utilisateur Claude123 / secret_sauce"],
             ["2 - Jira", "Ticket KAN-21 créé en To Do"],
             ["3 - Gherkin", "1 scénario @enhancement @acceptance @login"],
             ["4 - Selenium", "<font color='#dc2626'><b>FAILED</b></font> : Claude123 non reconnu"],
             ["5 - Jira", "KAN-21 -&gt; In Progress, rapport posté"]], [40*mm, 130*mm]),
      P("4.2  Gestion des anomalies (bug tracking)", "h3"), codebox("""
Analyse le ticket d'amélioration après l'exécution des tests.
Si un bug est détecté :
- Créer un nouveau ticket BUG en statut TODO.
- Ajouter la description détaillée de l'anomalie.
- Lier techniquement le ticket BUG au ticket QA Enhancement concerné.
- Assigner le ticket à : <EMAIL_TESTEUR>"""),
      P("Résultat obtenu", "h3")]
E += bullets(["Ticket <b>KAN-22</b> : <i>[BUG] L'utilisateur Claude123 n'est pas reconnu par l'application</i>, priorité <b>High</b>.",
              "Rapport structuré : étapes de reproduction, comportement attendu / observé, données de l'assertion Selenium.",
              "Lien Jira <b>KAN-22 blocks KAN-21</b> + commentaire de traçabilité sur KAN-21."])
E += [PageBreak(), P("Bonnes pratiques de prompting", "h1"),
      P("Ce qui rend ces prompts fiables et reproductibles.", "tag"),
      table([["Technique", "Exemple", "Pourquoi"],
             ["Rôle explicite", "« Tu es un expert QA et Jira »", "Cadre le niveau d'expertise et le vocabulaire"],
             ["Contexte limité", "« Lis seulement le fichier Login »", "Évite le mélange de sources"],
             ["Étapes numérotées", "Étape 1 ... Étape 5", "Workflow déterministe et traçable"],
             ["Format imposé", "Feature / Scenario / Given-When-Then", "Sortie directement exploitable"],
             ["Règles conditionnelles", "Succès -&gt; Done, échec -&gt; In Progress", "La décision est automatisée"],
             ["Critères de fin", "Definition of Done dans le ticket", "Le résultat est vérifiable"]],
            [38*mm, 62*mm, 70*mm]),
      Spacer(1, 14), P("Ressources", "h3")]
E += bullets(["Dépôt GitHub : <b>github.com/adama007/claude-mcp-qa-automation</b>",
              "Configuration des serveurs MCP : <i>docs/mcp-setup.md</i>",
              "Rapports générés : <i>reports/KAN-20_execution_report.md</i>, <i>reports/KAN-22_bug_report.md</i>"])
E += [Spacer(1, 30), P("<i>Guide généré pour l'optimisation des processus de test logiciel.</i>", "tag")]
doc.build(E)
