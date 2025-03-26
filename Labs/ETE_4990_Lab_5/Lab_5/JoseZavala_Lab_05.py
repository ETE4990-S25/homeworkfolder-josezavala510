class Sage(object):
    """Wise Healer character to help"""
    def __init__(self, name, variety, health, healing=100):
        """Initialize the name, variety, health, and healing attributes."""
        self.name = name
        self.variety = variety
        self.health = health
        self.healing = healing 

    def heal(self):
        """Heal a certain amount of life."""
        return self.name + " heals " + str(self.healing)

# Example usage
sage = Sage("Eagus", "Mystical", 150)
print(sage.heal())

# Unit tests
import unittest

class TestSage(unittest.TestCase):

    def setUp(self):
        self.sage = Sage("Eagus", "Mystical", 150)

    def test_initialization(self):
        self.assertEqual(self.sage.name, "Eagus")
        self.assertEqual(self.sage.variety, "Mystical")
        self.assertEqual(self.sage.health, 150)
        self.assertEqual(self.sage.healing, 100)

    def test_heal(self):
        self.assertEqual(self.sage.heal(), "Eagus heals 100")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    