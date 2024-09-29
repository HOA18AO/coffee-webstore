use mysql;
drop database if exists coffee_webstore;
create database if not exists coffee_webstore;

/*
use coffee_webstore;
-- Drop delivery table
DROP TABLE IF EXISTS delivery;
-- Drop payment table
DROP TABLE IF EXISTS payment;
-- Drop order_items table
DROP TABLE IF EXISTS order_items;
-- Drop orders table
DROP TABLE IF EXISTS orders;
-- Drop product_images table
DROP TABLE IF EXISTS product_images;

-- Drop coffee_product table
DROP TABLE IF EXISTS coffee_product;
-- Drop category table
DROP TABLE IF EXISTS category;
-- Drop users table
DROP TABLE IF EXISTS users;
-- Drop address table
DROP TABLE IF EXISTS address;
-- Drop district table
DROP TABLE IF EXISTS district;
-- Drop city table
DROP TABLE IF EXISTS city;
store_coffeeproduct
*/
/*
-- Create city table
CREATE TABLE city (
  city_id INT AUTO_INCREMENT PRIMARY KEY,
  city_name VARCHAR(30) NOT NULL
);

-- Create district table
CREATE TABLE district (
  district_id INT AUTO_INCREMENT PRIMARY KEY,
  city_id INT NOT NULL,
  district_name VARCHAR(30) NOT NULL,
  FOREIGN KEY (city_id) REFERENCES city(city_id) ON DELETE CASCADE
);

-- Create address table
CREATE TABLE address (
  address_id INT AUTO_INCREMENT PRIMARY KEY,
  address_line VARCHAR(100) NOT NULL,
  district_id INT NOT NULL,
  FOREIGN KEY (district_id) REFERENCES district(district_id) ON DELETE CASCADE
);

-- Create users table
CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  role VARCHAR(20) NOT NULL, -- customers, admins
  username VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  mobile VARCHAR(11) UNIQUE NOT NULL,
  email VARCHAR(50) UNIQUE NOT NULL,
  full_name VARCHAR(100),
  address_id INT,
  sex VARCHAR(10),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  status ENUM('active', 'inactive', 'banned') NOT NULL DEFAULT 'active',
  FOREIGN KEY (address_id) REFERENCES address(address_id) ON DELETE SET NULL
);

-- Create category table
CREATE TABLE category(
	category_id INT PRIMARY KEY auto_increment,
    category_name VARCHAR(50),
    description VARCHAR(255)
);

-- Create coffee_product table
CREATE TABLE coffee_product (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(30) NOT NULL,
  category_id INT,
  status BOOLEAN NOT NULL default 1, -- currently available or not
  cost DECIMAL(10, 2) NOT NULL,
  description VARCHAR(200),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  foreign key (category_id) references category(category_id) on delete cascade
);

-- Create product_images table
CREATE TABLE product_images (
  image_id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT NOT NULL,
  image VARCHAR(100) NOT NULL, -- link, url
  is_main boolean not null default 0,
  FOREIGN KEY (product_id) REFERENCES coffee_product(product_id) ON DELETE CASCADE
);

-- Create orders table
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  address_id INT NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'done', 'cancelled') NOT NULL DEFAULT 'pending',
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL,
  FOREIGN KEY (address_id) REFERENCES address(address_id) ON DELETE CASCADE
);

-- Create order_items table
CREATE TABLE order_items (
  order_id INT NOT NULL,
  item_id INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (order_id, item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (item_id) REFERENCES coffee_product(product_id) ON DELETE CASCADE
);

-- Create payment table
CREATE TABLE payment (
  order_id INT NOT NULL,
  payment_method VARCHAR(20) NOT NULL, -- online or cash
  payment_date DATETIME,
  status ENUM('pending', 'paid') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (order_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Create delivery table
CREATE TABLE delivery (
  order_id INT NOT NULL,
  delivery_method VARCHAR(50),
  received_date DATETIME,
  status ENUM('received', 'not_received') NOT NULL DEFAULT 'not_received',
  PRIMARY KEY (order_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);
*/

