# Lecture d’un fichier CSV dans un DataFrame Spark
df = spark.read.csv(
    r" C:\votre_chemin_local\mon_fichier.csv", #mon_fichier.csv
    header=True,      # Première ligne = noms des colonnes
    inferSchema=True  # Détection automatique des types de données
)

# Affiche les premières lignes du DataFrame (Action)
df.show()

# Message de confirmation
print("Lecture du fichier CSV avec succès !")

# Affiche la structure (noms des colonnes et types): Affichage du schéma
df.printSchema()

# Affiche les statistiques descriptives des colonnes numériques
df.describe().show()

# Sélectionne uniquement les colonnes "nom" et "score"
# puis affiche le résultat
df.select("nom", "score").show()
