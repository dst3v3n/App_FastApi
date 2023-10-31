from fastapi import FastAPI , Response , Form
from fastapi.responses import HTMLResponse , FileResponse
from fastapi.staticfiles import StaticFiles
from database import * 

app = FastAPI ()

app.mount ("/static" , StaticFiles (directory="./public/static") , name="static")

@app.get ("/" , response_class=HTMLResponse)
async def root ():
    html_adress = "./public/static/index.html"
    return FileResponse (html_adress , status_code=200)

@app.post ("/data")
async def usuario (nombre:str = Form() , apellido:str = Form() , email:str = Form() , password:str = Form() , re_password:str = Form()):
    if password == re_password:
        new = usuarios()
        new.crear_usuarios(nombre , apellido , email , password)
        return {"exito" : "REGISTRO EXITOSO"}
    else:
        return {"404" : "not found"}

@app.post ("/inicio")
async def user (username:str = Form() , password:str = Form()):
    new = usuarios ()
    if new.verificar_usuario(username , password) == True:
        return {"exito" : "Inicio de sesion exitoso"}
    else:
        return {"failed" : "Email o contraseña equivocada"}
    
@app.delete ("/eliminar_usuario/")
async def eliminacion (email:str):
    new = usuarios () 
    if new.eliminar_usuario (email) == True:
        return {"exitoso" : "Eliminacion exitosa"}
    
@app.put ("/actualizar_dato/nombre/")
async def actualizar_nombres (nombre , email):
    new = usuarios () 
    if new.actualizar_nombre (nombre , email) == True:
        return {"exitoso" : "actualizacion exitosa"}
    
@app.put ("/actualizar_dato/apellido/")
async def actualizar_apellidos (apellido , email):
    new = usuarios () 
    if new.actualizar_apellido (apellido , email) == True:
        return {"exitoso" : "actualizacion exitosa"}
    
@app.put ("/actualizar_dato/password/")
async def actualizar_passwords (password , email):
    new = usuarios () 
    if new.actualizar_passwd (password , email) == True:
        return {"exitoso" : "actualizacion exitosa"}
    
@app.get ("/visualizar/datos")
async def visualizar_todos ():
    new = usuarios ()
    return new.datos ()