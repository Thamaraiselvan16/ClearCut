-- create database in mysql database don't use in vs_code



create database clearcut;

use clearcut;

CREATE TABLE image (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_name VARCHAR(255),
    rembg_name VARCHAR(255),
    image_data LONGBLOB,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from image;
select * from app_image;

