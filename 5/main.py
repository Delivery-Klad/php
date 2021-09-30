from fastapi import FastAPI
from typing import Optional
import psycopg2

app = FastAPI()


def db_connect():
    con = psycopg2.connect(
        host="ec2-54-198-252-9.compute-1.amazonaws.com",
        database="d7sjscgk5e4258",
        user="slllyeejcwnmyt",
        port=5432,
        password="76e7f204bbb6559b72bcaef582731d086e7fd40dfca9ad358485ed5ece8c2b0a"
    )
    return con, con.cursor()


def create_database(name: str):
    try:
        connect, cursor = db_connect()
        current_isolation_level = connect.isolation_level
        connect.set_isolation_level(0)
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
        connect.set_isolation_level(current_isolation_level)
        connect.commit()
        return True
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connect.close()


def create_tables():
    try:
        connect, cursor = db_connect()
        cursor.execute("CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS owners(id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS owners_cars(id_car INTEGER REFERENCES cars (id),"
                       "id_owner INTEGER REFERENCES owners (id),"
                       "CONSTRAINT owners_cars_pkey PRIMARY KEY (id_car, id_owner))")
        connect.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()
        connect.close()


def add_item(table_name: str, name: Optional[str] = None, id_car: Optional[int] = None, id_owner: Optional[int] = None):
    try:
        connect, cursor = db_connect()
        if name is not None:
            cursor.execute(f"SELECT count(id) FROM {table_name}")
            max_id = int(cursor.fetchone()[0]) + 1
            cursor.execute(f"INSERT INTO {table_name} VALUES ({max_id}, '{name}')")
        else:
            if id_car is None or id_owner is None:
                return False
            cursor.execute(f"INSERT INTO owners_cars VALUES ({id_car}, {id_owner})")
        connect.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()
        connect.close()


def get_joined_tables():
    try:
        connect, cursor = db_connect()
        cursor.execute("SELECT owners.name, cars.name FROM owners_cars JOIN cars ON cars.id = owners_cars.id_car "
                       "JOIN owners ON owners.id = owners_cars.id_owner")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()
        connect.close()


def get_table(table_name: str):
    try:
        connect, cursor = db_connect()
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()
        connect.close()


@app.post("/create")
async def create__database_tables():
    try:
        return create_tables()
    except Exception as e:
        print(e)


@app.get("test/")
def test():
    try:
        return get_joined_tables()
    except Exception as e:
        print(e)
