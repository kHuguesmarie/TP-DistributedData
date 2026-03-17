from kafka import KafkaProducer
import json, time, random

# Utiliser l'IP publique de la VM pour envoyer depuis l'extérieur
producer = KafkaProducer(
    bootstrap_servers='<IP_PUBLIQUE_VM>:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {"capteur_id": random.randint(1,5), "temperature": round(random.uniform(18,45),2), "humidity": round(random.uniform(30,90),2), "timestamp": time>
    producer.send("capteurs-iot", data)
    print(f" Envoyé : {data}")
   time.sleep(1)
