from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from core import DataBase
import repo


fl =  Flask(__name__)
CORS(fl)


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
def set_up():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        data_users = repo.users_all(DataBase())

        if email != None and password != None:
            data_user_id = None

            for i in data_users:
                if i['email'] == email and check_password_hash(i['password'], password):
                    data_user = i['id']

            if data_user == None:
                return jsonify(('status', 404))

            else:
                return jsonify(repo.users_id(DataBase(), data_user))

        return render_template("index2.html")
    
    except:
        return jsonify(('status', 500))



@fl.route("/profil/user/<int:id>", methods = ["POST","GET"])
def profil(id):
    try:
        return jsonify(repo.users_id(DataBase(), id))
    
    except:
        return jsonify(('status', 500))



@fl.route("/basket/<int:user_id>", methods = ["POST","GET"])
def bascet(user_id):
    try:
        return jsonify(repo.basket(DataBase(), user_id))
    
    except:
        return jsonify(('status', 500))



@fl.route("/products", methods = ["POST","GET"])
def prod_all():
    try:
        return jsonify(repo.prod_all(DataBase()))
    
    except:
        return jsonify(('status', 500))



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



@fl.route("/prod/<int:products_id>", methods = ["POST","GET"])
def prod(products_id):
    try:
        return jsonify(repo.prod_id(DataBase(), products_id))
    
    except:
        return jsonify(('status', 500))



if __name__ == "__main__":
    fl.run(debug=False)