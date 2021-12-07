import unittest
import pdb
import repositories.staff_repository as staff_repository
from models.staff import Staff

class TestStaff_Repo(unittest.TestCase):
    
    def setUp(self):
        staff_repository.delete_all()
        self.person1 = Staff("Noah", "2000BC", "Emergency Planning", 5)
        self.person2 = Staff("Mogli", "1912", "Animal Liason Officer", 3)
        self.person3 = Staff("Brian", "2020", "HR officer", 2)

    def test_can_save(self):
        self.assertIsNone(self.person1.id)
        person = staff_repository.save(self.person1)
        self.assertIsNotNone(person.id)

    def test_select_all(self):
        staff_repository.save(self.person1)
        staff_repository.save(self.person2)
        staff_repository.save(self.person3)
        result = len(staff_repository.select_all())
        expected = 3
        self.assertEqual(expected, result)

    def test_delete_all(self):
        staff_repository.save(self.person1)
        staff_repository.save(self.person2)
        staff_repository.save(self.person3)
        result = len(staff_repository.select_all())
        expected = 3
        self.assertEqual(expected, result)
        staff_repository.delete_all()
        result = len(staff_repository.select_all())
        expected = 0
        self.assertEqual(expected, result)

    


