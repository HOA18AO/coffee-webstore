use coffee_webstore;

select * from store_coffeeproduct;
select * from store_category;

select * from store_productimage;

SELECT * FROM store_coffeeproduct;

insert into store_category(category_id, category_name, `description`)
values
(1, 'Cà phê phin', "Chất lượng hảo hạng"),
(2, 'Cà phê hạt', "Chất lượng nguyên bản");

insert into store_coffeeproduct(product_id, product_name, `status`, cost, `description`,  created_at, category_id)
values
(8, 'BBCS',  true, 40000, "the best in market", curdate(), 2),
(9, 'BCDC',  true, 40000, "the best in market", curdate(), 2),
(10, 'ASJN',  true, 80000, "the best in market", curdate(), 2),
(11, 'FVC',  true, 40000, "the best in market", curdate(), 2),
(12, 'BACF',  true, 87000, "the best in market", curdate(), 2),
(13, 'ASSC',  true, 80000, "the best in market", curdate(), 1);


insert into store_productimage(image_id, image, product_id, is_main)
values
(1, 'https://placehold.co/1200x750', 1, true),
(2, 'https://placehold.co/1200x750', 2, true),
(3, 'https://placehold.co/1200x750', 3, true),
(4, 'https://placehold.co/1200x750', 4, true),
(5, 'https://placehold.co/1200x750', 5, true),
(6, 'https://placehold.co/1200x750', 6, true),
(7, 'https://placehold.co/1200x750', 7, true);

