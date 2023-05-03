CREATE OR REPLACE PROCEDURE delete_contact(name VARCHAR, phone VARCHAR)
AS $$
BEGIN
  IF name IS NOT NULL THEN
    DELETE FROM phonebook WHERE name = name;
  ELSIF phone IS NOT NULL THEN
    DELETE FROM phonebook WHERE phone = phone;
  ELSE
    RAISE EXCEPTION 'At least one of name or phone must be provided.';
  END IF;
END;
$$ LANGUAGE plpgsql;