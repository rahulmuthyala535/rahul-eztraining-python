import random
num = random.randrange(1, 30)
print(num)
guess = int(input("Enter any number: "))
while guess != num:

    if guess > num:
        print('Too High!')
        guess = int(input('Enter number again: '))
    elif guess < num:
        print('Too Low!')
        guess = int(input('Enter number again: '))
    else:
        break
print('You guessed it right!')
