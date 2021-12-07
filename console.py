from models.staff import Staff
import repositories.staff_repository as staff_repo

person = staff_repo.select(70)
person.name = "Zebedee"
person.performance = 1
staff_repo.update(person)