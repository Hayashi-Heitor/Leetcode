# Returns the product name, year and price from the joined tables by product_id
SELECT product_name, year, price
FROM Product p
JOIN Sales s
ON p.product_id = s.product_id;