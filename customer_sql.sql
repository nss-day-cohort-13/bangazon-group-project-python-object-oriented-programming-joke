BEGIN TRANSACTION;
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
