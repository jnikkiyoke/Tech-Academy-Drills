SELECT dbo.Borrower.CardNo,Name,BookID
FROM dbo.BORROWER INNER JOIN dbo.BOOK_LOANS
ON dbo.BORROWER.CardNo = dbo.BOOK_LOANS.CardNo
