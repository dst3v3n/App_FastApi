import mysql.connector
from encriptar import *

database = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "suples_shop_colombia"
)

cursor = database.cursor ()

class usuarios:
    def __init__ (self , Email:str , Password:str):
        self.__nombre:str = None
        self.__apellido:str = None
        self.__email:str = Email
        self.__password:str = Password
    
    def crear_usuarios (self , nombre:str , apellido:str):
        new_password = encriptar(self.__password)[1]
        cursor.execute (f'CALL crear_usuario ("{nombre}" , "{apellido}" , "{self.__email}" , "{new_password}")')
        print(new_password)
        database.commit ()
        return True
    
    def verificar_usuario (self , correo:str , contraseña:str):
        cursor.execute (f"SELECT * FROM verificacion WHERE email = '{correo}'")
        email , passwd =  cursor.fetchone ()
        passw = encriptar(contraseña)[1][:-13]
        return email == correo and passwd == passw

def eliminar_usuario (correo):
    cursor.execute (f"CALL delete_usuarios ('{correo}')")
    database.commit()
    return True

def actualizar_nombre (nombre , email):
    cursor.execute (f'CALL update_nombre ("{nombre}" , "{email}")')
    database.commit()
    return True

def actualizar_apellido (apellido , email):
    cursor.execute (f'CALL update_apellido ("{apellido}" , "{email}")')
    database.commit()
    return True

def actualizar_passwd (passwd , email):
    new_password = encriptar(passwd)[1]
    cursor.execute (f'CALL update_passwd ("{new_password}" , "{email}")')
    database.commit()
    return True