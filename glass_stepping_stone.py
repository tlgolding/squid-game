import random

def glass_bridge_with_order():
    # game setup
    bridge_length = 16
    players = 16
    bridge = [[random.choice([True, False]), random.choice([True, False])] for _ in range(bridge_length)]

    # randomize player order
    player_order = list(range(1, players + 1))
    random.shuffle(player_order)

    # what number do you get?
    user_position = random.choice(player_order)
    print(f"You are player #{user_position} in the order.\n")

    # your opponents
    player_progress = [0] * players  # track each player's position
    for current_player in range(1, user_position):
        print(f"Next up is #{player_order[current_player - 1]}")
        while player_progress[current_player - 1] < bridge_length:
            row = player_progress[current_player - 1]
            choice = random.choice([0, 1])  # randomly pick left or right 
            if bridge[row][choice]:  # safe tile
                player_progress[current_player - 1] += 1
            else:  # unsafe tile
                print(f"Player #{player_order[current_player - 1]} eliminated at {row + 1}!\n")
                break

    print(f"Next up is Player Number #{user_position}")
    position = 0
    while position < bridge_length:
        # the bridge now based on others’ decisions
        visible_bridge = ["?" if all(tile for tile in row) else "X" for row in bridge[:position]]
        print("Visible Bridge: ", " -> ".join(visible_bridge))

        print(f"Row {position + 1}: Left or right? (left/right)")
        player_choice = input("> ").strip().lower()

        if player_choice == "left":
            choice_index = 0
        elif player_choice == "right":
            choice_index = 1
        else:
            print("Invalid choice. Please type 'left' or 'right'.")
            continue

        # are they safe?
        if bridge[position][choice_index]:
            print("Next tile!\n")
            position += 1
        else:
            print(f"Player #{user_position}: Eliminated..\n")
            return glass_bridge_with_order()  # restart

    print("Success!")
    play_again = input("Vote x to end the games, vote o to try again. (X/O) ").strip().lower()
    if play_again == "o":
        glass_bridge_with_order()
    else:
        print("You have voted x. You may take your winnings and go.")

# start the enhanced game
glass_bridge_with_order()


