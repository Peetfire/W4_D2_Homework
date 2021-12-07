import unittest

from models.animal import Animal
from models.staff import Staff
import repositories.staff_repository as staff_repo

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.keeper = Staff("Bobby", "2020", "Animal Testing", 2)
        staff_repo.save(self.keeper)
        self.animal1 = Animal("Tony", "Tiger", self.keeper)

    def test_has_name(self):
        result = self.animal1.name
        expected = "Tony"
        self.assertEqual(result, expected)

    def test_has_species(self):
        result = self.animal1.species
        expected = "Tiger"
        self.assertEqual(result, expected)

    def test_keeper_id_is_None(self):
        result = self.animal1.keeper.id
        expected = self.keeper.id
        self.assertEqual(result, expected)