# Write your MySQL query statement below

# Select Department,Employee,Salary from (
# Select Department.name as Department ,Employee.name as Employee,Employee.salary as Salary,Dense_rank() over (partition by departmentId order by salary desc ) as 'SalaryRank'
# from Employee left join Department on Employee.departmentId=Department.Id
# ) a
# where SalaryRank <=3

SELECT d.Name AS Department, e1.Name AS Employee, e1.Salary FROM Employee e1
JOIN Department d 
ON e1.DepartmentID = d.Id
WHERE 3 > (
    select count(distinct(e2.Salary)) 
                  from Employee e2 
                  where e2.Salary > e1.Salary 
                  and e1.DepartmentId = e2.DepartmentId
                  )