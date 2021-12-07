from db.run_sql import run_sql

from models.staff import Staff

import repositories.staff_repository as staff_repository

def save(staff):
    sql = "INSERT INTO staff (name, start_date, department, performance) VALUES ( %s %s %s %s) RETURNING *"
    values = [staff.name, staff.start_date, staff.department, staff.performance]
    results = run_sql(sql, values)
    staff.id = results[0]['id']

def select_all():
    staff = []

    sql = "SELECT * FROM staff"
    results = run_sql(sql)

    for row in results:
        person = Staff(row['name'], row['start_date'], row['department'], row['performance'], row['id'])
        staff.append(person)
    return staff