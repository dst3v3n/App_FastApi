import bcrypt

def encriptar (Contraseña:str):
    password = Contraseña.encode('utf-8')
    salt = b'$2b$12$tO6x66Zxi6sn6THHX/M.A.'
    hashed = bcrypt.hashpw(password, salt)
    return [password , str(hashed)]

# def desencriptar (Contraseña):
#     encript = encriptar(Contraseña)
#     if bcrypt.checkpw(encript[0], encript[1]):
#         return True
#     else:
#         return False