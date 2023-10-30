CREATE DATABASE suples_shop_colombia;

USE suples_shop_colombia;

CREATE TABLE usuarios (
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL UNIQUE,
  passwd VARCHAR(300) NOT NULL
  );
  
# CREAR USUARIOS #

DELIMITER //
CREATE PROCEDURE crear_usuario (
	Nombre VARCHAR (50),
   Apellido VARCHAR (50),
   Email VARCHAR (50),
   Passwd VARCHAR (50)
)
BEGIN
	INSERT INTO usuarios () VALUES (Nombre , Apellido , Email , Passwd);
END //
DELIMITER ;
 
# LEER USUARIOS #
CREATE VIEW leer_usuarios AS
SELECT * FROM usuarios;

# VERIFICACION #
CREATE VIEW verificacion AS
SELECT email , passwd FROM usuarios;

# ACTUALIZACION USUARIOS #
#Nombre
DELIMITER //
CREATE PROCEDURE update_nombre (
	Nombre VARCHAR (50),
   Email VARCHAR (50)
)
BEGIN
	UPDATE usuarios SET nombre = Nombre
   WHERE email = Email;
END //
DELIMITER ;

#Apellido
DELIMITER //
CREATE PROCEDURE update_apellido (
	Apellido VARCHAR (50),
   Email VARCHAR (50)
)
BEGIN
	UPDATE usuarios SET apellido = Apellido
   WHERE email = Email;
END //
DELIMITER ;

#passwd
DELIMITER //
CREATE PROCEDURE update_passwd (
	Passwd VARCHAR (50),
   Email VARCHAR (50)
)
BEGIN
	UPDATE usuarios SET passwd = Passwd
   WHERE email = Email;
END //
DELIMITER ;

# ELIMINAR USUARIOS #

DELIMITER //
CREATE PROCEDURE delete_usuarios (
   Email VARCHAR (50)
)
BEGIN
	DELETE FROM usuarios
   WHERE email = Email;
END //
DELIMITER ;

select * from leer_usuarios;