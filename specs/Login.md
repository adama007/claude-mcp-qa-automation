# Spécification fonctionnelle : module Login

> Spécification d'exemple utilisée comme **entrée** des prompts [01](../prompts/01-ticket-jira.md) et [02](../prompts/02-scenarios-gherkin.md).

| Élément | Valeur |
|---|---|
| Application | Swag Labs : https://www.saucedemo.com/ |
| Module | Login |
| Environnement | Test / QA |

## 1. Description

La page de connexion permet à un utilisateur enregistré d'accéder au catalogue de produits (`/inventory.html`) grâce à un nom d'utilisateur et un mot de passe.

## 2. Éléments de l'interface

- Champ **Username**
- Champ **Password** (saisie masquée)
- Bouton **Login**
- Zone de message d'erreur (bandeau rouge avec bouton de fermeture)

## 3. Comptes de test

| Username | Comportement attendu |
|---|---|
| `standard_user` | Connexion normale |
| `locked_out_user` | Connexion refusée : compte bloqué |
| `problem_user` | Connexion OK, anomalies d'affichage connues |
| `performance_glitch_user` | Connexion OK mais lente |
| `error_user` | Connexion OK, erreurs sur certaines actions |
| `visual_user` | Connexion OK, anomalies visuelles |

Mot de passe commun : `secret_sauce`

## 4. Règles de gestion

| ID | Règle |
|---|---|
| RG-01 | Identifiants valides → redirection vers `/inventory.html` |
| RG-02 | Username vide → « Epic sadface: Username is required » |
| RG-03 | Password vide → « Epic sadface: Password is required » |
| RG-04 | Identifiants incorrects → « Epic sadface: Username and password do not match any user in this service » |
| RG-05 | Compte bloqué → « Epic sadface: Sorry, this user has been locked out. » |
| RG-06 | En cas d'erreur, les champs sont surlignés en rouge avec une icône ✖ |
| RG-07 | Accès direct à `/inventory.html` sans être connecté → retour à la page de login avec un message d'erreur |
| RG-08 | Après « Logout », l'utilisateur revient à la page de login avec des champs vides |
| RG-09 | La page d'inventaire doit se charger en moins de 3 secondes pour `standard_user` |
