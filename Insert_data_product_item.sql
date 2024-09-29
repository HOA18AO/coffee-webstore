use coffee_webstore;

-- Insert categories
INSERT INTO category (category_name, description)
VALUES 
('Cà phê Bột', 'Cà phê đã được xay thành bột, sẵn sàng để pha chế.'),
('Cà phê Hạt', 'Cà phê nguyên hạt, giữ nguyên hương vị tự nhiên khi pha chế.');

-- Insert products into coffee_product
INSERT INTO coffee_product (product_name, category_id, status, cost, description, created_at)
VALUES
-- Cà phê Bột products
('Cà phê Bột Arabica', 1, TRUE, 120000, 'Cà phê Bột Arabica thơm ngon, vị chua nhẹ đặc trưng.', NOW()),
('Cà phê Bột Robusta', 1, TRUE, 90000, 'Cà phê Bột Robusta đậm đà, hàm lượng caffeine cao.', NOW()),
('Cà phê Bột Moka', 1, TRUE, 150000, 'Cà phê Bột Moka hảo hạng, hương thơm mạnh mẽ.', NOW()),
-- Cà phê Hạt products
('Cà phê Hạt Arabica', 2, TRUE, 110000, 'Cà phê Hạt Arabica nguyên chất, hương vị đặc trưng.', NOW()),
('Cà phê Hạt Robusta', 2, TRUE, 85000, 'Cà phê Hạt Robusta đậm đà, phù hợp cho những ai yêu thích vị đắng mạnh.', NOW()),
('Cà phê Hạt Moka', 2, TRUE, 140000, 'Cà phê Hạt Moka với hương vị phong phú và cân bằng.', NOW());

-- Inserting sample images for product_id 1
INSERT INTO product_images (product_id, image, is_main) VALUES
(1, 'https://placehold.co/1200x900', 1), -- Main image
(1, 'https://placehold.co/1200x900', 0),
(1, 'https://placehold.co/1200x900', 0);

-- Inserting sample images for product_id 2
INSERT INTO product_images (product_id, image, is_main) VALUES
(2, 'https://placehold.co/1200x900', 1), -- Main image
(2, 'https://placehold.co/1200x900', 0),
(2, 'https://placehold.co/1200x900', 0);

-- Inserting sample images for product_id 3
INSERT INTO product_images (product_id, image, is_main) VALUES
(3, 'https://placehold.co/1200x900', 1), -- Main image
(3, 'https://placehold.co/1200x900', 0),
(3, 'https://placehold.co/1200x900', 0);

-- Inserting sample images for product_id 4
INSERT INTO product_images (product_id, image, is_main) VALUES
(4, 'https://placehold.co/1200x900', 1), -- Main image
(4, 'https://placehold.co/1200x900', 0),
(4, 'https://placehold.co/1200x900', 0);

-- Inserting sample images for product_id 5
INSERT INTO product_images (product_id, image, is_main) VALUES
(5, 'https://placehold.co/1200x900', 1), -- Main image
(5, 'https://placehold.co/1200x900', 0),
(5, 'https://placehold.co/1200x900', 0);



select * from coffee_product;