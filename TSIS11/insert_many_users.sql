CREATE OR REPLACE PROCEDURE add_multiple_contacts(names VARCHAR[], phones VARCHAR[])
AS $$
DECLARE
  i INT;
BEGIN
  FOR i IN 1..array_length(names, 1) LOOP
    IF LENGTH(phones[i]) = 10 AND phones[i] ~ '^[0-9]+$' THEN
      INSERT INTO phonebook (name, phone) VALUES (names[i], phones[i]);
    ELSE
      RAISE EXCEPTION 'Incorrect phone number: %', phones[i];
    END IF;
  END LOOP;
END;
$$ LANGUAGE plpgsql;