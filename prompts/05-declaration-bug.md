# 05 · Gestion des anomalies (bug tracking)

> **MCP utilisé :** Atlassian (Jira) · **Déclencheur :** échec du test de [l'étape 04](04-workflow-amelioration.md)

## Prompt

```text
Analyse le ticket d'amélioration après l'exécution des tests.
Si un bug est détecté :
- Créer un nouveau ticket BUG en statut TODO.
- Ajouter la description détaillée de l'anomalie.
- Lier techniquement le ticket BUG au ticket QA Enhancement concerné.
- Assigner le ticket à : <EMAIL_TESTEUR>
```

## Ce que fait Claude

1. Relit `KAN-21` : statut **In Progress**, 3 assertions en échec → **bug confirmé**.
2. Récupère les types de tickets et les types de liens disponibles (`getIssueLinkTypes`).
3. Crée le ticket **BUG** avec un rapport structuré.
4. Crée le lien **`KAN-22` blocks `KAN-21`**.
5. Ajoute un commentaire de traçabilité sur `KAN-21`.

## Résultat obtenu dans la démo

| Champ | Valeur |
|---|---|
| Ticket | `KAN-22` |
| Titre | [BUG] L'utilisateur Claude123 n'est pas reconnu par l'application, module Login |
| Priorité / sévérité | **High** |
| Labels | `Authentication` `Blocker` `Bug` `Enhancement` `Login` |
| Lien | `KAN-22` **blocks** `KAN-21` |

Rapport complet : [`reports/KAN-22_bug_report.md`](../reports/KAN-22_bug_report.md)
