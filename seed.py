import json
import os
from api.database import SessionLocal, Machine, init_db

def seed():
    init_db()
    db = SessionLocal()
    
    catalog_path = os.path.join("data", "catalog.json")
    if not os.path.exists(catalog_path):
        print(f"Error: {catalog_path} not found.")
        return

    with open(catalog_path, "r") as f:
        data = json.load(f)
        machines = data.get("machines", [])
    
    for m_name in machines:
        exists = db.query(Machine).filter(Machine.name == m_name).first()
        if not exists:
            db.add(Machine(name=m_name))
            print(f"Added: {m_name}")
    
    db.commit()
    db.close()
    print("Database seeded successfully from catalog.json!")

if __name__ == "__main__":
    seed()
