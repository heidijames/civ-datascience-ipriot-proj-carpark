# main.py
# This script simulates a simple smart carpark using sensors and car objects

"""
main.py
Simulates a smart carpark system using entry and exit sensors,
and displays the current carpark status and temperature.
"""

from smartpark.models import Car, Carpark
from smartpark.sensors import EntrySensor, ExitSensor
from smartpark.display import Display
from datetime import datetime
import time
import os
from config_parser import parse_config

# Correct way to resolve config path once, outside main
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config.json")

def main():
    # Use the resolved absolute path
    config = parse_config(config_path)

    location = config.get('location', 'Unnamed Carpark')
    total_spaces = config.get('total_spaces', 5)

    print(f"\n🚗 Carpark Simulation Started: {location}")
    print(f"Total Bays Available: {total_spaces}")

    # Initialize components
    carpark = Carpark(total_bays=total_spaces)
    entry_sensor = EntrySensor()
    exit_sensor = ExitSensor()
    display = Display()

    # Define 5 real car objects
    cars = [
        Car("ABC123", "Toyota Corolla"),
        Car("XYZ789", "Honda Civic"),
        Car("DEF456", "Hyundai Tucson"),
        Car("GHI321", "Mazda CX-5"),
        Car("JKL999", "Ford Focus")
    ]

    # Simulate each car entering
    for car in cars:
        entry_sensor.detect(car, carpark)
        display.show_driver_display(carpark)
        display.show_admin_monitor(carpark)
        time.sleep(1)

    # Simulate 3 cars exiting
    for plate in ["ABC123", "DEF456", "JKL999"]:
        exit_sensor.detect(plate, carpark)
        display.show_admin_monitor(carpark)
        time.sleep(1)

    # Simulate overflow (attempt to enter more cars than capacity)
    print("\n--- Overflow Simulation ---")
    for i in range(total_spaces):
        plate = f"DUMMY{i:03}"
        model = f"OverflowCar{i+1}"
        car = Car(plate, model)
        entry_sensor.detect(car, carpark)

    # One more car beyond full capacity
    overflow_car = Car("OVER999", "Overflow Max")
    entry_sensor.detect(overflow_car, carpark)

    display.show_driver_display(carpark)
    display.show_admin_monitor(carpark)


if __name__ == "__main__":
    main()