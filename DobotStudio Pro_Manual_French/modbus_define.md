# Annexe A La définition du registre Modbus

<h2 id="desc" class="m2">1 Introduction sur Modbus</h2>

Modbus est un protocole de communication série qui permet aux robots de communiquer avec des équipements externes. Lorsque vous souhaitez contrôler un robot à partir d’un équipement externe comme un PLC via Modbus, l’équipement externe agit généralement en tant que maître et le robot en tant que station esclave.
Il existe plusieurs programmes pour Modbus :

- Modbus-RTU : compact, utilisant une représentation binaire des données. Une approche de somme de contrôle utilisant des sommes de contrôle de redondance cyclique.

- Modbus-ASCII : représentation lisible et redondante des chaînes de caractères basée sur les codes ASCII. Une approche de somme de contrôle utilisant des sommes de contrôle de redondance longitudinale.

- Modbus-TCP : connexion via TCP sur TCP/IP. Cette méthode ne nécessite pas le calcul de la somme de contrôle.

- Modbus-RTU-over-TCP : paquets avec contenu RTU transmis via TCP.

Nous proposons actuellement Modbus-TCP et Modbus-RTU-over-TCP.

Selon le protocole Modbus, les adresses Modbus attribuées au robot collaboratif 6 axes Dobot sont les suivantes :

- 00001-09999 : registre des bobines, la valeur ne supporte que 0 ou 1, utilisé pour contrôler le robot, lisible et inscriptible.

- 10001-19999 : registre de contact, la valeur ne prend en charge que 0 ou 1, utilisé pour obtenir l'état du robot, lecture seule.

- 30001-39999 : registres d'entrée, la valeur maximale prend en charge un nombre à virgule flottante double précision de 64 bits, utilisé pour obtenir les données de retour en temps réel du robot, en lecture seule.

- 40001-49999 : registres de maintien, la valeur maximale prend en charge un nombre à virgule flottante de 64 bits à double précision, utilisé pour l'interaction PLC du robot, lecture-écriture.

Les codes de fonction Modbus correspondant à chaque type de registre suivent le protocole Modbus standard :

| Types de registres| Lecture du registre| Écriture dans un seul registre| Écriture dans plusieurs registres|
|----------|----------|----------|----------|
| Registre de bobine| 01| 05| 0F|
| Registre de contact| 02| \-| \-|
| Registre d'entrée| 04| \-| \-|
| Registre de maintien| 03| 06| 10|

Le robot fournit deux tables pour l'accès par des dispositifs externes. map1 est accessible par les ports 502 (Modbus-TCP) et 503 (RTU-over-TCP), et map2 est accessible par les ports 1502 (Modbus-TCP) et 1503 (RTU-over-TCP). Ses ressources sont décrites ci-dessous :

| Paramètres/Station esclave| 502| 503| 1502| 1503|
|----------|----------|----------|----------|----------|
| Nombre de bobine| 10000| 10000| 10000| 10000|
| Nombre d'entrées discrètes| 10000| 10000| 10000| 10000|
| Nombre du registre d'entrée| 10000| 10000| 10000| 10000|
| Nombre du registre de maintien| 10000| 10000| 10000| 10000|
| Carte située| map1| map1| map2| map2|
| Port associé| 502| 503| 1502| 1503|
| Forme du protocole Modbus| TCP| RTU-sur-TCP| TCP| RTU-sur-TCP|
| Nombre maximal de maîtres pris en charge| 20| 20| 20| 20|
| ID de la station esclave| 1| 1| 1| 1|

Certaines des adresses de map1 sont utilisées par défaut par le système robotique, voir les définitions des registres ci-dessous. map2 est actuellement vide, les utilisateurs peuvent l'utiliser en fonction de leurs besoins.

<br/>

<h2 id="coil" class="m2">2 Registres des bobines (map1, robot de commande)</h2>

| Adresse PLC| Adresse du script (Get/SetCoils)| Types de registres| Fonction|
|:----------:|:----------:|:----------:|:----------:|
| 00001| 0| Bit| Commencer|
| 00002| 1| Bit| Arrêter|
| 00003| 2| Bit| Pause|
| 00004| 3| Bit| Activer|
| 00005| 4| Bit| Activation de la descente|
| 00006| 5| Bit| Supprimer l'alarme|
| 00007| 6| Bit| Entrer en mode de glisser-déposer|
| 00008| 7| Bit| Quitter le mode glisser-déposer|
| 00009| 8| Bit| Passage en mode automatique|
| 00010| 9| Bit| Passage en mode manuel|
| 00011 à 01024| 10 à 1023| Bit| Bit réservé|
| 01025 à 09999| 1024 à 9998| Bit| Personnaliser par l’utilisateur|

<br/>

<h2 id="contact" class="m2">3 Définition du registre des contacts (map1, état du robot)</h2>

| Adresse PLC| Adresse du script (GetInBits)| Types de registres| Fonction|
|:----------:|:----------:|:----------:|:----------:|
| 10001| 0| Bit| État de fonctionnement|
| 10002| 1| Bit| État d'arrêt|
| 10003| 2| Bit| État de pause|
| 10004| 3| Bit| État du point d’origine de sécurité|
| 10005| 4| Bit| État de pause de la peau de sécurité|
| 10006| 5| Bit| État de repos|
| 10007| 6| Bit| État de mise sous tension|
| 10008| 7| Bit| État d'activation|
| 10009| 8| Bit| État d'alarme|
| 10010| 9| Bit| État de collision|
| 10011| 10| Bit| État glisser-déposer|
| 10012| 11| Bit| État du mode de récupération|
| 10013 à 19999| 12 à 9998| Bit| Indéfini|

<br/>

<h2 id="input" class="m2">4 Définition du registre d'entrée (map1, données de retour en temps réel du robot)</h2>

L'adresse PLC de 30001 à 30999 et la fonction du registre de 31722 à 39999 ne sont pas définies (à l'exception des adresses 32001 à 32067, qui contiennent les informations suivantes du type de données U16 : numéro de série du contrôleur, numéro de série du corps ainsi que la somme de contrôle de sécurité). L'ordre des octets est conforme à l'ordre des octets de la petite bascule de fin.

| Adresse PLC| Type de donnée| Numéro| Taille de l’octet| Adresse du script (GetInRegs)| Type| Fonction|
|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| 31000| unsigned short| 1| 2| 999| U16| Validité des données|
| 31001| unsigned short| 1| 2| 1000| U16| Longueur totale des octets du message|
| 31002 à 31004| \-| \-| \-| 1001 à 1003| \-| Bit réservé|
| 31005 à 31008| uint64| 1| 8| 1004 à 1007| U64| Entrée numérique, voir la <a href="#dido">description DI/DO</a> pour plus de détails|
| 31009 à 31012| uint64| 1| 8| 1008 à 1011| U64| Sortie numérique, voir la <a href="#dido">description DI/DO</a> pour plus de détails|
| 31013 à 31016| uint64| 1| 8| 1012 à 1015| U64| Mode robot, voir <a href="#robotmode">RobotMode</a> pour plus de détails|
| 31017 à 31020| uint64| 1| 8| 1016 à 1019| U64| Horodatage Unix (en ms)|
| 31021 à 31024| \-| \-| \-| 1020 à 1023| \-| Bit réservé|
| 31025 à 31028| uint64| 1| 8| 1024 à 1027| U64| Valeurs standard de test de la structure mémoire<br/>0x0123 4567 89AB CDEF|
| 31029 à 31032| \-| \-| \-| 1028 à 1031| \-| Bit réservé|
| 31033 à 31036| double| 1| 8| 1032 à 1035| F64| Taux de vitesse|
| 31037 à 3104| \-| \-| \-| 1036 à 1039| \-| Bit réservé|
| 31041 à 31044| double| 1| 8| 1040 à 1043| F64| Tension de la carte de commande|
| 31045 à 31048| double| 1| 8| 1044 à 1047| F64| Tension du robot|
| 31049 à 31052| double| 1| 8| 1048 à 1051| F64| Courant du robot|
| 31053 à 31056| double| 1| 8| 1052 à 1055| F64| État d’exécution du script|
| 31057| unsigned short| 1| 2| 1056| U16| État d’entréé d’E/S de sécurité|
| 31058| unsigned short| 1| 2| 1057| U16| État de sortie d’E/S de sécurité|
| 31059 à 31096| \-| \-| \-| 1058 à 1095| \-| Bit réservé|
| 31097 à 31120| double| 6| 48| 1096 à 1119| F64| Position de l'articulation cible|
| 31121 à 31144| double| 6| 48| 1120 à 1143| F64| Vitesse de l'articulation cible|
| 31145 à 31168| double| 6| 48| 1144 à 1167| F64| Accélération de l'articulation cible|
| 31169 à 31192| double| 6| 48| 1168 à 1191| F64| Courant de l'articulation cible|
| 31193 à 31216| double| 6| 48| 1192 à 1215| F64| Couple de l'articulation cible|
| 31217 à 31240| double| 6| 48| 1216 à 1239| F64| Position réelle de l'articulation|
| 31241 à 31264| double| 6| 48| 1240 à 1263| F64| Vitesse réelle de l'articulation|
| 31265 à 31288| double| 6| 48| 1264 à 1287| F64| Courant réel de l'articulation|
| 31289 à 31312| double| 6| 48| 1288 à 1311| F64| Valeur de la force du capteur TCP<br/> (calculée à partir des forces à six dimensions)|
| 31313 à 31336| double| 6| 48| 1312 à 1335| F64| Valeurs réelles des coordonnées cartésiennes TCP|
| 31337 à 31360| double| 6| 48| 1336 à 1359| F64| Vitesses réelles des coordonnées cartésiennes TCP|
| 31361 à 31384| double| 6| 48| 1360 à 1383| F64| Valeur de la force TCP<br/> (calculée à partir des courants d'articulation)|
| 31385 à 31408| double| 6| 48| 1384 à 1407| F64| Valeur des coordonnées cartésiennes de la cible TCP|
| 31409 à 31432| double| 6| 48| 1408 à 1431| F64| Valeur de la vitesse cartésienne de la cible TCP|
| 31433 à 31456| double| 6| 48| 1432 à 1455| F64| Température de l’articulation|
| 31457 à 31480| double| 6| 48| 1456 à 1479| F64| Mode de contrôle de l’articulation.<br/> 8 : mode de position ; <br/>10 : mode de couple|
| 31481 à 31504| double| 6| 48| 1480 à 1503| F64| Tension de l’articulation|
| 31505 à 31506| \-| \-| \-| 1504 à 1505| \-| Bit réservé|
| 31507| char| 1| 1| 1506 Octet de poids faible| I8| Systèmes de coordonnées d’utilisateurs|
| 31507| char| 1| 1| 1506 Octet de poids fort| I8| Systèmes de coordonnées d’outils|
| 31508| char| 1| 1| 1507 Octet de poids faible| I8| Indicateur d'exécution de la file d'attente de l'algorithme|
| 31508| char| 1| 1| 1507 Octet de poids fort| I8| Indicateur de pause de la file d'attente d'algorithmes|
| 31509| char| 1| 1| 1508 Octet de poids faible| I8| Taux de vitesse articulaire|
| 31509| char| 1| 1| 1508 Octet de poids fort| I8| Taux d’accélération articulaire|
| 31510| char| 1| 1| 1509 Octet de poids faible| I8| Taux de jerk articulaire|
| 31510| char| 1| 1| 1509 Octet de poids fort| I8| Taux de vitesse de position cartésienne|
| 31511| char| 1| 1| 1510 Octet de poids faible| I8| Taux de vitesse d’attitude cartésienne|
| 31511| char| 1| 1| 1510 Octet de poids fort| I8| Taux d’accélération de position cartésienne|
| 31512| char| 1| 1| 1511 Octet de poids faible| I8| Taux d’accélération d’attitude cartésienne|
| 31512| char| 1| 1| 1511 Octet de poids fort| I8| Taux de jerk de position cartésienne|
| 31513| char| 1| 1| 1512 Octet de poids faible| I8| Taux de jerk d’attitude cartésienne|
| 31513| char| 1| 1| 1512 Octet de poids fort| I8| État des freins du robot, voir la <a href="#brake_status">description de BrakeStatus</a> pour plus de détails|
| 31514| char| 1| 1| 1513 Octet de poids faible| I8| État d'activation du robot|
| 31514| char| 1| 1| 1513 Octet de poids fort| I8| État de traînée du robot|
| 31515| char| 1| 1| 1514 Octet de poids faible| I8| État de mouvement du robot|
| 31515| char| 1| 1| 1514 Octet de poids fort| I8| État d'alarme du robot|
| 31516| char| 1| 1| 1515 Octet de poids faible| I8| État de jog du robot|
| 31516| char| 1| 1| 1515 Octet de poids fort| I8| Type de machine, voir <a href="#robot_type">RobotType</a> pour plus de détails|
| 31517| char| 1| 1| 1516 Octet de poids faible| I8| Signal de glissement de la plaque de boutons|
| 31517| char| 1| 1| 1516 Octet de poids fort| I8| Signal d’activation de la plaque de boutons|
| 31518| char| 1| 1| 1517 Octet de poids faible| I8| Signal d'enregistrement de la plaque de boutons|
| 31518| char| 1| 1| 1517 Octet de poids fort| I8| Signal de reproduction de la plaque de boutons|
| 31519| char| 1| 1| 1518 Octet de poids faible| I8| Signal de contrôle de la pince de la plaque de boutons|
| 31519| char| 1| 1| 1518 Octet de poids fort| I8| État en ligne de la force 6D|
| 31520| char| 1| 1| 1519 Octet de poids faible| I8| État de collision|
| 31520| char| 1| 1| 1519 Octet de poids fort| I8| (Peau de sécurité) État de pause d'approche du petit bras|
| 31521| char| 1| 1| 1520 Octet de poids faible| I8| (Peau de sécurité) État de pause d'approche du J4|
| 31521| char| 1| 1| 1520 Octet de poids fort| I8| (Peau de sécurité) État de pause d'approche du J5|
| 31522| char| 1| 1| 1521 Octet de poids faible| I8| (Peau de sécurité) État de pause d'approche du J6|
| 31522| char| 1| 1| 1521 Octet de poids fort| I8| Bit réservé|
| 31523 à 31552| \-| \-| \-| 1522 à 1551| \-| Bit réservé|
| 31553 à 31556| double| 1| 8| 1552 à 1555| F64| Bit réservé|
| 31557 à 31560| uint64| 1| 8| 1556 à 1559| U64| ID de la file d'attente de l'algorithme actuel|
| 31561 à 31584| double| 6| 48| 1560 à 1583| F64| Couple réel|
| 31585 à 31588| double| 1| 8| 1584 à 1587| F64| Poids de la charge (kg)|
| 31589 à 31592| double| 1| 8| 1588 à 1591| F64| Distance d'excentricité dans la direction X (mm)|
| 31593 à 31596| double| 1| 8| 1592 à 1595| F64| Distance d'excentricité dans la direction Y (mm)|
| 31597 à 31600| double| 1| 8| 1596 à 1599| F64| Distance d'excentricité dans la direction Z (mm)|
| 31601 à 31624| double| 6| 48| 1600 à 1623| F64| Valeurs de coordonnées d’utilisateurs|
| 31625 à 31648| double| 6| 48| 1624 à 1647| F64| Valeurs de coordonnées d'outils|
| 31649 à 31652| double| 1| 8| 1648 à 1651| F64| Index d'exécution de réplication de trajectoire|
| 31653 à 31676| double| 6| 48| 1652 à 1675| F64| Valeurs brutes des données de la force 6D actuelle|
| 31677 à 31692| double| 4| 32| 1676 à 1691| F64| [qw,qx,qy,qz] quaternions cibles|
| 31693 à 31708| double| 4| 32| 1692 à 1707| F64| [qw,qx,qy,qz] quaternions réels|
| 31709| unsigned short| 1| 2| 1708| U16| Statut manuel/automatique .<br/> 1 :  Manuel<br/> 2 : mode automatique <br/>0 : commutation de mode non activée|
| 31710| unsigned short| 1| 2| 1709| U16| État d’exportation par clé USB|
| 31711| char| 1| 1| 1710 Octet de poids faible| I8| État de sécurité|
| 31711| char| 1| 1| 1710 Octet de poids fort| I8| Bit réservé d’état de sécurité|
| 31712 à 31721| \-| \-| \-| 1711 à 1720| \-| Bit réservé|
| | | | 1440| | | Total 1440 octets|



| Adresse PLC| Adresse du script (GetInRegs)| Type| Fonction|
|:----------:|:----------:|:----------:|:----------:|
| 32001 à 32032| 2000 à 2031| U16| Les caractères 1 <br/>à 32 du numéro de série du contrôleur|
| 32033 à 32065| 2032 à 2064| U16| Les caractères 1 <br/>à 32 du numéro de série du corps|
| 32066| 2065| U16| «&nbsp;Somme de contrôle de sécurité&nbsp;» 4 caractères plus bas<br/> (2 octets)|
| 32067| 2066| U16| «&nbsp;Somme de contrôle de sécurité&nbsp;» 4 caractères plus haut<br/> (2 octets)|



<p id="mot_para"><b>Description des valeurs de retour de paramètres de mouvement</b></p>

Si les paramètres de mouvement (vitesse, accélération, etc.) sont définis individuellement dans le projet, les valeurs de retour correspondantes ne sont pas mises à jour immédiatement, mais seulement lorsque le robot exécute l'instruction de mouvement suivante.



<p id="dido"><b>Description sur DI/DO</b></p>

DI/DO occupe chacun 8 octets, chaque octet a 8 bits (binaires) et peut représenter l'état d'un maximum de 64 ports pour DI/DO. Chaque octet indique l'état d'une borne, de bas en haut, 1 indiquant que la borne correspondante est activée et 0 indiquant que la borne correspondante est désactivée ou qu'il n'y a pas de borne correspondante.

Par exemple, le premier octet de DI est 0x01, la représentation binaire est 00000001, ce qui indique l'état de D1_1 ~ DI_8 de bas en haut, c'est-à-dire que DI_1 est ON, et les 7 autres DI sont OFF ;

Le deuxième octet est 0x02, la représentation binaire est 00000010, de bas en haut indique respectivement l'état de D1_9 ~ DI_16, c'est-à-dire que DI_10 est ON et les 7 autres DI sont OFF ;

Les octets suivants et ainsi de suite, selon les différentes armoires de commande, le nombre de bornes d'E/S est également différent, plus que le nombre de bornes d'E/S des bits binaires seront remplis avec tous les 0.




<p id="robotmode"><b>Description sur RobotMode</b></p>

| Plage de valeurs| Définition| Description|
|:----------:|:----------:|:----------:|
| 1| ROBOT_MODE_INIT| État initial|
| 2| ROBOT_MODE_BRAKE_OPEN| Déblocage du frein avec n'importe quelle articulation|
| 3| ROBOT_MODE_POWEROFF| État de mise hors tension du bras|
| 4| ROBOT_MODE_DISABLED| Non activé (pas de desserrage du frein)|
| 5| ROBOT_MODE_ENABLE| Activé et inactif|
| 6| ROBOT_MODE_BACKDRIVE| Mode « glisser-déposer »|
| 7| ROBOT_MODE_RUNNING| État de fonctionnement (projet, mouvement de la file d'attente TCP, etc.)|
| 8| ROBOT_MODE_SINGLE_MOVE| État de mouvement unique (jog, RunTo, etc.)|
| 9| ROBOT_MODE_ERROR| Des alarmes non résolues existes. Cet état a la priorité la plus élevée et renvoie 9 en cas d'alarme, quel que soit l'état du bras.|
| 10| ROBOT_MODE_PAUSE| État de pause du projet|
| 11| ROBOT_MODE_COLLISION| État de déclenchement de la détection de collision|



<p id="brake_status"><b>Description sur BrakeStatus</b></p>

Cet octet exprime l'état du frein de chaque articulation par bit, et le bit correspondant est 1, ce qui signifie que le frein de l'articulation a été desserré. La correspondance entre le nombre de bits et les articulations est indiquée dans le tableau ci-dessous :

| Nombre de bits| 7| 6| 5| 4| 3| 2| 1| 0|
|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| **Signification**| Bit réservé| Bit réservé| Articulation 1| Articulation 2| Articulation 3| Articulation 4| Articulation 5| Articulation 6|

Exemple :

- 0x01 (00000001) : l'articulation 6 desserre le frein de maintien
- 0x02 (00000010) : l'articulation 5 desserre le frein de maintien
- 0x03 (00000011) : l'articulation 5 et l'articulation 6 desserrent le frein de maintien
- 0x04 (00000100) : l'articulation 4 desserre le frein de maintien



<p id="robot_type"><b>Description sur RobotType</b></p>

| Plage de valeurs| Modèle|
|----------|----------|
| 3| CR3|
| 5| CR5|
| 7| CR7|
| 10| CR10|
| 12| CR12|
| 16| CR16|
| 101| Nova 2|
| 103| Nova 5|
| 113| CR3A|
| 115| CR5A|
| 117| CR7A|
| 120| CR10A|
| 122| CR12A|
| 126| CR16A|
| 130| CR20A|
| 150| Magician E6|

<br/>

<h2 id="hold" class="m2">5 Définition du registre de maintien (map1, interaction PLC du robot)</h2>

| Adresse PLC| Adresse du script (Get/SetHoldRegs)| Types de registres| Fonction|
|:----------:|:----------:|:----------:|:----------:|
| 40001 à 41024| 0 à 1023| \-| Bit réservé|
| 41025 à 49999| 1024 à 9998| \-| Personnaliser par l’utilisateur|
