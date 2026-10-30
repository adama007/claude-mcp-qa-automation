# 02 · Conception BDD (Gherkin)

> **Rôle :** Expert QA Automation · **Entrée :** [`specs/Login.md`](../specs/Login.md) · **Sortie :** [`features/login.feature`](../features/login.feature)

## Prompt

```text
Tu es un expert QA Automation.
Lis le document de spécification du module Login.

Actions requises :
1. Identifie toutes les fonctionnalités du login.
2. Génère tous les scénarios possibles de test (positifs, négatifs, edge cases).
3. Transforme ces scénarios en format Cucumber (Gherkin).

Format attendu :
Feature: Login
Scenario: [Nom du scénario]

Inclure : Given / When / Then, cas utilisateur valide / invalide / bloqué,
mot de passe incorrect, champs vides et comportement UI attendu.
```

## Ce que fait Claude

1. Lit la spécification et liste les fonctionnalités (authentification, messages d'erreur, session, sécurité, performance).
2. Génère un fichier `.feature` complet, organisé par sections et **tagué** (`@smoke`, `@regression`, `@negative`, `@security`, `@performance`…).

## Résultat

Le fichier généré est disponible ici : [`features/login.feature`](../features/login.feature).

Extrait :

```gherkin
@smoke @regression
Scenario: Connexion réussie avec l'utilisateur standard
  Given je suis sur la page de connexion "https://www.saucedemo.com/"
  When je saisis le username "standard_user"
  And je saisis le password "secret_sauce"
  And je clique sur le bouton "Login"
  Then je suis redirigé vers la page d'inventaire "/inventory.html"
  And le titre de la page est "Swag Labs"
```
