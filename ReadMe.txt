Informations complémentaires ChatCROM V3


1 Précisions sur le programme.

	1.1 Finalité.
	Ce programme est un outil de messagerie dédie à l'association CROM

	1.2 A qui s'adresse-t-il    ?
	Ce programme est réservé aux membres actifs et/ou aux membres fondateurs de l'association

	1.3 Conséquences.
	Pour ces raisons, il est demandé aux membres de ne pas distribuer ce programme hors association.

	1.4 Prérequis.
	L’accès aux fonctionnalités du programme nécessite la création d'un compte, donc de choisir un couple utilisateur/mot de passe
en cas de perte de ce mot de passe, un mail devra être envoyé à l'admin afin de choisir un nouveau mot de passe.


2. Outils employés pour le développement de ce programme.

	2.1. Le SGBD utilisé pour le stockage des données est MySQL/MariaDB.

	2.2. Le programme a été développé en Python 3.4/3.5.

	2.3. Le connecteur SGBD employé est PyMySQL.

	2.4. La bibliothèque employée pour la construction de la GUI est Tkinter.ttk.

	2.5. La compilation du code python s'est effectué à l'aide de cx_freeze.

	2.6. Les éléments graphiques.
	Ils sont la propri騁�de l'association pour le logo de la fen黎re de login, et proviennent de la biblioth鑷ue d'icones gratuite FatCow Web Hosting free icons library


3. Manuel d'utilisation.

	3.1 Téléchargement.
	Le programme peut 黎re t駘馗harg�depuis le FTP CROM ftp://killian68.synology.me

	3.2 Installation.
	Le programme fonctionne sous windows xp et plus. Pour lancer l'installation, double cliquez sur le fichier setupChatCROM.exe est laissez vous guider.
	En cas de mise à jour, il est recommandé de désinstaller la version précédente avant d'installer la nouvelle version.

	3.3 Connexion.
	Au lancement du programme, vous devez choisir votre nom d'utilisateur dans la liste déroulante et vous identifier. Les connexions anonymes (sans login et/ou mot de passe) ne sont pas autorisées. Un mot de passe vide ou erroné mettra fin au programme.

	3.4 Interface.
	
		3.4.1. La fenêtre principale.

			3.4.1.1. Affichage des messages.
			Cette zone vous donne la date et l'heure de l'envoi du message, l’émetteur de ce message ainsi qu'une vue du début du message. Si le message est trop long ou bien dépasse une certaine taille, un signe plus apparaîtra en vert devant l'heure du message. Vous pourrez alors sélectionner le message et cliquer sur détail pour voir le message en entier.
			Les messages que vous avez envoyés apparaissent en blanc. Les messages reçus publics apparaissent en blanc cassé. Les messages privés qui vous sont destinés sont surlignés en gris, et les messages de l'administrateur apparaissent surlignés en rosés.
			Vous pouvez double-cliquer sur un message pour afficher directement les détails de ce dernier.

			3.4.1.2. Liste des utilisateurs de la messagerie.
			Dans cette liste apparaissent tous les pseudos des personnes ayant accès au programme. Une puce verte devant leur nom indique qu'ils sont actuellement connectés, une puce rouge indique qu'ils sont hors ligne.
			Un double clic sur un nom ouvre une fenêtre de nouveau message avec cet utilisateur comme destinataire (cela peut être changé grâce à la liste déroulante). De même, choisir un destinataire dans la liste et cliquer sur le bouton nouveau message pré renseignera cet utilisateur comme destinataire.

			3.4.1.3. Les boutons d'action
			Trois boutons sont accessibles. Nouveau message, Détail et Quitter. Nouveau message fait apparaître la fenêtre de rédaction de nouveau message. Le bouton détail n'est accessible que si un message est sélectionné. Il permet d'afficher le détail d'un message.
			Le bouton Quitter vous déconnecte de la base et vous fait quitter le programme.

			3.4.1.4. Le menu Action.
			Depuis ce menu vous pouvez, créer un nouveau message, cela revient à cliquer sur le bouton nouveau message. Vous pouvez aussi accéder à la fenêtre de configuration. Cette fenêtre est aussi accessible depuis la fenêtre de connexion (bouton configuration en bas à droite de la fenêtre).

		3.4.2. La fenêtre de nouveau message.

		Cette fenêtre vous permet de choisir un destinataire (ou de changer de destinataire si vous avez double cliqué ou pré choisi un destinataire). Par défaut, les messages sont à destination de tout le monde. L'horodatage du message (que vous ne pouvez pas changer) Puis votre message.
		Etant donné que vous pouvez utiliser des retours chariots dans votre texte, pour valider et envoyer votre message, ou bien annuler l'envoi, vous devez utiliser les boutons de l'interface.

		3.4.3. La fenêtre de connexion.

		Depuis cette fenêtre, vous pouvez choisir dans la liste déroulante votre pseudo et renseigner votre mot de passe. Si la liste déroulante est vide, c'est que votre connexion à la base de données ne peut être établie, et vous avez normalement déjà du avoir un message d'erreur. Vous pouvez malgré tout accéder à la fenêtre de configuration afin de vérifier la méthode de connexion à la base de données.

3.4.4. La fenêtre de configuration.

		Depuis cette fenêtre, vous pouvez choisir votre méthode de connexion à la base de données qui stocke les messages. Si vous êtes connectés à internet depuis le réseau local de l'auteur du programme, il vous faut choisir «  192.168.1.100  ». Si vous êtes dans n'importe quelle autre situation, il vous faut choisir «  killian68.synology.me  ».
		Vous avez aussi la possibilité de choisir le type de son qui sera joué pour indiquer un nouveau message. Les choix sont : Pas de son, aucun son n'est joué – son par défaut, un bip simple – et choisir son fichier. Vous pourrez alors parcourir votre disque dur afin de choisir un son personnalisé. Notez au passage que seuls les fichiers wav sont sélectionnables pour les alarmes. Ce n'est pas un bug, c'est une limitation volontaire.
		IMPORTANT : Le fait d’accéder à la fenêtre de configuration, que vous changiez les paramétrés ou non vous obligera à relancer le programme. C'est tout à fait normal.
