from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI", "mongodb://mongodb:27017"))
db = client["iot"]
collection = db["capteurs"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    docs = list(collection.find({}, {"_id": 0}).sort("window", -1).limit(100))
    for doc in docs:
        if "window" in doc:
            doc["window_start"] = str(doc["window"].get("start", ""))
            doc["window_end"] = str(doc["window"].get("end", ""))
            del doc["window"]
    return jsonify(docs)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="localhost", port=port, debug=True)
