CREATE DATABASE crud_qt;

USE crud_qt;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni INT,
    nombre VARCHAR(100),
    email VARCHAR(100),
    pais VARCHAR(100)
);
