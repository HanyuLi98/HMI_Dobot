# Blocs de construction Modbus

Les blocs de construction Modbus sont utilisés pour la communication Modbus. Vous pouvez vous référer à la [DEMO correspondante](qs_modbus.md) pour une expérience rapide de l'utilisation des commandes correspondantes.

Les codes de fonction Modbus pour chaque registre suivent le protocole Modbus standard :

| Types de registres| Lecture du registre| Écriture dans un seul registre| Écriture dans plusieurs registres|
|----------|----------|----------|----------|
| Registre de bobine| 01| 05| 0F|
| Registre de contact| 02| \-| \-|
| Registre d'entrée| 04| \-| \-|
| Registre de maintien| 03| 06| 10|

<h3 class="lua-cmd" id="create" >Créer un Modbus</h3>

<div align=center><img src="images/modbus_new.png" width="400" /></div>

**Description:** Créer un maître Modbus TCP basé sur la prise Ethernet de l’armoire de commande et établir le lien avec la station esclave Il est possible de connecter jusqu'à 15 esclaves en même temps.

**Paramètres :**

- Saisissez l'adresse IP de l'esclave Modbus.
- Saisissez le port de l'esclave Modbus.
- Sélectionnez l’ID de l’esclave Modbus.

Lors de la connexion à l'esclave du robot, l'IP est définie sur l'IP du robot (192.168.5.1 par défaut, modifiable) et le port est défini sur 502 (map1) ou 1502 (map2), voir [l'annexe A Définitions des registres Modbus pour plus de détails](../modbus_define.md).

Lors de la connexion d'un esclave tiers, veuillez vous référer à la définition de l'adresse du registre Modbus de l'esclave correspondant pour la plage de valeurs et la définition de l'adresse du registre lors de la lecture et de l'écriture des registres.

<h3 class="lua-cmd" id="create-robot485" >Créer un Modbus basé sur l'extrémité RS485</h3>

<div align=center><img src="images/modbus_robot_ip.png"/></div>

**Description:** Créer un maître Modbus TCP basé sur l'interface terminale RS485 et établir le lien avec la station esclave Il est possible de connecter jusqu'à 15 appareils en même temps.

**Paramètres :**

- Saisissez l'adresse IP de l'esclave Modbus.

- Entrez le débit en bauds de l'interface RS485.

- Sélectionnez l’ID de l’esclave Modbus.

- Choisir s'il y a un bit de parité ou non.

- Sélectionnez la longueur du bit d'arrêt.

Lors de la connexion de l'esclave du robot, l'IP est définie sur l'IP du robot (192.168.5.10 par défaut, modifiable) et le port est de 60000 (non paramétrable et non modifiable).

Lors de la connexion d'un esclave tiers, veuillez vous référer à la définition de l'adresse du registre Modbus de l'esclave correspondant pour la plage de valeurs et la définition de l'adresse du registre lors de la lecture et de l'écriture des registres.

<h3 class="lua-cmd" id="create485" >Créer un Modbus basé sur RS485</h3>

<div align=center><img src="images/modbus_new485.png"/></div>

**Description:** Créer un maître Modbus RTU basé sur l’interface RS485 de l’armoire de commande et établir le lien avec la station esclave Il est possible de connecter jusqu'à 15 appareils en même temps.

**Paramètres :**

- Entrez le débit en bauds de l'interface RS485.
- Sélectionnez l’ID de l’esclave Modbus.
- Choisir s'il y a un bit de parité ou non.
- Entrer la longueur du bit de données, la version actuelle n'en supporte que 8.
- Sélectionnez la longueur du bit d'arrêt.

<h3 class="lua-cmd" id="cr_result" >Obtenir le résultat de la création du Modbus</h3>

![](images/modbus_new_result.png)

**Description:** Obtenir le résultat de la création du maître modbus.

**Valeur de retour :**

- 0 : Créer un Modbus avec succès
- 1 : Il y a déjà 15 maîtres créés, échec de la création d'un nouveau maître.
- 2 : Échec de l'initialisation du maître, suggérer de vérifier l'IP, le port, le réseau est normal, etc.
- 3 : Échec de la connexion de l'esclave, suggérer de vérifier si l'esclave est créé normalement, si le réseau est normal, etc.

<h3 class="lua-cmd" id="waitin" >Attendre registre d'entrée</h3>

![](images/modbus_wait_input.png)

**Description:** Attendre que la valeur de l'adresse spécifiée dans le registre d'entrée remplisse la condition avant de passer à l'exécution de l'instruction suivante.

**Paramètres :**

- Adresse de début du registre d'entrée
- Sélectionner le type de données à lire :
  - U16 : entier non signé de 16 bits (2 octets, occupe 1 registre)
  - U32 : entier non signé de 32 bits (4 octets, occupe 2 registres)
  - F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres)
  - F64 : nombre à virgule flottante de 64 bits à double précision (8 octets, occupe 4 registres)
- Saisir les conditions à remplir par la valeur à l'adresse spécifiée dans le registre.

<h3 class="lua-cmd" id="waithold" >Attendre registre de maintien</h3>

![](images/modbus_wait_hold.png)

**Description:** Attendre que la valeur à l'adresse spécifiée du registre de maintien satisfasse à la condition avant de passer à l'instruction suivante.

**Paramètres :**

- Adresse de début du registre de maintien
- Sélectionner le type de données à lire :
  - U16 : entier non signé de 16 bits (2 octets, occupe 1 registre)
  - U32 : entier non signé de 32 bits (4 octets, occupe 2 registres)
  - F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres)
  - F64 : nombre à virgule flottante de 64 bits à double précision (8 octets, occupe 4 registres)
- Les conditions à remplir pour conserver la valeur de l'adresse spécifiée par le registre.

<h3 class="lua-cmd" id="waitcontact" >Attendre registre de contact</h3>

![](images/modbus_wait_contact.png)

**Description:** Attend que la condition soit remplie par la valeur à l'adresse spécifiée du registre de contact avant de passer à l'instruction suivante.

**Paramètres :**

- Adresse de début du registre de contact

- La condition à remplir par la valeur de l'adresse spécifiée du registre des contacts.

<h3 class="lua-cmd" id="waitcoil" >Attendre registre de bobine</h3>

![](images/modbus_wait_coil.png)

**Description:** Attendre que la valeur à l'adresse spécifiée du registre des bobines satisfasse à la condition avant de passer à l'instruction suivante.

**Paramètres :**

- Adresse de début du registre de bobine

- La condition à remplir par la valeur de l'adresse spécifiée du registre des bobines.

<h3 class="lua-cmd" id="readin" >Lecture de la valeur du registre d'entrée</h3>

![](images/modbus_get_input.png)

**Description:** Obtenir la valeur de l'adresse spécifiée du registre d'entrée.

**Paramètres :**

- Adresse de début du registre d'entrée
- Sélectionner le type de données à lire :
  - U16 : entier non signé de 16 bits (2 octets, occupe 1 registre)
  - U32 : entier non signé de 32 bits (4 octets, occupe 2 registres)
  - F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres)
  - F64 : nombre à virgule flottante de 64 bits à double précision (8 octets, occupe 4 registres)

**Valeur de retour:** La valeur à l'adresse spécifiée du registre d'entrée.

<h3 class="lua-cmd" id="readhold" >Lecture de la valeur du registre de maintien</h3>

![](images/modbus_get_hold.png)

**Description:** Obtient la valeur à l'adresse spécifiée dans le registre de maintien.

**Paramètres :**

- Adresse de début du registre de maintien
- Sélectionner le type de données à lire :
  - U16 : entier non signé de 16 bits (2 octets, occupe 1 registre)
  - U32 : entier non signé de 32 bits (4 octets, occupe 2 registres)
  - F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres)
  - F64 : nombre à virgule flottante de 64 bits à double précision (8 octets, occupe 4 registres)

**Valeur de retour:** La valeur à l'adresse spécifiée du registre de maintien.

<h3 class="lua-cmd" id="readcontact" >Lecture de la valeur du registre des contacts</h3>

![](images/modbus_get_contact.png)

**Description:** Obtient la valeur à l'adresse spécifiée dans le registre de contact.

**Paramètre:** Adresse de début du registre de contact.

**Valeur de retour:** Valeur à l'adresse spécifiée du registre des contacts.

<h3 class="lua-cmd" id="readcoil" >Lecture de la valeur du registre des bobines</h3>

![](images/modbus_get_coil.png)

**Description:** Obtient la valeur à l'adresse spécifiée dans le registre de bobine.

**Paramètre:** Adresse de début du registre des bobines.

**Valeur de retour:** Valeur de l'adresse spécifiée du registre des bobines.

<h3 class="lua-cmd" id="readcoilg" >Lecture en continu de la valeur du registre des bobines</h3>

![](images/modbus_get_coil_bit.png)

**Description:** La valeur de l'adresse spécifiée du registre des bobines est lue en continu.

**Paramètres :**

- Adresse de début du registre de bobine
- Le nombre de bits de registre à lire consécutivement.

**Valeur de retour:** La valeur à l'adresse spécifiée du registre des bobines est stockée dans un tableau. La première valeur du tableau correspond à la valeur à l'adresse de départ du registre de bobines.

<h3 class="lua-cmd" id="readholdg" >Lecture en continu de la valeur du registre de maintien</h3>

![](images/modbus_get_hold_bit.png)

**Description:** Lecture continue de la valeur à l'adresse spécifiée du registre de maintien.

**Paramètres :**

- Adresse de début du registre de maintien
- Nombre de valeurs à lire en continu.
- Sélectionner le type de données à lire :
  - U16 : entier non signé de 16 bits (2 octets, occupe 1 registre)
  - U32 : entier non signé de 32 bits (4 octets, occupe 2 registres)
  - F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres)
  - F64 : nombre à virgule flottante de 64 bits à double précision (8 octets, occupe 4 registres)

**Valeur de retour:** La valeur à l'adresse spécifiée du registre de bobine est stockée dans le tableau. La première valeur du tableau correspond à la valeur à l'adresse de départ du registre de bobines.

<h3 class="lua-cmd" id="writecoil" >Écriture dans un registre des bobines</h3>

![](images/modbus_set_coil.png)

**Description:** Écrit la valeur spécifiée à l'adresse spécifiée par le registre de bobines.

**Paramètres :**

- Adresse de début du registre de bobine
- Sélectionne la valeur à écrire, qui ne peut être que 0 ou 1.

<h3 class="lua-cmd" id="writecoilg" >Écriture en continu dans un registre des bobines</h3>

![](images/modbus_set_coil_bit.png)

**Description:** Écrit successivement la valeur spécifiée à l'adresse spécifiée par le registre des bobines.

**Paramètres :**

- Adresse de début du registre de bobine
- Saisit la valeur à écrire, les valeurs multiples sont séparées par des virgules et chaque bit ne peut être que 0 ou 1.

<h3 class="lua-cmd" id="writehold" >Écriture dans un registre de maintien</h3>

![](images/modbus_set_hold.png)

**Description:** Écrit la valeur spécifiée à l'adresse spécifiée par le registre de maintien.

**Paramètres :**

- Adresse de début du registre de maintien
- La sélection de la valeur à écrire doit correspondre au type de données sélectionné.
- Sélectionnez le type de données à écrire :
  - U16 : Entier non signé de 16 bits (2 octets, occupant 1 registre)
  - U32 : entier non signé de 32 bits (4 octets, occupant 2 registres)
  - F32 : nombre à virgule flottante 32 bits à simple précision (4 octets, occupe 2 registres)
  - F64 : nombre à virgule flottante 64 bits à double précision (8 octets, occupe 4 registres)

<h3 class="lua-cmd" id="close" >Fermer un Modbus</h3>

![](images/modbus_close.png)

**Description:** Arrête le maître Modbus et déconnecte tous les esclaves.