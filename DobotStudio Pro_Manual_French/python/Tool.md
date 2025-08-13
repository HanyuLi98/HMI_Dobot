# Outil de terminal

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

Les commandes d'outils d'extrémité sont utilisées pour effectuer des lectures/écritures et des paramétrages connexes pour les OI d'extrémité du système de bras robotique.

| Instruction| Fonction|
|----------|----------|
| [ToolDI](#tooldi)| Lire l’état du port d’entrée numérique terminal|
| [ToolDO](#tooldo)| Définir l'état du port de sortie numérique terminal|
| [GetToolDO](#gettooldo)| Obtenir l'état actuel du port de sortie numérique|
| [SetToolPower](#settoolpower)| Définir l'état d'alimentation électrique de l'outil terminal|

<h3 class="lua-cmd" >ToolDI</h3>

**Prototype :**

```python
ToolDI(index)
```

**Description :**

Lire l'état du port d'entrée numérique terminal.

**Paramètres obligatoires :**

index : numéro du terminal DI final.

**Retour :**

L'état (ON/OFF) du terminal DI correspondant.

**Exemple :**

```python
# Lorsque DI1 de terminal est ON, le bras robotique se déplace en ligne droite jusqu'au point P1.
if ToolDI(1)==ON:
	MovL(P1)
```

<h3 class="lua-cmd" >ToolDO</h3>

**Prototype :**

```python
ToolDO(index,ON|OFF)
```

**Description :**

Définir l'état du port de sortie numérique terminal.

**Paramètres obligatoires :**

- index : numéro de la borne DO finale.
- ON|OFF : état du port DO à définir.

**Exemple :**

```python
# Définir DO1 de terminal sur ON.
ToolDO(1,ON)
```

<h3 class="lua-cmd" >GetToolDO</h3>

**Prototype :**

```python
GetToolDO(index)
```

**Description :**

Obtenir l'état actuel du port de sortie numérique.

**Paramètres obligatoires :**

index : numéro de la borne DO finale.

**Retour**

L'état (ON/OFF) du terminal DO correspondant.

**Exemple :**

```python
# Obtenir l'état actuel de DO1 de terminal.
GetToolDO(1)
```

<h3 class="lua-cmd" >SetToolPower</h3>

**Prototype :**

```python
SetToolPower(status)
```

**Description :**

Définit l'état de l'alimentation électrique de l'outil final, généralement utilisé pour redémarrer l'alimentation électrique de l'outil final, par exemple pour réalimenter la pince terminale en vue de l'initialisation. Si vous devez appeler cette interface en permanence, il est recommandé d'avoir un intervalle d'au moins 4 ms.

**Paramètres obligatoires :**

État : L'état d'alimentation électrique de l'outil terminal

- 0 : Coupe l'alimentation électrique.
- 1 : Débranchez l'alimentation électrique.

**Exemple :**

```python
# Redémarrer l’alimentation électrique de l’outil de terminal
SetToolPower(0)
Wait(5)
SetToolPower(1)
```