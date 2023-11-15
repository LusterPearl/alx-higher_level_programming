-- Creating database hbtn_0d_2 if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating user_0d_2 if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Granting SELECT privilege to user_0d_2 on hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- FLUSH privileges to apply changes
FLUSH PRIVILEGES;
