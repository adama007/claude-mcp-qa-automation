# 00 · Connexion à Jira (vérification du MCP)

> **Rôle :** aucun · **MCP utilisé :** Atlassian (Jira) · **Objectif :** vérifier que Claude accède bien à l'instance Jira.

## Prompt

```text
Connecte-toi à Jira et donne-moi la liste des projets existants.
```

## Ce que fait Claude

1. Recherche les outils disponibles et récupère le **Cloud ID** de l'instance Atlassian (`getAccessibleAtlassianResources`).
2. Liste les projets accessibles (nom, clé, type).

## Résultat attendu

- Connexion confirmée à l'instance `<votre-instance>.atlassian.net`.
- Le projet cible apparaît dans la liste (dans la démo : **My Software Team**, clé `KAN`).

> 💡 Si la connexion échoue, voir [docs/mcp-setup.md](../docs/mcp-setup.md).
