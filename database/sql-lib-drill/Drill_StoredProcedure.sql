SELECT * FROM dbo.BOOK_LOANS

USE dbLibrary
GO

CREATE PROCEDURE GetBorrowerInfo @Name nvarchar(30) = NULL, @BookID nvarchar(30) = NULL 
AS
SELECT Name, BookID, BOOK_LOANS.CardNo
FROM dbo.BORROWER LEFT OUTER JOIN dbo.BOOK_LOANS
ON dbo.BORROWER.CardNo = dbo.BOOK_LOANS.CardNo
WHERE Name = ISNULL(@Name,Name)
AND BookID LIKE '%' + ISNULL(@BookID, BookID) + '%'
GO
