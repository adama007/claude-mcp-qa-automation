# 01 · Initialisation & ticket Jira

> **Rôle :** Expert QA & Jira · **MCP utilisé :** Atlassian (Jira) · **Entrée :** fichier [`specs/Login.md`](../specs/Login.md)

## Prompt

```text
Tu es un expert QA et Jira.
Lis seulement le fichier « Login » fourni en contexte.
Crée un ticket Jira de type "TODO" pour un testeur QA dans le projet "My Software Team".

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

Format attendu : prêt à copier dans Jira.
```

## Ce que fait Claude

1. Lit la spécification du module Login.
2. Retrouve l'identifiant Jira du testeur (`lookupJiraAccountId`).
3. Crée le ticket en statut **To Do**, assigné au testeur, avec les labels demandés.

## Résultat obtenu dans la démo

| Champ | Valeur |
|---|---|
| Ticket | `KAN-20` |
| Statut | To Do |
| Priorité | Medium |
| Labels | `QA` `automation` `login` `regression` |
| Application | https://www.saucedemo.com/ |
| Environnement | Test / QA |
