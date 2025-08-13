# IO

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

L'instruction IO est utilisée pour effectuer la lecture/écriture de l'E/S du système du bras robotique et le réglage des paramètres correspondants.

| Instruction| Fonction|
|----------|----------|
| [DI](#di)| Obtenir l'état du port DI|
| [Groupe DI](#digroup)| Obtenir l'état actuel de plusieurs ports de sortie numérique|
| [DO](#do)| Définir l'état du port de sortie numérique|
| [Groupe DO](#dogroup)| Définir l'état du port de sortie numérique|
| [GetDO](#getdo)| Obtenir l'état actuel du port de sortie numérique|
| [Groupe GetDO](#getdogroup)| Obtenir l’état actuel de plusieurs ports de sortie numérique|
| [AI](#ai)| Obtenir la valeur du port AI|
| [AO](#ao)| Définir la valeur du port de sortie analogique|
| [GetAO](#getao)| Obtenir la valeur actuelle du port de sortie analogique|

<h3 class="lua-cmd" >DI</h3>

**Prototype :**

```lua
DI(index)
```

**Description :**

Lire l’état du port d’entrée numérique.

**Paramètres obligatoires :**

index : numéro du terminal DI.

**Retour :**

L'état (ON/OFF) du terminal DI correspondant.

**Exemple :**

```lua
-- Lorsque DI1 est ON, le bras robotique se déplace en ligne droite jusqu'au point P1.
if (DI(1)==ON) 
then
	MovL(P1)
end
```

<h3 class="lua-cmd" >DIGroup</h3>

**Prototype :**

```lua
DIGroup(index1,...,indexN)
```

**Description :**

Lire l'état du port d'entrée numérique.

**Paramètres obligatoires :**

index : numéro du terminal DI, plusieurs peuvent être saisis, séparés par des virgules.

**Retour :**

L'état (ON/OFF) du terminal DI correspondant est renvoyé sous forme de tableau.

**Exemple :**

```lua
-- Lorsque DI1 et DI2 sont ON, le bras robotique se déplace en ligne droite jusqu'au point P1.
local digroup = DIGroup(1,2)
if (digroup[1]&digroup[2]==ON) 
then
	MovL(P1)
end
```

<h3 class="lua-cmd" >DO</h3>

**Prototype :**

```lua
DO(index,ON|OFF,time_ms)
```

**Description :**

Définir l'état du port de sortie numérique

**Paramètres obligatoires :**

- index : numéro du terminal DO.
- ON|OFF : état du port DO à définir.

**Paramètres facultatifs :**

time_ms : Temps de sortie continu en ms, plage de valeurs : [25, 60000]. Si ce paramètre est défini, le système inversera automatiquement l'OD après le temps spécifié. L'inversion est une action asynchrone qui ne bloque pas la file d'attente des commandes, et le système exécute la commande suivante après avoir exécuté la sortie DO.

**Exemple :**

```lua
-- Définir DO1 sur ON.
DO(1,ON)
```

```lua
-- Définir DO1 sur ON, puis l'automatiquement sur OFF après 50 ms.
DO(1,ON,50)
```

<h3 class="lua-cmd" >DOGroup</h3>

**Prototype :**

```lua
DOGroup({index1,ON|OFF},..,{indexN,ON|OFF})
```

**Description :**

Définir l'état du port de sortie numérique

**Paramètres obligatoires :**

- index : numéro du terminal DO.
- ON|OFF : état du port DO à définir.

Plusieurs groupes peuvent être définis ; chaque groupe est placé entre crochets et séparé par une virgule.

**Exemple :**

```lua
-- Définir DO1 et DO2 sur ON.
DOGroup({1,ON},{2,ON})
```

<h3 class="lua-cmd" >GetDO</h3>

**Prototype :**

```lua
GetDO(index)
```

**Description :**

Obtenir l'état actuel du port de sortie numérique

**Paramètres obligatoires :**

index : numéro du terminal DO.

**Retour**

L'état (ON/OFF) du terminal DI correspondant.

**Exemple :**

```lua
-- Obtenir l'état actuel de DO1.
local do1 = GetDO(1)
```

<h3 class="lua-cmd" >GetDOGroup</h3>

**Prototype :**

```lua
GetDOGroup(index1,...,indexN)
```

**Description :**

Obtenir l'état actuel de plusieurs ports de sortie numérique

**Paramètres obligatoires :**

index : numéro de la borne DO, plusieurs peuvent être saisis, séparés par des virgules.

**Retour :**

L'état (ON/OFF) du terminal DO correspondant est renvoyé sous forme de tableau.

**Exemple :**

```lua
-- Obtenir l'état actuel de DO1 et DO2.
local dogroup = GetDOGroup(1,2)
local do1 = dogroup[1]
local do2 = dogroup[2]
```

<h3 class="lua-cmd" >AI</h3>

**Prototype :**

```lua
AI(index)
```

**Description :**

Lire la valeur du port d'entrée analogique La signification de la valeur (tension/courant) peut être visualisée et modifiée dans la page **Surveillance > Armoire de commande AI/AO** de DobotStudio Pro.

**Paramètres obligatoires :**

index : numéro du terminal AI.

**Retour :**

La valeur de la borne AI correspondante.

**Exemple :**

```lua
-- Lire la valeur d’AI1
local ai1 = AI(1)
```

<h3 class="lua-cmd" >AO</h3>

**Prototype :**

```lua
AO(index,value)
```

**Description :**

Définir la valeur du port de sortie analogique La signification de la valeur (tension/courant) peut être visualisée et modifiée dans la page **Surveillance > Armoire de commande AI/AO** de DobotStudio Pro.

**Paramètres obligatoires :**

- index : numéro de la borne AO.
- valeur : valeur à régler, plage de tension : [0,10], unité : V ; plage de courant : [4,20], unité : mA.

**Exemple :**

```lua
-- Définir la valeur de sortie d’AO1 à 2.
AO(1,2)
```

<h3 class="lua-cmd" >GetAO</h3>

**Prototype :**

```lua
GetAO(index)
```

**Description :**

Obtenir la valeur actuelle du port de sortie analogique La signification de la valeur (tension/courant) peut être visualisée et modifiée dans la page **Surveillance > Armoire de commande AI/AO** de DobotStudio Pro.

**Paramètres obligatoires :**

index : numéro de la borne AO.

**Retour**

La valeur de la borne AO correspondante.

**Exemple :**

```lua
-- Obtenir l'état actuel d’AO1.
local ao1 = GetAO(1)
```