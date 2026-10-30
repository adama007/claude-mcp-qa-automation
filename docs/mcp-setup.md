# ⚙️ Configuration des serveurs MCP

Le **Model Context Protocol (MCP)** est un standard ouvert qui permet à Claude d'utiliser des outils externes.
Ce projet en utilise deux :

| Serveur MCP | Rôle dans le workflow |
|---|---|
| **Atlassian (Jira)** | Lire / créer des tickets, changer les statuts, commenter, lier des tickets |
| **Selenium** | Piloter un navigateur Chrome : ouvrir une page, saisir, cliquer, vérifier |

## Prérequis

- [Claude Desktop](https://claude.ai/download)
- [Node.js](https://nodejs.org/) 18+ (pour `npx`)
- Google Chrome
- Un compte Atlassian avec un projet Jira (plan gratuit suffisant)

## 1. Connecter Jira (Atlassian)

**Option A : connecteur intégré (recommandé).**
Dans Claude : **Paramètres → Connecteurs → Atlassian**, puis autoriser l'accès à votre site `*.atlassian.net`.

**Option B : fichier de configuration.**
Ajouter le serveur MCP distant d'Atlassian dans `claude_desktop_config.json` via `mcp-remote` :

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
    }
  }
}
```

> L'URL du serveur peut évoluer : vérifier la documentation officielle d'Atlassian.

## 2. Ajouter le serveur MCP Selenium

Dans `claude_desktop_config.json` :

```json
{
  "mcpServers": {
    "selenium": {
      "command": "npx",
      "args": ["-y", "@angiejones/mcp-selenium"]
    }
  }
}
```

Emplacement du fichier :

| OS | Chemin |
|---|---|
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |

Un exemple complet est fourni : [`config/claude_desktop_config.example.json`](../config/claude_desktop_config.example.json).

## 3. Vérifier

1. Redémarrer Claude Desktop.
2. Lancer le prompt [00 · Connexion à Jira](../prompts/00-connexion-jira.md).
3. Demander : *« Ouvre https://www.saucedemo.com/ avec Selenium »* → une fenêtre Chrome « contrôlée par un logiciel de test automatisé » doit s'ouvrir.

## 🔒 Sécurité

- Ne jamais commiter de token, mot de passe ou email personnel dans ce dépôt.
- Utiliser une instance Jira et une application **de test** (ici SauceDemo).
