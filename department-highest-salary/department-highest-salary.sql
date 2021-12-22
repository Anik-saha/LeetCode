# Write your MySQL query statement below

  # Select name as Department, a.ename as Employee, a.Salary(
Select name as Department, ename as Employee, Salary from (
    Select dep.name, Employee.name as ename , Employee.Salary, DENSE_RANK() over (partition by Employee.departmentId order by salary desc ) as 'ranksal' from Employee
left join Department dep on dep.id =Employee.departmentId  
      )a
 where a.ranksal=1
