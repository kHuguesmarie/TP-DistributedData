a)	Préparation du fichier de données sur cloud 
Si le fichier se trouve sur le stockage cloud, sur Azure, on utilise Azure Blob Storage ou Azure Data Lake Storage Gen2 :
•	Créer un Storage Account (gratuit avec le mail étudiant @viacesi)
•	Aller sur : https://portal.azure.com 
•	Create Resource → Storage Account/Compte de stockage
•	Abonnement : Azure for students
•	Groupe de ressources : rg-spark-tp
•	Nom du compte de stockage : monsparkstorage
•	Région : (Europe) France Central
•	Type de stockage préféré : Laisse vide ou par défaut.
•	Performance : Standard (recommandé)
•	Redondance : Stockage localement redondant (LRS)
•	Vérifier et créer
•	Créer
•	Accéder à la ressource
Créer un container
•	Aller dans la section “Stockage de données” dans le menu de gauche 
•	Puis clique sur : Conteneurs
•	Une fois dans Conteneurs, en haut de la page cliquer sur le bouton : + Ajouter un container
•	Nom du conteneur : sparkdata
•	Niveau d’accès public : Privé (recommandé)
•	Puis clique sur : Créer
•	Tu dois voir : sparkdata
•	Clique dessus → bouton Télécharger/Charger → ajouter le fichier depuis l’ordinateur : etudiants.csv
Récupérer la clé d’accès et lire depuis Spark (Azure Blob)
•	Storage Account → Access keys ” dans le menu de gauche
•	Dans le menu latéral gauche, cherche Security + réseau → Access keys
•	Une fois ouvert, tu verras le Account Name Key1 et Key2. Coper le nom du compte (monsparkstorage) ; copier Key1 (ou Key2)
