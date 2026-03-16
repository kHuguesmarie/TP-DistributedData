#python
# Import de la classe SparkSession
# SparkSession est le point d'entrée principal pour manipuler
# les DataFrames et utiliser Spark SQL dans Apache Spark
from pyspark.sql import SparkSession

# Création et configuration de la session Spark
spark = (
    SparkSession.builder
    
    # Nom de l'application (visible dans Spark UI)
    .appName("TP1_Spark_Azure")
    
    # Mode d'exécution :
    # local[*] signifie que Spark s'exécute en local
    # en utilisant tous les cœurs CPU disponibles
    .master("local[*]")
    
    # Ajout des dépendances nécessaires pour accéder
    # au stockage Azure (Blob Storage ou ADLS Gen2)
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-azure:3.3.4")

# Création de la session Spark (ou récupération si déjà existante)
    .getOrCreate()
)

# Message de confirmation
print("Spark Session configurée avec succès pour Azure !")
