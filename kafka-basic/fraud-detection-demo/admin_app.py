from kafka import KafkaConsumer
import json

print("=== Fraud Alert System ===")

admin_id = input("Enter Admin ID to login: ")

if admin_id != "101":
    print("Access Denied!")
    exit()

print("Admin Login Successful")
choice = input(
    "\n1. View My Alerts\n"
    "2. View All Alerts (Admin)\n"
    "Enter choice: "
)

consumer = KafkaConsumer(
    'fraud-notification',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("\nListening for alerts...\n")

for message in consumer:

    alert = message.value

    # Show only logged-in user's alerts
    if choice == "1":
        if alert.get("userId") != admin_id:
            continue

    # Show all alerts
    print("\n🚨 FRAUD ALERT 🚨")
    print(f"User ID: {alert.get('userId')}")
    print(f"User Name: {alert.get('name')}")
    print(f"Transaction ID: {alert.get('tx_id')}")
    print(f"Amount: ${alert.get('amount'):.2f}")
    print("-" * 50)