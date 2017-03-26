SELECT Name, Address, COUNT(Name)
FROM dbo.BORROWER INNER JOIN dbo.BOOK_LOANS
ON dbo.BORROWER.CardNo = dbo.BOOK_LOANS.CardNo
GROUP BY Name, Address
HAVING (COUNT(Name) > 5)
