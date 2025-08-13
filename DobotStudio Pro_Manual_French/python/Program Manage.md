# Contrôle du processus

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

Les fonctions de contrôle du programme sont des fonctions générales liées au contrôle du fonctionnement du programme.

| Instruction| Fonction|
|----------|----------|
| [Imprimer](#print)| Imprime des informations de débogage sur la console.|
| [Attendre](#wait)| Attendre pendant une période de temps spécifiée ou jusqu'à ce qu'une condition spécifiée soit remplie avant de passer à la commande suivante.|
| [Pause](#pause)| Suspendre l’exécution du script|
| [Réinitialiser le temps écoulé](#resetelapsedtime)| Réinitialiser le comptage-temps|
| [Temps écoulé](#elapsedtime)| Terminer le comptage-temps|
| [Systime](#systime)| Obtenir l'heure du système|

<h3 class="lua-cmd" >Print</h3>

**Prototype :**

```python
Print(value)
```

**Description :**

Imprime des informations de débogage sur la console (le nom de la commande peut également être écrit comme `print`).

**Paramètres obligatoires :**

valeur : les données à imprimer.

**Exemple :**

```python
# Imprimer la chaîne de caractères Success sur la console.
Print('Success')
```

<h3 class="lua-cmd" >Wait</h3>

**Prototype :**

```python
Wait(time_ms)
Wait(check_str)
Wait(check_str, timeout_ms)
```

**Description :**

Une fois que le bras robotique a terminé la commande précédente, attendez le temps spécifié ou remplissez les conditions spécifiées avant de poursuivre l'exécution de la commande suivante.

**Paramètres obligatoires :**

- time_ms : lorsque la valeur du paramètre est de type entier, il s'agit de spécifier le temps d'attente, lorsqu'il est inférieur ou égal à 0, il s'agit de ne pas attendre. Unité : ms
- check_str : si la valeur du paramètre est une chaîne de caractères, il s'agit d'une logique de jugement, la logique est vraie avant de continuer à exécuter la commande suivante.

**Paramètres facultatifs :**

timeout_ms : délai d'attente. Unité : ms.

- Si la logique de jugement est toujours fausse et que le temps d'attente dépasse ce délai, le système continuera à exécuter l'instruction suivante et renverra un message faux.
- S'il est inférieur ou égal à 0, cela signifie qu'il n'y a pas d'attente et que le délai d'attente est immédiatement respecté.
- Si ce paramètre n'est pas défini, il n'y aura pas de délai d'attente et le système attendra jusqu'à ce que la logique de jugement soit vraie.

**Retour :**

- Si la condition est remplie et que l'exécution se poursuit, vraie est renvoyé.
- Si la condition n'est pas remplie et que l'exécution se poursuit en raison d'un dépassement de délai, fausse est renvoyé.

**Exemple :**

```python
# Attendre 300 ms.
Wait(300)
```

```python
# Continuer à fonctionner lorsque DI1 est sur ON.
Wait("DI(1) == ON")
```

```python
# Continuer à fonctionner lorsque DO1 est sur ON et AI(1) est inférieur à 7.
Wait("GetDO(1) == ON and AI(1) < 7")
```

```python
# Exécuter des logiques d'affaires différentes en fonction de l'état de DI1 au cours de 1 seconde.
if Wait("DI(1) == ON", 1000):
    # L’état de DI1 est sur ON.
else：
    # L'état de DI1 est sur OFF et le délai dépasse 1 seconde.
```

<h3 class="lua-cmd" >Pause</h3>

**Prototype :**

```python
Pause()
```

**Description :**

Suspendre l’exécution du script. Doit être commandé par un logiciel de contrôle ou une télécommande pour continuer à fonctionner.

**Exemple :**

```python
# Le bras robotique s'arrête après avoir atteint le point P1, et ne continue à fonctionner vers le point P2 qu'après avoir reçu un contrôle externe pour reprendre l'exécution.
MovJ(P1)
Pause()
MovJ(P2)
```

<h3 class="lua-cmd" >ResetElapsedTime</h3>

**Prototype :**

```python
ResetElapsedTime()
```

**Description :**

Commence à chronométrer l'exécution de toutes les instructions avant cette instruction, doit être utilisé avec ElapsedTime(), peut être utilisé pour calculer le temps d'exécution.

**Exemple :**

Veuillez vous référer à l'exemple de ElapsedTime.

<h3 class="lua-cmd" >ElapsedTime</h3>

**Prototype :**

```python
ElapsedTime()
```

**Description :**

Fin du chronométrage, renvoi de la différence de temps, à utiliser avec ResetElapsedTime().

**Retour :**

Différence de temps entre l'heure de début et l'heure de fin, en millisecondes. Le maximum peut être compté 4294967295ms (environ 49,7 jours), après avoir dépassé ce temps, le décompte recommence à partir de 0.

**Exemple :**

```python
# Calculer le temps que le bras robotique mettra pour se déplacer du point actuel à P2 via P1, puis l’imprimer dans la console.
ResetElapsedTime()
MovL(P1)
MovL(P2)
print(ElapsedTime())
```

<h3 class="lua-cmd" >Systime</h3>

**Prototype :**

```python
Systime()
```

**Description :**

Obtenir l'heure du système

**Retour :**

Horodatage Unix de l'heure actuelle du système, converti en millisecondes, c'est-à-dire le nombre de millisecondes entre 00:00 GMT le 1er janvier 1970 et l'heure actuelle, généralement utilisé pour calculer le décalage horaire. Si vous avez besoin d'obtenir l'heure locale, veuillez utiliser la conversion de l'heure moyenne de Greenwich obtenue en fonction du fuseau horaire local.

**Exemple :**

```python
# Obtenir l’heure actuel du système.
time1 = Systime() 
print(time1)  # 1686304295963, converti en heure de Beijing est 09/06/2023 17:51:35 (ajout de 963 millisecondes).
time2 = Systime() 
print(time2)  # 1686304421968, converti en heure de Beijing est 09/06/2023 17:53:41 (ajout de 968 millisecondes).

# Calculer le temps du bras robotique met pour se déplacer jusqu'au point P1, unité : millisecondes.
time1 = Systime()
MovL(P1)
time2 = Systime()
print(time2-time1)
```