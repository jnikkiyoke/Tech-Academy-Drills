SELECT Book.BookID, Title, BranchID, No_of_Copies FROM dbo.BOOK INNER JOIN dbo.BOOK_COPIES
ON dbo.BOOK.BookID = dbo.BOOK_COPIES.BookID
WHERE Book.BookID = 6 AND BranchID = 1