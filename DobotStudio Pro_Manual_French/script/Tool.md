# Outil de terminal

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

Les commandes d'outils d'extrémité sont utilisées pour effectuer des lectures/écritures et des paramétrages connexes pour les OI d'extrémité du système de bras robotique.

| Instruction| Fonction|
|----------|----------|
| [ToolDI](#tooldi)| Lire l’état du port d’entrée numérique terminal|
| [ToolDO](#tooldo)| Définir l'état du port de sortie numérique terminal|
| [GetToolDO](#gettooldo)| Obtenir l'état actuel du port de sortie numérique|
| [ToolAI](#toolai)| Lire la valeur du port d’entrée analogique terminal|
| [SetToolMode](#settoolmode)| Définit le mode de communication du terminal multiplexé en bout de chaîne|
| [GetToolMode](#gettoolmode)| Obtenir le mode de communication du terminal multiplexé en bout de ligne|
| [SetToolPower](#settoolpower)| Définir l'état d'alimentation électrique de l'outil terminal|
| [SetTool485](#settool485)| Définit le format de données correspondant à l'interface RS485 de l'outil final|

<h3 class="lua-cmd" >ToolDI</h3>

**Prototype :**

```lua
ToolDI(index)
```

**Description :**

Lire l'état du port d'entrée numérique terminal.

**Paramètres obligatoires :**

index : numéro du terminal DI final.

**Retour :**

L'état (ON/OFF) du terminal DI correspondant.

**Exemple :**

```lua
-- Lorsque DI1 de terminal est ON, le bras robotique se déplace en ligne droite jusqu'au point P1.
if (ToolDI(1)==ON) 
then
	MovL(P1)
end
```

<h3 class="lua-cmd" >ToolDO</h3>

**Prototype :**

```lua
ToolDO(index,ON|OFF)
```

**Description :**

Définir l'état du port de sortie numérique terminal.

**Paramètres obligatoires :**

- index : numéro du terminal DO final.
- ON|OFF : état du port DO à définir.

**Exemple :**

```lua
-- Définir DO1 de terminal sur ON.
ToolDO(1,ON)
```

<h3 class="lua-cmd" >GetToolDO</h3>

**Prototype :**

```lua
GetToolDO(index)
```

**Description :**

Obtenir l'état actuel du port de sortie numérique.

**Paramètres obligatoires :**

index : numéro du terminal DO final.

**Retour**

L'état (ON/OFF) du terminal DO correspondant.

**Exemple :**

```lua
-- Obtenir l'état actuel de DO1 de terminal.
GetToolDO(1)
```

<h3 class="lua-cmd" >ToolAI</h3>

**Prototype :**

```lua
ToolAI(index)
```

**Description :**

Lire la valeur du port d'entrée analogique terminal

La borne doit être configurée en mode d'entrée analogique par SetToolMode avant d'être utilisée.

<div class="info1"><img src="images/info.png"  height="18" /><b>Description : </b><div>Un bras robotique qui n’a pas l’interface AI de terminal n’aura aucun effet lors de l’appel de cette interface. </div></div>

<br/>

**Paramètres obligatoires :**

index : Numéro de la borne AI finale.

**Retour :**

La valeur de la borne AI correspondante.

**Exemple :**

```lua
-- Lire la valeur d’AI1 de terminal et l’attribuer à la variable test.
test = ToolAI(1)
```

<h3 class="lua-cmd" >SetToolMode</h3>

**Prototype :**

```lua
SetToolMode(mode,type,identify)
```

**Description :**

Pour les modèles où les interfaces AI1 et AI2 à l'extrémité du bras du robot sont multiplexées avec les terminaux d'interface 485, le mode des terminaux multiplexés d'extrémité peut être défini via cette interface.

Le mode par défaut est le mode 485.

<div class="info1"><img src="images/info.png"  height="18" /><b>Description : </b><div>Un bras robotique qui ne prend pas en charge le changement de mode d’extrémité n’aura aucun effet lors de l’appel de cette interface. </div></div>

<br/>

**Paramètres obligatoires :**

- mode : mode du terminal multiplexé.
  
  - 1 : Mode 485
  - 2 : Mode d'entrée analogique
  
- type :
  
  - Lorsque le mode est 1, ce paramètre n'est pas valide.
  
  - Lorsque le mode est 2, ce paramètre est utilisé pour définir le mode d'entrée analogique.
  
  Le premier chiffre indique le mode de AI1, le deuxième chiffre indique le mode de AI2, et seul le premier chiffre peut être saisi lorsque le dixième chiffre est 0.
  
  **Valeurs :**
  
  - 0 : Mode d'entrée de tension 0~10V.
  - 1 : Collecte de courant.
  - 2 : Mode d'entrée de tension 0~5V.
  
  **Exemple :**
  
  - 0 : AI1 et AI2 sont tous deux en mode d'entrée de tension 0~10V.
  
  - 1 : AI2 est en mode d'entrée de tension 0~10V et AI1 est en mode d'acquisition de courant.
  
  - 11 : AI2 et AI1 sont tous deux en mode d'acquisition de courant.
  
  - 12 : AI2 est en mode d'acquisition de courant et AI1 est en mode d'entrée de tension 0~5V.
  
  - 20 : AI2 est en mode d'entrée de tension 0~5V, AI1 est en mode d'entrée de tension 0~10V.

**Paramètres facultatifs :**

identifier : utilisé pour spécifier le connecteur aérien lorsque le bras du robot a plus d'un connecteur aérien d'extrémité. Valeur par défaut : 1.

- 1 représente la Fiche aviation 1
- 2 représente la Fiche aviation 2

**Exemple :**

```lua
-- Définir le terminal multiplexé de fin en mode 485.
SetToolMode(1,0)
```

```lua
-- Définir le terminal multiplexé du connecteur de fin 2 du CR20A en mode 485.
SetToolMode(1,0,2)
```

```lua
-- Définir le terminal multiplexé de fin en mode entrée analogique, avec deux voies en mode entrée de tension de 0 à 10V.
SetToolMode(2,0)
```

```lua
-- Définir le terminal multiplexé de fin en mode entrée analogique, avec AI1 en mode entrée de tension de 0 à 10V et AI2 en mode entrée courant.
SetToolMode(2,10)
```

<h3 class="lua-cmd" >GetToolMode</h3>

**Prototype :**

```lua
GetToolMode(identify)
```

**Description :**

Obtenir le mode actuel de la borne de multiplexage d'extrémité.

**Paramètres facultatifs :**

identifier : utilisé pour spécifier le connecteur aérien lorsque le bras du robot a plus d'un connecteur aérien d'extrémité. Valeur par défaut : 1.

- 1 représente la Fiche aviation 1
- 2 représente la Fiche aviation 2

**Retour :**

- mode : mode du terminal multiplexé.
- Type : Mode d'entrée analogique

Voir le paramètre SetToolMode du même nom pour plus de détails.

**Exemple :**

```lua
-- Obtenir le mode du terminal multiplexé de fin.
local mode,type = GetToolMode()
```

```lua
-- Obtenir le mode du terminal multiplexé du connecteur de fin 2 du CR20A.
local mode,type = GetToolMode(2)
```

<h3 class="lua-cmd" >SetToolPower</h3>

**Prototype :**

```lua
SetToolPower(status)
```

**Description :**

Définit l'état de l'alimentation électrique de l'outil final, généralement utilisé pour redémarrer l'alimentation électrique de l'outil final, par exemple pour réalimenter la pince terminale en vue de l'initialisation.

Si vous devez appeler cette interface en permanence, il est recommandé d'avoir un intervalle d'au moins 4 ms.

<div class="info1"><img src="images/info.png"  height="18" /><b>Description : </b><div>La sortie DO de l'extrémité sera également désactivée lorsque l'alimentation de l'extrémité sera coupée.</div></div>

<br/>

**Paramètres obligatoires :**

État : L'état d'alimentation électrique de l'outil terminal

- 0 : Coupe l'alimentation électrique.
- 1 : Débranchez l'alimentation électrique.

**Exemple :**

```lua
-- Redémarrer l’alimentation électrique de l’outil de terminal
SetToolPower(0)
Wait(5)
SetToolPower(1)
```

<h3 class="lua-cmd" >SetTool485</h3>

**Prototype :**

```lua
SetTool485(baud,parity,stopbit,identify)
```

**Description :**

Définir le format de données correspondant à l'interface RS485 de l'outil final.

<div class="info1"><img src="images/info.png"  height="18" /><b>Description : </b><div>Un bras robotique qui n’a pas l’interface 485 de terminal n’aura aucun effet lors de l’appel de cette interface. </div></div>

<br/>

**Paramètres obligatoires :**

baud : vitesse de transmission de l'interface RS485.

**Paramètres facultatifs :**

- parity : présence ou non d'un bit de parité.
  
  - "0" : Parité impaire.
  - "E" : Parité paire.
  - "N" : pas de bit de parité.
  - La valeur par défaut est "N".

- stopbit : longueur du bit de stop. Plage : 0,5, 1, 1,5, 2. Valeur par défaut : 1.
  
  Si l'erreur est comprise dans ±0,1, elle sera sélectionnée automatiquement (0,4001 correspond à 0,5, 0,3999 correspond à 0,3999, 1,09999 correspond à 1).

- identifier : lorsque le bras du robot a plus d'une extrémité d'insertion aérienne, il est utilisé pour spécifier l'insertion aérienne, 1 signifie l'insertion aérienne 1, 2 signifie l'insertion aérienne 2.

**Exemple :**

```lua
-- Définir le bitrate de l’interface RS485 de l’outil de terminal à 115200 Hz, sans bits de parité et avec une longueur de bit d’arrêt de 1.
SetTool485(115200,"N",1)
```