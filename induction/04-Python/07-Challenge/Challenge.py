import random

def get_computer_choice(options_lst = ["Rock","Paper","Scissors"]):
    return random.choice(options_lst)

def game():
    player_choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()

    computer_choice = get_computer_choice().lower()

    res = None
    '''
    res =  0 => draw
    res =  1 => player wins
    res = -1 => player loses
    '''
    if player_choice == computer_choice:
        res = 0
    elif player_choice == "rock":
        if computer_choice == "scissors":
            res = 1
        else:
            res = -1
    elif player_choice == "paper":
        if computer_choice == "rock":
            res = 1
        else:
            res = -1
    elif player_choice == "scissors":
        if computer_choice == "paper":
            res = 1
        else:
            res = -1

    print(f"You chose {player_choice}, the computer chose {computer_choice}.")

    if res == 1:
        print(f"{player_choice} kills {computer_choice}! You win.")
        return 1
    elif res == -1:
        print(f"{computer_choice} kills {player_choice}! You lose.")
        return -1
    else:
        print(f"Both chose {player_choice}! Draw!")
        return 0

play_again = True
player_score = 0
computer_score = 0
while play_again:
    res = game()
    if res == 1:
        player_score += 1
    elif res == -1:
        computer_score += 1

    if input("Play again? (y/n)") == "n":
        play_again = False

print("Final Scores: ")
print(f"Computer: {computer_score}")
print(f"Player: {player_score}")