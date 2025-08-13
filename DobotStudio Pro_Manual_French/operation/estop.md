# 5.8 Arrêt d'urgence et récupération

Cliquer sur ce bouton pour arrêter le bras en cas d'urgence pendant le fonctionnement du robot.

L'utilisateur peut déclencher la fonction d'arrêt d'urgence par les méthodes suivantes :

- En appuyant sur le bouton d'arrêt d'urgence connecté au contrôleur du robot.
- Déclencher l'entrée d'arrêt d'urgence de l'utilisateur dans l'interface [E/S de sécurité](../monitoring/io_monitor_safe_io.md).
- En cliquant sur le bouton d'arrêt d'urgence dans le coin supérieur droit de l'interface logicielle.

<div align=center><img src="image/estop.png" /></div>

<br/>

Après le déclenchement de l'événement d'arrêt d'urgence, le robot a deux états d'arrêt comme suit :

- S'il est arrêté dans les 500 ms, le robot est uniquement désactivé et n'est pas mis hors tension ;

- Si le robot est toujours en mouvement après 500 ms, il est forcé d'être désactivé et mis hors tension.

<br/>

<div class="caution2"><img src="../image/caution.png" height="18" /><b> Attention : </b><div><ul>
    Pour la série de robots Magician E6, un déclenchement d'arrêt d'urgence entraînera une désactivation directe.
    </ul>
    </div></div>

<br/>

Les deux états génèrent respectivement les alarmes correspondantes.
Lorsqu'un arrêt d'urgence se produit, l'icône du bouton d'arrêt d'urgence clignote. Si vous devez réactiver le robot, cliquez à nouveau sur le bouton d'arrêt d'urgence pour réinitialiser, puis effacer les alarmes et enfin réactiver le robot (si le robot est hors tension, vous devez d'abord le mettre sous tension conformément à la fenêtre contextuelle).

<br/>

<div class="caution2"><img src="../image/caution.png" height="18" /><b> Attention : </b><div><ul>
    <li>Le bouton d'arrêt d'urgence sur l'interface logicielle n'est qu'un complément à la fonction d'arrêt d'urgence matériel. En cas d'urgence, il est préférable de privilégier l'utilisation de la fonction d'arrêt d'urgence matériel pour arrêter le robot. </li>
    <li>Un arrêt d'urgence déclenché par un bouton d'arrêt d'urgence physique ou par l’E/S de sécurité modifiera également l'état de ce bouton. Cependant, dans ce cas, il n'est pas possible de réinitialiser le bouton via l'interface logicielle ; il doit être réinitialisé via la source d'entrée correspondante. </li>
    </ul>
    </div></div>
