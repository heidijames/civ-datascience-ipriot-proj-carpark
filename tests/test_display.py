# test_display.py

# tests/test_display.py

import unittest
from smartpark.display import Display
from smartpark.models import Carpark, Car

class TestDisplay(unittest.TestCase):

    def setUp(self):
        self.display = Display()
        self.carpark = Carpark(total_bays=3)

    def test_driver_display_output(self):
        output = self.display.show_driver(self.carpark, temperature="23")
        self.assertIn("Available Bays: 3", output)
        self.assertIn("Temperature: 23°C", output)

    def test_admin_display_output_empty(self):
        output = self.display.show_admin(self.carpark)
        self.assertIn("Available Bays: 3", output)
        self.assertIn("Currently Parked Cars:", output)

    def test_admin_display_output_with_car(self):
        car = Car("XYZ123", "Mazda 3")
        self.carpark.car_entry(car)
        output = self.display.show_admin(self.carpark)
        self.assertIn("Mazda 3 (XYZ123)", output)
        self.assertIn("Bay 1", output)
        self.assertIn("Entry Time:", output)

    def test_driver_display_alias(self):
        output = self.display.show_driver_display(self.carpark, temperature="20")
        self.assertIn("Temperature: 20°C", output)

    def test_admin_display_alias(self):
        output = self.display.show_admin_monitor(self.carpark)
        self.assertIn("Currently Parked Cars:", output)

if __name__ == '__main__':
    unittest.main()
