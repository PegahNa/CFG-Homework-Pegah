# You work as a primary school teacher and are teaching numbers by showing how
# they are composed of units of ten and one.Write a program for students to play
# with to understand this concept.You will be asking for them to enter numbers
# between 1 and 25 (they haven’t gone higher than that!),so you do not need to
# consider bigger numbers.The function needs to print to the screen and the
# message must be grammatically correct and in the format shown below.
# For example:
# ●If 15 was the input, the function output should be:
# One Ten, Five Ones
# ●If 21 was the input, the function output should be:
# Two Tens, One One
# ●If 20 was the input, the function output should be:
# Two Tens, Zero Ones
# ●If 8 was the input, the function output should be:
# Zero Tens, Eight Ones

def decompose_number(number):
    tens = number // 10
    ones = number % 10
    tens_label = "Ten" if tens != 1 else "One Ten"
    ones_label = "one" if ones == 1 else "Zero" if ones == 0 else f"{ones} Ones"
    print(f"{tens_label}, {ones_label}")
number = int(input("Enter a number between 1 and 25: "))
if 1 <= number <= 25:
    decompose_number(number)
else:
    print("Invalid input. Please enter a number between 1 and 25.")