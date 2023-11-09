from flask import render_template, session, redirect, request, flash
from app_flask.modelos.modelo_usuarios import Usuario
from app_flask import app

@app.route("/", methods=["GET"])
def despliega_login_registro():
    return render_template('login_registro.html')

@app.route('/procesa/registro', methods=['POST'])
def procesa_registro():
    if Usuario.validar_registro(request.form) == False:
        return redirect('/')