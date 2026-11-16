import sqlite3

DB_NAME = "measurements.db"


def init_db():
    connection = sqlite3.connect(DB_NAME)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER NOT NULL,  
            location TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            air_quality INTEGER NOT NULL
        )
    """)

    connection.commit()  
    connection.close()


def save_reading(reading):
    connection = sqlite3.connect(DB_NAME)

    connection.execute("""
        INSERT INTO measurements (
            sensor_id,
            location,
            timestamp,
            temperature,
            humidity,
            air_quality
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        reading["sensor_id"],
        reading["location"],
        reading["timestamp"].isoformat(timespec="seconds"),
        reading["temperature"],
        reading["humidity"],
        reading["air_quality"]
    ))

    connection.commit()
    connection.close()

def get_readings():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.execute("SELECT * FROM measurements")
    readings = cursor.fetchall()
    connection.close()
    return readings

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
