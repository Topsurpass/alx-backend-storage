-- An SQL script that creates a trigger that resets the attribute valid_email only
-- when the email has been changed.
-- Update the valid_email column of table users to 0 when the email has been changed i.e
-- the old email != new email. This should trigger before update is made on the table users


DROP TRIGGER IF EXISTS validate_email_trigger;
DELIMITER ||
CREATE TRIGGER validate_email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email = NEW.valid_email;
    END IF;
END ||
DELIMITER ;
