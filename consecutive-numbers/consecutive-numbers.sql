# Write your MySQL query statement below
Select distinct num as ConsecutiveNums  from ( 
Select num,  LEAD(num) OVER(ORDER BY id) as next_row_value,
LAG(num) OVER(ORDER BY id) as prev_row_value
FROM Logs
)a 
where a.num=a.next_row_value
and a.prev_row_value=a.next_row_value