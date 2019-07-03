PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

DROP TABLE "foodspark_fooditem";
CREATE TABLE IF NOT EXISTS "foodspark_fooditem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(500) NOT NULL, "cuisine" varchar(100) NOT NULL, "course" varchar(1) NOT NULL, "price" real NOT NULL, "ordercount" integer NOT NULL, "resid_id" varchar(254) NOT NULL REFERENCES "foodspark_restaurant" ("email"));
INSERT INTO foodspark_fooditem VALUES(5,'Pork Rib Noodle','Chinese','m',3.0,32,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(6,'Bak Kut Teh Mee','Chinese','m',3.5,11,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(7,'Ban Mee','Chinese','m',3.0,0,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(8,'Zha Jiang Mian','Chinese','m',2.5,0,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(9,'Sliced Fish Noodle','Chinese','m',3.0,0,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(10,'Bak Chor Mee $2 (S)','Chinese','m',2.0,0,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(11,'Bak Chor Mee $2.5 (L)','Chinese','m',2.5,0,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(12,'Fishball Noodle (S)','Chinese','m',2.0,0,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(13,'Fishball Noodle $2.5 (L)','Chinese','m',2.5,0,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(14,'Prawn Noodle','Chinese','m',3.0,0,'wan862@gmail.com');
INSERT INTO foodspark_fooditem VALUES(15,'Add On Fruit','Chinese','d',0.29999999999999998889,0,'wan862@gmail.com');

DROP TABLE "foodspark_restaurant";
CREATE TABLE IF NOT EXISTS "foodspark_restaurant" ("email" varchar(254) NOT NULL PRIMARY KEY, "password" varchar(100) NOT NULL, "name" varchar(200) NOT NULL, "address" text NOT NULL, "cuisine" varchar(100) NULL, "phone" varchar(15) NOT NULL, "imgurl" varchar(1000) NULL);
INSERT INTO foodspark_restaurant VALUES('wan862@gmail.com','123456','Fishball Noodle','Stall No.3, HC Canteen','Chinese','81865372','/static/img/fishball_noodle.jpg');

COMMIT;
