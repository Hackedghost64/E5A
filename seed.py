from api.database import SessionLocal, Machine, init_db

def seed():
    init_db()
    db = SessionLocal()
    
    machines = ["Mini Tractor", "Power Sprayer", "Heavy Duty Plough", "Rice Mill", "Water Pump"]
    
    for m_name in machines:
        exists = db.query(Machine).filter(Machine.name == m_name).first()
        if not exists:
            db.add(Machine(name=m_name))
    
    db.commit()
    db.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
