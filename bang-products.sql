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
COMMIT;
