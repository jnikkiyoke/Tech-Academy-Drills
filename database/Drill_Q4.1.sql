SELECT Title, DueDate, Name, Address FROM dbo.BOOK_LOANS INNER JOIN dbo.BORROWER
ON dbo.BOOK_LOANS.CardNo = dbo.BORROWER.CardNo
INNER JOIN dbo.BOOK ON dbo.BOOK_LOANS.BookID = dbo.BOOK.BookID
WHERE DueDate = 'Today'
