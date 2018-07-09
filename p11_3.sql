.mode column
.headers on
SELECT title,name FROM bookCreator
INNER join creator ON bookCreator.creatorId=creator.id
INNER join book ON bookCreator.bookid=book.id
WHERE bookCreator.bookID="4";
