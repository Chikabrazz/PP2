CREATE OR REPLACE PROCEDURE add_or_update_contact(name VARCHAR, phone VARCHAR)
AS $$
BEGIN
  IF EXISTS (SELECT 1 FROM phonebook WHERE name = name) THEN
    UPDATE phonebook SET phone = phone WHERE name = name;
  ELSE
    INSERT INTO phonebook (name, phone) VALUES (name, phone);
  END IF;
END;
$$ LANGUAGE plpgsql;