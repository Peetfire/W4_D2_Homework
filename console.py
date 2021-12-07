from models.staff import Staff
import repositories.staff_repository as staff_repo

person1 = Staff("Noah", "2000BC", "Emergency Planning", 5)
staff_repo.save(person1)