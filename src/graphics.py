def game_title():
    game_title = """
 __   __    _     _                
 \ \ / /_ _| |__ | |_ _______  ___ 
  \ V / _` | '_ \| __|_  / _ \/ _ \\
   | | (_| | | | | |_ / /  __/  __/
   |_|\__,_|_| |_|\__/___\___|\___|
                                   
                                   """

    dice_art = """
  ____
 /\\' .\\    _____
/: \\___\\  / .  /\\
\\' / . / /____/..\\
 \\/___/  \\'  '\\  /
          \\'__'\\/
"""

    # Split both arts into lines
    title_lines = game_title.split('\n')
    dice_lines = dice_art.split('\n')

    # Calculate the maximum number of lines to pad
    max_lines = max(len(title_lines), len(dice_lines))

    # Pad each art with empty lines to ensure equal height
    title_lines += [''] * (max_lines - len(title_lines))
    dice_lines += [''] * (max_lines - len(dice_lines))

    # Combine the lines side by side
    combined_art = [title_line + '  ' + dice_line for title_line, dice_line in zip(title_lines, dice_lines)]

    # Print the combined art
    print('\n'.join(combined_art))


dice_faces = {
    1: ["-----",
        "|   |",
        "| o |",
        "|   |",
        "-----"],
    2: ["-----",
        "|o  |",
        "|   |",
        "|  o|",
        "-----"],
    3: ["-----",
        "|o  |",
        "| o |",
        "|  o|",
        "-----"],
    4: ["-----",
        "|o o|",
        "|   |",
        "|o o|",
        "-----"],
    5: ["-----",
        "|o o|",
        "| o |",
        "|o o|",
        "-----"],
    6: ["-----",
        "|o o|",
        "|o o|",
        "|o o|",
        "-----"]
}
