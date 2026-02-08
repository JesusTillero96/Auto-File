import csv
import os
from datetime import datetime

log_file = "logs/activity_log.csv"

def log_action(action):
    os.makedirs("logs", exist_ok=True)
    with open(log_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action])
