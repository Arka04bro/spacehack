import sqlite3
weight, height, biometric, gender, job, disease, ethos, blood_type, room = input("Введите данные через пробел: ").split()
conn = sqlite3.connect('medical_data.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS MedicalRecords (
    id INTEGER PRIMARY KEY,
    weight REAL,
    height REAL,
    gender TEXT,
    biometric_data TEXT,
    job TEXT,
    room TEXT,
    disease TEXT,
    blood_type TEXT,
    ethos TEXT
)
''')
cursor.execute('''
INSERT INTO MedicalRecords (weight, height, biometric_data, gender, job, disease, ethos, blood_type, room)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (weight, height, biometric, gender, job, disease, ethos, blood_type, room))
conn.commit()
conn.close()
