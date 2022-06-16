# fintech_challenge7

GOAL:
In this challenge we analyzed 4 different ETF (GOST, GS, PYPL, and SQ)


Technologies used:
1. sqlite - This is the database that was used to store all the information about the aformentioned ETFs
2. Python Pandas library to read data from the database and create the dataframes
3. hvplot for graphical represenations of data.
4. voila library to convert the notebook to a web applciation which can be viewed in the browser.

Steps:
1.  We began by pulling all the data from the database related to paypal using the select * from pypal query.

2.  We then graphed the cumulative returns by using the formula combined with the cumprod function.

3.  We then modifed our sql query to only return rows where the closing price was above 200 (SELECT time, close FROM PYPL WHERE close > 200)

4.  We were able to find the top ten rows that had the highest daily returns by first order by decending order and selecting the the first ten rows.  By doing this this, the column had the highest values first (SELECT time, close FROM PYPL ORDER BY daily_returns DESC LIMIT 10)

5.  SELECT * FROM GDOT INNER JOIN GS INNER JOIN PYPL INNER JOIN SQ ON GDOT.time = GS.time AND GDOT.time = PYPL.time and GDOT.time = SQ.time
    This query allows us to join columbs.  Because each table shares a time column, we join them on their time column.
    
6.  We then averages all the ETF daily returns and calculated the annualized returns by using the mean function and multiplying it by 365 days.

7.  We finally calculated the cumulative returns of the of the entire portoflio and graphed it using hvplot.

