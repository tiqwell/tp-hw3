import csv
import random
import os
import sys

NUM_ROWS = 100


COLUMNS = ["order_id", "item_name", "price", "quantity"]

def generate_row(row_id):
    items = ["book1", "book2", "book3", "book4", "book5"]
    item = random.choice(items)
    
    prices = {"book1": 250, "book2": 180, "book3": 110, "book4": 90, "book5": 150}
    
    return {

        "order_id": row_id,
        "item_name": item,
        "price": prices[item],
        "quantity": random.randint(1, 4),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row(i) for i in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

