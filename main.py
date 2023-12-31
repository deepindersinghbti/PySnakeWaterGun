import random

choices = {
    'S': 'Snake',
    'W': 'Water',
    'G': 'Gun'
}

def get_input():
    user_choice = input("Enter your choice (S/W/G): ").upper()
    while user_choice not in choices:
        print("Invalid input.\n")
        user_choice = input("Enter your choice (S/W/G): ").upper()
    return user_choice

def get_computer_choice():
    return random.choice(list(choices.keys()))

def get_result(user_choice, comp_choice):
    global player_score, comp_score
    if user_choice == comp_choice:
        return "Draw"
    elif (
        (user_choice == 'S' and comp_choice == 'W') or
        (user_choice == 'W' and comp_choice =='G') or
        (user_choice == 'G' and comp_choice == 'S')
    ):
        player_score += 1
        return "Player"
    else:
        comp_score += 1
        return "Computer"

def play_game():
    global player_score, comp_score, draws
    player_score = 0
    comp_score = 0
    draws = 0

    while True:
        user_choice = get_input()
        comp_choice = get_computer_choice()
        print("You chose", choices[user_choice])
        print("Computer chose", choices[comp_choice])

        if user_choice != comp_choice:
            print("Winner is", get_result(user_choice, comp_choice), ".\n")
        else:
            print("It's a", get_result(user_choice, comp_choice), ".\n")
            draws += 1

        while True:
            replay_choice = int(input("Enter 0 to replay or 1 to exit: "))
            print("\n")
            if replay_choice == 0:
                break
            elif replay_choice == 1:
                print("Your final score is", player_score)
                print("Computer's final score is", comp_score)
                print("Number of draws:", draws)
                print("Thanks for playing.")
                return
            else:
                print("Invalid input.\n")

play_game()
