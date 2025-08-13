# Commande de mouvement relatif

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

La fonction de commande de mouvement relatif est utilisée pour contrôler le bras du robot afin d'effectuer un mouvement décalé. **Veuillez lire la [description générale](common.md) avant de l'utiliser**.

| Instruction| Fonction|
|----------|----------|
| [RelPointUser](#relpointuser)| Décalage par rapport au point cartésien du système de coordonnées d'utilisateurs|
| [RelPointTool](#relpointtool)| Décalage par rapport au point cartésien du système de coordonnées d'outils|
| [RelMovJTool](#relmovjtool)| Commande de mouvement relatif le long du système de coordonnées d'outils avec un mouvement articulaire comme mouvement terminal|
| [RelMovLTool](#relmovltool)| Commande de mouvement relatif le long du système de coordonnées d'outils avec un mouvement linéaire comme mouvement terminal|
| [RelMovJUser](#relmovjuser)| Commande de mouvement relatif le long du système de coordonnées d'utilisateurs avec un mouvement articulaire comme mouvement terminal|
| [RelMovLUser](#relmovluser)| Commande de mouvement relatif le long du système de coordonnées d'utilisateurs avec un mouvement linéaire comme mouvement terminal|
| [RelJointMovJ](#reljointmovj)| Mouvement de l'articulation vers l'angle de décalage spécifié|
| [RelJoint](#reljoint)| Décalage du point par rapport à l'angle d'articulation spécifié|

<h3 class="lua-cmd" >RelPointUser</h3>

**Prototype :**

```lua
RelPointUser(P, {OffsetX, OffsetY, OffsetZ, OffsetRx, OffsetRy, OffsetRz})
```

**Description :**

Décale le point spécifié le long du système de coordonnées de l'utilisateur spécifié et renvoie le point de décalage.

**Paramètres obligatoires :**

- P : Le point spécifié à décaler.
- {OffsetX, OffsetY, OffsetZ, OffsetRx, OffsetRy, OffsetRz} : le décalage dans le système de coordonnées de l'utilisateur spécifié. x, y, z indiquent le décalage spatial en mm ; rx, ry, rz indiquent le décalage angulaire en °.
  - Si le point spécifié est un point d'apprentissage, le décalage est basé sur le système de coordonnées utilisateur du point d'apprentissage.
  - Si le point spécifié est une variable d'articulation ou une variable de position, le décalage est basé sur le [système de coordonnées utilisateur global] (Motion Params.html#user).

**Retour :**

- Si le point spécifié est un point d'apprentissage, la constante du point d'apprentissage décalé est renvoyée.
- Si le point spécifié est une variable d'articulation ou une variable de position, la variable de position de décalage est renvoyée : {pose = {x, y, z, rx, ry, rz}}.

**Exemple :**

```lua
-- Décaler P1 d'une certaine distance dans le système de coordonnées d’utilisateurs spécifié, puis se déplacer vers le point après décalage.
local Offset={OffsetX, OffsetY, OffsetZ, OffsetRx, OffsetRy, OffsetRz}
local p = RelPointUser(P1, Offset)
MovL(p)
```

<h3 class="lua-cmd" >RelPointTool</h3>

**Prototype :**

```lua
RelPointTool(P, {OffsetX, OffsetY, OffsetZ, OffsetRx, OffsetRy, OffsetRz})
```

**Description :**

Effectue un décalage du point spécifié le long du système de coordonnées de l'outil spécifié et renvoie le point de décalage.

**Paramètres obligatoires :**

- P : Le point spécifié à décaler.
- {OffsetX, OffsetY, OffsetZ, OffsetRx, OffsetRy, OffsetRz} : décalage dans le système de coordonnées de l'outil spécifié. x, y, z indiquent le décalage spatial en mm ; rx, ry, rz indiquent le décalage angulaire en °.
  - Si le point spécifié est un point d'apprentissage, le décalage est basé sur le système de coordonnées de l'outil du point d'apprentissage.
  - Si le point spécifié est une variable d'articulation ou de position, le décalage est basé sur le [système de coordonnées global de l'outil] (Motion Params.html#tool).

**Retour :**

- Si le point spécifié est un point d'apprentissage, la constante du point d'apprentissage décalé est renvoyée.
- Si le point spécifié est une variable d'articulation ou une variable de position, la variable de position de décalage est renvoyée : {pose = {x, y, z, rx, ry, rz}}.

**Exemple :**

```lua
-- Décaler P1 d'une certaine distance dans le système de coordonnées d’outils spécifié, puis se déplacer vers le point après décalage.
local Offset={OffsetX, OffsetY, OffsetZ, OffsetRx, OffsetRy, OffsetRz}
local p = RelPointTool(P1, Offset)
MovL(p)
```

<h3 class="lua-cmd" >RelMovJTool</h3>

**Prototype :**
```lua
RelMovJTool({x, y, z, rx, ry, rz}, {user = 1, tool = 0, a = 20, v = 50, cp = 100, stopcond = "expression"})
```

**Description :**

Effectue un mouvement relatif à partir de la position actuelle le long du système de coordonnées de l'outil spécifié dans un mouvement articulé. La trajectoire du mouvement de l'articulation n'est pas linéaire et toutes les articulations effectuent le mouvement en même temps.

**Paramètres obligatoires :**

{x, y, z, rx, ry, rz} : décalage du point cible par rapport à la position actuelle dans le système de coordonnées de l'outil spécifié. x, y, z indiquent le décalage spatial en mm ; rx, ry, rz indiquent le décalage angulaire en °.

**Paramètres facultatifs :**

- utilisateur : système de coordonnées de l'utilisateur pour le point cible.
- outil : système de coordonnées de l'outil au point cible.
- a : rapport d'accélération du mouvement du bras du robot lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].
- v : rapport de la vitesse du mouvement du bras lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].
- CP : Taux de transition lisse. Plage de valeurs : [0,&nbsp;100].
- stopcond : expression de la condition d'arrêt ; lorsque cette condition est remplie, le mouvement en cours est interrompu et l'instruction suivante est exécutée.

Pour plus de détails, veuillez vous reporter à la [description générale](common.md).

**Exemple :**

```lua
-- Le bras robotique se déplace en suivant les paramètres par défaut le long des axes articulaires du système de coordonnées d’outils global jusqu'au point de décalage spécifié.
RelMovJTool({10, 10, 10, 0, 0, 0})
```

Pour plus d'exemples relatifs aux paramètres facultatifs, veuillez vous reporter à MovJ.

<h3 class="lua-cmd" >RelMovLTool</h3>

**Prototype :**

```lua
RelMovLTool({x, y, z, rx, ry, rz}, {user = 1, tool = 0, a = 20, v = 50, speed = 500, cp = 100, r = 5, stopcond = "expression"})
```

**Description :**

Effectuer un mouvement relatif à partir de la position actuelle le long du système de coordonnées de l'outil spécifié dans un mouvement linéaire.

**Paramètres obligatoires :**

{x, y, z, rx, ry, rz} : décalage du point cible par rapport à la position actuelle dans le système de coordonnées de l'outil spécifié. x, y, z indiquent le décalage spatial en mm ; rx, ry, rz indiquent le décalage angulaire en °.

**Paramètres facultatifs :**

- utilisateur : système de coordonnées de l'utilisateur pour le point cible.

- outil : système de coordonnées de l'outil au point cible.

- a : rapport d'accélération du mouvement du bras du robot lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].

- v : rapport de la vitesse du mouvement du bras lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].

- vitesse : la vitesse cible de mouvement du bras robotique lors de l’exécution de cette instruction, avec une plage de valeurs : [1, vitesse maximale de mouvement], unité : mm/s.
  
  Une fois ce paramètre défini, le paramètre v est ignoré.

- CP : Taux de transition lisse. Plage de valeurs : [0,&nbsp;100].

- r : rayon de transition lisse, plage de valeurs : [0,100], unité : mm.
  
  Lorsque ce paramètre est défini, le paramètre cp est ignoré.

- stopcond : expression de la condition d'arrêt ; lorsque cette condition est remplie, le mouvement en cours est interrompu et l'instruction suivante est exécutée.

Pour plus de détails, veuillez vous reporter à la [description générale](common.md).

**Exemple :**

```lua
-- Le bras robotique se déplace en suivant les paramètres par défaut le long des axes linéaires du système de coordonnées d’outils global jusqu'au point de décalage spécifié.
RelMovLTool({10, 10, 10, 0, 0, 0})
```

Pour plus d'exemples relatifs aux paramètres facultatifs, voir MovL.

<h3 class="lua-cmd" >RelMovJUser</h3>

**Prototype :**

```lua
RelMovJUser({x, y, z, rx, ry, rz}, {user = 1, tool = 0, a = 20, v = 50, cp = 100, stopcond = "expression"})
```

**Description :**

Mouvement relatif à partir de la position actuelle le long du système de coordonnées de l'utilisateur spécifié dans le cadre d'un mouvement conjoint. La trajectoire du mouvement de l'articulation n'est pas linéaire et toutes les articulations effectuent le mouvement en même temps.

**Paramètres obligatoires :**

{x, y, z, rx, ry, rz} : décalage du point cible par rapport à la position actuelle dans le système de coordonnées de l'utilisateur spécifié. x, y, z indiquent le décalage spatial en mm ; rx, ry, rz indiquent le décalage angulaire en °.

**Paramètres facultatifs :**

- utilisateur : système de coordonnées de l'utilisateur pour le point cible.
- outil : système de coordonnées de l'outil au point cible.
- a : rapport d'accélération du mouvement du bras du robot lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].
- v : rapport de la vitesse du mouvement du bras lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].
- CP : Taux de transition lisse. Plage de valeurs : [0,&nbsp;100].
- stopcond : expression de la condition d'arrêt ; lorsque cette condition est remplie, le mouvement en cours est interrompu et l'instruction suivante est exécutée.

Pour plus de détails, veuillez vous reporter à la [description générale](common.md).

**Exemple :**

```lua
-- Le bras robotique se déplace en suivant les paramètres par défaut le long des axes articulaires du système de coordonnées d’utilisateurs global jusqu'au point de décalage spécifié.
RelMovJUser({10, 10, 10, 0, 0, 0})
```

Pour plus d'exemples relatifs aux paramètres facultatifs, veuillez vous reporter à MovJ.

<h3 class="lua-cmd" >RelMovLUser</h3>

**Prototype :**

```lua
RelMovLUser({x, y, z, rx, ry, rz}, {user = 1, tool = 0, a = 20, v = 50, speed = 500, cp = 100, r = 5, stopcond = "expression"})
```

**Description :**

Mouvement relatif à partir de la position actuelle le long du système de coordonnées de l'utilisateur spécifié dans un mouvement linéaire.

**Paramètres obligatoires :**

{x, y, z, rx, ry, rz} : décalage du point cible par rapport à la position actuelle dans le système de coordonnées de l'utilisateur spécifié. x, y, z indiquent le décalage spatial en mm ; rx, ry, rz indiquent le décalage angulaire en °.

**Paramètres facultatifs :**

- utilisateur : système de coordonnées de l'utilisateur pour le point cible.

- outil : système de coordonnées de l'outil au point cible.

- a : rapport d'accélération du mouvement du bras du robot lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].

- v : rapport de la vitesse du mouvement du bras lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].

- vitesse : la vitesse cible de mouvement du bras robotique lors de l’exécution de cette instruction, avec une plage de valeurs : [1, vitesse maximale de mouvement], unité : mm/s.
  
  Une fois ce paramètre défini, le paramètre v est ignoré.

- CP : Taux de transition lisse. Plage de valeurs : [0,&nbsp;100].

- r : rayon de transition lisse, plage de valeurs : [0,100], unité : mm.
  
  Lorsque ce paramètre est défini, le paramètre cp est ignoré.

- stopcond : expression de la condition d'arrêt ; lorsque cette condition est remplie, le mouvement en cours est interrompu et l'instruction suivante est exécutée.

Pour plus de détails, veuillez vous reporter à la [description générale](common.md).

**Exemple :**

```lua
-- Le bras robotique se déplace en suivant les paramètres par défaut le long des axes linéaires du système de coordonnées d’utilisateurs global jusqu'au point de décalage spécifié.
RelMovLUser({10, 10, 10, 0, 0, 0})
```

Pour plus d'exemples relatifs aux paramètres facultatifs, voir MovL.

<h3 class="lua-cmd" >RelJointMovJ</h3>

**Prototype :**

```lua
RelJointMovJ({Offset1, Offset2, Offset3, Offset4, Offset5, Offset6}, {a = 20, v = 50, cp = 100})
```

**Description :**

Déplacement de la position actuelle en mouvement articulé vers l'angle de décalage de l'articulation spécifié.

**Paramètres obligatoires :**

{Offset1, Offset2, Offset3, Offset4, Offset5, Offset6} : valeur du décalage dans la direction de l'axe J1 ~ axe J6 dans le système de coordonnées de l'articulation, unité : °.

**Paramètres facultatifs :**

- a : rapport d'accélération du mouvement du bras du robot lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].
- v : rapport de la vitesse du mouvement du bras lors de l'exécution de cette instruction. Plage de valeurs : (0,&nbsp;100].
- CP : Taux de transition lisse. Plage de valeurs : [0,&nbsp;100].

Pour plus de détails, veuillez vous reporter à la [description générale](common.md).

**Exemple :**

```lua
-- Le bras robotique se déplace en suivant les paramètres par défaut le long des axes articulaires jusqu'à l’angle de décalage spécifié.
RelJointMovJ({20,20,10,0,10,0})
```

<h3 class="lua-cmd" >RelJoint</h3>

**Prototype :**

```lua
RelJoint(P, {Offset1, Offset2, Offset3, Offset4, offset5, offset6})
```

**Description :**

Ajouter le décalage de l'axe J1~J6 au point spécifié dans le système de coordonnées de l'articulation et renvoyer la variable de l'articulation après le décalage.

**Paramètres obligatoires :**

- P : Le point spécifié à décaler.
- Offset1~Offset6 : la valeur de l'offset dans la direction de l'axe J1 ~ l'axe J6 sous le système de coordonnées de l'articulation, unité : °.

**Retour :**

Variable d'articulation après décalage : {joint = {j1, j2, j3, j4, j5, j6}}.

**Exemple :**

```lua
-- Décaler P1 d'un certain angle respectivement sur les axes J1 à J6, puis se déplacer vers le point après décalage.
local Offset = {Offset1, Offset2, Offset3, Offset4, offset5, offset6}
local p = RelJoint(P1, Offset)
MovJ(p)
```