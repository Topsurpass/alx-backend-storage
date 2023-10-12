--  An SQL script that creates a trigger that decreases the quantity of an item
-- after adding a new order.
-- Update items table, set its column quntity value to be the previous value minus
-- the value in the column number of table orders, provided the name of the product
-- in items table is the same with that of order table.


DROP TRIGGER IF EXISTS update_item;
DELIMITER ||
CREATE TRIGGER update_item
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END ||
DELIMITER ;
