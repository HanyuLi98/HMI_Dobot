# Fonctions générales pour le traitement des chaînes de caractères

Lua fournit des fonctions générales pour la manipulation des chaînes de caractères, qui permettent d'effectuer des recherches, des substitutions et d'autres opérations.

### string.sub(s, i, j)

Utilisée pour intercepter la chaîne de caractères.

**Paramètres obligatoires**

- s : la chaîne à intercepter.
- i : le début de la position interceptée, à partir de 1.

**Paramètres facultatifs**

- j : la fin de la position interceptée, par défaut -1, c'est-à-dire le dernier caractère.

**Retour**

Intercepter la chaîne obtenue.

**Exemple**

```lua
sub1 = string.sub("abcde", 3)  --À partir du 3ème caractère, extraire : cde
sub2 = string.sub("abcde", 1, 3) --À partir du 1er jusqu’au 3ème caractère, extraire : cde
sub3 = string.sub("abcde", 3, 3) --3ème caractère, extraire : c
```

### string.find(s, sub, i, plain)

Trouve une sous-chaîne dans la chaîne spécifiée et renvoie l'index auquel elle a été trouvée.

**Paramètres obligatoires**

- s : la chaîne à trouver.
- sub : la sous-chaîne à trouver.

**Paramètres facultatifs**

- i : la position de départ de la recherche, la valeur par défaut est 1.
- plain : utilisation ou non du mode texte brut. Lorsque vous spécifiez ce paramètre, vous devez également spécifier le paramètre i.
  - vraie : utiliser le mode texte brut, la sous-chaîne sera traitée comme une chaîne de texte brut.
  - fausse : valeur par défaut, lorsque sub prend en charge le mécanisme de recherche de motifs.

**Retour**

- Les indices de début et de fin de la première sous-chaîne correspondante dans la chaîne originale.
- Si la capture est définie dans le motif, la valeur capturée est renvoyée après deux indices.
- Retourne nil si aucune sous-chaîne n'est trouvée.

**Exemple**

```lua
i,j = string.find("abcde", "cd")  --Rechercher cd dans abcde, retourner les indices : i est 3, j est 4

if string.find(str1, str2) ~= nil --Si str1 contient str2, exécuter le contenu de TODO.
  then
  --TODO
  end

--Utilisation avancée
i,j = string.find("abcabc", "ab", 3)  --Rechercher cd dans abcde, retourner les indices à partir du 3ème caractère : i est 4, j est 5

i,j = string.find("123%abc", "%a")  --Par défaut, le mécanisme de correspondance de motifs est activé, et le paramètre %a est interprété comme un caractère générique (représentant n’importe quel caractère). Par conséquent, il correspondra à la première lettre a dans la chaîne d’origine, avec i et j tous deux égaux à 5
i,j = string.find("123%abc", "%a", 1, true)  --En utilisant le mode texte brut, le paramètre %a est considéré comme du texte brut, il correspondra donc à %a dans la chaîne d’origine, avec i égal à 4 et j égal à 5.

i,j,sub = string.find("abc 10 edf 100", "(%d+)")  --Trouver et capturer la première séquence de chiffres, retourner les indices trouvés et le résultat capturé : i est 5, j est 6, sub est 10
```

### string.match(s, sub, i)

Recherche une sous-chaîne dans la chaîne spécifiée, renvoie la capture ou la sous-chaîne correspondant au motif.

**Paramètres obligatoires**

- s : la chaîne à trouver.
- sub : la sous-chaîne à rechercher, qui prend en charge le [mécanisme de correspondance des motifs](#pattern).

**Paramètres facultatifs**

- i : la position de départ de la recherche, la valeur par défaut est 1.

**Retour**

- Renvoie la sous-chaîne correspondante.
- Si la capture est définie dans le motif, renvoie toutes les captures.
- Retourne nil si aucune sous-chaîne n'est trouvée.

**Exemple**

```lua
sub1 = string.match("abcde", "cd")  --Rechercher cd dans abcde, retourner la sous-chaîne trouvée : cd 

sub2 = string.match("abc 10 edf 100", "%a+", 4)  --%a+ signifie une séquence continue de lettres, la recherche commence à partir du 4ème position, le résultat de la correspondance retourné est : edf

sub3 = string.match("abc 10 edf 100", "%a+ (%d+) %a+")  --Capturer le chiffre entre deux séquences de lettres, retourner le résultat capturé : 10
```

### string.gmatch(s, sub)

Boucle la chaîne spécifiée pour trouver une sous-chaîne, renvoyant la capture ou la sous-chaîne correspondant au motif.

**Paramètres obligatoires**

- s : la chaîne à trouver.
- sub : la sous-chaîne à rechercher, qui prend en charge le [mécanisme de correspondance des motifs](#pattern).

**Retour**

- Renvoie une fonction itérateur, chaque appel à cette fonction renvoie une correspondance.
- Si aucune correspondance n'est trouvée, la fonction itérateur renvoie nil.

**Exemple**

```lua
for word in string.gmatch("Hello world from dobot", "%a+") 
do 
    print(word)
end
--[[
 L’effet de l’exécution est d’imprimer chaque mot ligne par ligne :
 Hello
 world
 from
 dobot
 --]]
```

### string.gsub(s, find, repl, n)

Utilisée pour remplacer la partie spécifiée d'une chaîne de caractères.

**Paramètres obligatoires**

- s : la chaîne de caractères sur laquelle on travaille.
- find : le caractère à remplacer, sub prend en charge le [mécanisme de recherche de motifs](#pattern).
- repl : le caractère à remplacer.

**Paramètres facultatifs**

- n : le nombre maximum de remplacements. S'il n'est pas spécifié, cela signifie remplacer tout.

**Retour**

La chaîne de caractères à remplacer et le nombre de fois qu'elle doit être remplacée.

**Exemple**

```lua
str, n = string.gsub("aaaa","a","z"); --Remplacer tous les occurrences de a par z, retourner : str est zzzz, n est 4

str, n = string.gsub("aaaa","a","z",3); --Remplacer les 3 premières occurrences de a par z, retourner : str est zzza, n est 3

str, n = string.gsub("a1b2c3","%d","z"); --Remplacer tous les chiffres par z, retourner : str est azbzcz, n est 3
```

<h3 id="pattern">Mécanisme de correspondance de motifs</h3>

Le mécanisme de filtrage de Lua est similaire aux expressions régulières, qui peuvent être utilisées dans **string.find, string.gmatch, string.gsub, string.match** pour obtenir un filtrage flou.

**Caractère**

Les classes de caractères sont l'unité de base de la recherche de motifs et sont utilisées pour représenter une collection de caractères spécifiques. Les principales classes de caractères sont les suivantes :

- Caractère unique (except`^$()%.[]\*+-?`) : Correspond au caractère lui-même.
- `.` : Un seul point indique une correspondance avec n'importe quel caractère.
- `%a` : Lettre : Correspond à n'importe quelle lettre.
- `%c` : Correspond à n'importe quel caractère de contrôle (par exemple `\n`).
- `%d` : Caractère de contrôle (par exemple) : correspond à n'importe quel nombre.
- `%l` : Lettre minuscule : correspond à n'importe quelle lettre minuscule.
- `%p` : Correspond à toute ponctuation.
- `%s` : Correspond à un caractère vide (espace).
- `%u` : Correspond à n'importe quelle lettre majuscule.
- `%w` : Correspond à n'importe quelle lettre/chiffre.
- `%x` : Correspond à n'importe quel nombre hexadécimal.
- `%x`(où x est un caractère non alphabétique et non numérique) : correspond au caractère x. Cette fonction est principalement utilisée pour traiter les problèmes de correspondance avec des caractères spéciaux (`^$()%.[]*+-?`), tels que la correspondance `%%` avec `%`.
- `[Plusieurs classes de caractères]` : Correspondance avec n'importe quelle classe de caractères contenue dans n'importe quelle classe de caractères `[]`. Par exemple, une correspondance de `[%w_]` avec une lettre/un chiffre (`%w`) ou un trait de soulignement (`_`).
- `[^Plusieurs classes de caractères]` : Correspond à toute classe de caractères qui n'est pas contenue dans `[]`. Par exemple, `[^%s%p]` correspond à tout caractère autre qu'un espace blanc ou une ponctuation.

Toutes les classes représentées par une seule lettre (`%a`, `%c`, etc.), lorsqu'elles sont en majuscules, représentent le complément correspondant. Par exemple, `%S` représente tous les caractères sans espace.

**Mode**

Une entrée de modèle est une combinaison d'une classe de caractères et d'un symbole spécial qui spécifie le modèle de correspondance de la classe de caractères. Les entrées de motif couramment utilisées sont les suivantes :

- Une classe de caractères unique correspond à n'importe quel caractère de la classe ;
- Une classe de caractères unique suivie d'un `*` correspondra à zéro ou plusieurs caractères de cette classe. Cette entrée correspond toujours à la chaîne de caractères la plus longue possible ;
- Une classe de caractères unique suivie d'un `+`, correspondra à un ou plusieurs caractères de cette classe. Cette entrée correspond toujours à la chaîne de caractères la plus longue possible ;
- Une classe de caractères unique suivie d'un `-` correspondra à zéro ou plusieurs caractères de cette classe. Contrairement aux autres classes `*`, cette entrée correspond toujours à la chaîne la plus courte possible ;
- Une classe de caractères unique suivie d'un `?` correspondra à zéro ou un caractère de cette classe.
- `%n`, n désigne un nombre entier compris entre 1 et 9 ; cette entrée correspond à une sous-chaîne égale à la capture n (voir **Capture** plus loin).

**Mode**

Un motif est une séquence d'entrées de motifs. Exemple comme ci-dessous :

- Pour faire correspondre des dates au format **jj/mm/aaaa**, utilisez des motifs`%d%d/%d%d/%d%d%d%d`.
- Pour faire correspondre des mots dont les premières lettres sont en majuscules, utilisez le motif`%u%l+`.

**Capture**

Les motifs peuvent avoir un sous-motif interne entre parenthèses, ces sous-motifs sont appelés captures.

Lorsqu'une correspondance est réussie, la sous-chaîne correspondant à la capture est enregistrée et renvoyée ou utilisée dans une opération. Les captures sont numérotées dans l'ordre de leurs parenthèses gauches. Par exemple, pour le motif `(a*(.)%w(%s*))`:

- La chaîne de caractères correspondant à `a*(.)%w(%s*)` est la capture numéro 1.
- Les caractères correspondant à «&nbsp;`.`&nbsp;» sont la capture numéro 2.
- La chaîne correspondant à «&nbsp;`%s*`&nbsp;» est la capture numéro 3.
- Les captures 2 et 3 sont des sous-chaînes de la capture 1.

Dans un cas particulier, la valeur nulle `()` capturera la position du caractère correspondant dans la chaîne. Par exemple, si un motif `()aa()` est appliqué à la chaîne `flaaap`, deux captures sont produites : 3 et 5.

### Autres méthodes courantes

| Méthode| Description|
|----------|----------|
| string.upper (argument)| Convertit une chaîne de caractères en majuscules.|
| string.lower (argument)| string.lower (argument) Convertit toutes les chaînes en minuscules|
| string.reverse(arg)| Chaîne de caractères|
| string.format(...)| Retourne une chaîne formatée comme un printf.|
| string.len(arg)| Calcule la longueur d'une chaîne de caractères|
| string.rep(string, n)| Renvoie n copies de la chaîne.|

**Exemple :**

```lua
str = "Lua"
print(string.upper(str))       --Convertir toute la chaîne en majuscules, résultat imprimé : LUA.
print(string.lower(str))       --Convertir toute la chaîne en minuscules, résultat imprimé : lua
print(string.upper(str))       --Inverser la chaîne, résultat imprimé : auL
print(string.len("abc"))	   --Calculer la longueur de la chaîne abc, résultat imprimé : 3
print(string.format("the value is: %d",4))	 --résultat imprimé : the value is: 4
print(string.rep(str,2))       --Copier 2 fois la chaîne, résultat imprimé : LuaLua
```

### Autres opérateurs

| Symbole d’instruction| Description|
|----------|----------|
| ..| Joindre deux chaînes de caractères|
| # | Renvoie la longueur d'une chaîne ou d'un tableau|

```lua
a = "Hello "
b = "World"
c = {1,2,3}

print(a..b ) --Imprimer la chaîne résultant de la concaténation de a et b : Hello World

print(#b) --Imprimer la longueur de la chaîne b : 5

print(#b) --Imprimer la longueur de la table c : 3
```