.mode column
.headers on
.width 30
SELECT publisher, AVG(price), SUM(price) FROM book
GROUP BY publisher;
