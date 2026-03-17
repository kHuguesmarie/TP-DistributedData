from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='<IP_WINDOWS>:9092',  # Windows → Docker (remplace <IP_WINDOWS> par ton IP locale sur Windows )
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "capteur_id": random.randint(1,5),
        "temperature": round(random.uniform(18,45),2),
        "humidity": round(random.uniform(30,90),2),
        "timestamp": time.time()
    }
    producer.send("capteurs-iot", data)
    print(data)
    time.sleep(1)
