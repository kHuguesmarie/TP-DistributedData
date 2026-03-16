# 1 Informations Azure Blob Storage: Paramètres Azure Blob Storage
storage_account_name = " votre_nom_de_compte"  # Nom de ton Storage Account
storage_account_key = "votre_cle_d_acces_secrete # Copie de Key1 depuis Access Keys
container_name = " votre_nom_de_container"              # Nom du container où se trouve le fichier

# 2 Configuration de la clé d'accès dans le contexte Hadoop de Spark
# Injection de la clé d'accès dans la configuration Hadoop de Spark
spark._jsc.hadoopConfiguration().set(
    f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net",
    storage_account_key
)

# 3 Définition du Chemin du fichier sur Azure Blob Storage (wasbs://)
path_azure = (
    f"wasbs://{container_name}@"
    f"{storage_account_name}.blob.core.windows.net/"
    "mon_fichier.csv" #mon_fichier.csv
)

# 5️ Lecture du DataFrame
df = spark.read.csv(
    path_azure,
    header=True,        # Première ligne = noms de colonnes
    inferSchema=True    # Détection automatique des types
)

# 6️ Affichage des 5 premières lignes
df.show(5)

# Affiche la structure (noms des colonnes et types): Affichage du schéma
df.printSchema()

# Affiche les statistiques descriptives des colonnes numériques
df.describe().show()

# Sélectionne uniquement les colonnes "nom" et "score"
# puis affiche le résultat
df.select("nom", "score").show()
