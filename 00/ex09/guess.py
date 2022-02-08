from random import randint

print(
    """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n""")


secret_number = randint(1, 99)
attempts = 0
while True:
    print("What's your guess between 1 and 99?")
    num_str = input("> ")

    if num_str == 'exit':
        print('the secret number is', secret_number)
        print('zmatek :etu:')
        break
    if not num_str.isnumeric():
        print("That's not a number.")
        continue

    num = int(num_str)
    attempts += 1
    if num > secret_number:
        print('Too Hight!')
    elif num < secret_number:
        print('Too Low!')
    else:
        print("Congratulations, you've got it!")
        print(f'You won in {attempts} attempts')
        break
