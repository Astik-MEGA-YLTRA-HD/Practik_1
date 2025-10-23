from core import DataBase

def prod_all(db: DataBase):
    sql = """
    SELECT catalog, title, description, count_m, prise, structure, width, density, date, made_in, discounts.title_discounts, discounts.discount FROM products
    JOIN discounts ON discounts.id = discount_id;
    """

    return db.exec_read(sql)

def users_all():
    pass

def basket_all():
    pass


if __name__ == "__main__":
    db = DataBase()
    prod_all(db)