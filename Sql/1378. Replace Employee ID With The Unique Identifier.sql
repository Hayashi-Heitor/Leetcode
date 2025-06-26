# Selects employees unique ids and names where employee id IN uniqueID table
SELECT u.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI u
ON e.id = u.id;