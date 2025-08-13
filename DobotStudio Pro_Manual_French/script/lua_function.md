# Fonction

Les fonctions constituent la principale méthode d'abstraction des déclarations et des expressions et sont définies dans le format suivant :

```lua
function function_name(argument1, argument2, argument3..., argumentn)
    function_body
    return result_params_comma_separated
end
```

- **nom_de_la_fonction** : Nom de la fonction. Les fonctions peuvent être définies puis appelées par le nom de la fonction, ou directement définies au moment de l'appel ; dans ce dernier cas, le nom de la fonction peut être omis.
- **argument1, argument2, argument3... , argumentn :** Arguments de la fonction, plusieurs arguments séparés par des virgules. Les fonctions peuvent également être définies sans arguments.
- **function_body :** Le corps de la fonction, le bloc de code à exécuter dans la fonction.
- **result_params_comma_separated :** Les fonctions Lua peuvent renvoyer plusieurs valeurs, chacune étant séparée par une virgule. Les fonctions peuvent ne pas avoir de valeur de retour.

**Exemple 1** : fonction sans paramètres d'entrée ni valeur de retour

```lua
function greet()
    print("Hello, Lua!")  -- Corps de la fonction
end

greet()  -- Appeler la fonction, sortir : Hello, Lua!
```

**Exemple 2** : fonction avec paramètres d'entrée et sans valeur de retour

```lua
function printSquare(number)
    print("Square of " .. number .. " is " .. (number * number))  -- Corps de la fonction
end

printSquare(5) -- Appeler la fonction, sortir : Square of 5 is 25
```

**Exemple 3** : fonction avec paramètres d'entrée et valeur de retour

```lua
function maximum(a)
    local mi = 1  -- Index de la valeur maximale
    local m = a[mi]  -- Valeur maximale
    for i, val in ipairs(a) do
        if val > m then
            mi = i
            m = val
        end
    end
    return m, mi  -- Retourner la valeur maximale et l’index
end

local maxVal, maxIndex = maximum({8, 10, 23, 12, 5})
print("Max value:", maxVal)  -- Sortir :  Max value: 23
print("Index of max value:", maxIndex)  -- Sortir :  Index of max value: 3
```

<div class="info1"><img src="images/info.png"  height="18" /><b>Description : </b><div>Ce manuel principalement introduit l’utilisation des fonctions prédéfinies de Dobot, et les utilisateurs peuvent également définir leurs propres fonctions. Pour définir une fonction personnalisée, veuillez écrire la définition de la fonction dans le fichier global.lua ou en haut du fichier src*.lua qui appelle cette fonction. Sinon, une erreur se produira lors de l’exécution. </div></div>
