```
 __   __    _     _                    ____
 \ \ / /_ _| |__ | |_ _______  ___    /\' .\    _____
  \ V / _` | '_ \| __|_  / _ \/ _ \  /: \___\  / .  /\
   | | (_| | | | | |_ / /  __/  __/  \' / . / /____/..\
   |_|\__,_|_| |_|\__/___\___|\___|   \/___/  \'  '\  /
                                               \'__'\/
                                     
```

# Yahtzee-Style Dice Game in Python

This is a Python implementation of a Yahtzee-style dice game. The game allows multiple players to roll dice, decide which dice to keep or reroll, and accumulate points based on the number of dice showing the same number.

## Game Setup and Rules

- The game is played by multiple players.
- Each player rolls five dice up to three times in a turn.
- After each roll, the player can choose to reroll some or all of the dice.
- Points are scored based on the frequency of the dice numbers.

## Code Structure

1. **Import Statements**
   - Random module for dice rolls.
   - Collections' Counter for counting dice frequencies.
   - Custom graphics module for game visuals.

2. **Function Definitions**
   - `print_dice(dice_values)`: Prints a visual representation of the dice.
   - `roll_dice(num_dice)`: Rolls a specified number of dice, returning their values.
   - `calculate_points(dice_values)`: Calculates points based on the most common dice value.
   - `reroll_dice(dice_values, reroll_indices)`: Rerolls the specified dice.
   - `get_reroll_indices(retry_input)`: Parses user input to determine which dice to reroll.

3. **Main Game Function**
   - `game()`: Manages the game play, including player turns, dice rolling, rerolling, and scoring. Determines the game winner based on the scores.

4. **Execution Check**
   ```
        python3 main.py
   ```