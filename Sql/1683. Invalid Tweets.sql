# Selects the id from the tweets with more then 15 chars
SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15