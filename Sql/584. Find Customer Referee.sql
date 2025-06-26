# Returns all names that are null or have a referee_id different of two
SELECT name FROM Customer WHERE referee_id IS NULL OR referee_id != 2 