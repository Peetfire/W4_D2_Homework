from db.run_sql import run_sql

from models.animal import Animal

import repositories.staff_repository as staff_repository

def save(animal):
    sql = "INSERT INTO animals (name, species, keeper_id) VALUES ( %s, %s, %s) RETURNING *"
    values = [animal.name, animal.species, animal.keeper.id]
    results = run_sql(sql, values)
    animal.id = results[0]['id']
    return animal