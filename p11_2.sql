.mode column
.headers on
SELECT bookId,name FROM bookCreator
INNER join creator
ON bookCreator.creatorId=creator.Id
WHERE bookID="4";
