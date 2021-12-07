from models.animal import Animal
from models.staff import Staff
import repositories.staff_repository as staff_repo
import repositories.animal_repository as animal_repo

keeper1 = staff_repo.select(30)
a1 = Animal("Tony", "Tiger", keeper1)
animal_repo.save(a1)
