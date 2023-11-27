/*
Given a table of Facebook posts, for each user who posted at least twice in 2021, write a query to find the number of days between each user’s first post of the year and last post of the year in the year 2021. Output the user and number of the days between each user's first and last post.

*/

SELECT user_id, 
(max(post_date::DATE) - min(post_date::DATE)) as days_between
from posts
where date_part('year', post_date::DATE) = 2021
GROUP BY user_id
HAVING count(post_id)>1;
