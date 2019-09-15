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
        print('Take a guess.') # There are four spaces in front of print.
        guess = input()
        guessesTaken = guessesTaken + 1
        if guess =='q':
            print('u quit')
            quit(0);
        if int(guess) < number:
            print('Your guess is too low.') # There are eight spaces in front of print.
        if int(guess) > number:
            print('Your guess is too high.')
        if int(guess) ==int(number):
            guess=int(guess)
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

compare()