# 📚 Bibliothèque de prompts

Les prompts sont classés dans l'ordre du workflow. Chacun est **prêt à copier** dans Claude.

| # | Prompt | Rôle | MCP | Sortie |
|---|---|---|---|---|
| 00 | [Connexion à Jira](00-connexion-jira.md) | — | Jira | Liste des projets |
| 01 | [Ticket Jira](01-ticket-jira.md) | Expert QA & Jira | Jira | Ticket `KAN-20` (To Do) |
| 02 | [Scénarios Gherkin](02-scenarios-gherkin.md) | Expert QA Automation | — | `features/login.feature` |
| 03 | [Exécution Selenium](03-execution-selenium.md) | — | Selenium + Jira | Test exécuté, `KAN-20` → Done |
| 04 | [Workflow amélioration](04-workflow-amelioration.md) | QA Automation Engineer | Selenium + Jira | `KAN-21` → In Progress |
| 05 | [Déclaration de bug](05-declaration-bug.md) | — | Jira | Bug `KAN-22` lié à `KAN-21` |

## Variables à remplacer

| Variable | Description |
|---|---|
| `<EMAIL_TESTEUR>` | Email Atlassian du testeur à qui assigner les tickets |
| `My Software Team` | Nom de votre projet Jira |
| `KAN-20`, `KAN-21` | Clés de vos tickets |

## Bonnes pratiques utilisées

- **Rôle explicite** (« Tu es un expert QA… ») pour cadrer le niveau d'expertise.
- **Contexte limité** (« Lis seulement le fichier… ») pour éviter que Claude mélange les sources.
- **Étapes numérotées** pour un workflow déterministe et traçable.
- **Format de sortie imposé** (Gherkin, ticket prêt à copier) pour un résultat directement exploitable.
- **Règles conditionnelles** (succès → Done, échec → In Progress) pour automatiser la décision.

📄 Version PDF : [Guide_Prompts_QA_Workflow.pdf](../docs/Guide_Prompts_QA_Workflow.pdf)
