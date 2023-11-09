from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS, EMAIL_REGEX


class Usuario:
    def __init__(self, datos):
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.passsword = datos["password"]
        self.fecha_creacion = datos["fecha_creacion"]
        self.fecha_actualizacion = ["fecha_actualizacion"]

    @staticmethod
    def validar_registro(datos):
        es_valido = True
        if len(datos["nombre"]) < 2:
            es_valido = False
            flash("Por favor escribe tu nombre.", "error_nombre")
        if len(datos["apellido"]) < 2:
            es_valido = False
            flash("Por favor escribe tu apellido.", "error_apellido")
        if not EMAIL_REGEX.match(datos["email"]):
            es_valido = False
            flash("Por favor ingresa un correo válido", "error_email")
        if datos["password"] != datos["password_confirmar"]:
            es_valido = False
            flash("Tus contraseñas no coinciden.", "error_password")
        if len(datos["password"]) < 1:
            es_valido = False
            flash("Por favor proporciona un password.", "error_password")
            return es_valido
