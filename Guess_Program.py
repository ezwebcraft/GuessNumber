import random

print('----------------------------')
print('   Guess That Number Game   ')
print('----------------------------')
print()

the_number = random.randint(0, 100)

guess = -1

name = input('Player, Please your name')

while guess !=  the_number:

    guess_test = input('Guess a number between 0 and 100: ')

    guess = int(guess_test)

    if guess < the_number:
        print('Hey {} Your Number {} was too Low !!!'.format(name, guess))
    elif guess > the_number:
        print('Hey {} Your Number {} was too High !!!'.format(name, guess))
    else:
        print('Hey {} you wish'.format(name))

# TODO: remove this line
# print(guess_test, type(guess_test))
# print(guess, type(guess))


print('done')
