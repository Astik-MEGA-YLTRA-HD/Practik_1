from flask import Flask, request, jsonify, render_template
import repo
from core import DataBase

fl =  Flask(__name__)

@fl.route("/log_in", methods = ["POST","GET"])
def log_in():

    last_name = request.form.get("last_name")
    ferst_name = request.form.get("ferst_name")
    email = request.form.get("email")
    phon = request.form.get("phon")
    password = request.form.get("password")

    return render_template("index.py")



@fl.route("/set_up", methods = ["POST","GET"])
def set_up():
    global email
    global password

    email = request.form.get("email")
    password = request.form.get("password")

    return jsonify(repo.users_all(DataBase()))



@fl.route("/profil/user/<int:id>", methods = ["GET"])
def profil(id):
    return jsonify(repo.users_id(DataBase(), id))


@fl.route("/basket/<int:user_id>", methods = ["GET"])
def bascet(user_id):
    return jsonify(repo.basket(DataBase(), user_id))



@fl.route("/products", methods = ["GET"])
def prod_all():
    return jsonify(repo.prod_all(DataBase()))



@fl.route("/prod/<int:products_id>", methods = ["GET"])
def prod(products_id):
    return jsonify(repo.prod_id(DataBase(), products_id))



if __name__ == "__main__":
    fl.run(debug=True)