from core import DataBase

def prod_all(db: DataBase):
    sql = """
    SELECT catalog, title, description, count_m, prise, structure, width, density, date, made_in, discounts.title_discounts, discounts.discount FROM products
    JOIN discounts ON discounts.id = discount_id;
    """

    return db.exec_read(sql)



def prod_id(db: DataBase, id):
    sql = """
    SELECT catalog, title, description, count_m, prise, structure, width, density, date, made_in, discounts.title_discounts, discounts.discount FROM products
    JOIN discounts ON discounts.id = discount_id
    WHERE products.id == ?;
    """

    return db.exec_read(sql, (id,))



def users_all(db: DataBase):
    sql = """
    SELECT first_name, last_name, email, phon
    FROM users;
    """

    return db.exec_read(sql)



def users_id(db: DataBase, id):
    sql = """
    SELECT first_name, last_name, email, phon
    FROM users
    WHERE id == ?;
    """

    return db.exec_read(sql, (id,))



def basket(db: DataBase, id):
    sql = """
    SELECT products.catalog, products.title, products.description, products.count_m, products.prise, products.structure, products.width, products.density, products.date, products.made_in, discounts.title_discounts, discounts.discount
    FROM basket
    JOIN products ON products.id = product_id
    JOIN discounts ON discounts.id = products.discount_id
    JOIN users ON users.id = user_id
    WHERE users.id == ?;
    """

    return db.exec_read(sql, (id,))


if __name__ == "__main__":
    db = DataBase()
    prod_all(db)