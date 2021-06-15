#Guess the even number in range 1 to 50
import random
number=random.randrange(0,50,2)
player_name=input("Hello,what's your name?")
for i in range(0,5):
    guess = int(input("enter the number"))
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        print('You guessed the number ')
        break
if guess!=number:
     print('You did not guess the number, The number was ' + str(number))