# smartpark/display.py

# display.py
# Handles displaying carpark information to drivers and admins

from smartpark.weather import read_temperature
from datetime import datetime

class Display:
    def show_driver_display(self, carpark, temperature=None):
        """
        Display available bays and temperature for drivers.
        Returns the display string (for testing).
        """
        if temperature is None:
            temperature = read_temperature()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = (
            f"\n[Driver Display]\n"
            f"Time: {current_time}\n"
            f"Available Bays: {carpark.available_bays()}\n"
            f"Bays: {carpark.available_bays_list}\n"
            f"Temperature: {temperature}°C"
        )
        print(output)
        return output

    def show_admin_monitor(self, carpark):
        """
        Display full admin carpark status.
        Returns the display string (for testing).
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_lines = [
            "\n--- Carpark Monitor ---",
            f"Time: {current_time}",
            f"Available Bays: {carpark.available_bays()}",
            f"Available Bay Numbers: {carpark.available_bays_list}",
            "Currently Parked Cars:"
        ]
        for plate, car in carpark.active_cars.items():
            bay = carpark.car_to_bay[plate]
            entry_time = car.entry_time.strftime('%H:%M:%S')
            output_lines.append(f"- {car.model} ({car.license_plate}) → Bay {bay}")
            output_lines.append(f"  ⏰ Entry Time: {entry_time}")
        output_lines.append("------------------------")

        full_output = "\n".join(output_lines)
        print(full_output)
        return full_output

    # For backwards compatibility with older test cases
    def show_driver(self, carpark, temperature=None):
        return self.show_driver_display(carpark, temperature)

    def show_admin(self, carpark):
        return self.show_admin_monitor(carpark)
