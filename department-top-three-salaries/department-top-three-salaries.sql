# Write your MySQL query statement below

Select Department,Employee,Salary from (
Select Department.name as Department ,Employee.name as Employee,Employee.salary as Salary,Dense_rank() over (partition by departmentId order by salary desc ) as 'SalaryRank'
from Employee left join Department on Employee.departmentId=Department.Id
) a
where SalaryRank in (1,2,3)