from db.run_sql import run_sql

from models.staff import Staff

import repositories.staff_repository as staff_repository

def save(person):
    sql = "INSERT INTO staff (name, start_date, department, performance) VALUES ( %s, %s, %s, %s) RETURNING *"
    values = [person.name, person.start_date, person.department, person.performance]
    results = run_sql(sql, values)
    person.id = results[0]['id']
    return person

def delete_all():
    sql = "DELETE FROM staff" 
    run_sql(sql)
    # sql = "DBCC CHECKIDENT ('staff', RESEED, 0)"
    # run_sql(sql)

def select_all():
    staff = []

    sql = "SELECT * FROM staff"
    results = run_sql(sql)

    for row in results:
        person = Staff(row['name'], row['start_date'], row['department'], row['performance'], row['id'])
        staff.append(person)
    return staff

def select(id):
    person = None
    sql = "SELECT * FROM staff WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        person = Staff(result['name'], result['start_date'], result['department'], result['performance'], result['id'])
    return person

def delete(id):
    sql = "DELETE FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(person):
    sql = "UPDATE staff SET (name, start_date, department, performance) = (%s, %s, %s, %s) WHERE id = %s"
    values = [person.name, person.start_date, person.department, person.performance, person.id]
    run_sql(sql, values)


