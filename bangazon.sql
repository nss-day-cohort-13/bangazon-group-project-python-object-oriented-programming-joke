BEGIN TRANSACTION;
CREATE TABLE `Product` (
	`productId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`price`	INTEGER
);
INSERT INTO `Product` VALUES (1,'Charmin',7);
INSERT INTO `Product` VALUES (2,'Cottonelle',9.75);
INSERT INTO `Product` VALUES (3,'Everyone Poops: the Book',12.99);
INSERT INTO `Product` VALUES (4,'Party Pooper: the Game',10.5);
INSERT INTO `Product` VALUES (5,'Nickleback',3.5);
INSERT INTO `Product` VALUES (6,'Sharknado 3',1);
CREATE TABLE `Payment_Option` (
	`paymentId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`customerId`	INTEGER,
	`type`	TEXT,
	`number`	INTEGER
);
INSERT INTO `Payment_Option` VALUES (1,1,'Visa',1234123412341234);
INSERT INTO `Payment_Option` VALUES (2,1,'Mastercard',234023402340234);
INSERT INTO `Payment_Option` VALUES (3,1,'AmEx',5678901245678901);
INSERT INTO `Payment_Option` VALUES (4,2,'Visa',1212121234343434);
INSERT INTO `Payment_Option` VALUES (5,2,'Mastercard',6666666666666666);
INSERT INTO `Payment_Option` VALUES (6,2,'AmEx Giftcard',2222222222222222);
INSERT INTO `Payment_Option` VALUES (7,3,'Diner''s Club',3322332233333333);
INSERT INTO `Payment_Option` VALUES (8,3,'Mastercard',1111222233334444);
INSERT INTO `Payment_Option` VALUES (9,4,'AmEx Giftcard',5432543254325432);
INSERT INTO `Payment_Option` VALUES (10,4,'Visa Giftcard',6767676767676767);
INSERT INTO `Payment_Option` VALUES (11,5,'Visa',4242535364647575);
INSERT INTO `Payment_Option` VALUES (12,5,'Discover',9870654732140981);
INSERT INTO `Payment_Option` VALUES (13,5,'Checking',123123123123123000);
INSERT INTO `Payment_Option` VALUES (14,6,'Checking',567567567567567000);
INSERT INTO `Payment_Option` VALUES (15,6,'Discover',9999999999999999);
CREATE TABLE "Order_line_item" (
	`lineItemId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`productId`	INTEGER,
	`orderId`	INTEGER
);
INSERT INTO `Order_line_item` VALUES (1,1,2);
INSERT INTO `Order_line_item` VALUES (2,1,3);
INSERT INTO `Order_line_item` VALUES (3,2,3);
INSERT INTO `Order_line_item` VALUES (4,4,3);
INSERT INTO `Order_line_item` VALUES (5,5,2);
INSERT INTO `Order_line_item` VALUES (6,5,3);
INSERT INTO `Order_line_item` VALUES (7,5,4);
INSERT INTO `Order_line_item` VALUES (8,4,4);
INSERT INTO `Order_line_item` VALUES (9,6,4);
INSERT INTO `Order_line_item` VALUES (10,6,8);
INSERT INTO `Order_line_item` VALUES (11,5,8);
INSERT INTO `Order_line_item` VALUES (12,5,7);
INSERT INTO `Order_line_item` VALUES (13,3,1);
INSERT INTO `Order_line_item` VALUES (14,3,5);
INSERT INTO `Order_line_item` VALUES (15,5,5);
INSERT INTO `Order_line_item` VALUES (16,6,6);
CREATE TABLE "Order" (
	`orderId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`paymentId`	INTEGER,
	`customerId`	INTEGER,
	`isPaid`	INTEGER NOT NULL DEFAULT 0
);
INSERT INTO `Order` VALUES (1,1,1,1);
INSERT INTO `Order` VALUES (2,2,1,1);
INSERT INTO `Order` VALUES (3,3,1,1);
INSERT INTO `Order` VALUES (4,4,2,1);
INSERT INTO `Order` VALUES (5,8,3,1);
INSERT INTO `Order` VALUES (6,9,4,1);
INSERT INTO `Order` VALUES (7,11,5,1);
INSERT INTO `Order` VALUES (8,14,6,0);
CREATE TABLE "Customer" (
	`customerId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`address`	TEXT,
	`city`	TEXT,
	`state`	TEXT,
	`zipcode`	TEXT,
	`phoneNumber`	TEXT
);
INSERT INTO `Customer` VALUES (1,'Human Person','123 Street Rd','Nashville','TN','37215','615-555-5555');
INSERT INTO `Customer` VALUES (2,'Larry Garry','200 Road St','Waxhaw','NC','28173','615-444-5555');
INSERT INTO `Customer` VALUES (3,'Joe Schmoe','290 Road St','Atlanta','GA','30301','615-444-5555');
INSERT INTO `Customer` VALUES (4,'Spongebob Squarepants','1 Pineapple','Bikini Bottoms','PAO','00000','234-234-2345');
INSERT INTO `Customer` VALUES (5,'George Michael Bluth','1 Lucille Lane','Newport Beach','CA','92663','432-234-2345');
INSERT INTO `Customer` VALUES (6,'Joey Tribbiani','100 Bedford St','New York City','NY','10014','111-222-3333');
COMMIT;
