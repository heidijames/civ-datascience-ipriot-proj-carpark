# models.py
# This file defines two classes: Car and Carpark

"""
models.py
Defines the Car and Carpark classes used in the Smart Carpark system.
Handles car entry/exit, bay management, and logging.
"""

from datetime import datetime
from pathlib import Path
import os


class Car:
    """Represents a car with license plate, model, entry, and exit times."""

    def __init__(self, license_plate, model):
        self.license_plate = license_plate
        self.model = model
        self.entry_time = None
        self.exit_time = None


class Carpark:
    """Manages parking bays, active cars, and logs actions to file."""

    def __init__(self, total_bays=5):
        self.total_bays = total_bays
        self.available_bays_list = list(range(1, total_bays + 1))
        self.active_cars = {}           # license_plate → Car object
        self.car_to_bay = {}            # license_plate → bay number
        self.log_file = str(Path(__file__).resolve().parents[1] / "log.txt")
        self.car_log_data = {}          # license_plate → [entry, exit, fee, bay, model]

    def available_bays(self):
        """Returns the number of available bays."""
        return len(self.available_bays_list)

    def car_entry(self, car):
        """Handles car entry into the carpark."""
        if self.available_bays() > 0:
            bay = self.available_bays_list.pop(0)
            car.entry_time = datetime.now()
            self.active_cars[car.license_plate] = car
            self.car_to_bay[car.license_plate] = bay

            # Log the entry action
            self._log_action(car.license_plate, "ENTRY", car.entry_time, bay)
        else:
            print("No available bays.")

    def car_exit(self, license_plate):
        """Handles car exit from the carpark and computes fee."""
        if license_plate in self.active_cars:
            car = self.active_cars.pop(license_plate)
            car.exit_time = datetime.now()
            bay = self.car_to_bay.pop(license_plate)
            self.available_bays_list.append(bay)
            self.available_bays_list.sort()

            # Calculate parking fee: $0.05 per minute
            duration = (car.exit_time - car.entry_time).total_seconds() / 60
            charge = round(duration * 0.05, 2)

            self._log_action(
                license_plate, "EXIT", car.exit_time, bay, charge
            )
            print(f"Charged ${charge:.2f} for {round(duration)} minutes.")
        else:
            print(f"Car with license plate {license_plate} not found.")

    def _log_action(self, license_plate, action, timestamp, bay, charge=None):
        """Stores car activity (entry or exit) in memory before logging to file."""
        time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        if action == "ENTRY":
            model = self.active_cars[license_plate].model
            self.car_log_data[license_plate] = [
                time_str, "", "", f"Bay {bay}", model
            ]
        elif action == "EXIT" and license_plate in self.car_log_data:
            self.car_log_data[license_plate][1] = time_str
            self.car_log_data[license_plate][2] = f"${charge:.2f}"

        self._write_log_table()

    def _write_log_table(self):
        """Writes the structured table log to the log file."""
        log_file_exists = Path(self.log_file).exists()
        write_header = (
            not log_file_exists or Path(self.log_file).stat().st_size == 0
        )

        with open(self.log_file, "a") as file:
            if write_header:
                header = (
                    f"{'ENTRY TIME':<20} | {'EXIT TIME':<20} | "
                    f"{'FEE':<5} | {'BAY':<6} | {'MODEL':<16} | LICENSE PLATE"
                )
                divider = "-" * len(header)
                file.write(header + "\n" + divider + "\n")

            for plate, data in self.car_log_data.items():
                entry, exit_time, fee, bay, model = data
                if exit_time:
                    line = (
                        f"{entry:<20} | {exit_time:<20} | {fee:<5} | "
                        f"{bay:<6} | {model:<16} | {plate}"
                    )
                    file.write(line + "\n")

            file.flush()
            os.fsync(file.fileno())

        # Keep only active (not-yet-exited) car entries in memory
        self.car_log_data = {
            k: v for k, v in self.car_log_data.items() if not v[1]
        }
