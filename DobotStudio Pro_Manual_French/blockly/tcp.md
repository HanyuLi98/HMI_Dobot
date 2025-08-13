# Blocs de construction TCP

Les blocs TCP sont utilisés pour les opérations liées à la communication TCP. Vous pouvez vous référer à la [DEMO correspondante](qs_tcp.md) pour une expérience rapide de l'utilisation des commandes correspondantes.

<h3 class="lua-cmd" id="connect" >Connexion d'un SOCKET</h3>

![](images/tcp_open.png)

**Description:** Créer un client TCP pour communiquer avec le serveur TCP spécifié.

**Paramètres :**

- Sélectionnez le numéro de SOCKET pour créer jusqu'à 4 liens de communication TCP.
- Adresse IP du serveur TCP.
- Le port du serveur TCP.

<h3 class="lua-cmd" id="con_result" >Obtenir le résultat de la connexion d'un SOCKET</h3>

![](images/tcp_open_result.png)

**Description:** Obtenir le résultat de la liaison de communication TCP.

**Paramètres:** Sélectionnez le numéro de SOCKET.

**Valeur de retour:** Renvoie 0 en cas de connexion réussie et 1 en cas d'échec de la connexion.

<h3 class="lua-cmd" id="create" >Création d'un SOCKET</h3>

![](images/tcp_new.png)

**Description:** Crée un serveur TCP et attend que le client se connecte.

**Paramètres :**

- Sélectionnez le numéro SOCKET pour créer jusqu'à 4 liens de communication TCP.

- Adresse IP du serveur TCP.

- Le port du serveur TCP. N'utilisez pas les ports suivants qui sont déjà occupés par le système, ce qui entraînerait l'échec de la création du serveur.
  
  7, 13, 22, 37,
  
  139, 445, 502, 503,
  
  1501, 1502, 1503, 4840, 8172, 9527,
  
  11740, 22000, 22001, 29999, 30004, 30005, 30006,
  
  60000~65504, 65506, 65511~65515, 65521, 65522

<h3 class="lua-cmd" id="cr_result" >Obtenir le résultat de la création d'un SOCKET</h3>

![](images/tcp_new_result.png)

**Description:** Obtenir le résultat de la création du serveur TCP.

**Paramètres:** Sélectionnez le numéro de SOCKET.

**Valeur de retour:** Renvoie 0 si la création a réussi et 1 si elle a échoué.

<h3 class="lua-cmd" id="close" >Fermer un SOCKET</h3>

![](images/tcp_close.png)

**Description:** Ferme le SOCKET spécifié et déconnecte le lien de communication.

**Paramètres:** Sélectionnez le numéro de SOCKET.

<h3 class="lua-cmd" id="getvar" >Lecture des variables</h3>

![](images/tcp_get_var.png)

**Description:** Lit la variable via la communication TCP et la sauvegarde.

**Paramètres :**

- Sélectionnez le numéro de SOCKET.
- Sélectionnez le type de variable à recevoir, les valeurs numériques et les chaînes de caractères sont prises en charge.
- La variable utilisée pour sauvegarder les données reçues, en utilisant le bloc de construction de variable créé.
- Remplissez le délai d'attente, s'il est fixé à 0, il n'y aura pas de délai d'attente, il attendra jusqu'à ce que la variable soit reçue.

<h3 class="lua-cmd" id="r_result" >Obtenir le résultat de la lecture de variable</h3>

![](images/tcp_read_result.png)

**Description:** Obtenir le résultat de la lecture de variable TCP

**Paramètres:** Sélectionnez le numéro de SOCKET.

**Valeur de retour:** Le succès de la lecture renvoie 0, l'échec de la lecture renvoie 1.

<h3 class="lua-cmd" id="sendvar" >Envoyer la variable</h3>

![](images/tcp_send_var.png)

**Description:** Envoie la variable via une communication TCP.

**Paramètres :**

- Sélectionnez le numéro de SOCKET.
- Les données envoyées peuvent être remplies directement ou utiliser d'autres blocs ovales avec des valeurs de retour sous forme de chaînes ou de valeurs numériques.

<h3 class="lua-cmd" id="s_result" >Obtenir le résultat de l'envoi de la variable</h3>

![](images/tcp_send_result.png)

**Description:** Obtenir le résultat de l'envoi de la variable TCP

**Paramètres:** Sélectionnez le numéro de SOCKET.

**Valeur de retour:** Envoi d'un succès renvoie 0, envoi d'un échec renvoie 1.