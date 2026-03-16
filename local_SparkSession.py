#Création d’un SparkSession
# Import de la classe SparkSession
# SparkSession est le point d'entrée principal pour travailler avec
# les DataFrames et Spark SQL dans Apache Spark
from pyspark.sql import SparkSession

# Création de la SparkSession
# Le builder permet de configurer les paramètres de l'application Spark
spark = (
    SparkSession.builder
    
    # Nom de l'application (visible dans Spark UI)
    .appName("TP1_Spark_Local")
    
    # Mode d'exécution :
    # local[*] signifie exécution en local en utilisant
    # tous les cœurs CPU disponibles de la machine
    .master("local[*]")
    
    # Création de la session Spark
    # Si une session existe déjà, elle sera réutilisée
    .getOrCreate()
)

# Affichage d'un message de confirmation
print("Spark Session configurée avec succès !")
