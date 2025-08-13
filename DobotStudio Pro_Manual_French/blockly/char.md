# Blocs de caractères

Les blocs de caractères contiennent des fonctions communes pour les chaînes de caractères et les tableaux.

<h3 class="lua-cmd" id="strn" >Obtenir le nième caractère d'une chaîne de caractères</h3>

![](images/char_first.png)

**Description:** Obtient le nième caractère de la chaîne utilisée comme variable.

**Paramètres :**

- Le premier argument remplit la chaîne, soit en utilisant d'autres blocs de construction elliptiques, soit directement.
- Le deuxième argument spécifie le nième caractère de la chaîne à retourner.

**Valeur de retour:** Le caractère à la position spécifiée dans la chaîne.

<h3 class="lua-cmd" id="strcontain" >Déterminer si la première chaîne contient la deuxième</h3>

![](images/char_contain.png)

**Description:** Détermine si la chaîne de caractères du premier paramètre contient la chaîne de caractères du second paramètre.

**Paramètres:** Les deux chaînes de caractères à juger, vous pouvez utiliser des blocs ovales avec la valeur de retour de la chaîne de caractères ou simplement les remplir.

**Valeur de retour:** Retourne vrai si la chaîne un contient la chaîne deux, sinon retourne faux.

<h3 class="lua-cmd" id="joinstr" >Joindre deux chaînes de caractères</h3>

![](images/char_joint.png)

**Description:** Séparer deux chaînes de caractères en une seule, la deuxième chaîne suivra la première.

**Paramètres:** Les deux chaînes de caractères à séparer, vous pouvez utiliser les blocs ovales avec la valeur de retour en tant que chaîne de caractères ou simplement les remplir.

**Valeur de retour:** La chaîne de caractères après l'épissage.

<h3 class="lua-cmd" id="strlen" >Longueur de la chaîne de caractères ou du tableau de donnée</h3>

![](images/char_length.png)

**Description:** Obtient la longueur de la chaîne ou du tableau spécifié. La longueur de la chaîne est le nombre de caractères qu'elle contient, et la longueur du tableau est le nombre d'éléments qu'il contient.

**Paramètres:** La chaîne ou le tableau dont la longueur doit être calculée ; un bloc elliptique avec une valeur de retour de chaîne ou de tableau peut être utilisé.

**Valeur de retour:** Longueur de la chaîne de caractères ou du tableau de donnée.

<h3 class="lua-cmd" id="strcomp" >Comparer deux chaînes de caractères</h3>

![](images/char_compare.png)

**Description:** Compare la taille de deux chaînes de caractères selon le code ACS II.

**Paramètres:** Deux chaînes à comparer, possibilité d'utiliser des blocs ovales dont la valeur de retour est une chaîne de caractères ou de les remplir.

**Valeur de retour:** Rend 0 si la chaîne un et la chaîne deux sont égales, -1 si la chaîne un est plus petite que la chaîne deux, et 1 si la chaîne un est plus grande que la chaîne deux.

<h3 class="lua-cmd" id="arrtostr" >Convertir un tableau de données en une chaîne de caractères</h3>

![](images/char_a_to_s.png)

**Description:** Convertit le tableau spécifié en une chaîne de caractères et utilise le séparateur spécifié pour séparer les différents éléments du tableau dans la chaîne. Par exemple, si le tableau est {1,2,3} et que le séparateur est |, la chaîne convertie est «&nbsp;1|2|3&nbsp;».

**Paramètres :**

- Pour convertir un tableau en chaîne de caractères, utilisez un bloc de construction elliptique dont la valeur de retour est le tableau.
- Le délimiteur utilisé pour la conversion.

**Valeur de retour:** La chaîne convertie.

<h3 class="lua-cmd" id="strtoarr" >Convertir une chaîne de caractères en un tableau de données</h3>

![](images/char_s_to_a.png)

**Description:** Convertit la chaîne spécifiée en un tableau, en séparant les chaînes selon le séparateur spécifié. Par exemple, si la chaîne est «&nbsp;1|2|3&nbsp;» et que le séparateur est |, le tableau converti est {[1]=1,[2]=2,[3]=3}.

**Paramètres :**

- Pour convertir un tableau en une chaîne de caractères, vous pouvez soit utiliser un bloc d'ellipse avec une valeur de retour d'une chaîne de caractères, soit l'entrer directement.
- Le délimiteur utilisé pour la conversion.

**Valeur de retour:** Le tableau converti.

<h3 class="lua-cmd" id="strind" >Obtenir l'élément d'un tableau avec un indice spécifié</h3>

![](images/char_index.png)

**Description:** Obtient l'élément à la position d'indice spécifiée dans le tableau spécifié. L'indice indique la position de l'élément dans le tableau, par exemple, l'indice de 8 dans le tableau {7,8,9} est 2.

**Paramètres :**

- Cible un tableau, en utilisant un bloc elliptique dont la valeur de retour est un tableau.
- Spécifie les indices des éléments.

**Valeur de retour:** La valeur de l'élément à la position spécifiée dans le tableau.

<h3 class="lua-cmd" id="strindn" >Obtenir plusieurs éléments spécifiés d'un tableau</h3>

![](images/char_traver.png)

**Description:** Obtient les éléments du tableau spécifié à plusieurs positions d'indice spécifiées. Obtient l'élément en fonction de la valeur du pas dans la plage de l'indice de début et de l'indice de fin.

**Paramètres :**

- Cible un tableau, en utilisant un bloc elliptique dont la valeur de retour est un tableau.
- La plage d'éléments à récupérer est spécifiée par l'indice de début et l'indice de fin.
- La valeur de l'étape est utilisée pour déterminer la fréquence à laquelle les éléments sont récupérés, 1 étant tous les éléments, 2 étant récupéré tous les deux éléments, et ainsi de suite.

**Valeur de retour:** Un nouveau tableau contenant les éléments spécifiés.

<h3 class="lua-cmd" id="strset" >Définir l'élément spécifié dans un tableau</h3>

![](images/char_set.png)

**Description:** Fixe la valeur de l'élément à la position d'indice spécifiée dans le tableau.

**Paramètres :**

- Cible un tableau, en utilisant un bloc elliptique dont la valeur de retour est un tableau.
- Spécifie les indices des éléments.
- Spécifie la valeur de l'élément.