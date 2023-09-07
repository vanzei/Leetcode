WITH total_tweets as (
SELECT user_id, 
count(tweet_id) AS tweet_count_per_user
FROM tweets
WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY user_id)
SELECT tweet_count_per_user as tweet_bckt, count(user_id) as num_users
FROM total_tweets
GROUP BY tweet_count_per_user
