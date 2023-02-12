from random import randint
from time import sleep

user_score = computer_score = 0
option = ['', 'Rock', 'Paper', 'Scissor']
end_game = False

while True:
    print('\033[1;31m-\033[m'*30)
    print(f'\033[1;33m{"ROCK - PAPER - SCISSOR":^30}\033[m')
    print('\033[1;31m-\033[m'*30)
    print(f'\033[1;32m{"[1]"}\033[m \033[1;34m{"Rock":<26}\033[m')
    print(f'\033[1;32m{"[2]"}\033[m \033[1;34m{"Paper":<26}\033[m')
    print(f'\033[1;32m{"[3]"}\033[m \033[1;34m{"Scissor":26}\033[m')
    print('\033[1;31m-\033[m'*30)

    try:
        while True:
            user_choice = int(input('\033[1;33mYour choice:\033[m '))
            if 0 < user_choice < 4:
                break
            print('\033[1;31mERROR! Invalid choice!\033[m')
    except:
        print('\033[1;31mERROR! Invalid choice!\033[m')
        continue

    computer_choice = randint(1, 3)

    if user_choice == computer_choice:
        pass
    elif user_choice == 1 and computer_choice == 3:
        user_score += 1
    elif user_choice == 2 and computer_choice == 1:
        user_score += 1
    elif user_choice == 3 and computer_choice == 2:
        user_score += 1
    else:
        computer_score += 1

    print('\033[1;31m-\033[m'*30)
    print(f'\033[1;36m{option[user_choice]}\033[m \033[1;31m{"x"}\033[m \033[1;32m{option[computer_choice]}\033[m')
    sleep(1)
    print(f'\033[1;36mPlayer Score:\033[m \033[1;34m{user_score}\033[m')
    print(f'\033[1;32mComputer Score:\033[m \033[1;34m{computer_score}\033[m')
    print('\n\n')
    sleep(1)

    if user_score == 5 or computer_score == 5:
        end_game = True
        print('\033[1;33mGame Over!\033[m')
        break

if end_game == True and user_score > computer_score:
    print('\033[1;32mCongrats! You WON!!\033[m')
else:
    print('\033[1;31mYou LOST =(\033[m')

