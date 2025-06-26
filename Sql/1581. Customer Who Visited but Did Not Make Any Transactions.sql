# Selects customers id and counts the visit_ids
SELECT customer_id, COUNT(v.visit_id) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t # Joins from the left with transactions on visit_id
ON v.visit_id = t.visit_id
WHERE transaction_id IS null # Grabs only there are no transactions_id
GROUP BY customer_id # Groups by customers_id