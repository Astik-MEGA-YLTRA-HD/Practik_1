from flask import Flask, request, jsonify, render_template, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from core import DataBase
import repo


fl =  Flask(__name__)
CORS(fl)
fl.secret_key = 'your-secret-key-here'

@fl.route("/log_in", methods = ["POST","GET"])
def log_in():
    try:
        last_name = request.form.get("last_name")
        ferst_name = request.form.get("ferst_name")
        email = request.form.get("email")
        phon = request.form.get("phon")
        password = request.form.get("password")


        sql = """
        INSERT INTO users(first_name, last_name, email, phon, password)
        VALUES(?, ?, ?, ?, ?);
        """

        if last_name != None and ferst_name != None and email != None and phon != None and password != None:
            try:
                hash_pasword = generate_password_hash(password)
                data = (last_name, ferst_name, email, phon, hash_pasword)
                db = DataBase()
                db.exec_write(sql, data)

            except:
                return jsonify(('status', 'пользователь уже существует'))

        return render_template("index.html")

    except:
        return jsonify(('status', 500))



@fl.route("/in", methods = ["POST","GET"])
def get_user():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        data_users = repo.users_all(DataBase())

        if email != None and password != None:

            for i in data_users:
                if i['email'] == email and check_password_hash(i['password'], password):
                    data_user = i['id']

            if data_user == None:
                return jsonify(('status', 404))

            else:
                resp = make_response('добро пожаловать')
                resp.set_cookie("user_id", value = f'{data_user}')
                return resp

        return render_template("index2.html")
    
    except:
        return jsonify(('status', 500))



@fl.route("/profil/user", methods = ["POST","GET"])
def profil():
    try:
        user_id = request.cookies.get("user_id")
        return jsonify(repo.users_id(DataBase(), user_id))
    
    except:
        return jsonify(('status', 500))



@fl.route("/basket", methods = ["POST","GET"])
def bascet():
    # try:
        product_id = request.form.get("product_id")

        sql = """
        DELETE FROM basket
        WHERE product_id=? AND user_id=?;
        """

        if product_id != None:
            user_id = request.cookies.get("user_id")

            db = DataBase()
            db.exec_write(sql, (product_id, user_id))

            return jsonify(repo.basket(DataBase(), user_id))
        
        return render_template("index6.html")
    
    # except:
    #     return jsonify(('status', 500))



@fl.route("/products", methods = ["POST","GET"])
def prod_all():
    # try:
        products_id = request.form.get("products_id")
        count = request.form.get("count")

        sql = """
        INSERT INTO basket(user_id, product_id, count)
        VALUES(?, ?, ?);
        """

        if products_id != None and count != None:
            user_id = request.cookies.get("user_id")

            data = (user_id, products_id, count)

            db = DataBase()
            db.exec_write(sql, data)

            return jsonify(repo.prod_all(DataBase()))
        
        return render_template('index4.html')
    # except:
    #     return jsonify(('status', 500))



@fl.route("/product/append", methods = ["POST","GET"])
def prod_append():
    catalog = request.form.get('catalog')
    title = request.form.get('title')
    description = request.form.get('description')
    count_m = request.form.get('count_m')
    prise = request.form.get('prise')
    structure = request.form.get('structure')
    width = request.form.get('width')
    density = request.form.get('density')
    date = request.form.get('date')
    made_in = request.form.get('made_in')
    discount_id = request.form.get('discount_id')

    sql = """
    INSERT INTO products(catalog, title, description, count_m, prise, structure, width, density, date, made_in, discount_id)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    if catalog != None and title != None and description != None and count_m != None and prise != None and structure != None and width != None and density != None and date != None and made_in != None and discount_id != None:
            try:
                data = (catalog, title, description, count_m, prise, structure, width, density, date, made_in, discount_id)
                db = DataBase()
                db.exec_write(sql, data)
            except:
                return jsonify(('status', 500))
    
    return render_template('index3.html')



@fl.route("/product/catalog", methods = ["POST","GET"])
def catalog():
    catalog = request.form.get("catalog")

    sql = """
    SELECT catalog, title, description, count_m, prise, structure, width, density, date, made_in, discounts.title_discounts, discounts.discount FROM products
    JOIN discounts ON discounts.id = discount_id
    WHERE catalog == ?;
    """
    if catalog != None:
        db = DataBase()
        data = db.exec_read(sql, (catalog,))

        return jsonify(data)
    
    return render_template("index5.html")



@fl.route("/prod/<int:products_id>", methods = ["POST","GET"])
def prod(products_id):
    try:
        return jsonify(repo.prod_id(DataBase(), products_id))
    
    except:
        return jsonify(('status', 500))

if __name__ == "__main__":
    fl.run(debug=True)