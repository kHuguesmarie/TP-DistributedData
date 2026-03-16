#python
import findspark
findspark.init()  # Configure Spark et Hadoop

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TestSparkWindows") \
    .master("local[*]") \
    .getOrCreate()

# Exemple : lire un CSV local
df = spark.read.csv("Chemin_absolu_vers_fichier/etudiants.csv", header=True, inferSchema=True)
df.show()

spark.stop()
