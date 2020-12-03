import unittest
from activities import eat

class ActivityTest(unittest.TestCase):
    def test_eat_unhealthy(self):
        """eat healthy"""
        self.assertEqual(eat("broccoli", is_healthy=True),
                         "I'm eating broccoli, because my body is a temple")
    def test_eat_healthy(self):
        """eat unhealthy"""
        self.assertEqual(eat("pizza", is_healthy=False),
                         "I'm eating pizza, because YOLO!")
    # def test_short_nap(self):
    #     pass

if __name__ == "__main__":
    unittest.main()