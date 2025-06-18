# tests/test_config.py

import unittest
import tomli
import os
import json
import config_parser as pc
from config_parser import parse_config

class TestConfigParser(unittest.TestCase):
    def setUp(self):
        # Create a temporary config file for testing
        self.test_config_file = "test_config.json"
        self.sample_data = {
            "location": "Test Carpark",
            "total_spaces": 42
        }
        with open(self.test_config_file, "w") as f:
            json.dump(self.sample_data, f)

    def tearDown(self):
        # Delete the temporary file after test
        if os.path.exists(self.test_config_file):
            os.remove(self.test_config_file)

    def test_parse_config_returns_correct_dict(self):
        config = parse_config(self.test_config_file)
        self.assertEqual(config["location"], "Test Carpark")
        self.assertEqual(config["total_spaces"], 42)

if __name__ == "__main__":
    unittest.main()
