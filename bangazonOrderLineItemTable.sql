BEGIN TRANSACTION;
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
COMMIT;
