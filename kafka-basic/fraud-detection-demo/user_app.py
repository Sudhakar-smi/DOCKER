from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'fraud-notification',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for Fraud Alerts...")

for message in consumer:
    alert = message.value

    print("\n🚨 FRAUD ALERT 🚨")
    print(f"User ID: {alert['userId']}")
    print(f"Transaction ID: {alert['tx_id']}")
    print(f"Amount: ₹{alert['amount']}")