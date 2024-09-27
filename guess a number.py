print('enter your name')
name=input()
import random
print('Hello ' + name +' I am thinking of a number between 1 to 20')
print('your task is to guess that number within 6 trials')
num=random.randint(1,20)

for i in range (1,7):
    print('guess no ' +str(i)+ '; guess a number')
    guess=input()

    if int(guess) > num:
        print('sorry, number I was thinking is smaller than your guess')
    elif int(guess) < num:
        print('sorry, number I was thinking is higher than your guess')
    else:
        break
if num == int(guess):
    print('bingo!! you correctly guessed my number in ' + str(i) + ' guesses')
else:
    print('try again!! your trials to guess that number has ended')
    print('the number I was thinking is ' + str(num))
    
5
