import unittest
from models.staff import Staff

class TestStaff(unittest.TestCase):
    
    def setUp(self):
        self.staff = Staff("Noah", "2000BC", "Emergency Planning", 5)

    def test_has_name(self):
        expected = "Noah"
        result = self.staff.name
        self.assertEqual(expected, result)

    def test_has_date(self):
        expected = "2000BC"
        result = self.staff.start_date
        self.assertEqual(expected, result)

    def test_has_department(self):
        expected = "Emergency Planning"
        result = self.staff.department
        self.assertEqual(expected, result)

    def test_has_performance(self):
        expected = 5
        result = self.staff.performance
        self.assertEqual(expected, result)

    def test_has_id(self):
        expected = None
        result = self.staff.id
        self.assertEqual(expected, result)

