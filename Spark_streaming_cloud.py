from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# 1. Initialize Spark Session
# Note: Packages are already passed via spark-submit, but keeping config for consistency
spark = SparkSession.builder \
    .appName("PipelineKafkaSpark") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3,org.mongodb.spark:mongo-spark-connector_2.12:10.3.0") \
    .getOrCreate()

# Reduce verbosity to see data clearly
spark.sparkContext.setLogLevel("WARN")

# Define Schema based on your producer output
schema = StructType([
    StructField("capteur_id", IntegerType()),
    StructField("temperature", DoubleType()),
    StructField("humidity", DoubleType()),
    StructField("timestamp", DoubleType())
])

# 2. Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "capteurs-iot") \
    .option("startingOffsets", "latest") \
    .load()

# 3. Parse JSON and convert timestamp
data_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .withColumn("event_time", timestamp_seconds(col("timestamp")))

# 4. Processing & Aggregation
# Using a 10-second window to group sensor data
agg_df = data_df.filter(col("temperature").isNotNull()) \
    .groupBy(
        window(col("event_time"), "10 seconds"),
        col("capteur_id")
    ).agg(
        avg("temperature").alias("avg_temp"),
        avg("humidity").alias("avg_humidity")
    )

# 5. Writing to Sinks
# 

# Sink A: MongoDB
# For v10.x, use 'database' and 'collection' options
query_mongo = agg_df.writeStream \
    .format("mongodb") \
    .queryName("MongoWriter") \
    .outputMode("complete") \
    .option("checkpointLocation", "/tmp/checkpoints/mongo") \
    .option("connection.uri", "mongodb://mongodb:27017") \
    .option("database", "iot") \
    .option("collection", "capteurs") \
    .start()

# Sink B: Console - "update" is fine here, but "complete" is safer for consistency
query_console = agg_df.writeStream \
    .format("console") \
    .queryName("ConsoleWriter") \
    .outputMode("complete") \
    .option("truncate", "false") \
    .start()

# Wait for the termination of the streams
spark.streams.awaitAnyTermination()
