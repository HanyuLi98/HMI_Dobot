# Fonctions générales pour les calculs mathématiques

Lua fournit quelques fonctions mathématiques de base en complément des opérateurs arithmétiques.

### math.abs(X)

Renvoie la valeur absolue de X. Exemple :

```lua
print("math.abs(-10):", math.abs(-10))  -- Imprimer :  10
```

### math.floor(X)

Renvoie la plus grande valeur entière non supérieure à X (arrondi à l'inférieur), Exemple :

```lua
print("math.floor(3.7):", math.floor(3.7))  -- Imprimer :  3
```

### math.ceil(X)

Renvoie la plus petite valeur entière non inférieure à X (arrondi à l'unité supérieure), exemple : math.ceil(X)

```lua
print("math.ceil(3.2):", math.ceil(3.2))  -- Imprimer :  4
```

### math.sqrt(X)

Renvoie la racine carrée de X. Exemple :

```lua
print("math.sqrt(16):", math.sqrt(16))  -- Imprimer :  4
```

### math.rad(X)

Renvoie la valeur en radian de l'angle X (angle en radians), ex :

```lua
print("math.rad(180):", math.rad(180))  -- Imprimer :  3,1415926535898
```

### math.deg(X)

Renvoie la valeur en radians de l'angle X (radians à angle), ex :

```lua
print("math.deg(math.pi):", math.deg(math.pi))  -- Imprimer :  180
```

### math.sin(X)

Renvoie le sinus du radian X.

Si vous souhaitez utiliser un angle comme argument, utilisez la conversion math.rad, ex :

```lua
print("math.sin(math.rad(30)):", math.sin(math.rad(30)))  -- Imprimer :  0,5
```

### math.cos(X)

Renvoie le cosinus du radian X.

Si vous souhaitez utiliser un angle comme argument, utilisez la conversion math.rad, ex :

```lua
print("math.cos(math.rad(60)):", math.cos(math.rad(60)))  -- Imprimer :  0,5
```

### math.tan(X)

Renvoie la tangente du radian X.

Si vous souhaitez utiliser un angle comme argument, utilisez la conversion math.rad, ex :

```lua
print("math.tan(math.rad(45)):", math.tan(math.rad(45)))  -- Imprimer :  1
```

### math.asin(X)

Renvoie l'arcsinus de X en radians, qui peut être converti en angle à l'aide de math.deg, ex :

```lua
print("math.deg(math.asin(0.5)):", math.deg(math.asin(0.5)))  -- Imprimer :  30, la valeur de retour est l’angle
```

### math.acos(X)

Renvoie le cosinus inverse de X. La valeur de retour est en radians, ce qui peut être converti en angle à l'aide de math.deg, ex :

```lua
print("math.deg(math.acos(0.5)):", math.deg(math.acos(0.5)))  -- Imprimer :  60, la valeur de retour est l’angle
```

### math.atan(X)

Renvoie la tangente inverse de X. La valeur de retour est en radians et peut être convertie en angle à l'aide de math.deg, ex :

```lua
print("math.deg(math.atan(1)):", math.deg(math.atan(1)))  -- Imprimer :  45, la valeur de retour est l’angle
```

### math.log(X)

Renvoie le logarithme naturel de X, ex :

```lua
print("math.log(10):", math.log(10))  -- Imprimer :  2,302585092994
```

### math.exp(X)

Renvoie la puissance X de la constante naturelle e, ex :

```lua
print("math.exp(1):", math.exp(1))  -- Imprimer :  2,718281828459
```