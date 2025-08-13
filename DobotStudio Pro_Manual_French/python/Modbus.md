# Modbus

<h3 class="lua-cmd" id="list" >Liste des commandes</h3>

La fonction Modbus est utilisée pour établir la communication entre le maître et l'esclave Modbus. Veuillez vous référer à la définition de l'adresse du registre Modbus de l'esclave correspondant pour la plage de valeurs et la définition.

| Instruction| Fonction|
|----------|----------|
| [ModbusCreate](#modbuscreate)| Créer un Modbus|
| [ModbusRTUCreate](#modbusrtucreate)| Créer un Modbus basé sur l'interface RS485 et établir le lien avec la station esclave|
| [ModbusClose](#modbusclose)| Déconnexion de l'esclave Modbus|
| [GetInBits](#getinbits)| Lecture de la valeur du registre des contacts|
| [GetInRegs](#getinregs)| Lecture de la valeur du registre d'entrée|
| [GetCoils](#getcoils)| Lecture de la valeur du registre des bobines|
| [SetCoils](#setcoils)| Écriture dans un registre des bobines|
| [GetHoldRegs](#getholdregs)| Lecture de la valeur du registre de maintien|
| [SetHoldRegs](#setholdregs)| Écriture dans un registre de maintien|

Les codes de fonction Modbus pour chaque registre suivent le protocole Modbus standard :

| Types de registres| Lecture du registre| Écriture dans un seul registre| Écriture dans plusieurs registres|
|----------|----------|----------|----------|
| Registre de bobine| 01| 05| 0F|
| Registre de contact| 02| \-| \-|
| Registre d'entrée| 04| \-| \-|
| Registre de maintien| 03| 06| 10|

<h3 class="lua-cmd" >ModbusCreate</h3>

**Prototype :**

```python
ModbusCreate(IP, port, slave_id, isRTU)
```

**Description :**

Créer un Modbus et établir le lien avec la station esclave Il est possible de connecter jusqu'à 15 appareils en même temps.

Lors de la connexion à l'esclave du robot, l'IP est définie sur l'IP du robot (192.168.5.1 par défaut, modifiable) et le port est défini sur 502 (map1) ou 1502 (map2), voir [l'annexe A Définitions des registres Modbus](../modbus_define.md) pour plus de détails.

Lors de la connexion d'un esclave tiers, l'IP et le port correspondent à l'adresse de l'esclave tiers. Pour la plage de valeurs et la définition de l'adresse du registre lors de la lecture et de l'écriture des registres, veuillez vous référer à la définition de l'adresse du registre Modbus de l'esclave correspondant.

**Paramètres obligatoires :**

- IP : l’adresse IP de la station esclave.
- port : port de l'esclave.

**Paramètres facultatifs :**

- slave_id : ID de l'esclave.

- isRTU : valeur booléenne.
  
  - Si isRTU est faux, la communication Modbus TCP est établie sur la base du port réseau de l'armoire de commande.
  
  - Si isRTU est vrai, la communication Modbus RTU basée sur RS485 à l'extrémité du corps est établie, et seul le port 60000 peut être utilisé.
    
    <div class="caution1"><img src="images/caution.png"  height="18" /><b> Attention : </b><div>Ce paramètre détermine le format de protocole utilisé pour la transmission des données après l'établissement de la connexion, mais il n'affecte pas le résultat de la connexion.  Par conséquent, si ce paramètre est mal configuré lors de la création de la station maître, la création peut tout de même réussir, mais cela entraînera des anomalies lors des communications ultérieures. </div></div>


**Retour :**

- err :
  - 0 : Créer un Modbus avec succès.
  - 1 : Les maîtres créés ont atteint le nombre maximum, la création de nouveaux maîtres a échoué.
  - 2 : Échec de l'initialisation du maître, suggérer de vérifier l'IP, le port, le réseau est normal, etc.
  - 3 : Échec de la connexion de l'esclave, suggérer de vérifier si l'esclave est créé normalement, si le réseau est normal, etc.
- id : index du maître renvoyé, utilisé lors de l'appel ultérieur d'autres commandes Modbus. Plage de valeurs : [0, 14].

**Exemple :**

```python
# Créer un Modbus et établir le lien avec la station esclave spécifiée.
ip="192.168.5.123" 
port=503 
err=0
id=0
err, id = ModbusCreate(ip, port, 1)
```

```python
# Créer un Modbus et établir le lien avec la station esclave du robot.
ip="192.168.5.1" 
port=502
err=0
id=0
err, id = ModbusCreate(ip, port)
```

<h3 class="lua-cmd" >ModbusRTUCreate</h3>

**Prototype :**

```python
ModbusRTUCreate(slave_id, baud, parity, data_bit, stop_bit)
```

**Description :**

Créer un Modbus basé sur l'interface RS485 de l’armoire de commande et établir le lien avec la station esclave Il est possible de connecter jusqu'à 15 appareils en même temps.

**Paramètres obligatoires :**

- slave_id : ID de l'esclave.
- baud : vitesse de transmission de l'interface RS485.

**Paramètres facultatifs :**

- parity : présence ou non d'un bit de parité.
  - "0" : Parité impaire.
  - "E" : Parité paire.
  - "N" : pas de bit de parité.
  - La valeur par défaut est "E" sans paramètre.
- data_bit : longueur des bits de données. Plage de valeurs : 8. La valeur par défaut est 8 sans référence.
- stopbit : longueur du bit de stop. Plage de valeurs : 1, 2. La valeur par défaut est 1 sans référence.

**Retour :**

- err : 0 signifie que la création du maître Modbus réussit, 1 signifie que la création du maître Modbus échoue.
- id : l'index du maître retourné, utilisé lors de l'appel d'autres commandes Modbus.

**Exemple :**

```python
# Créer un Modbus et établir le lien avec la station esclave via l'interface RS485, l'ID de la station esclave étant 1 et la vitesse de transmission de 115200 bauds.
err, id = ModbusRTUCreate(1, 115200)
```

<h3 class="lua-cmd" >ModbusClose</h3>

**Prototype :**

```python
ModbusClose(id)
```

**Description :**

Déconnexion de la station esclave de Modbus, libérer le maître.

**Paramètres obligatoires :**

id : index du maître créé.

**Retour :**

Opération

- 0 : Déconnexion réussie.
- 1 : Déconnexion échouée.

**Exemple :**

```python
# Déconnexion de l'esclave Modbus.
ModbusClose(id)
```

<h3 class="lua-cmd" >GetInBits</h3>

**Prototype :**

```python
GetInBits(id, addr, count)
```

**Description :**

Lire la valeur de l'adresse du registre de contact de la station esclave du Modbus Correspond au code de fonction Modbus 02.

**Paramètres obligatoires :**

- id : index du maître créé.
- addr : adresse de départ du registre de contact.
- count : nombre de registres de contacts à lire consécutivement. Plage de valeurs : [1, 2000] (Limitations du protocole ModbusTCP, la plage réelle des valeurs doit être déterminée en fonction du nombre de registres esclaves ou de la spécification du protocole).

**Retour :**

La valeur de l'adresse du registre de contact lu est stockée dans le tableau. La première valeur du tableau correspond à la valeur de l'adresse de départ du registre des contacts.

**Exemple :**

```python
# Lire les valeurs de 5 adresses consécutives, débutant à l'adresse 0.
inBits = GetInBits(id,0,5)
```

<h3 class="lua-cmd" >GetInRegs</h3>

**Prototype :**

```python
GetInRegs(id, addr, count, type)
```

**Description :**

Lire la valeur de l'adresse du registre d'entrée de la station esclave du Modbus Correspond au code de fonction Modbus 04.

**Paramètres obligatoires :**

- id : index du maître créé.
- addr : adresse de début du registre d'entrée.
- count : nombre de registres d'entrée à lire consécutivement. Plage de valeurs : [1, 125] (limitations du protocole ModbusTCP, la plage de valeurs réelle doit être déterminée en fonction du nombre de registres esclaves ou de la spécification du protocole).

**Paramètres facultatifs :**

type : type de données.

- S'il est vide, la valeur par défaut est U16.
- U16 : entier non signé de 16 bits (2 octets, occupe 1 registre).
- U32 : entier non signé de 32 bits (4 octets, occupe 2 registres).
- F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres).
- F64 : nombre à virgule flottante de 64 bits à double précision (8 octets, occupe 4 registres).

**Retour :**

La valeur de l'adresse du registre d'entrée est lue et stockée dans le tableau. La première valeur du tableau correspond à la valeur de l'adresse de départ du registre d'entrée.

**Exemple :**

```python
# Lire un entier non signé de 32 bits à partir de l'adresse 2048.
data = GetInRegs(id, 2048, 2, "U32")
```

<h3 class="lua-cmd" >GetCoils</h3>

**Prototype :**

```python
GetCoils(id, addr, count)
```

**Description :**

Lire la valeur de l'adresse du registre de bobine de la station esclave du Modbus Correspond au code de fonction Modbus 01.

**Paramètres obligatoires :**

- id : index du maître créé.
- addr : adresse de début du registre de la bobine.
- count : nombre de registres de bobines à lire consécutivement. Plage de valeurs : [1, 2000] (limitation du protocole ModbusTCP, la plage de valeurs réelle doit être déterminée en fonction du nombre de registres esclaves ou de la spécification du protocole).

**Retour :**

La valeur de l'adresse du registre bobine lu est stockée dans le tableau. La première valeur du tableau correspond à la valeur à l'adresse de départ du registre de bobines.

**Exemple :**

```python
# Lire les valeurs de 5 adresses consécutives, débutant à l'adresse 0.
Coils = GetCoils(id,0,5)
```

<h3 class="lua-cmd" >SetCoils</h3>

**Prototype :**

```python
SetCoils(id, addr, count, table)
```

**Description :**

Écrit la valeur spécifiée à l'adresse spécifiée dans le registre des bobines. Correspond aux codes de fonction Modbus 05 (écriture simple) et 0F (écriture multiple).

**Paramètres obligatoires :**

- id : index du maître créé.
- addr : adresse de départ du registre des bobines.
- count : nombre d'écritures consécutives dans le registre des bobines. Plage de valeurs : [1, 1968] (limitation du protocole ModbusTCP, la plage de valeurs réelle doit être déterminée en fonction du nombre de registres esclaves ou de la spécification du protocole).
- tableau : les valeurs à écrire dans les registres de bobine sont stockées dans le tableau. La première valeur du tableau correspond à la valeur à l'adresse de départ du registre de bobines.

**Exemple :**

```python
# Écrire 5 bobines consécutives à partir de l'adresse 1024.
local Coils = {0,1,1,1,0}
SetCoils(id, 1024, #coils, Coils)
```

<h3 class="lua-cmd" >GetHoldRegs</h3>

**Prototype :**

```python
GetHoldRegs(id, addr, count, type)
```

**Description :**

Lire la valeur de l'adresse du registre de maintien de la station esclave du Modbus Correspond au code de fonction Modbus 03.

**Paramètres obligatoires :**

- id : index du maître créé.
- addr : adresse de départ du registre de maintien.
- count : nombre de registres de maintien à lire consécutivement. Plage de valeurs : [1, 125] (limitations du protocole ModbusTCP, la plage de valeurs réelle doit être déterminée en fonction du nombre de registres esclaves ou de la spécification du protocole).

**Paramètres facultatifs :**

type : type de données.

- S'il est vide, la valeur par défaut est U16.
- U16 : entier non signé de 16 bits (2 octets, occupe 1 registres).
- U32 : entier non signé de 32 bits (4 octets, occupe 2 registres).
- F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres).
- F64 : nombre à virgule flottante de 64 bits à double précision (8 octets, occupe 4 registres).

**Retour :**

La valeur de l'adresse du registre de maintien est lue et stockée dans le tableau. La première valeur du tableau correspond à la valeur de l'adresse de départ du registre de stockage.

**Exemple :**

```python
# Lire un entier non signé de 32 bits à partir de l'adresse 2048.
data = GetHoldRegs(id, 2048, 2, "U32")
```

<h3 class="lua-cmd" >SetHoldRegs</h3>

**Prototype :**

```python
SetHoldRegs(id, addr, count, table, type)
```

**Description :**

Écrit la valeur spécifiée à l'adresse spécifiée dans le registre de maintien selon le type de données spécifié. Correspond aux codes de fonction Modbus 06 (écriture simple) et 10 (écriture multiple).

**Paramètres obligatoires :**

- id : index du maître créé.
- addr : adresse de départ du registre de maintien.
- count : nombre d'écritures successives à effectuer dans le registre de maintien. Plage de valeurs : [1, 123] (limitations du protocole ModbusTCP, la plage de valeurs réelle doit être déterminée en fonction du nombre de registres esclaves ou de la spécification du protocole).
- tableau : la valeur à écrire dans le registre de maintien est stockée dans le tableau. La première valeur du tableau correspond à la valeur de l'adresse de départ du registre de maintien.

**Paramètres facultatifs :**

type : type de données.

- S'il est vide, la valeur par défaut est U16.
- U16 : entier non signé de 16 bits (2 octets, occupe 1 registre).
- U32 : entier non signé de 32 bits (4 octets, occupe 2 registres).
- F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres).
- F64 : nombre à virgule flottante de 64 bits à double précision (8 octets, occupe 4 registres).

**Exemple :**

```python
# Écrire un nombre à virgule flottante de 64 bits à double précision à partir de l'adresse 2048.
local data = {95.32105}
SetHoldRegs(id, 2048, 4, data, "F64")
```