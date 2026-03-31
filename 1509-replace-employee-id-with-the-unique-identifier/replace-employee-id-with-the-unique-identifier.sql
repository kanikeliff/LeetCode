# Write your MySQL query statement below
Select a.unique_id, e.name from Employees e
left join EmployeeUNI a
on e.id = a.id

