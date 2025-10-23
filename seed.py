from core import DataBase
from config import DATA_products, DATA_discounts, DATA_users, DATA_basket, DATA_job

# создание таблиц в базе данных
def create_db(db: DataBase):
    sql = """
    DROP TABLE IF EXISTS basket;
    DROP TABLE IF EXISTS products;
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS discounts;
    DROP TABLE IF EXISTS image_product;
    DROP TABLE IF EXISTS job;
    DROP TABLE IF EXISTS image_job;

    CREATE TABLE products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        catalog TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        count_m REAL,
        prise INTEGER NOT NULL,
        structure TEXT,
        width REAL,
        density REAL,
        date TEXT,
        made_in TEXT NOT NULL,
        discount_id INTEGER,
        FOREIGN KEY (discount_id) REFERENCES discounts(id) ON DELETE RESTRICT
    );

    CREATE TABLE discounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title_discounts TEXT NOT NULL,
        discount INTEGER
    );

    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phon TEXT,
        password TEXT NOT NULL
    );

    CREATE TABLE basket(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT
    );

    CREATE TABLE job(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title_job TEXT,
        description TEXT
    );
    """

    db.exec_script(sql)

def seed_db(db: DataBase):
    seed_product = """
    INSERT INTO products(catalog, title, description, count_m, prise, structure, width, density, made_in, discount_id)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    seed_discounts = """
    INSERT INTO discounts(title_discounts, discount)
    VALUES(?, ?);
    """
    seed_users = """
    INSERT INTO users(first_name, last_name, email, phon, password)
    VALUES(?, ?, ?, ?, ?);
    """
    seed_basket = """
    INSERT INTO basket(product_id, user_id)
    VALUES(?, ?);
    """
    seed_job = """
    INSERT INTO job(title_job, description)
    VALUES(?, ?);
    """

    db.exec_write(seed_product, DATA_products)
    db.exec_write(seed_discounts, DATA_discounts)
    db.exec_write(seed_users, DATA_users)
    db.exec_write(seed_basket, DATA_basket)
    db.exec_write(seed_job, DATA_job)

if __name__ == "__main__":
    db = DataBase()
    create_db(db)
    seed_db(db)