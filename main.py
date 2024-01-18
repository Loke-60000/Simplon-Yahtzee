import random
from collections import Counter
from src.graphics import game_title, dice_faces

def print_dice(dice_values):
    """Print the visual representation of dice."""
    dice_art = [dice_faces[value] for value in dice_values]
    for i in range(len(dice_art[0])):
        print(" ".join(dice_line[i] for dice_line in dice_art))

def roll_dice(num_dice):
    """Roll a specified number of dice."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def calculate_points(dice_values):
    """Calculate points based on the most common dice value."""
    frequency = Counter(dice_values)
    most_common_num, count = frequency.most_common(1)[0]
    return most_common_num * count

def reroll_dice(dice_values, reroll_indices):
    """Reroll selected dice."""
    for i in reroll_indices:
        dice_values[i] = random.randint(1, 6)

def get_reroll_indices(retry_input):
    """Get indices of dice to reroll from user input."""
    reroll = retry_input[5:].replace(" ", "")
    return [int(d) - 1 for d in reroll.split(',') if d.isdigit()]

def game():
    """Main game function."""
    game_title()  # Display the game title
    num_players = int(input("Enter the number of players: "))
    players = list(range(1, num_players + 1))
    current_player = 1
    max_points = 0
    winning_player = None
    scores = {player: 0 for player in players}

    for round in range(1, 14):
        print(f"Round {round}")
        print(f"Player {current_player}'s turn:")
        
        dice_values = roll_dice(5)  # Roll 5 dice

        for _ in range(3):  # Allow up to 3 rerolls
            print("Current dice values:")
            print_dice(dice_values)

            retry_input = input("Enter 'retry' followed by the dice numbers to reroll, or any other key to change players: ")
            if retry_input.startswith('retry'):
                reroll_dice(dice_values, get_reroll_indices(retry_input))
            else:
                break

        points = calculate_points(dice_values)
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

if __name__ == '__main__':
    game()
