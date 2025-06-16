# test_simulations.py
# Simulate both normal and full bay scenarios for the smart carpark

from smartpark.models import Car, Carpark
from smartpark.sensors import EntrySensor, ExitSensor
from smartpark.display import Display
from config_parser import parse_config
import time

def simulate_normal_usage():
    print("\n--- Simulation: Normal Usage ---")
    config = parse_config("config.json")
    total_spaces = config.get("total_spaces", 5)
    carpark = Carpark(total_bays=total_spaces)
    entry_sensor = EntrySensor()
    exit_sensor = ExitSensor()
    display = Display()

    car1 = Car("TEST001", "Mazda 3")
    car2 = Car("TEST002", "Hyundai i30")

    entry_sensor.detect(car1, carpark)
    display.show_driver_display(carpark)
    display.show_admin_monitor(carpark)


    entry_sensor.detect(car2, carpark)
    display.show_driver_display(carpark)
    display.show_admin_monitor(carpark)


    time.sleep(2)

    exit_sensor.detect("TEST001", carpark)
    display.show_admin_monitor(carpark)

def simulate_full_bays():
    print("\n--- Simulation: Full Bays ---")
    config = parse_config("config.json")
    total_spaces = config.get("total_spaces", 5)
    carpark = Carpark(total_bays=total_spaces)
    entry_sensor = EntrySensor()
    display = Display()

    for i in range(total_spaces):
        car = Car(f"DUMMY{i:03}", f"CarModel{i+1}")
        entry_sensor.detect(car, carpark)
        display.show_admin_monitor(carpark)

    # Attempt one more car
    extra_car = Car("FULL000", "Overflow Car")
    entry_sensor.detect(extra_car, carpark)
    display.show_driver_display(carpark)
    display.show_admin_monitor(carpark)

if __name__ == "__main__":
    simulate_normal_usage()
    simulate_full_bays()
