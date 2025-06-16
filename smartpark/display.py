# smartpark/display.py

from datetime import datetime
from smartpark.weather import read_temperature


# display.py
# Handles displaying carpark information to drivers and admins

from smartpark.weather import read_temperature
from datetime import datetime

class Display:
    def show_driver_display(self, carpark):
        """
        Display available bays and temperature for drivers.
        """
        temperature = read_temperature()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n[Driver Display]")
        print(f"Time: {current_time}")
        print(f"Available Bays: {carpark.available_bays()}")
        print(f"Bays: {carpark.available_bays_list}")
        print(f"Temperature: {temperature}°C")

    def show_admin_monitor(self, carpark):
        """
        Display full admin carpark status.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n--- Carpark Monitor ---")
        print(f"Time: {current_time}")
        print(f"Available Bays: {carpark.available_bays()}")
        print(f"Available Bay Numbers: {carpark.available_bays_list}")
        print("Currently Parked Cars:")
        for plate, car in carpark.active_cars.items():
            bay = carpark.car_to_bay[plate]
            entry_time = car.entry_time.strftime('%H:%M:%S')
            print(f"- {car.model} ({car.license_plate}) → Bay {bay}")
            print(f"  ⏰ Entry Time: {entry_time}")
        print("------------------------")
