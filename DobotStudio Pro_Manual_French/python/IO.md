# IO

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

L'instruction IO est utilisée pour effectuer la lecture/écriture de l'E/S du système du bras robotique et le réglage des paramètres correspondants.

| Instruction| Fonction|
|----------|----------|
| [DI](#di)| Obtenir l'état du port DI|
| [Groupe DI](#digroup)| Obtenir l'état actuel de plusieurs ports de sortie numérique|
| [DO](#do)| Définir l'état du port de sortie numérique|
| [Groupe DO](#dogroup)| Définir l'état du port de sortie numérique|
| [GetDO](#getdo)| Obtenir l’état actuel du port de sortie numérique|
| [Groupe GetDO](#getdogroup)| Obtenir l’état actuel de plusieurs ports de sortie numérique|

<h3 class="lua-cmd" >DI</h3>

**Prototype :**

```python
DI(index)
```

**Description :**

Lire l’état du port d’entrée numérique.

**Paramètres obligatoires :**

index : numéro du terminal DI.

**Retour :**

L'état (ON/OFF) du terminal DI correspondant.

**Exemple :**

```python
# Lorsque DI1 est ON, le bras robotique se déplace en ligne droite jusqu'au point P1.
if DI(1)==ON:
	MovL(P1)
```

<h3 class="lua-cmd" >DIGroup</h3>

**Prototype :**
```python
DIGroup(index1,...,indexn)
```

**Description :**

Lire l'état du port d'entrée numérique.

**Paramètres obligatoires :**

index : numéro du terminal DI, plusieurs peuvent être saisis, séparés par des virgules.

**Retour :**

L'état (ON/OFF) du terminal DI correspondant est renvoyé sous forme de tableau.

**Exemple :**

```python
# Lorsque DI1 et DI2 sont ON, le bras robotique se déplace en ligne droite jusqu'au point P1.
digroup = DIGroup(1,2)
if digroup[1]&digroup[2]==ON:
	MovL(P1)
```

<h3 class="lua-cmd" >DO</h3>

**Prototype :**

```python
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

```python
# Définir DO1 sur ON.
DO(1,ON)
```

```python
# Définir DO1 sur ON, puis l'automatiquement sur OFF après 50 ms.
DO(1,ON,50)
```

<h3 class="lua-cmd" >DOGroup</h3>

**Prototype :**

```python
DOGroup([index1,ON|OFF],..,[indexN,ON|OFF])
```

**Description :**

Définir l'état du port de sortie numérique

**Paramètres obligatoires :**

- index : numéro du terminal DO.
- ON|OFF : état du port DO à définir.

Plusieurs groupes peuvent être définis ; chaque groupe est placé entre crochets et séparé par une virgule.

**Exemple :**

```python
# Définir DO1 et DO2 sur ON.
DOGroup([1,ON],[2,ON])
```

<h3 class="lua-cmd" >GetDO</h3>

**Prototype :**

```python
GetDO(index)
```

**Description :**

Obtenir l'état actuel du port de sortie numérique

**Paramètres obligatoires :**

index : numéro du terminal DO.

**Retour**

L'état (ON/OFF) du terminal DI correspondant.

**Exemple :**

```python
# Obtenir l'état actuel de DO1.
GetDO(1)
```

<h3 class="lua-cmd" >GetDOGroup</h3>

**Prototype :**

```python
GetDOGroup(index1,...,indexN)
```

**Description :**

Obtenir l'état actuel de plusieurs ports de sortie numérique

**Paramètres obligatoires :**

index : numéro de la borne DO, plusieurs peuvent être saisis, séparés par des virgules.

**Retour :**

L'état (ON/OFF) du terminal DO correspondant est renvoyé sous forme de tableau.

**Exemple :**

```python
# Obtenir l'état actuel de DO1 et DO2.
GetDOGroup(1,2)
```