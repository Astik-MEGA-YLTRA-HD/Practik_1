from flask import Flask, request, render_template

fl =  Flask(__name__)


@fl.route("/log_in", methods = ["POST","GET"])
def log_in():
    global last_name
    global ferst_name
    global email
    global phon
    global password

    last_name = request.form.get("last_name")
    ferst_name = request.form.get("ferst_name")
    email = request.form.get("email")
    phon = request.form.get("phon")
    password = request.form.get("password")

    return render_template("Login.jsx")


@fl.route("/set_up", methods = ["POST","GET"])
def set_up():
    global email
    global password

    email = request.form.get("email")
    password = request.form.get("password")

    return render_template("index.html")

if __name__ == "__main__":
    fl.run(debug=True)