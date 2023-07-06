
FOUNDATION ASSESSMENT
Section 1
Q 1
What is the process called where databases get restructured to
better data integrity ?
Database normalisation is a process that improves data integrity by removing
redundancy and creating relationships between tables.
Q 2
What is the type of JOIN statement that returns rows when there is
at least one match in both tables? Present a venn diagram which
shows this visually.
The type of JOIN statement that returns rows when there is at least one match in
both tables is called an INNER JOIN.



Q 3
What is the difference between functions and methods?
Functions:
Functions are reusable blocks of code that perform a specific task, can
be called from anywhere in a program, and can accept parameters,
manipulate data, and return values or perform actions.
Methods:
Methods, on the other hand, are functions associated with objects or
classes. They are defined within the scope of a class, used to define
object behaviour or perform operations on data, and can access and
manipulate object attributes and interact with other methods.
The main difference is that functions are more generic and can exist
independently, while methods are specific to objects or classes.
Q 4
What is a subquery?
A subquery is a query embedded within another query, used to retrieve data from
one or more tables based on the results of another query.
It is enclosed within parentheses and typically placed in the WHERE or HAVING
clause of the outer query.
The result of the subquery is used for further filtering or comparison in the outer
query. Subqueries help break down complex problems into smaller parts and can
be used in various clauses such as WHERE, HAVING, SELECT, FROM, JOIN,
ORDER BY, and GROUP BY. They provide a flexible way to manipulate and retrieve
data from databases.



Q 5
Explain the difference between “x = y” and “x == y” in python?
x = y : This is an assignment operator used to assign the value of y to
the variable x. It is used to store a value in a variable.
For example, if we have the statement "x = 10", it means that the value
10 is assigned to the variable x.
x == y : This is a comparison operator used to compare the equality of x
and y. It checks whether the values of x and y are equal. If they are
equal, it returns True; otherwise, it returns False. This is used to evaluate
equality between two values or variables.
For example, if we have the statement "x == 10", it checks if the value
of x is equal to 10.
Q6
What are the notations for a list, set and tuple?
List: Lists are denoted by square brackets [] and can contain elements of any
data type. The elements can be modified.
my_list = [1, 2, 3, 'a', 'b', ‘c’]
Set: Sets are denoted by curly braces {} or by using the set() function. Sets
contain unique elements and are unordered, meaning their elements have no
specific order. Sets are mutable.
my_set = {1, 2, 3, 4, 5} or my_set = set([1, 2, 3, 4, 5])
Tuple: Tuples are denoted by parentheses () and can contain elements of any
data type. The elements cannot be modified once defined.
my_tuple = (1, 2, 'a', 'b')



Q 7
Explain the relationship between the following sets: {1,2,7,8}, {7,1,2,8}, {1,2}, {3}
{1, 2, 7, 8} and {7, 1, 2, 8}:
These two sets have the same elements, but they are written in a different
order.
The order of elements does not affect the set itself, so these two sets are
considered equal.
So {1, 2, 7, 8} = {7, 1, 2, 8}.
{1, 2}:
This set contains only the elements 1 and 2.
It is a subset of the sets {1, 2, 7, 8} and {7, 1, 2, 8}, as all its elements are
present in those sets.
So {1, 2} ⊆ {1, 2, 7, 8} and {1, 2} ⊆ {7, 1, 2, 8}.
{3}:
This set contains only the element 3.
It is not a subset of the sets {1, 2, 7, 8} or {7, 1, 2, 8}, as it does not have any
common elements with those sets.
So {3} is disjoint from {1, 2, 7, 8} and {7, 1, 2, 8}.
Data
Structure Notation Order Uniqueness Mutability
List [] Yes No Yes
Set {} No Yes No
Tuple () Yes Yes No



Q 8
Describe the behaviour of the following code.
while True:
print(“Hello”)
The code will print the string "Hello" repeatedly, until the program is
terminated manually.
The while True statement will keep executing the body of the loop as long as
the condition True is met. In this case, the condition True is always met, so
the body of the loop will keep executing indefinitely.
Q 9
Give 2 examples of libraries you can use in Python and what they
are used for?
NumPy:
Used for numerical computing in Python. It provides functions for working with
arrays, making it useful for tasks like mathematical operations, linear algebra, and
random number generation. It is commonly used in scientific computing and data
analysis.
Pandas:
Used for data manipulation and analysis. It offers easy-to-use data structures for
handling and analysing data, such as DataFrames and Series. It is commonly used
for tasks like data cleaning, transformation, and exploration. Pandas is widely used
in data science and other fields where structured data is involved.



Q 10
List 3 differences between stored procedures and stored functions?
Purpose:
Stored Procedures: They are used for performing actions, executing a series of
statements, or modifying data in the database.
Stored Functions: They are used to calculate values or perform specific operations
within a query.
Return Value:
Stored Procedures: They may or may not return a value. They focus on executing
tasks rather than providing a result.
Stored Functions: They always return a value. They are designed to calculate and
return a specific result.
Usage in Queries:
Stored Procedures: They are called separately from queries or can be used within a
query for executing actions.
Stored Functions: They are used directly within a query to retrieve specific values or
perform calculations.



Section 2
Q 2.1
students = ["Ana", "beth", “CHARLIE"]
formatted_students = [student.lower() for student in students]
Q 2.2
input_str = "practice"
output_str = input_str[4] + input_str[2] + input_str[0]
print(output_str)
Q 2.3
with open("input.txt", "r") as file:
lines = file.readlines()
line_count = len(lines)
with open("input.txt", "a") as file:
for line in lines:
file.write(line.rstrip() + "...\n")
print("Number of lines:", line.count)



Q 2.4
def calculate_total_price(receipt):
total_price = sum(receipt.values())
formatted_price = "{:.2f}".format(total_price)
return formatted_price
receipt = {
"item1": 9.99,
"item2": 5.50,
"item3": 2.75,
"item4": 12.99
}
if len(receipt) >= 4:
total_price = calculate_total_price(receipt)
print("Total price: $", total_price)
else:
print("Receipt should contain at least 4 items.”)



Section 3
from datetime import datetime, timedelta
print("Please select one of the following options: add, compare")
option = input()
if option == "add":
date_str = input("What is the date you want to add to? Please enter in DD/
MM/YYYY format: ")
days_to_add = int(input("How many days do you want to add? "))
date = datetime.strptime(date_str, "%d/%m/%Y")
new_date = date + timedelta(days=days_to_add)
resultant_date = new_date.strftime("%d/%m/%Y")
print("The resultant date is", resultant_date)
elif option == "compare":
date1_str = input("Please give Date 1 in DD/MM/YYYY format: ")
date2_str = input("Please give Date 2 in DD/MM/YYYY format: ")
date1 = datetime.strptime(date1_str, "%d/%m/%Y")
date2 = datetime.strptime(date2_str, "%d/%m/%Y")
diff_days = abs((date1 - date2).days)
print("There are", diff_days, "days between the given dates.")
else:
print("Invalid option selected. Please try again.")



Section 4
Q 4.1
A:
CREATE TABLE students (
Student_ID INT PRIMARY KEY,
FORENAME VARCHAR,
SURNAME VARCHAR
);
B:
CREATE TABLE exams (
Exam_ID INT PRIMARY KEY,
Exam_Name VARCHAR,
Max_Mark INT
);
C:
CREATE TABLE results (
Result_ID INT PRIMARY KEY,
Student_ID INT,
Exam_ID INT,
Mark INT,
FOREIGN KEY (Student_ID) REFERENCES students (Student_ID),
FOREIGN KEY (Exam_ID) REFERENCES exams (Exam_ID)
);



Q 4.2
USE foundation_assessment_i;
SELECT students.Forname, students.surname, exam.Exam_Name
FROM students
JOIN results ON students.Student_ID = result.students_ID
JOIN exam ON results.Exam_ID = exam.Exam_ID
WHERE results.Mark > 60
Q 4.3
SELECT CONCAT(s.Forename, ' ', s.Surname) AS Full_Name, r1.Exam_ID AS
Suspected_Exam, r1.Mark
FROM results r1, results r2, students s
WHERE r1.Exam_ID = r2.Exam_ID AND r1.Mark = r2.Mark AND r1.Student_ID
< r2.Student_ID
AND s.Student_ID = r1.Student_ID;