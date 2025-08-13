# 6.3 Programmation de script

<h2 id="overview" class="m3">6.3.1 Généralités</h2>

Le robot Dobot fournit de riches interfaces API Dobot, telles que des commandes de mouvement, des commandes TCP/UDP, etc. Il adopte le langage Lua, ce qui est pratique pour les utilisateurs dans le cadre du développement secondaire. DobotStudio Pro fournit un environnement de programmation pour les scripts Lua, de sorte que les utilisateurs peuvent écrire leurs propres scripts Lua pour contrôler le fonctionnement du robot.
**Projet** : La programmation des scripts est éditée et exécutée en tant que projet, ce qui facilite le débogage. L'accès à la page de programmation par l'icône de la page d'accueil de l'application crée par défaut un nouveau projet sans nom, qui doit être nommé et sauvegardé après la programmation avant d'être débogué et exécuté. Le projet est enregistré dans le contrôleur du bras robotique et prend en charge l'importation et l'exportation.

Un projet comprend les fichiers de script suivants, qui sont affichés sous forme d'onglets :

- Le fichier **src0.lua** est le **fil d'exécution principal** et peut appeler toute commande<br/>
- Le fichier **global.lua** est utilisé uniquement pour définir les variables et les sous-fonctions.<br/>
- 0 à 4 **sous-filières** nommées **src1.lua**~**src4.lua**. Programmes parallèles exécutés avec le programme principal, pour lesquels vous pouvez définir les E/S et les variables, mais lesquels ne peuvent appeler aucune commande de mouvement.

<br/>

Après le démarrage du projet, le robot exécute les instructions du fil principal et des fils secondaires un par un, de haut en bas, et l'utilisateur n'a pas besoin de définir la fonction d'entrée (principale). Pour plus d'informations sur la syntaxe de base de Lua, veuillez vous référer à l'[annexe C](..\script\lua.md).
**Points de sauvegarde** : au cours du processus de programmation, l'utilisateur peut déplacer le robot à tout moment en le touchant ou en le faisant glisser, puis ouvrir la liste des points de sauvegarde pour enregistrer la position actuelle du robot en tant que point d'apprentissage. Les points d'apprentissage de la liste des points de sauvegarde sont liés au projet et peuvent être utilisés comme paramètres de la commande. Si vous souhaitez enregistrer des points d'apprentissage pouvant être appelés dans plusieurs projets, utilisez des [variables globales](../monitoring/global_var.md).

L'interface principale de la programmation de scripts est illustrée ci-dessous.

<div align=center><img src="images/script_main.png" /></div>

<br/>

<table width="100%">
  <colgroup>
    <col style="width: 10%">
    <col style="width: 90%">
  </colgroup>
  <tr>
    <th>Numéro de série</th>
    <th>Description</th>
  </tr>
  <tr>
    <td style="text-align:center">1</td>
    <td>Pour afficher la désignation du projet et gérer les projets. </td>
  </tr>
  <tr>
    <td style="text-align:center">2</td>
    <td>Cliquez pour ouvrir l'interface des points de sauvegarde, utilisée pour gérer les points de sauvegarde dans les projets. </td>
  </tr>
  <tr>
    <td style="text-align:center">3</td>
    <td>Boutons relatifs au débogage et à l'exécution du projet. </td>
  </tr>
  <tr>
    <td style="text-align:center">4</td>
    <td>Pour rechercher et utiliser les fonctions de programmation. Cliquez sur <img src="images/help.png" height="22"/>pour consulter le document de description de la fonction. </td>
  </tr>
  <tr>
    <td style="text-align:center">5</td>
    <td>Zone d'édition du programme, vous pouvez cliquer sur les onglets pour basculer entre les fichiers Script ou cliquer sur + pour ajouter un sous-filière. <br/>Cliquez sur<img src="images/undo_redo.png" height="20" />en haut à droite pour annuler/refaire une opération de programmation. </td>
  </tr>
  <tr>
    <td style="text-align:center">6</td>
    <td>Barre des journaux d'exécution, utilisée pour consulter les journaux d'exécution du projet. <ul><li>Cliquez sur l'icône<img src="images/log_icon.png" width="25" /> la plus à droite pour développer ou réduire la zone d'affichage des journaux ; </li><li>Les options à gauche permettent de filtrer les types de journaux affichés ; </li><li>Cliquez sur <img src="images/search_icon.png" height="18"/> <b>Rechercher</b> pour trouver un caractère spécifié dans les journaux ;</li><li>Cliquez sur <img src="images/clear_icon.png" height="18"/> <b>Effacer</b> pour vider la zone d'affichage des journaux. </li></td>
  </tr>
</table>

<h2 id="project" class="m3">6.3.2 Gestion de projet</h2>

   <div align=center><img src="images/script_manage.png" width="300" /></div>

Lorsque vous ouvrez l'interface de script, une nouvelle page de projet vierge est affichée par défaut, et le nom du projet **n'est pas nommé**.

Cliquer sur <img src="images/file.png" height="16"/> pour ouvrir le menu Fichier pour créer, ouvrir, enregistrer, importer ou exporter un projet.

<div class="info1"><img src="../image/info.png"  height="18" /><b> Description : </b><div>Lors de la création d'un nouveau projet, vous pouvez choisir un projet vide ou sélectionner un modèle de programmation de script. </div><br/><div align=center><img src="images/script_new.png" width="300"/></div></div>

<br/>

Cliquer sur <img src="images/save.png" height="16"/> pour enregistrer le projet actuel. Saisir une désignation d'abord si le projet n'est pas encore nommé.

DobotStudio Pro sauvegarde automatiquement le projet dans les scénarios suivants :

- DobotStudio Pro vérifie toutes les dix minutes si le projet actuellement ouvert a été modifié ; si c'est le cas, il sauvegarde automatiquement le projet en cours sur le contrôleur.<br/>
- Avant que le projet ne commence à s'exécuter, DobotStudio Pro vérifie si le projet actuellement ouvert a été modifié ; si c'est le cas, il sauvegarde automatiquement le projet actuel sur le contrôleur.<br/>
- Lorsque DobotStudio Pro est déconnecté du contrôleur (déconnexion active ou déconnexion anormale), DobotStudio Pro vérifie s'il y a des modifications au projet actuellement ouvert ; si c'est le cas, il sauvegarde automatiquement le projet en cours sur le local (PC ou tablette).<br/>

La sauvegarde sur le contrôleur et le projet local peuvent être ouverts via l'option **Ouvrir le projet** de sauvegarde du menu <img src="images/file.png" height="16"/>.

<h2 id="point" class="m3">6.3.3 Points de sauvegarde</h2>

L'utilisateur peut déplacer le robot jusqu'à la position souhaitée en le [jog](../operation/jog_oper.md) ou en le [faisant glisser](../operation/drag.md), puis enregistrer la position dans la liste des points de sauvegarde.

<div class="info1"><img src="../image/info.png"  height="18" /><b> Description : </b><div>Lorsque la liste des points de sauvegarde est ouverte, appuyez sur le bouton <b>POINT</b> sur le côté de la rotule finale du CR20A pour ajouter un point d’enseignement. </div></div>

<br/>

<div align=center><img src="images/blockly_point.png" /></div>

<table width="100%">
  <tr>
    <th>Numéro de série</th>
    <th>Description</th>
  </tr>
  <tr>
    <td style="text-align:center">1</td>
      <td><ul><li>Cliquez sur le bouton <img src="images/add_icon.png" height="18"/> <b>Point d’ajout</b> pour enregistrer la position actuelle du robot comme un nouveau point d’enseignement. </li><li>Après avoir sélectionné un point d’enseignement, cliquez sur le bouton <img src="images/cov_icon.png" height="18"/> <b>Remplacer</b> pour remplacer ce point par la position actuelle du robot. </li><li>Après avoir sélectionné un point d’enseignement, cliquez sur le bouton <img src="images/del_icon.png" height="18"/> <b>Supprimer</b> pour effacer ce point. </li><li>Cliquez sur <b>Filtrage par alias</b> pour filtrer et afficher dans la liste les points correspondant aux critères spécifiés. </li></ul></td>
  </tr>
  <tr>
    <td style="text-align:center">2</td>
    <td>Liste des points d’enseignement. Après avoir sélectionné un point d’enseignement, cliquez sur n'importe quelle valeur autre que <b>NO.</b> et <b>Point</b> pour modifier directement cette valeur. </td>
  </tr>
  <tr>
    <td style="text-align:center">3</td>
    <td>Contrôlez le robot pour qu'il se déplace vers le point sélectionné en utilisant le mode de mouvement spécifié. </td>
  </tr>
</table>

<br/>

La position du point sélectionné dans la liste de sauvegarde s'affiche sous la forme d'un contour bleu dans la zone de simulation du panneau de pointage et de clic, comme le montre la figure ci-dessous.

<div align=center><img src="images/point2.png" /></div>

<br/>

<h2 id="program" class="m3">6.3.4 Programmation</h2>

L'utilisateur peut insérer des commandes de la manière centralisée suivante :

- Recherchez la fonction que vous souhaitez utiliser dans le menu Fonction à gauche et cliquez sur <img src="images/insert_cmd.png" height="16" /> sur le côté droit de celle-ci pour afficher la fenêtre de réglage des paramètres. Définir les paramètres dans la fenêtre et cliquer sur <b>Confirmer</b> pour ajouter une commande paramétrée à la position du curseur dans la zone de programmation.

<div align=center><img src="images/script_cmd.png" width="400" /></div>

<br />

- Recherchez la fonction que vous souhaitez utiliser dans le menu de gauche et double-cliquez dessus pour insérer rapidement l'instruction dans la zone de programmation avec le paramètre par défaut, puis modifiez la valeur du paramètre en fonction de vos besoins.

<div align=center><img src="images/script_insert.png" width="600" /></div>

<br />

- Saisir le programme directement dans la zone de programmation de droite et prenez en charge l'autocomplétion des instructions à l'aide de la touche TAB du clavier.
- **Ajouter des points d'arrêt** : cliquez sur la ligne de code avec la souris ou le doigt pour ajouter des points d'arrêt, qui sont marqués comme indiqué dans les lignes 3 et 5 de la figure suivante. Lorsque le script atteint la ligne de code définie comme point d'arrêt, il s'interrompt ; à ce moment, le curseur reste sur la ligne du point d'arrêt et celle-ci n'est pas exécutée.
  
  <div align=center><img src="images/point_add.png" width="200" /></div>
  
  <br />
  
- **Supprimer les points d'arrêt** : cliquez à nouveau sur la ligne de code comportant des points d'arrêt pour les supprimer, ou cliquez sur le bouton **Effacer les points d'arrêt** <img src="images/clear_point.png" height="18"/> pour effacer tous les points d'arrêt du projet en cours. Il est interdit d'utiliser le bouton **Effacer les points d'arrêt** <img src="images/clear_point.png" height="18"/> pendant l'exécution du programme.

<br/>

<div class="info2"><img src="../image/info.png"  height="18" /><b> Description : </b><div><ul>
    <li>Lorsque le programme est en état de pause, il est possible d'ajouter ou de supprimer des points d'arrêt. </li><li>Seul le script src0.lua pour la programmation de script prend en charge l'ajout de points d'arrêt. </li>
    </ul></div></div>

<br/>

Avant de commencer la programmation, définissez la fonction que vous souhaitez réaliser. Cette section décrit comment écrire un projet de script en donnant un exemple d'écriture d'un programme permettant de contrôler le robot pour qu'il se déplace de manière cyclique entre deux points.
1. Ajoutez le point de départ P1 et le point d'arrivée P2 du mouvement cyclique du robot dans l'ordre dans la page Enregistrer les points.

2. Écrivez la fonction de boucle `while` d'ajout de l'une des manières ci-dessus.

3. Ajoutez une instruction de déplacement `MovJ` avant `end` du code de la boucle, avec le point cible P1.

4. Ajoutez une autre instruction de déplacement `MovJ` avec le point cible P2. Le code final est le suivant.

```lua
while(true)
do
    MovJ(P1)
    MovJ(P2)
end
```

A ce stade, un programme simple de mouvement cyclique a été écrit.

Si vous avez besoin d'écrire un sous-programme, vous pouvez cliquer sur <b>+</b> sur le côté droit de l'onglet en haut de la zone de programmation, puis passer à l'onglet Sub-Thread pour écrire le programme.

Pour plus d'informations sur les scripts, cliquez sur Vue <img src="images/help.png" height="22"/> dans le menu Fonctions, qui est le même que celui de [l'annexe C](..\script\script_manual.md).