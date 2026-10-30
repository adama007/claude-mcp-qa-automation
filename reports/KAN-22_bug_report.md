# 🐞 [BUG] L'utilisateur Claude123 n'est pas reconnu par l'application · Module Login

> Ticket Jira `KAN-22` créé automatiquement par Claude (prompt [05](../prompts/05-declaration-bug.md)).

| Champ | Valeur |
|---|---|
| Ticket lié | `KAN-21` : [QA Enhancement] Vérification de l'ajout du nouvel utilisateur Claude123 |
| Lien | `KAN-22` **blocks** `KAN-21` |
| Détecté par | QA Automation (Selenium / Claude AI) |
| Environnement | https://www.saucedemo.com/ (Chrome, Selenium WebDriver) |
| Sévérité | 🔴 High |
| Priorité | 🔴 High |
| Labels | `Authentication` `Blocker` `Bug` `Enhancement` `Login` |
| Statut | To Do |

## Description du bug

L'amélioration `KAN-21` spécifie que l'utilisateur `Claude123` doit être ajouté à la liste des utilisateurs autorisés de l'application SauceDemo et doit pouvoir s'authentifier avec le mot de passe `secret_sauce`.

Lors de l'exécution du test d'acceptation automatisé (Selenium), la tentative de connexion `Claude123` / `secret_sauce` échoue : l'application ne reconnaît pas cet utilisateur et affiche un message d'erreur bloquant.

## Étapes de reproduction

1. Ouvrir l'application : https://www.saucedemo.com/
2. Saisir le username : `Claude123`
3. Saisir le password : `secret_sauce`
4. Cliquer sur le bouton **Login**
5. Observer le résultat

## ✅ Comportement attendu

- L'utilisateur `Claude123` est reconnu par l'application.
- La connexion réussit sans message d'erreur.
- L'utilisateur est redirigé vers `/inventory.html`.
- La barre de navigation (logo, menu burger, panier) est visible.

## ❌ Comportement observé

- L'application reste sur la page de connexion (`https://www.saucedemo.com/`).
- Aucune redirection vers `/inventory.html`.
- La barre de navigation est absente.
- Les champs username et password sont surlignés en rouge avec des icônes ✖.
- Message affiché : *« Epic sadface: Username and password do not match any user in this service »*.

## Cause racine

`Claude123` n'existe pas encore dans la liste des utilisateurs de SauceDemo : l'amélioration n'a pas été implémentée côté application.

## Plan de résolution

1. **Implémentation** : ajouter `Claude123` aux utilisateurs autorisés.
2. **Validation** : vérifier que `Claude123` apparaît dans la liste affichée sur la page de login.
3. **Re-test** : rejouer le scénario d'acceptation Selenium de `KAN-21`.
4. **Fermeture** : si le test passe à 100 %, fermer ce bug et passer `KAN-21` en Done.
