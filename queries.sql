-- ======================================================
-- 1. Display all records from investor_transactions
-- ======================================================
SELECT * FROM investor_transactions;

-- ======================================================
-- 2. Total number of transactions
-- ======================================================
SELECT COUNT(*) AS Total_Transactions
FROM investor_transactions;

-- ======================================================
-- 3. Total transaction amount
-- ======================================================
SELECT SUM(amount_inr) AS Total_Amount
FROM investor_transactions;

-- ======================================================
-- 4. Average transaction amount
-- ======================================================
SELECT AVG(amount_inr) AS Average_Amount
FROM investor_transactions;

-- ======================================================
-- 5. Transactions greater than ₹10,000
-- ======================================================
SELECT *
FROM investor_transactions
WHERE amount_inr > 10000;

-- ======================================================
-- 6. Number of transactions by type
-- ======================================================
SELECT transaction_type,
       COUNT(*) AS Total
FROM investor_transactions
GROUP BY transaction_type;

-- ======================================================
-- 7. Total investment by transaction type
-- ======================================================
SELECT transaction_type,
       SUM(amount_inr) AS Total_Investment
FROM investor_transactions
GROUP BY transaction_type;

-- ======================================================
-- 8. Top 10 schemes by AUM
-- ======================================================
SELECT scheme_name,
       aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;

-- ======================================================
-- 9. Average expense ratio
-- ======================================================
SELECT AVG(expense_ratio_pct) AS Average_Expense_Ratio
FROM scheme_performance;

-- ======================================================
-- 10. Highest 1-Year Return
-- ======================================================
SELECT scheme_name,
       return_1yr_pct
FROM scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- ======================================================
-- 11. Number of schemes by risk grade
-- ======================================================
SELECT risk_grade,
       COUNT(*) AS Total_Schemes
FROM scheme_performance
GROUP BY risk_grade;

-- ======================================================
-- 12. NAV History Count
-- ======================================================
SELECT COUNT(*) AS Total_NAV_Records
FROM nav_history;

-- ======================================================
-- 13. Highest NAV
-- ======================================================
SELECT MAX(nav) AS Highest_NAV
FROM nav_history;

-- ======================================================
-- 14. Lowest NAV
-- ======================================================
SELECT MIN(nav) AS Lowest_NAV
FROM nav_history;

-- ======================================================
-- 15. Average NAV
-- ======================================================
SELECT AVG(nav) AS Average_NAV
FROM nav_history;