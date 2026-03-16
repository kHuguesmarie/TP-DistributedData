#python
spark = SparkSession.builder \
    .appName("SparkAzure") \
    .master("local[*]") \
    .getOrCreate()

#spark.conf.set(
# "fs.azure.account.key.<NOM_DU_COMPTE>.blob.core.windows.net",
# "<KEY1_COPIEE>"
#)
spark.conf.set(
    "fs.azure.account.key.monsparkstorage.blob.core.windows.net",
    "VOTRE_CLE_ICI"
)

#df = spark.read.csv(
#"wasbs://<NOM_CONTAINER>@<NOM_DU_COMPTE>.blob.core.windows.net/#etudiants.csv",
#header=True,
#inferSchema=True
#)

df = spark.read.csv(
    "wasbs://sparkdata@monsparkstorage.blob.core.windows.net/mon_fichier.csv", ##"wasbs://<NOM_CONTAINER>@<NOM_DU_COMPTE>.blob.core.windows.net/mon_fichier.csv"
    header=True,
    inferSchema=True
)

# Transformations here


# Actions here
df.show()
