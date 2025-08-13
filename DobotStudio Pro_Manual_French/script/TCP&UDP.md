# TCP&UDP

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

Les fonctions TCP\&UDP sont utilisées pour la communication TCP ou UDP.

| Instruction| Fonction|
|----------|----------|
| [TCPCreate](#tcpcreate)| Crée un objet réseau TCP|
| [TCPStart](#tcpstart)| Établir un lien TCP|
| [TCPRead](#tcpread)| Recevoir des données via TCP|
| [TCPWrite](#tcpwrite)| Envoi de données à un homologue TCP|
| [TCPDestroy](#tcpdestroy)| Déconnecte la connexion TCP et détruit l'objet socket.|
| [UDPCreate](#udpcreate)| Créer un objet réseau UDP|
| [UDPRead](#udpread)| Recevoir des données envoyées par l'autre extrémité de l'UDP|
| [UDPWrite](#udpwrite)| Envoi de données à l'homologue UDP|

<h3 class="lua-cmd" >TCPCreate</h3>

**Prototype :**

```lua
TCPCreate(isServer, IP, port)
```

**Description :**

Création d'un objet réseau TCP, un seul peut être créé.

**Paramètres obligatoires :**

- isServer : crée ou non un serveur.
  
  - vraie : signifie créer un serveur.
  - fausse : signifie créer un client.

- IP : adresse IP du serveur. Elle doit se trouver dans le même segment de réseau que l'adresse IP du client et ne doit pas être en conflit.
  
  - Lors de la création d'un serveur, il s'agit de l'adresse IP du bras robotique.
  - Lors de la création d'un client, il s'agit de l'adresse de l'extrémité opposée.

- port : Port du serveur.
  
  N'utilisez pas les ports suivants qui sont déjà occupés par le système, ce qui entraînerait l'échec de la création du serveur.
  
  7, 13, 22, 37, 139, 445, 502, 503 (les ports entre 0 et 1024 sont des ports personnalisés du système linux, qui ont une forte probabilité d'être occupés, veuillez donc éviter de les utiliser autant que possible),
  
  1501, 1502, 1503, 4840, 8172, 9527,
  
  11740, 22000, 22001, 29999, 30004, 30005, 30006,
  
  60000~65504, 65506, 65511~65515, 65521, 65522。

**Retour :**

- err : 0 signifie que la création de l'objet réseau TCP a réussi, 1 signifie que la création de l'objet réseau TCP a échoué.
- socket : l'objet socket créé.

**Exemple 1 :**

```lua
-- Créer un serveur TCP.
local ip="192.168.5.1" -- L'adresse IP du bras robotique sert d'adresse IP du serveur
local port=6001 -- Port du serveur
local err=0
local socket=0
err, socket = TCPCreate(true, ip, port)
```

**Exemple 2 :**

```lua
-- Créer un client TCP.
local ip="192.168.5.25" -- L'adresse IP des équipements externes, tels que la caméra, sert d'adresse IP du serveur
local port=6001 -- Port du serveur
local err=0
local socket=0
err, socket = TCPCreate(false, ip, port)
```

<h3 class="lua-cmd" >TCPStart</h3>

**Prototype :**

```lua
TCPStart(socket, timeout)
```

**Description :**

Établir un lien TCP.

- Lorsque le bras robotique agit en tant que serveur, il attend que le client se connecte.
- Lorsque le bras robotique agit en tant que client, il prend l'initiative de se connecter au serveur.

**Paramètres obligatoires :**

- socket : objet socket créé.
- timeout : délai d'attente en secondes.
  - S'il est fixé à 0, il attendra que la connexion soit établie.
  - S'il n'est pas fixé à 0, il renverra l'échec de la connexion après avoir dépassé le délai fixé.

**Retour :**

Obtenir le résultat de la connexion de %1

- 0 : Connexion réussie.
- 1 : erreur de paramètre d'entrée.
- 2 : L'objet socket n'existe pas.
- 3 : Erreur de définition du délai d'attente.
- 4\. Poutre de liaison échouée.

**Exemple :**

```lua
-- Commencer à établir la connexion TCP, et attendre jusqu'à ce que la connexion soit établie avec succès.
err = TCPStart(socket, 0) -- socket est l'objet socket retourné avec succès par TCPCreate
```

<h3 class="lua-cmd" >TCPRead</h3>

**Prototype :**

```lua
TCPRead(socket, timeout, type)
```

**Description :**

Recevoir des données via TCP

**Paramètres obligatoires :**

socket : objet socket créé.

**Paramètres facultatifs :**

- timeout : délai d'attente en secondes.
  - S'il n'est pas défini ou s'il est défini à une valeur inférieure ou égale à 0, il attendra jusqu'à ce que les données soient lues et passera ensuite à l'exécution suivante.
  - S'il a une valeur supérieure à 0, il attendra que les données soient lues avant de passer à l'étape suivante.
- type : le type de valeur de retour.
  - S'il n'est pas défini ou s'il est défini à "table", le format de cache de RecBuf est une table.
  - Si la valeur est "string", RecBuf est mis en cache sous la forme d'une chaîne.

**Retour :**

- err : 0 signifie que la réception des données a réussi, 1 signifie que la réception des données a échoué.
- Recbuf : tampon de données de réception.

**Exemple :**

```lua
-- Recevoir les données TCP sans délai d’attente, et les données reçues sont sauvegardées sous forme de table.
-- socket est l'objet socket retourné avec succès par TCPCreate
err, RecBuf = TCPRead(socket) -- Le type de données de RecBuf est une table
```

```lua
-- Recevoir les données TCP avec un délai d’attente de 5 secondes, et les données reçues sont sauvegardées sous forme de table.
-- socket est l'objet socket retourné avec succès par TCPCreate
err, RecBuf = TCPRead(socket,5) -- Le type de données de RecBuf est une table
```

```lua
-- Recevoir les données TCP sans délai d’attente, et les données reçues sont sauvegardées sous forme de chaîne de caractères.
-- socket est l'objet socket retourné avec succès par TCPCreate
err, RecBuf = TCPRead(socket,0,"string") -- Le type de données de RecBuf est une chaîne de caractères
```

<h3 class="lua-cmd" >TCPWrite</h3>

**Prototype :**

```lua
TCPWrite(socket, buf, timeout)
```

**Description :**

Envoi de données à un homologue TCP.

**Paramètres obligatoires :**

- socket : objet socket créé.

- buf : données à envoyer.

**Paramètres facultatifs :**

timeout : délai d'attente en secondes.

- S'il n'est pas défini ou s'il est défini à 0, il attendra jusqu'à ce que l'autre extrémité ait fini de recevoir les données et passera ensuite à l'exécution suivante.
- S'il n'est pas fixé à 0, il attendra que l'autre extrémité ait reçu les données, puis passera à l'étape suivante.

**Retour :**

Résultat de l’envoi.

- 0 : Envoyé avec succès.
- 1 : Échec de l'envoi du courrier.

**Exemple :**

```lua
-- Envoyer des données via TCP, le contenu des données étant "test", sans délai d’attente.
TCPWrite(socket, "test") -- socket est l'objet socket retourné avec succès par TCPCreate
```

```lua
-- Envoyer des données via TCP, le contenu des données étant "test", avec un délai d’attente de 5 secondes.
TCPWrite(socket, "test", 5) -- socket est l'objet socket retourné avec succès par TCPCreate
```

<h3 class="lua-cmd" >TCPDestroy</h3>

**Prototype :**

```lua
TCPDestroy(socket)
```

**Description :**

Déconnexion de la connexion TCP et destruction de l'objet socket.

**Paramètres obligatoires :**

socket : objet socket créé.

**Retour :**

Résultat de l’exécution.

- 0 : Exécution réussie.
- 1 : Échec d'exécution.

**Exemple :**

```lua
-- Se déconnecter de l’extrémité opposée TCP.
TCPDestroy(socket) -- socket est l'objet socket retourné avec succès par TCPCreate
```

<h3 class="lua-cmd" >UDPCreate</h3>

**Prototype :**

```lua
UDPCreate(isServer, IP, port)
```

**Description :**

Création d'un objet réseau UDP, un seul peut être créé.

**Paramètres obligatoires :**

- isServer : crée ou non un serveur.
  - vraie : signifie créer un serveur.
  - fausse : signifie créer un client.
- IP : Indiquer l'adresse IP de l'autre extrémité lors de la création d'un serveur et d'un client. Elle doit se trouver dans le même segment de réseau que l'adresse IP du bras robotique et ne doit pas être en conflit.
- port :
  - Indique le port à utiliser par l'extrémité locale et l'extrémité opposée lors de la création de l'extrémité serveur. Veuillez ne pas utiliser le port qui a été occupé par le système, voir la description des paramètres de TCPCreate pour plus de détails.
  - Lors de la création d'un client, il s'agit du port de l'extrémité opposée. Dans ce cas, cette extrémité utilisera un port aléatoire lors de l'envoi de données.

**Retour :**

- err : 0 signifie que la création de l'objet réseau UDP a réussi, 1 signifie que la création de l'objet réseau UDP a échoué.
- socket : l'objet socket créé.

**Exemple 1 :**

```lua
-- Créer un serveur UDP.
local ip="192.168.5.25" -- L'adresse IP des équipements externes, tels que la caméra, sert d'adresse IP de l’extrémité opposée
local port=6001 -- Le port est utilisé par l'extrémité locale et l'extrémité opposée
local err=0
local socket=0
err, socket = UDPCreate(true, ip, port)
```

**Exemple 2 :**

```lua
-- Créer un client UDP.
local ip="192.168.5.25" -- L'adresse IP des équipements externes, tels que la caméra, sert d'adresse IP de l’extrémité opposée
local port= 6001-- Port de l’extrémité opposée
local err=0
local socket=0
err, socket = UDPCreate(false, ip, port)
```

<h3 class="lua-cmd" >UDPRead</h3>

**Prototype :**

```lua
UDPRead(socket, timeout, type)
```

**Description :**

Réception des données envoyées par l'homologue UDP.

**Paramètres obligatoires :**

socket : objet socket créé.

**Paramètres facultatifs :**

- timeout : délai d'attente en secondes.
  - S'il n'est pas défini ou s'il est défini à une valeur inférieure ou égale à 0, il attendra jusqu'à ce que les données soient lues et passera ensuite à l'exécution suivante.
  - S'il a une valeur supérieure à 0, il attendra que les données soient lues avant de passer à l'étape suivante.
- type : le type de valeur de retour.
  - S'il n'est pas défini ou s'il est défini à "table", le format de cache de RecBuf est une table.
  - Si la valeur est "string", RecBuf est mis en cache sous la forme d'une chaîne.

**Retour :**

- err : 0 signifie que la réception des données a réussi, 1 signifie que la réception des données a échoué.
- Recbuf : tampon de données de réception.

**Exemple :**

```lua
-- Recevoir les données UDP, et les données reçues sont respectivement sauvegardées sous forme de chaîne de caractères et de table.
-- socket est l'objet socket retourné avec succès par UDPCreate
err, RecBuf = UDPRead(socket,0,"string") -- Le type de données de RecBuf est une chaîne de caractères
err, RecBuf = UDPRead(socket,0) -- Le type de données de RecBuf est une table
```

<h3 class="lua-cmd" >UDPWrite</h3>

**Prototype :**

```lua
UDPWrite(socket, buf, timeout)
```

**Description :**

Envoi de données à l'homologue UDP.

**Paramètres obligatoires :**

- socket : objet socket créé.

- buf : données à envoyer.

**Paramètres facultatifs :**

timeout : délai d'attente en secondes.

- S'il n'est pas défini ou s'il est défini à 0, il attendra jusqu'à ce que l'autre extrémité ait fini de recevoir les données et passera ensuite à l'exécution suivante.
- S'il n'est pas fixé à 0, il attendra que l'autre extrémité ait reçu les données, puis passera à l'étape suivante.

**Retour :**

Résultat de l’envoi.

- 0 : Envoyé avec succès.
- 1 : Échec de l'envoi du courrier.

**Exemple :**

```lua
-- Envoyer des données via UDP, le contenu des données étant "test".
UDPWrite(socket, "test") -- socket est l'objet socket retourné avec succès par UDPCreate
```