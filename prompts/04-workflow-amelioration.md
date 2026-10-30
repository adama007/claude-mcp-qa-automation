# 04 · Workflow complet : amélioration & reporting

> **Rôle :** QA Automation Engineer (Jira, Cucumber, Selenium) · **Entrée :** [`specs/Amelioration.md`](../specs/Amelioration.md) · **MCP :** Jira + Selenium

Ce prompt enchaîne **tout le cycle en une seule demande** : analyse → ticket → scénario → exécution → mise à jour Jira.

## Prompt

```text
Tu es un QA Automation Engineer expert en Jira, Cucumber et Selenium.
🎯 Objectif : lire uniquement le fichier « Amélioration » fourni et automatiser
tout le workflow QA autour de cette amélioration.

📌 Étape 1 — Analyse du fichier d'amélioration.
📌 Étape 2 — Création du ticket Jira TODO
   - Labels : QA, Automation, Login, Enhancement
   - Assigné à : <EMAIL_TESTEUR>
📌 Étape 3 — Génération d'un seul scénario Gherkin d'acceptation.
📌 Étape 4 — Exécution du test Selenium.
📌 Étape 5 — Mise à jour Jira :
   - Commentaire de reporting.
   - Si succès  -> DONE.
   - Si échec   -> IN PROGRESS.
```

## Résultat obtenu dans la démo

| Étape | Action | Résultat |
|---|---|---|
| 1 · Analyse | Lecture de `Amelioration.txt` | Ajout de l'utilisateur `Claude123` / `secret_sauce` |
| 2 · Jira | Création du ticket `KAN-21` | ✅ To Do, labels QA / Automation / Login / Enhancement |
| 3 · Gherkin | Scénario d'acceptation généré | 1 scénario `@enhancement @acceptance @login` |
| 4 · Selenium | Exécution sur Chrome / SauceDemo | ❌ **FAILED** : `Claude123` non reconnu |
| 5 · Jira | Transition + commentaire | 🟡 **In Progress**, rapport complet posté |

Scénario généré : [`features/enhancement_claude123.feature`](../features/enhancement_claude123.feature)

**Cause racine :** l'utilisateur `Claude123` n'existe pas encore dans SauceDemo. L'application renvoie
*« Epic sadface: Username and password do not match any user in this service »*.
