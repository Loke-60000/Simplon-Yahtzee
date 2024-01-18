import random
from collections import Counter

def dices():
    num_players = int(input("Enter the number of players: "))
    players = list(range(1, num_players + 1))
    current_player = 1
    max_points = 0
    winning_player = None
    scores = {player: 0 for player in players}

    for round in range(1, 14):
        print(f"Round {round}")
        print(f"Player {current_player}'s turn:")
        
        dice_values = [random.randint(1, 6) for _ in range(5)]

        for _ in range(3):
            print("Current dice values:")
            for i, value in enumerate(dice_values, 1):
                print(f"Dice {i}: {value}")

            retry_input = input("Enter 'retry' followed by the dice numbers to reroll (e.g., 'retry 1,3,5'), or any other key to change players: ")
            if retry_input.startswith('retry'):
                reroll = retry_input[5:].replace(" ", "")
                reroll_indices = [int(d) - 1 for d in reroll.split(',') if d.isdigit()]
                for i in reroll_indices:
                    dice_values[i] = random.randint(1, 6)
            else:
                break

        frequency = Counter(dice_values)
        most_common_num, count = frequency.most_common(1)[0]
        points = most_common_num * count
        print(f"Points for Player {current_player}: {points}")

        scores[current_player] += points

        if scores[current_player] > max_points:
            max_points = scores[current_player]
            winning_player = current_player

        change_player = input("Enter the number of the player to change to, or any other key to exit: ")
        if change_player.isdigit() and int(change_player) in players:
            current_player = int(change_player)
        else:
            break

    print("Game Over")
    print("Final Scores:")
    for player, score in scores.items():
        print(f"Player {player}: {score}")
    print(f"Player {winning_player} wins with {max_points} points!")

dices()