import unittest
from models.staff import Staff

class TestStaff(unittest.TestCase):
    
    def setUp(self):
        self.staff = Staff("Noah", "2000BC", "Emergency Planning", 5)

    def test_has_name(self):
        expected = "Noah"
        result = self.staff.name
        self.assertEqual(expected, result)