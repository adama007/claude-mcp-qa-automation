# 03 · Exécution Selenium & synchronisation Jira

> **MCP utilisés :** Selenium + Atlassian (Jira) · **Entrée :** un scénario de [`features/login.feature`](../features/login.feature) · **Ticket :** `KAN-20`

## Prompt

```text
Fais l'exécution avec Selenium de ce scénario :
Scenario: Connexion réussie avec l'utilisateur standard

Workflow post-exécution :
1. Change le statut du ticket "QA Login" sur Jira.
2. Ajoute un commentaire détaillant le résultat du test au ticket KAN-20.
```

## Ce que fait Claude, en temps réel

| Étape | Action | Outil MCP (indicatif) |
|---|---|---|
| 1 | Lancement du navigateur Chrome | `start_browser` |
| 2 | Navigation vers SauceDemo | `navigate` |
| 3 | **Given** : page de connexion chargée, champs visibles | `find_element` |
| 4 | **When** : saisie du username `standard_user` | `send_keys` |
| 5 | Saisie du password (masqué) | `send_keys` |
| 6 | Clic sur le bouton Login | `interact` |
| 7 | **Then** : redirection vers `/inventory.html`, titre et navbar vérifiés | `execute_script` |
| 8 | Fermeture du navigateur | `close_session` |
| 9 | Récupération des transitions du ticket | Jira |
| 10 | Transition `KAN-20` → **Done** + commentaire de rapport | Jira |

## Résultat obtenu dans la démo

- ✅ **8 / 8 étapes réussies**, taux de réussite **100 %**, durée ≈ **3 s**
- `KAN-20` : **To Do → Done**
- Rapport complet posté en commentaire : voir [`reports/KAN-20_execution_report.md`](../reports/KAN-20_execution_report.md)
