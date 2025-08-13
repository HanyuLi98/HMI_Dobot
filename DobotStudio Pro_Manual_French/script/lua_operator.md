# Opérateurs

### Opérateurs arithmétiques

| Symbole d’instruction| Description|
|----------|----------|
| + | Addition|
| - | Soustraction|
| * | Multiplication|
| / | Division en virgule flottante|
| //| Division par arrondi à l'inférieur|
| % | Division par le reste|
| ^ | Exponentiation|

Exemple :

```lua
a=20				
b=5					
print(a+b)			--Imprimer le résultat de a plus b : 25		
print(a-b)			--Imprimer le résultat de a moins b : 15
print(a*b)			--Imprimer le résultat de a multiplié par b : 100
print(a/b)			--Imprimer le résultat de a divisé par b : 4
print(a//b)			--Imprimer le résultat de a divisé par b avec un quotient entier : 4
print(a%b)			--Imprimer le reste de a divisé par b : 0
print(a^b)			--Imprimer le résultat de a élevé à la puissance b : 3200000
```

### Opérateurs bit

| Symbole d’instruction| Description|
|----------|----------|
| &  | Bitwise et arithmétique|
| \  | Conjugaison|
| ~  | Bitwise différent ou|
| << | Décalage à gauche par sens binaire|
| >> | Décalage vers la droite par bit|

Exemple :

```lua
print(a&b)			--Imprimer le résultat de l’opération ET bits à bits de a et b : 4
print(a-b)			--Imprimer le résultat de l’opération OU bits à bits de a et b : 21
print(a~b)			--Imprimer le résultat de l’opération OU exclusif de a et b : 17
print(a<<b)			--Imprimer le résultat du décalage à gauche de a de b bits : 640
print(a>>b)			--Imprimer le résultat du décalage à droite de a de b bits : 0
```

### Opérateurs relationnels

| Symbole d’instruction| Description|
|----------|----------|
| == | Égal à|
| ~= | Différent de|
| <= | Inférieur ou égal à|
| >= | Supérieur ou égal à|
| <  | Inférieur à|
| >  | Supérieur à|

Exemple :

```lua
a=20				--Créer la variable a
b=5					--Créer la variable b
print(a==b)			--Imprimer le résultat de la comparaison a égal à b : false
print(a~=b)			--Imprimer le résultat de la comparaison a différent de b : true
print(a<=b)			--Imprimer le résultat de la comparaison a inférieur ou égal à b : false
print(a>=b)			--Imprimer le résultat de la comparaison a supérieur ou égal à b : true
print(a<b)			--Imprimer le résultat de la comparaison a inférieur à b : false
print(a>b)			--Imprimer le résultat de la comparaison a supérieur à b : true
```

### Opérateurs logiques

| Symbole d’instruction| Description|
|----------|----------|
| et| Opérateurs logiques Le résultat est vrai lorsque les deux côtés sont vrais ; si l'un des côtés est faux, le résultat est faux.|
| ou| Opérateur logique ou, lorsque l'un des côtés est vrai, le résultat est vrai ; tant que les deux côtés sont faux, le résultat est faux.|
| non| Non-opérateur logique, le résultat du jugement sera directement inversé.|

```lua
a=true					
b=false						
print(a and b)			-- Imprimer : false, a et b doivent tous les deux être true pour que le résultat soit true
print(a or b)			-- Imprimer : true, le résultat est true si au moins un de a ou b est true
print(not a)            -- Imprimer : false, a est true, donc sa négation est false
print(not b)            -- Imprimer : true, b est false, donc sa négation est true
print(not (20>5))     -- Imprimer : false, 20 > 5 est true, donc sa négation est false
```