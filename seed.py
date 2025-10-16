from core import DataBase

# создание таблиц в базе данных
def create_db(db: DataBase):
    sql = """
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        count_m REAL,
        prise INTEGER,
        discount_id INTEGER,
        structure TEXT,
        width INTEGER,
        density REAL,
        made_in TEXT
    );

    CREATE TABLE IF NOT EXISTS discounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        discount INTEGER
    );

    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phon TEXT,
        password TEXT
    );
    """

    db.exec_script(sql)

if __name__ == "__main__":
    db = DataBase()
    create_db(db)