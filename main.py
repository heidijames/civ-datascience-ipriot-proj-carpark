# main.py
# This script simulates a simple smart carpark using sensors and car objects

"""
main.py
Simulates a smart carpark system using entry and exit sensors,
and displays the current carpark status and temperature.
"""

# main.py
# Simulates a smart carpark system using config file and sensors

from smartpark.models import Car, Carpark
from smartpark.sensors import EntrySensor, ExitSensor
from smartpark.display import Display
from config_parser import parse_config
from datetime import datetime
import time


def main():
    # Load configuration from config.json
    config = parse_config("config.json")  # or simply parse_config()
    location = config.get('location', 'Unnamed Carpark')
    total_spaces = config.get('total_spaces', 5)

    print(f"\n🚗 Carpark Simulation Started: {location}")
    print(f"Total Bays Available: {total_spaces}")

    # Initialize components
    carpark = Carpark(total_bays=total_spaces)
    entry_sensor = EntrySensor()
    exit_sensor = ExitSensor()
    display = Display()

    # Create car objects
    car1 = Car("ABC123", "Toyota Corolla")
    car2 = Car("XYZ789", "Honda Civic")

    # Car 1 enters
    entry_sensor.detect(car1, carpark)
    display.show_driver_display(carpark)
    display.show_admin_monitor(carpark)

    # Car 2 enters
    entry_sensor.detect(car2, carpark)
    display.show_driver_display(carpark)
    display.show_admin_monitor(carpark)

    # Simulate short parking duration
    time.sleep(2)

    # Car 1 exits
    exit_sensor.detect("ABC123", carpark)
    display.show_admin_monitor(carpark)


if __name__ == "__main__":
    main()
