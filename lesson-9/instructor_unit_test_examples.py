### TASK ONE ###

"""
This is a possible interview coding question. Let's check the task,
implement our solution and then write tests for it:

Task
Given an integer x perform the following conditional actions:

If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'

Constraint notes:
an input integer is always withing the range 1 to 100 inclusive
"""

# EXAMPLE SOLUTION

# students don't have this solution, so write the code together first
# then ask students to create a test file (use test_unit_test_example.py), import the function and test it.
#
def is_within_range(num, _min, _max):
    if _min <= num <= _max:
        return True
    return False


def is_even(num):
    return num % 2 == 0


def red_or_blue(num):
    if not is_even(num) or (is_even(num) and is_within_range(num, 6, 20)):
        return 'Red'

    if (is_even(num) and num > 20) or num in [2, 4]:
        return 'Blue'


#
# ### TASK TWO -- TDD ###
#
#
# """
# Let's write a test for our function first and then will write an actual code to ensure that
# all tests pass.
#
# Task
# Given a list of dictionaries where keys are student's  name and student's mark.
# calculate the average score for the exam.
#
# If mark is not within the range 1 to 10, raise an error
# Some mark values can be integers and some are strings, we need to process both
# If mark is missing, use value 5
#
# """
#
# # EXAMPLE SOLUTION
#
# # students don't have this solution!
# # write tests for this function first, let them fail and then write the actual function.
#
#
# def average_exam_score(student_marks):
#     denominator = len(student_marks)
#     marks = []
#
#     for result in student_marks:
#         try:
#             mark = int(result['mark'])
#         except KeyError:
#             mark = 5
#
#         if not 10 > mark > 1:
#             raise ValueError("Mark value is not in the valid range")
#
#         marks.append(mark)
#
#     return sum(marks) / denominator

#
