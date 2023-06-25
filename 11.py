def add_number(num1, num2, num3):
    return num1 + num2 + num3
result = add_number(24, 3, 5)
print(result)

def add_five(num):
    print(f"I have received {num}")
    num_after_adding = num + 5
    print(f"I have calculated {num} + 5 = {num_after_adding}")
    return num_after_adding

result = add_five(23)
print(result)

