# sensors.py
# Simulated sensor classes

"""
sensors.py
Defines simulated EntrySensor and ExitSensor classes used to trigger
carpark events like entry and exit detection.
"""

class EntrySensor:
    """
    Simulates an entry sensor. When a car passes through,
    it triggers the carpark to register the car's entry.
    """

    def detect(self, car, carpark):
        """
        Trigger the carpark entry process for the given car.

        Parameters:
        - car: Car object
        - carpark: Carpark object
        """
        carpark.car_entry(car)


class ExitSensor:
    """
    Simulates an exit sensor. When a car leaves,
    it triggers the carpark to register the car's exit.
    """

    def detect(self, license_plate, carpark):
        """
        Trigger the carpark exit process using the license plate.

        Parameters:
        - license_plate: str, car's license plate number
        - carpark: Carpark object
        """
        carpark.car_exit(license_plate)
