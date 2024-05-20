---- Створення бази даних
CREATE DATABASE store;

-- Використання бази даних
USE store;

-- Створення таблиці категорій
CREATE TABLE categories (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name CHAR(32) NOT NULL,
    PRIMARY KEY (id)
);

-- Створення таблиці продуктів
CREATE TABLE products (
    id INTEGER NOT NULL AUTO_INCREMENT,
    category_id INTEGER NOT NULL,
    name CHAR(32) NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
