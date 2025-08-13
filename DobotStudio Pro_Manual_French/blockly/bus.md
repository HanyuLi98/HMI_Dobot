# Blocs de construction Bus

Le jeu de blocs de construction Bus est utilisé pour lire et écrire des registres de bus Profinet ou Ethernet/IP. Veuillez vous référer à la documentation du protocole de communication de bus Dobot (EtherNet/IP, Profinet) pour l'utilisation de la fonction de communication de bus.

<div class="info1"><img src="images/info.png"  height="18" /><b>Description : </b><div>Magician E6 ne prend pas en charge cet ensemble de commande. </div></div>


<h3 class="lua-cmd" id="getbusreg" >Obtenir la valeur du registre de bus</h3>

![](images/bus_getreg.png)

**Description:** Obtient la valeur du registre de bus spécifié.

**Paramètres :**

- Sélectionner le type de registre, prendre en charge le registre d'entrée du bus et le registre de sortie du bus.
- Sélectionnez le type de données du registre, bool, int, float sont pris en charge.
- Sélectionnez l'adresse du registre de maintien.

**Valeur de retour:** La valeur du registre spécifié. La valeur du type bool est 0 ou 1.


<h3 class="lua-cmd" id="setbusreg" >Définir la valeur du registre de bus</h3>

![](images/bus_setreg.png)

**Description:** Définit la valeur du registre de bus spécifié.

**Paramètres :**

- Sélectionnez le type de registre ; actuellement, seuls les registres de sortie de bus sont pris en charge.
- Sélectionnez le type de données du registre, bool, int, float sont pris en charge.
- Sélectionnez l'adresse du registre de maintien.
- Saisir la valeur à définir. La valeur du type bool est 0 ou 1.