#_*_Coding:utf-8_*_
import random
def compare():
    guessesTaken= 0
    print('Hello! What is your name?')
    myName = input()
    number = int(random.randint(1, 100))
    print(number)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')
    while 1:
        print('Take a guess.')
        guess = input()
        guessesTaken = guessesTaken + 1
        if guess =='q':
            print('u quit')
            return 0
            quit(0);
        if int(guess) < number:
            print('Your guess is too low.')
            return 1
        if int(guess) > number:
            print('Your guess is too high.')
            return 2
        if int(guess) ==int(number):
            guess=int(guess)
            return 3
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
