# =====================================================================
# Scénario d'acceptation généré par Claude (prompt 04 · étape 3)
# Ticket : KAN-21 · Source : specs/Amelioration.md
# Résultat d'exécution : ❌ FAILED → bug KAN-22
# =====================================================================

Feature: Login - Ajout du nouvel utilisateur Claude123

  @enhancement @acceptance @login
  Scenario: Connexion réussie avec le nouvel utilisateur Claude123
    Given je suis sur la page de connexion "https://www.saucedemo.com/"
    When je saisis le username "Claude123"
    And je saisis le password "secret_sauce"
    And je clique sur le bouton "Login"
    Then je suis redirigé vers la page d'inventaire "/inventory.html"
    And aucun message d'erreur n'est affiché
    And la barre de navigation est visible
