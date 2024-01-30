# This Program says hello and asks for your name.
import random

print ('Hello')
print ('What is your name?')
yourName = input()
print ('It is nice to meet you, ' + yourName)
print ('Do you want to learn Python?')
answer = input()
finalAnswer = answer.lower()
if finalAnswer == 'yes':
    print ('visit ' + 'https://www.youtube.com')
else:
    print ('Ok, ' + 'Lets Play a Game')

print (yourName + ', I want your to guess my secret number. the number is between 1 to 20')
secretNum = random.randint(1, 20)

for guesses in range (1, 6):
    guess = int(input())
    if guess < secretNum:
        print('Ops!!, Your guess is low')
    elif guess > secretNum:
        print('Ops!!, Your guess is high')
    else:
        break
if secretNum == guess:
    print('Nice! Your Guess is correct')
else:
    print ('My secret number is actualy ' + str(secretNum) )