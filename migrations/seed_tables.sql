ALTER SEQUENCE carts_id_seq RESTART WITH 1;
ALTER SEQUENCE looks_id_seq RESTART WITH 1;
ALTER SEQUENCE products_id_seq RESTART WITH 1;
ALTER SEQUENCE users_id_seq RESTART WITH 1;

INSERT INTO public.products (title,price,description,category,image,size_available,color_available) VALUES
    ('Bolsa Masculina',30.5,'Mochila Masculina','Mochila Masculina','https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg','{"S","M","B"}','{"black"}'),
    ('Camiseta Basica',21.5,'Camiseta Basica Branca Com Mangas Pretas','Camiseta Masculina','https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg','{"S","M","B"}','{"black"}'),
    ('Jaqueta Masculina',109.99,'Jaqueta Masculina Bege','Jaqueta Masculina','https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg','{"S","M","B"}','{"black"}'),
    ('Camiseta Manga Longa',34.9,'Camiseta Masculina De Manga Longa','Camiseta Masculina Manga Longa','https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg','{"S","M","B"}','{"black"}'),
    ('Bracelete Masculino',30.5,'Bracelete Masculino Em Formato De Dragao','Bracelete Masculino','https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg','{"4","5","6"}','{"black"}'),
    ('Anel Prata',167.0,'Anel Feminino De Prata','Anel Feminino','https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg','{"11","12","13"}','{"black"}'),
    ('Anel Diamante',1400.0,'Anel Feminino Com Pedras De Diamante','Anel Feminino','https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg','{"11","12","13"}','{"black"}'),
    ('Anel Ouro',612.0,'Anel De Ouro Feminino','Anel Feminino','https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg','{"11","12","13","14"}','{"black","red"}'),
    ('Sobretudo Inverno',120.0,'Sobretudo Para o Inverno Lilas','Sobretudo Feminino','https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg','{"S","M","B"}','{"lilac"}'),
    ('Jaqueta Jeans Preto',45.0,'Jaqueta Jeans Preto','Jaqueta Feminina Preta','https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg','{"S","M","B"}','{"black"}'),
    ('Jaqueta Inverno',65.0,'Jaqueta Feminina Perfeita Para o Inverno','Jaqueta Feminina','https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2.jpg','{"S","M","B"}','{"blue"}'),
    ('Camisa Gola V',11.5,'Camisa Feminina Gola V Branca','Camisa Feminina','https://fakestoreapi.com/img/71z3kpMAYsL._AC_UY879_.jpg','{"S","M","B"}','{"white"}'),
    ('Camisa',12.5,'Camisa Feminina Vermelho','Camisa Feminina','https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg','{"S","M","B"}','{"red"}'),
    ('Camiseta',13.99,'Camiseta Feminina Rosa','Camiseta Feminina','https://fakestoreapi.com/img/61pHAEJ4NML._AC_UX679_.jpg','{"S","M","B"}','{"pink"}');

INSERT INTO public.users (email,username,first_name,last_name,"password",phone,address,document_number) VALUES
    ('angel@email.com','angel','Angelica','Hanston','ewedon','11952405707','{"city": "San Antonio", "number": 6454, "street": "Hunters Creek Dr", "zipcode": "98234-1734", "geolocation": {"lat": "50.3467", "long": "-20.1310"}}','29948400062'),
    ('derek@gmail.com','derek','derek','powell','jklg*_56','1-956-001-1945','{"city": "san Antonio", "number": 245, "street": "adams St", "zipcode": "80796-1234", "geolocation": {"lat": "40.3467", "long": "-40.1310"}}','22170625810'),
    ('david_r@gmail.com','david_r','david','russell','3478*#54','1-678-345-9856','{"city": "el paso", "number": 124, "street": "prospect st", "zipcode": "12346-0456", "geolocation": {"lat": "20.1677", "long": "-10.6789"}}','46911978181'),
    ('miriam@gmail.com','snyder','miriam','snyder','f238&@*$','1-123-943-0563','{"city": "fresno", "number": 1342, "street": "saddle st", "zipcode": "96378-0245", "geolocation": {"lat": "10.3456", "long": "20.6419"}}','86805609011'),
    ('william@gmail.com','hopkins','william','hopkins','William56$hj','1-478-001-0890','{"city": "mesa", "number": 1342, "street": "vally view ln", "zipcode": "96378-0245", "geolocation": {"lat": "50.3456", "long": "10.6419"}}','73814807278'),
    ('kate@gmail.com','kate_h','kate','hale','kfejk@*_','1-678-456-1934','{"city": "miami", "number": 345, "street": "avondale ave", "zipcode": "96378-0245", "geolocation": {"lat": "40.12456", "long": "20.5419"}}','14930022282'),
    ('jimmie@gmail.com','jimmie_k','jimmie','klein','klein*#%*','1-104-001-4567','{"city": "fort wayne", "number": 526, "street": "oak lawn ave", "zipcode": "10256-4532", "geolocation": {"lat": "30.24788", "long": "-20.545419"}}','72910559890'),
    ('gabriel@email.com','gabriel','Gabriel','Novaes','m38rmF$','11972218872','{"city": "kilcoole", "number": 7682, "street": "new road", "zipcode": "12926-3874", "geolocation": {"lat": "-37.3159", "long": "81.1496"}}','49351242021'),
    ('lucas@email.com','lucas','Lucas','Victor','83r5^_','11959972119','{"city": "kilcoole", "number": 7267, "street": "Lovers Ln", "zipcode": "12926-3874", "geolocation": {"lat": "-37.3159", "long": "81.1496"}}','03674327066'),
    ('lucas@email.com','eduardo','Eduardo','Lima','kev02937@','11998124315','{"city": "Cullman", "number": 86, "street": "Frances Ct", "zipcode": "29567-1452", "geolocation": {"lat": "40.3467", "long": "-30.1310"}}','63824835088'),
    ('isabella.ggomes@email.com','Isa','Isabella','Gomes','83r5^_','11954670489','{"city": "kilcoole", "number": 65, "street": "Radiator Springs", "zipcode": "12099-4655", "geolocation": {"lat": "-37.3159", "long": "81.1496"}}','19061060028');

INSERT INTO public.carts (user_id,created_at,updated_at,products) VALUES
	 (1,'2020-03-01 21:00:02-03','2021-08-11 20:37:54.930839-03','[{"quantity": 4, "productId": 1}, {"quantity": 1, "productId": 2}, {"quantity": 6, "productId": 3}]'),
	 (7,'2020-01-01 21:00:02-03','2021-08-11 20:37:54.930839-03','[{"quantity": 4, "productId": 2}, {"quantity": 10, "productId": 1}, {"quantity": 2, "productId": 5}]'),
	 (2,'2020-02-29 21:00:02-03','2021-08-11 20:37:54.930839-03','[{"quantity": 2, "productId": 1}, {"quantity": 1, "productId": 9}]'),
	 (3,'2019-12-31 21:00:02-03','2021-08-11 20:37:54.930839-03','[{"quantity": 4, "productId": 1}]'),
	 (5,'2020-02-29 21:00:02-03','2021-08-11 20:37:54.930839-03','[{"quantity": 1, "productId": 7}, {"quantity": 1, "productId": 8}]'),
	 (4,'2020-02-29 21:00:02-03','2021-08-11 20:37:54.930839-03','[{"quantity": 2, "productId": 10}, {"quantity": 3, "productId": 12}]'),
	 (8,'2020-02-29 21:00:02-03','2021-08-11 20:37:54.930839-03','[{"quantity": 1, "productId": 18}]');

INSERT INTO public.looks (shirt_id, jacket_id, shoe_id, pant_id, description, image, category) VALUES
(14, 12, NULL, NULL, '', 'Look casual simples feminino', 'Casual'),
(2, 3, NULL, NULL, '', 'Look casual simples masculino', 'Casual');
