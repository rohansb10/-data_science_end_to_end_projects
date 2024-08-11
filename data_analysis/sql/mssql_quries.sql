-- Insight: Distribution of Order Quantity
SELECT Order_Quantity, COUNT(*) AS Frequency
FROM mssql_quries
GROUP BY Order_Quantity
ORDER BY Order_Quantity;

-- Insight: Sales by Region
SELECT Region, AVG(Sales) AS Average_Sales, MIN(Sales) AS Min_Sales, MAX(Sales) AS Max_Sales
FROM mssql_quries
GROUP BY Region;

-- Insight: Profit by Customer Segment
SELECT Customer_Segment, AVG(Profit) AS Average_Profit, MIN(Profit) AS Min_Profit, MAX(Profit) AS Max_Profit
FROM mssql_quries
GROUP BY Customer_Segment;

-- Insight: Order Priority Distribution
SELECT Order_Priority, COUNT(*) AS Count
FROM mssql_quries
GROUP BY Order_Priority;

-- Insight: Sales by Product Category
SELECT Product_Category, SUM(Sales) AS Total_Sales
FROM mssql_quries
GROUP BY Product_Category;

-- Insight: Profit by Product Sub-Category
SELECT [Product_Sub-Category], SUM(Profit) AS Total_Profit
FROM mssql_quries
GROUP BY [Product_Sub-Category];

-- Insight: Ship Mode Distribution
SELECT Ship_Mode, COUNT(*) AS Count
FROM mssql_quries
GROUP BY Ship_Mode;

-- Insight: Top 10 Products by Sales
SELECT TOP 10 Product_Name, SUM(Sales) AS Total_Sales
FROM mssql_quries
GROUP BY Product_Name
ORDER BY Total_Sales DESC;
