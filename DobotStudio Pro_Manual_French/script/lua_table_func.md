# Fonctions générales pour la manipulation de tableaux

Lua fournit des fonctions générales pour la manipulation de tableaux, telles que l'insertion, le tri, etc. Le tableau utilisé dans les commandes suivantes doit être un tableau unaire contigu avec des index de 1 à n (n est la longueur du tableau) par défaut de Lua.

### table.concat (table, sep, start, end)

Concatène les éléments d'un tableau en une chaîne de caractères dans un ordre indexé, avec la possibilité de spécifier des séparateurs et des positions de début et de fin.

**Paramètres obligatoires**

- table : le tableau à manipuler.

**Paramètres facultatifs**

- sep : le séparateur. Par défaut, il n'y a pas de séparateur.
- début : position de départ. Valeur par défaut : 1.
- fin : position de fin. La valeur par défaut est la longueur du tableau.

**Retour**

Chaîne obtenue par épissage. Renvoie la chaîne vide si la position de départ est supérieure à la position d'arrivée.

**Exemple**

```lua
fruits = {"banana","orange","apple"}

print(table.concat(fruits)) --Utiliser la méthode par défaut pour concaténer, résultat imprimé : bananaorangeapple

print(table.concat(fruits,",")) --Spécifier un séparateur pour concaténer, résultat imprimé : banana,orange,apple

print(table.concat(fruits,",", 2,3)) --Spécifier un séparateur et des index pour concaténer, résultat imprimé : orange,apple
```

### table.insert (table, pos, value)

Insère l'élément spécifié dans le tableau à la position spécifiée.

**Paramètres obligatoires**

- table : le tableau à manipuler.
- valeur : l'élément à insérer.

**Paramètres facultatifs**

- pos : la position de l'insertion. La valeur par défaut est la longueur du tableau plus un, c'est-à-dire que l'élément est inséré à la fin du tableau.

**Exemple**

```lua
fruits = {"banana","orange","apple"}

table.insert(fruits,"mango") --Insérer à la fin
print(fruits[4])  --Résultat imprimé : mango

table.insert(fruits,2,"grapes") --Insérer à l’index 2
print(fruits[2],",",fruits[3]) --Résultat imprimé : grapes, orange
```

### table.remove(table, pos)

Supprime l'élément à la position spécifiée dans le tableau et renvoie la valeur supprimée.

**Paramètres obligatoires**

- table : le tableau à manipuler.

**Paramètres facultatifs**

- pos : la position de l'insertion. La valeur par défaut est la longueur du tableau, c'est-à-dire qu'elle est insérée à la fin du tableau.

**Retour**

La valeur est supprimée.

**Exemple**

```lua
fruits = {"banana","orange","apple"}

print(table.remove(fruits)) --Supprimer le dernier élément, imprimer l’élément supprimé : apple

print(table.remove(fruits),2) --Supprimer le deuxième élément, imprimer l’élément supprimé : orange
```

### table.sort(table, comp)

Trie les éléments du tableau, vous pouvez spécifier la méthode de tri.

**Paramètres obligatoires**

- table : le tableau à manipuler.

**Paramètres facultatifs**

- comp : la méthode de tri. Cet argument doit être une fonction qui répond aux exigences suivantes :
  
  - Elle peut prendre deux éléments du tableau comme arguments.
  - Retourne vrai si le premier paramètre doit précéder le second, sinon retourne faux.
  
  L'opérateur standard lua "<" est utilisé par défaut comme méthode de tri.

**Exemple**

```lua
fruits = {"banana","orange","apple","grapes"}

print("Avant le tri")
for k,v in ipairs(fruits) do
	print(v)         --Résultat imprimé : banana orange apple grapes
end

--Effectuer un tri croissant
table.sort(fruits)
print("Après le tri")
for k,v in ipairs(fruits) do
	print(v)         --Résultat imprimé : apple banana grapes orange
end

--Effectuer un tri décroissant
table.sort(fruits,function(a,b)
    return a > b
end)
print("Après le tri")
for k,v in ipairs(fruits) do
	print(v)         --Résultat imprimé : orange grapes banana apple
end
```