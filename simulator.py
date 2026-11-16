import random
from datetime import datetime
from database import init_db, save_reading, get_readings


class Sensor:
        def __init__(self, sensor_id, location):
            self.sensor_id = sensor_id
            self.location = location

        def generate_reading(self):
            temperature = round(random.uniform(18, 30), 2)
            humidity = round(random.uniform(30, 70), 2)
            air_quality = random.randint(0, 100)

            reading = {
                "sensor_id": self.sensor_id,
                "location": self.location,
                "timestamp": datetime.now(),
                "temperature": temperature,
                "humidity": humidity,
                "air_quality": air_quality
         }

            return reading

sensors = [
    Sensor(1, "Living Room"),
    Sensor(2, "Bedroom"),
    Sensor(3, "Kitchen")
]

init_db()

for sensor in sensors:
    reading = sensor.generate_reading()
    save_reading(reading)
    print(reading)

print("All readings saved successfully!")


print("\nReading data from database:\n")

readings = get_readings()

print(
    f"{'ID':<5}"
    f"{'Sensor':<8}"
    f"{'Location':<15}"
    f"{'Timestamp':<20}"
    f"{'Temp (°C)':>10}"
    f"{'Humidity':>10}"
    f"{'Air Quality':>13}"
)

print("-" * 81)

for reading in readings:
    id, sensor_id, location, timestamp, temperature, humidity, air_quality = reading

    print(
        f"{id:<5}"
        f"{sensor_id:<8}"
        f"{location:<15}"
        f"{timestamp:<20}"
        f"{temperature:>10.2f}"
        f"{humidity:>10.2f}"
        f"{air_quality:>13}"
    )

for reading in readings :
     print(reading)