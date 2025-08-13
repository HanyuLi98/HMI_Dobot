# Registre de bus

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

L'instruction du registre de bus permet de lire et d'écrire les registres de bus Profinet ou Ethernet/IP.

<div class="info1"><img src="images/info.png"  height="18" /><b>Description : </b><div>Magician E6 ne prend pas en charge cet ensemble de commande. </div></div>

<br/>

| Instruction| Fonction|
|----------|----------|
| [GetInputBool](#getinputbool)| Obtient la valeur bool à l'adresse spécifiée dans le registre d'entrée.|
| [GetInputInt](#getinputint)| Obtient la valeur int à l'adresse spécifiée dans le registre d'entrée.|
| [GetInputFloat](#getinputfloat)| Obtient la valeur float à l'adresse spécifiée dans le registre d'entrée.|
| [GetOutputBool](#getoutputbool)| Obtenir la valeur booléenne du registre de sortie|
| [GetOutputInt](#getoutputint)| Obtenir la valeur int du registre de sortie|
| [GetOutputFloat](#getoutputfloat)| Obtenir la valeur float du registre de sortie|
| [SetOutputBool](#setoutputbool)| Définir la valeur booléenne du registre de sortie|
| [SetOutputInt](#setoutputint)| Définir la valeur int du registre de sortie|
| [SetOutputFloat](#setoutputfloat)| Définir la valeur float du registre de sortie|

<h3 class="lua-cmd" >GetInputBool</h3>

**Prototype :**
```lua
GetInputBool(address)
```

**Description :**

Obtenir la valeur booléenne du registre de sortie

**Paramètres obligatoires :**

address : adresse du registre, plage de valeurs [0-63].

**Retour :**

Valeur de l'adresse de registre spécifiée, 0 ou 1.

**Exemple :**

```lua
-- Lorsque la valeur du registre d'entrée 0 est 1, exécutez les opérations suivantes.
if(GetInputBool(0)==1)
then
    -- Exécuter les opérations suivantes
end
```

<h3 class="lua-cmd" >GetInputInt</h3>

**Prototype :**

```lua
GetInputInt(address)
```

**Description :**

Obtenir la valeur int du registre de sortie

**Paramètres obligatoires :**

address : adresse du registre, plage de valeurs [0-23].

**Retour :**

La valeur de l'adresse du registre spécifié, sous la forme d'un entier (int32).

**Exemple :**

```lua
-- Lire la valeur du registre d'entrée 1 et l’attribuer à la variable regInt.
local regInt = GetInputInt(1)
```

<h3 class="lua-cmd" >GetInputFloat</h3>

**Prototype :**

```lua
GetInputFloat(address)
```

**Description :**

Obtenir la valeur float du registre de sortie

**Paramètres obligatoires :**

address : adresse du registre, plage de valeurs [0-23].

**Retour :**

La valeur de l'adresse de registre spécifiée est un nombre à virgule flottante de simple précision (float).

**Exemple :**

```lua
-- Lire la valeur du registre d'entrée 2 et l’attribuer à la variable regFloat.
local regFloat = GetInputFloat(2)
```

<h3 class="lua-cmd" >GetOutputBool</h3>

**Prototype :**

```lua
GetOutputBool(address)
```

**Description :**

Obtenir la valeur booléenne du registre de sortie

**Paramètres obligatoires :**

address : adresse du registre, plage de valeurs [0-63].

**Retour :**

Valeur de l'adresse de registre spécifiée, 0 ou 1.

**Exemple :**

```lua
-- Lorsque la valeur du registre de sortie 0 est 1, exécutez les opérations suivantes.
if(GetOutputBool(0)==1)
then
    -- Exécuter les opérations suivantes
end
```

<h3 class="lua-cmd" >GetOutputInt</h3>

**Prototype :**

```lua
GetOutputInt(address)
```

**Description :**

Obtenir la valeur int du registre de sortie

**Paramètres obligatoires :**

address : adresse du registre, plage de valeurs [0-23].

**Retour :**

La valeur de l'adresse du registre spécifié, sous la forme d'un entier (int32).

**Exemple :**

```lua
-- Lire la valeur du registre de sortie 1 et l’attribuer à la variable regInt.
local regInt = GetOutputInt(1)
```

<h3 class="lua-cmd" >GetOutputFloat</h3>

**Prototype :**

```lua
GetOutputFloat(address)
```

**Description :**

Obtenir la valeur float du registre de sortie

**Paramètres obligatoires :**

address : adresse du registre, plage de valeurs [0-23].

**Retour :**

La valeur de l'adresse de registre spécifiée est un nombre à virgule flottante de simple précision (float).

**Exemple :**

```lua
-- Lire la valeur du registre de sortie 2 et l’attribuer à la variable regFloat.
local regFloat = GetOutputFloat(2)
```

<h3 class="lua-cmd" >SetOutputBool</h3>

**Prototype :**

```lua
SetOutputBool(address, value)
```

**Description :**

Définir la valeur booléenne du registre de sortie

**Paramètres obligatoires :**

- address : adresse du registre, plage de valeurs [0-63].
- value : la valeur à définir, prend en charge les valeurs booléennes ou 0/1.

**Exemple :**

```lua
-- Définir la valeur du registre de sortie 0 à faux.
SetOutputBool(0,0)
```

<h3 class="lua-cmd" >SetOutputInt</h3>

**Prototype :**

```lua
SetOutputInt(address, value)
```

**Description :**

Définir la valeur int du registre de sortie

**Paramètres obligatoires :**

- address : adresse du registre, plage de valeurs [0-23].
- valeur : la valeur à définir, prend en charge les nombres entiers (int32).

**Exemple :**

```lua
-- Définir la valeur du registre de sortie 1 est 123.
SetOutputInt(1,123)
```

<h3 class="lua-cmd" >SetOutputFloat</h3>

**Prototype :**

```lua
SetOutputFloat(address, value)
```

**Description :**

Définir la valeur float du registre de sortie

**Paramètres obligatoires :**

- address : adresse du registre, plage de valeurs [0-23].

- valeur : la valeur à définir, prend en charge les nombres à virgule flottante de simple précision (float).
  
  En raison de la limitation du mécanisme de stockage des nombres à virgule flottante (IEEE754), les nombres à virgule flottante de simple précision peuvent enregistrer environ 6 à 7 chiffres significatifs (indépendamment de la position du point décimal). Les valeurs comportant plus de 6 chiffres significatifs enregistrés sous forme de nombres à virgule flottante de simple précision peuvent être biaisées, et plus il y a de chiffres significatifs, plus le biais peut être important.

**Exemple :**

```lua
-- Définir la valeur du registre de sortie 2 est 12,3.
SetOutputFloat(2,12.3)
```