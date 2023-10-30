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
    def __init__ (self):
        self.__nombre:str = None
        self.__apellido:str = None
        self.__email:str = None
        self.__password:str = None
    
    def crear_usuarios (self , nombre:str , apellido:str , email:str , password:str):
        new_password = encriptar(password)[1]
        cursor.execute (f'CALL crear_usuario ("{nombre}" , "{apellido}" , "{email}" , "{new_password}")')
        database.commit ()
        return True
    
    def verificar_usuario (self , correo:str , contraseña:str):
        cursor.execute (f"SELECT * FROM verificacion WHERE email = '{correo}'")
        email , passwd =  cursor.fetchone ()
        passw = encriptar(contraseña)[1]
        return email == correo and passwd == passw

    def eliminar_usuario (self , correo):
        cursor.execute (f"CALL delete_usuarios ('{correo}')")
        database.commit()
        return True

    def actualizar_nombre (self , nombre , email):
        cursor.execute (f'CALL update_nombre ("{nombre}" , "{email}")')
        database.commit()
        return True

    def actualizar_apellido (self , apellido , email):
        cursor.execute (f'CALL update_apellido ("{apellido}" , "{email}")')
        database.commit()
        return True

    def actualizar_passwd (self , passwd , email):
        new_password = encriptar(passwd)[1]
        cursor.execute (f'CALL update_passwd ("{new_password}" , "{email}")')
        database.commit()
        return True
    
    def dato (self , row):
        return {"nombre" : row[0],
                "apellido" : row[1],
                "email" : row[2],
                "password" : row[3]}
    
    def datos (self):
        cursor.execute("SELECT * FROM leer_usuarios")
        x = cursor.fetchall ()
        return [self.dato(row) for row in x]