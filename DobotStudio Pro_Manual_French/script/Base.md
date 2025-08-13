# Concepts de base

<div class="info1"><img src="images/info.png"  height="18" /><b> Description : </b><div>Si vous souhaitez apprendre systématiquement les connaissances relatives à la programmation Lua, veuillez rechercher des tutoriels Lua sur Internet. Ce manuel présente une sélection de syntaxes de base de Lua, afin de vous permettre de consulter rapidement les informations dont vous avez besoin. </div></div>

<br/>

### Identification

Une identification est utilisée pour définir une variable, une fonction ou un autre élément défini par l'utilisateur. Une identification commence par une lettre de A à Z ou de a à z ou un trait de soulignement **_** suivi de 0 ou plusieurs lettres, traits de soulignement et chiffres (0 à 9).

Il est préférable de ne pas utiliser le trait de soulignement et les lettres majuscules, comme le font les mots réservés de Lua.

Lua n'autorise pas l'utilisation de caractères spéciaux tels que **@**, **$**, et **%** pour définir des identifications.

**Lua est un langage de programmation sensible à la casse, et la casse de tous les identificateurs d'un programme doit être conforme aux exemples fournis dans ce manuel.**

### Mots-clés

Voici une liste des mots-clés réservés de Lua. Les mots-clés réservés ne peuvent pas être utilisés comme constantes, variables ou autres identifiants définis par l'utilisateur :

**and, break,  do,  else, elseif, end, false ,for, function, if ,  in , local, nil, not, or, repeat, return, then, true, until, while, goto**

Une convention générale veut que les noms qui commencent par un trait de soulignement relié à une chaîne de lettres majuscules (par exemple_VERSION) soient réservés aux variables globales internes de Lua.

### Commentaire

Les commentaires n'affectent pas l'exécution du programme, et sont principalement utilisés pour aider les personnes qui lisent le code à le comprendre.

**Commentaires sur une seule ligne**

Dans un code à une ligne, tout ce qui se trouve après deux signes moins est considéré comme un commentaire. Les commentaires peuvent se trouver sur une ligne séparée ou suivre le code.

```lua
-- Commentaires sur une seule ligne
print("Hello World！")  -- Commentaires sur une seule ligne
```

**Commentaires sur plusieurs lignes**

Les commentaires sur plusieurs lignes commencent par "--[[" et se terminent par " --]]", et tout ce qui se trouve entre les deux est considéré comme un commentaire.

```lua
--[[
 Commentaires sur plusieurs lignes
 Commentaires sur plusieurs lignes
 --]]
```