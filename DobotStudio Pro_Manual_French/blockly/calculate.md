# Blocs opérationnels

Les blocs opérationnels sont utilisés pour effectuer des opérations sur des variables ou des constantes.

<h3 class="lua-cmd" id="alg" >Quatre opérations</h3>

![](images/calc_arithmetic.png)

**Description:** Effectue quatre opérations sur des paramètres.

**Paramètres :**

- Les deux côtés sont remplis avec les variables ou les constantes impliquées dans l'opération, soit en utilisant des blocs ovales avec des valeurs de retour numériques, soit directement.
- Au milieu, sélectionnez l'opérateur habituel.

**Valeur de retour:** Valeur numérique du résultat de l'opération.

<h3 class="lua-cmd" id="comp" >Comparaison</h3>

![](images/calc_compare.png)

**Description:** Opération de comparaison sur des paramètres.

**Paramètres :**

- Les deux côtés sont remplis avec les variables ou les constantes impliquées dans l'opération, soit en utilisant des blocs ovales avec des valeurs de retour numériques, soit directement.
- Au milieu, sélectionnez l'opérateur de comparaison.

**Valeur de retour:** Retourne vrai si le résultat de la comparaison est vrai et faux s'il est faux.

<h3 class="lua-cmd" id="and" >Et</h3>

![](images/calc_and.png)

**Description:** Effectue l'opération et sur les arguments.

**Paramètres:** Remplir les variables impliquées dans l'opération des deux côtés, en utilisant les autres blocs hexagonaux.

**Valeur de retour:** Retourne vrai si les deux arguments sont vrais, faux si l'un des deux est faux.

<h3 class="lua-cmd" id="or" >Ou</h3>

![](images/calc_or.png)

**Description:** Effectue une opération ou sur les arguments.

**Paramètres:** Remplir les variables impliquées dans l'opération des deux côtés, en utilisant les autres blocs hexagonaux.

**Valeur de retour:** Retourne vrai si l'un des deux arguments est vrai, faux si les deux sont faux.

<h3 class="lua-cmd" id="not" >Non-opérateurs</h3>

![](images/calc_not.png)

**Description:** Effectue une opération non arithmétique sur les arguments.

**Paramètres:** Remplir les variables impliquées dans l'opération des deux côtés, en utilisant les autres blocs hexagonaux.

**Valeur de retour:** renvoie false lorsque le paramètre est vrai, true lorsqu'il est faux.

<h3 class="lua-cmd" id="mod" >Reste</h3>

![](images/calc_rem.png)

**Description:** Effectue une opération de reste sur les paramètres.

**Paramètres:** Les deux côtés sont remplis avec les variables ou les constantes impliquées dans l'opération, soit en utilisant des blocs ovales avec des valeurs de retour numériques, soit directement.

**Valeur de retour:** Valeur numérique du résultat de l'opération.

<h3 class="lua-cmd" id="flo" >Arrondi</h3>

![](images/calc_round.png)

**Description:** Opération d'arrondi sur les paramètres.

**Paramètres:** Les deux côtés sont remplis avec les variables ou les constantes impliquées dans l'opération, soit en utilisant des blocs ovales avec des valeurs de retour numériques, soit directement.

**Valeur de retour:** Valeur numérique du résultat de l'opération.

<h3 class="lua-cmd" id="abs" >Opérations à valeur unique</h3>

![](images/calc_abs.png)

**Description:** Effectue diverses opérations à valeur unique sur les arguments. Les valeurs d'entrée trigonométriques (sin/cos/tan) et les valeurs de retour trigonométriques inverses (asin/acos/atan) sont des angles.

**Paramètres :**

- Sélectionne le type d'opération.
  
  - Circuit de valeur absolue
  - Arrondir à l'inférieur
  - Arrondir à la hausse
  - Racine carrée
  - sin
  - cos
  - tan
  - asin
  - asin
  - atan
  - atan
  - loh
  - e^
  - 10^

- Les deux côtés sont remplis avec les variables ou les constantes impliquées dans l'opération, soit en utilisant des blocs ovales avec des valeurs de retour numériques, soit directement.

**Valeur de retour:** Valeur numérique du résultat de l'opération.

<h3 class="lua-cmd" id="print" >Imprimer</h3>

![](images/calc_print.png)

**Description:** Affiche les paramètres sur la console, principalement à des fins de débogage.

**Paramètres :**

Les variables ou constantes à envoyer à la console peuvent utiliser d'autres blocs ellipse ou être remplies directement.