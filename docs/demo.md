# 🎥 Démonstration

> 📺 **Vidéo (2 min) :** [voir la démo sur LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7521971767494471680/)

## Déroulé de la démo

| # | Séquence | Prompt | Résultat visible |
|---|---|---|---|
| 1 | Connexion de Claude à Jira | [00](../prompts/00-connexion-jira.md) | Instance Atlassian détectée, projets listés |
| 2 | Création du ticket QA | [01](../prompts/01-ticket-jira.md) | `KAN-20` créé en To Do, assigné, labels QA |
| 3 | Génération des scénarios BDD | [02](../prompts/02-scenarios-gherkin.md) | Fichier `login.feature` complet |
| 4 | Exécution Selenium en temps réel | [03](../prompts/03-execution-selenium.md) | Chrome s'ouvre, login `standard_user`, 8/8 étapes ✅ |
| 5 | Synchronisation Jira | [03](../prompts/03-execution-selenium.md) | `KAN-20` → Done + rapport en commentaire |
| 6 | Workflow d'amélioration | [04](../prompts/04-workflow-amelioration.md) | `KAN-21` créé, test `Claude123` ❌ → In Progress |
| 7 | Déclaration du bug | [05](../prompts/05-declaration-bug.md) | `KAN-22` (High) créé, lien *blocks* `KAN-21` |

## Tickets Jira produits

```text
KAN-20  QA Login                         To Do → Done          ✅ 8/8 PASSED
KAN-21  [QA Enhancement] Claude123       To Do → In Progress   ❌ FAILED
KAN-22  [BUG] Claude123 non reconnu      To Do (High)          🔗 blocks KAN-21
```
