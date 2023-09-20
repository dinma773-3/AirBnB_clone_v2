-- Creates a database hbnb_dev_db in MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants Permissions for user
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
