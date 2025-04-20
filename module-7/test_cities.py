# Jonah Aney CSD325 Module 7.2 Assignment: Test Cases

# Import the unit test module. - JHA
import unittest
# Import the get_location function from the city_functions.py file. - JHA
from city_functions import get_location

# Create a class to test the get_location function. - JHA
class LocationTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country = get_location('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

if __name__ == '__main__':
        unittest.main()
