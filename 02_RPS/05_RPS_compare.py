# Compares user choice

rps_list = ["rock", "paper", "scissors"]
comp_index = 0

for item in rps_list:
    user_index = 0
    for n in rps_list:
        user_move = rps_list[user_index]
        comp_move = rps_list[comp_index]

        winning_combinations = {'rock': 'scissors', 'paper': 'rock',
                                'scissors': 'paper'}

        user_index += 1

        # compare choices
        if user_move == comp_move:
            result = "tie"
        elif winning_combinations[user_move] == comp_move:
            result = "user wins"

        else:
            result = "computer wins"

        print(f"User chose {user_move}, computer chose {comp_move}.\nResult: {result}")

    comp_index += 1
    print()
