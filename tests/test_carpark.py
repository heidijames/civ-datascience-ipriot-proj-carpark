import unittest
from smartpark.models import Carpark, Car


class TestCarparkSystem(unittest.TestCase):
    def setUp(self):
        # Runs before each test
        self.carpark = Carpark(total_bays=3)
        self.car1 = Car("AAA111", "Toyota Yaris")
        self.car2 = Car("BBB222", "Mazda 3")

    def test_car_entry_adds_car(self):
        self.carpark.car_entry(self.car1)
        self.assertIn("AAA111", self.carpark.active_cars)
        self.assertIsNotNone(self.car1.entry_time)

    def test_car_exit_removes_car_and_frees_bay(self):
        self.carpark.car_entry(self.car1)
        self.carpark.car_exit("AAA111")
        self.assertNotIn("AAA111", self.carpark.active_cars)
        self.assertIn(1, self.carpark.available_bays_list)

    def test_charge_calculation(self):
        import time
        self.carpark.car_entry(self.car1)

        # Simulate that entry was 2 minutes ago
        self.car1.entry_time = self.car1.entry_time.replace(minute=self.car1.entry_time.minute - 2)
        self.carpark.car_exit("AAA111")

        self.assertIsNotNone(self.car1.exit_time)  # We expect an exit time

    def test_bay_allocation_order(self):
        self.carpark.car_entry(self.car1)
        self.carpark.car_entry(self.car2)

        bay1 = self.carpark.car_to_bay["AAA111"]
        bay2 = self.carpark.car_to_bay["BBB222"]

        self.assertLess(bay1, bay2)  # First car should get lower-numbered bay

if __name__ == "__main__":
    unittest.main()
