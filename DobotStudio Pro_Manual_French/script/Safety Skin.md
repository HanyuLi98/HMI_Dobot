# Peau de sécurité

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

La commande Peau de sécurité est utilisée pour configurer les fonctions liées à la sécurité de la peau.

| Instruction| Fonction|
|----------|----------|
| [EnableSafeSkin](#enablesafeskin)| Commutateur de la peau de sécurité|
| [SetSafeSkin](#setsafeskin)| Définit la sensibilité de chaque partie de la peau de sécurité|

<h3 class="lua-cmd" >EnableSafeSkin</h3>

**Prototype :**

```lua
EnableSafeSkin(ON|OFF)
```

**Description :**

Commutateur de la peau de sécurité

**Paramètres obligatoires :**

ON|OFF : ON signifie que la peau de sécurité est activée, OFF signifie que la peau de sécurité est désactivée.

**Retour :**

- 0 : L'opération a échoué, aucune peau de sécurité n'a été détectée.
- 1 : Opération réussie

**Exemple :**

```lua
-- Activer la peau de sécurité.
EnableSafeSkin(ON)
```

<h3 class="lua-cmd" >SetSafeSkin</h3>

**Prototype :**

```lua
SetSafeSkin(part,status)
```

**Description :**

Réglage de la sensibilité de chaque partie de la peau de sécurité.

**Paramètres obligatoires :**

- part : partie à régler, plage de valeurs [3, 6].
  - 3 : Petit bras.
  - 4 : Articulations J4
  - 5 : Articulations J5
  - 6 : Articulations J6
- status : Sensibilité à régler, plage de valeurs [0, 3].
  - 0 : Fermer
  - 1 : Sensibilité faible (proximité ≤ 5cm).
  - 2 : Sensibilité moyenne (proximité ≤ 10cm).
  - 3 : Sensibilité élevée (distance de proximité ≤15cm).

**Exemple :**

```lua
-- Désactiver la sensibilité de la peau de sécurité du petit bras.
SetSafeSkin(3,0)
```