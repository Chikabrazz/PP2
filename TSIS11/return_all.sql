CREATE OR REPLACE FUNCTION search_contacts(pattern VARCHAR)
  RETURNS TABLE (id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
  RETURN QUERY SELECT id, name, phone FROM phonebook WHERE name LIKE '%' || pattern || '%' OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;