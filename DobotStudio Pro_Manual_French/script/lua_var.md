# Type de la variable et donnée

Les variables sont utilisées pour stocker des valeurs, qui sont transmises en tant qu'arguments ou renvoyées en tant que résultats. Les variables sont assignées avec "=".

En Lua, les variables explicitement déclarées avec local sont des variables locales (effectives pour la fonction en cours), et les variables locales sont cadrées depuis l'emplacement de leur déclaration jusqu'à la fin de la fonction dans laquelle elles sont utilisées.

Les variables qui ne sont pas explicitement déclarées avec local sont des variables de niveau script (effectives pour le fichier de script en cours), et les variables de niveau script sont limitées à un seul fichier de script.

En outre, vous pouvez définir des variables globales au niveau du contrôleur, qui peuvent être appelées directement à partir de différents fichiers de script au sein du même contrôleur, via la page **Surveillance > Variables globales** dans DobotStudio Pro.

<div align=center><img src="../monitoring/image/global_var.png" width="600" /></div>

<br/>

**Exemple 1** : Cet exemple illustre la différence entre les variables locales et les champs d'application des variables au niveau du script.

```lua
function func()     -- Définir une fonction, qui imprime a et b lors de son exécution
    local a = 1     -- Variable locale
    b = 2           -- Variable au niveau du script
       
end

func()            -- Exécuter la fonction, imprimer a et b avec des valeurs respectives de 1 et 2
print(a)          --> nil (appel de variable en dehors de son scope, imprime nil, de même pour les suivants)
print(b)          --> 2
```

**Exemple 2** : Cet exemple montre que les variables locales peuvent avoir le même nom que les variables de niveau script, mais qu'elles ne sont valables qu'à l'intérieur d'une fonction. Les fonctions Do/end et les autres contrôles de flux (boucle, jugement conditionnel) du bloc de code appartiennent également à la fonction.

```lua
a = "a"

for i=10,1,-1 do
do
    local a = 6     -- Variable locale
    print(a)        --> 6, l’appel dans le bloc fait référence à la variable locale a
end

print(a)        --> a, l’appel en dehors du bloc fait référence à la variable a au niveau du script
```

**Exemple 3** : Cet exemple illustre la différence entre les variables globales et les deux autres types de champs d'application des variables, ainsi que la fonction de maintien global des variables globales.

```lua
-- Fichier src0.lua du projet 1
-- Supposons qu’on ait ajouté deux variables globales g1 et g2 sur la page des variables globales
-- g1 n’est pas en maintenir globalement, valeur de 10
-- g2 est en maintenir globalement, valeur de 20

local a = 1
b = 2
print(a)        --> 1
print(b)        --> 2

print(g1)           --> 10
print(g2)           --> 20
SetGlobalVariable("g1",11)  -- Assigner une valeur à une variable globale qui n'est pas en Maintenir globalement
SetGlobalVariable("g2",22)  -- Assigner une valeur à une variable globale qui est en Maintenir globalement
print(g1)           --> 11
print(g2)           --> 22

-- Fichier src0.lua du projet 2
-- Le projet 2 s'exécute après le projet 1

print(a)        --> nil
print(b)        --> nil
print(g1)       --> 10 (les variables non en Maintenir globalement sont restaurées à leur valeur avant la modification dans le projet 1)
print(g2)       --> 22 (les variables en Maintenir globalement deviennent la valeur après la modification dans le projet 1)
```

Les noms de variables peuvent être des lettres non numériques, des traits de soulignement et des chiffres de la chaîne, à l'exception des mots-clés réservés de Lua.

Les variables Lua ne nécessitent pas de définition de type ; il suffit d'assigner une valeur à la variable, et Lua détermine automatiquement le type de la variable en fonction de la valeur. L'affectation d'un type de valeur différent à une variable assignée dans un script modifiera le type de la variable ; toutefois, les variables définies dans la page **Surveillance > Variables globales** ne peuvent pas voir leur type modifié, et le type de la valeur assignée doit être le même que le type sélectionné lors de la création de la variable, sinon le contrôleur signalera une erreur lors de l'exécution du script.

Lua prend en charge divers types de données, notamment les nombres, les booléens, les chaînes de caractères et les tableaux. En Lua, un tableau est un type de table.

Lua dispose également d'un type de données spécial, nil, qui signifie nul (sans aucune valeur valide). Par exemple, si vous imprimez une variable à laquelle aucune valeur n'a été attribuée, vous obtiendrez une valeur nulle.

### Chiffre

Un nombre en Lua est un nombre réel à virgule flottante en double précision qui prend en charge une variété d'opérations, et qui est traité comme un nombre de la manière suivante :

- 2
- 2,2
- 0,2
- 2e+1
- 0.2e-1
- 7.8263692594256e-06

### Booléen

Le type booléen n'a que deux valeurs optionnelles : true et false. Lua traite false et nil comme faux, tout le reste est vrai, et le nombre 0 est également vrai.

### Chaîne de caractères

Une chaîne est une chaîne de caractères composée de chiffres, de lettres et de caractères de soulignement. Une chaîne peut être représentée de trois manières différentes :

- Une chaîne de caractères entre guillemets simples.
- Une chaîne de caractères entre guillemets doubles.
- Une chaîne de caractères entre **[[** et **]]**.

Lorsque des opérations arithmétiques sont effectuées sur une chaîne numérique, Lua tente de convertir la chaîne en un nombre.

```lua
-- Définir une chaîne de caractères avec des apostrophes
local str1 = 'Hello, Lua!'
print(str1)  -- Imprimer : Hello, Lua!

-- Définir une chaîne de caractères avec des doubles quotes
local str2 = "Hello, Lua!"
print(str2)  -- Imprimer : Hello, Lua!

-- Définir une chaîne de caractères multilignes avec [[ et ]]
local str3 = [[
This is a multi-line
string in Lua.
]]
print(str3)  
-- Imprimer :
-- This is a multi-line
-- string in Lua.

-- Lua convertit automatiquement les chaînes numériques en chiffres pour les opérations arithmétiques
local numStr = "10"
local result = numStr + 20  -- Convertit automatiquement “10” en chiffre 10
print(result)  -- Imprimer : 30
```

### Tableau

Un tableau est un ensemble indexé de données.

- La manière la plus simple de construire un tableau est {}, qui est utilisé pour créer un tableau vide, ou vous pouvez initialiser le tableau directement.

- Le tableau est en fait un tableau associatif et peut être indexé par n'importe quel type de valeur, mais cette valeur ne peut pas être nulle.

- La taille du tableau n'est pas fixe, vous pouvez l'agrandir en fonction de vos besoins.

- La longueur du tableau peut être obtenue en utilisant le symbole #.
  
  ```lua
  -- Initialiser une table avec des index continus
  local tbl = {[1] = 2, [2] = 6, [3] = 34, [4] = 5}
  print("Longueur de tbl ", #tbl) – Imprimer : 4
  ```

Dans cet exemple, les indices `[1]` à `[4]` de `tbl` sont consécutifs, la longueur `#tbl` est donc renvoyée correctement `4`.

### Tableau de données

Un tableau est une collection d'éléments du même type de données disposés dans un certain ordre, qui peut être un tableau unidimensionnel ou multidimensionnel.

En Lua, les tableaux sont de type `table`, les clés d'index peuvent être représentées par des entiers et la taille d'un tableau n'est pas fixe.

- Tableaux unidimensionnels : les tableaux les plus simples, dont la structure logique est un tableau linéaire.
- Tableaux multidimensionnels : c'est-à-dire que les tableaux contiennent des tableaux ou des tableaux unidimensionnels dont les clés d'indexation correspondent à un tableau.

En Lua, la valeur de l'index d'un tableau commence à 1 par défaut, mais vous pouvez spécifier qu'elle commence à 0 ou à un nombre négatif. L'accès à un élément de tableau avec un index inexistant renvoie nil.

**Exemple 1** : Un tableau unidimensionnel peut être accédé en parcourant les éléments du tableau à l'aide de for.

```lua
-- Créer un tableau unidimensionnel
local array = {"Lua", "Tutorial"} 

-- Utiliser une boucle for pour parcourir le tableau, en commençant à l’index 1
for i = 1, #array do   
    print(array[i])    -- Imprimer : Lua Tutorial
end
```

**Exemple 2** : tableau unidimensionnel avec des éléments numériques

```lua
-- Créer un tableau unidimensionnel dont les éléments internes sont des chiffres
local numbers = {10, 20, 30, 40, 50}  

-- Utiliser une boucle for pour parcourir le tableau, en commençant à l’index 1
for i = 1, #numbers do   
    print(numbers[i])    -- Imprimer : 10 20 30 40 50
end
```

**Exemple 3** : un tableau avec un index personnalisé

```lua
-- Créer un tableau et utiliser des index négatifs et positifs
local array = {} 
for i = -2, 2 do
    array[i] = i * 2 + 1  -- Assigner une valeur au tableau
end

-- Utiliser une boucle for pour parcourir le tableau, avec des index de -2 à 2
for i = -2, 2 do
    print(array[i])  -- Imprimer : -3 -1 1 3 5
end
```

**Exemple 4** : un tableau multidimensionnel à trois lignes et trois colonnes

```lua
-- Initialiser le tableau
array = {}
for i=1,3 do
 array[i] = {}
    for j=1,3 do
      array[i][j] = i*j
    end
end

-- Accéder au tableau
for i=1,3 do
  for j=1,3 do
     print(array[i][j])     --Les résultats imprimés sont respectivement : 1 2 3 2 4 6 3 6 9
  end
end
```