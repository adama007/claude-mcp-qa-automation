# =====================================================================
# Fichier généré par Claude (prompt 02 · Conception BDD)
# Source : specs/Login.md · Application : https://www.saucedemo.com/
# =====================================================================

Feature: Login
  En tant qu'utilisateur de Swag Labs
  Je veux me connecter avec mes identifiants
  Afin d'accéder au catalogue de produits

  Background:
    Given je suis sur la page de connexion "https://www.saucedemo.com/"

  # =================================================================
  # SCÉNARIOS POSITIFS
  # =================================================================

  @smoke @regression
  Scenario: Connexion réussie avec l'utilisateur standard
    When je saisis le username "standard_user"
    And je saisis le password "secret_sauce"
    And je clique sur le bouton "Login"
    Then je suis redirigé vers la page d'inventaire "/inventory.html"
    And le titre de la page est "Swag Labs"
    And la barre de navigation est visible avec le menu burger et le panier
    And la page "Products" est affichée

  @regression
  Scenario Outline: Connexion réussie avec les autres utilisateurs autorisés
    When je saisis le username "<username>"
    And je saisis le password "secret_sauce"
    And je clique sur le bouton "Login"
    Then je suis redirigé vers la page d'inventaire "/inventory.html"

    Examples:
      | username                |
      | problem_user            |
      | performance_glitch_user |
      | error_user              |
      | visual_user             |

  # =================================================================
  # SCÉNARIOS NÉGATIFS
  # =================================================================

  @negative @regression
  Scenario: Connexion refusée pour un utilisateur bloqué
    When je saisis le username "locked_out_user"
    And je saisis le password "secret_sauce"
    And je clique sur le bouton "Login"
    Then je reste sur la page de connexion
    And le message d'erreur "Epic sadface: Sorry, this user has been locked out." est affiché

  @negative @regression
  Scenario: Connexion refusée avec un mot de passe incorrect
    When je saisis le username "standard_user"
    And je saisis le password "wrong_password"
    And je clique sur le bouton "Login"
    Then le message d'erreur "Epic sadface: Username and password do not match any user in this service" est affiché
    And les champs username et password sont surlignés en rouge

  @negative
  Scenario: Connexion refusée avec un utilisateur inexistant
    When je saisis le username "unknown_user"
    And je saisis le password "secret_sauce"
    And je clique sur le bouton "Login"
    Then le message d'erreur "Epic sadface: Username and password do not match any user in this service" est affiché

  @negative @edge
  Scenario: Champs username et password vides
    When je clique sur le bouton "Login"
    Then le message d'erreur "Epic sadface: Username is required" est affiché

  @negative @edge
  Scenario: Champ password vide
    When je saisis le username "standard_user"
    And je clique sur le bouton "Login"
    Then le message d'erreur "Epic sadface: Password is required" est affiché

  @edge
  Scenario: Fermeture du message d'erreur
    Given un message d'erreur est affiché
    When je clique sur l'icône de fermeture du message
    Then le message d'erreur disparaît
    And les icônes d'erreur des champs disparaissent

  @edge
  Scenario: Le username est sensible à la casse
    When je saisis le username "STANDARD_USER"
    And je saisis le password "secret_sauce"
    And je clique sur le bouton "Login"
    Then le message d'erreur "Epic sadface: Username and password do not match any user in this service" est affiché

  # =================================================================
  # SCÉNARIOS DE SESSION & NAVIGATION
  # =================================================================

  @session @regression
  Scenario: Déconnexion et retour à la page de login
    Given je suis connecté en tant que "standard_user"
    When j'ouvre le menu burger
    And je clique sur "Logout"
    Then je suis redirigé vers la page de connexion
    And les champs username et password sont vides

  @session @security
  Scenario: Accès direct à l'inventaire sans être connecté
    Given je ne suis pas connecté
    When j'accède directement à "https://www.saucedemo.com/inventory.html"
    Then je suis redirigé vers la page de connexion
    And un message d'erreur est affiché "Epic sadface: You can only access '/inventory.html' when you are logged in."

  @session @security
  Scenario: Retour en arrière après déconnexion ne donne pas accès à l'inventaire
    Given je me suis déconnecté de l'application
    When j'utilise le bouton "Précédent" du navigateur
    Then je reste sur la page de connexion ou je suis redirigé vers elle
    And je n'ai pas accès à la page d'inventaire

  @security
  Scenario: Le mot de passe est masqué lors de la saisie
    When je saisis le password "secret_sauce"
    Then le champ password affiche des caractères masqués

  # =================================================================
  # SCÉNARIOS DE PERFORMANCE
  # =================================================================

  @performance @regression
  Scenario: Temps de chargement acceptable pour standard_user
    When je saisis le username "standard_user"
    And je saisis le password "secret_sauce"
    And je clique sur le bouton "Login"
    Then la page d'inventaire se charge en moins de 3 secondes

  @performance
  Scenario: Temps de chargement dégradé pour performance_glitch_user
    When je saisis le username "performance_glitch_user"
    And je saisis le password "secret_sauce"
    And je clique sur le bouton "Login"
    Then la page d'inventaire finit par se charger
    And le temps de chargement est mesuré et reporté
