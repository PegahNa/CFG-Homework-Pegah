# Createaprogramthattellsyouwhetherornotyouneedsunglasseswhenyouleave
# the house.
# The program should:
# 1. Ask you if it is sunny using input()
# 2. If the input is 'y', it should output 'Take your sunglasses’
# 3. If the input is 'n', it should output 'You don't need sunglasses’

weather = input("Is it sunny? (y/n): ")
if weather == "y":
    print("Take your sunglasses!")
elif weather == "n":
    print("You don't need sunglasses.")
else:
    print("Invalid input. Please enter 'y' or 'n'.")
