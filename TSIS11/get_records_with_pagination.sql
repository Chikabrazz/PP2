CREATE OR REPLACE FUNCTION get_contacts(limit INT, offset INT)
  RETURNS TABLE (id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
  RETURN QUERY SELECT id, name, phone FROM phonebook ORDER BY name LIMIT limit OFFSET offset;
END;
$$ LANGUAGE plpgsql;