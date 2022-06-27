import random

password = int(input('Enter your password:'))
guess = 0
while(guess != password):
    guess = random.randint(0, 9999)
    print(guess)
print('Your password is ' + str(guess))
