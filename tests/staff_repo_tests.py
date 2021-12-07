import unittest
import pdb
import repositories.staff_repository as staff_repository
from models.staff import Staff

class TestStaff_Repo(unittest.TestCase):
    
    def setUp(self):
        self.person1 = Staff("Noah", "2000BC", "Emergency Planning", 5)

    def test_can_save(self):
        person = staff_repository.save(self.person1)
        self.assertIsNotNone(person.id)