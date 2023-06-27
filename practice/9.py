from random import randint
fav_number = 77
guess_correct = False

while not guess_correct:
     guess = randint(0, 100)
     if guess == fav_number:
         print("You guessed right: 77!")
         guess_correct = True
     else:
         print(f"{guess} is wrong! Try again.")