from main import *
from collections import Counter

def calculate_mission(dice_values):

    """Calculate points based on the most common dice value and Yahtzee missions."""
    frequency = Counter(dice_values)
    most_common_num, count = frequency.most_common(1)[0]

    if count == 5:
        # Yahtzee (cinq dés identiques)
        return 50
    elif count == 4:
        # Carré (quatre dés identiques)
        return sum(dice_values)
    elif count == 3 and len(frequency) == 2:
        # Full (trois dés identiques et deux dés identiques)
        return 25
    elif all(value in dice_values for value in [1, 2, 3, 4, 5]):
        # Petite suite (1, 2, 3, 4, 5)
        return 30
    elif all(value in dice_values for value in [2, 3, 4, 5, 6]):
        # Grande suite (2, 3, 4, 5, 6)
        return 40

    # Si aucune mission n'est remplie, retourne le produit du nombre le plus commun et de son nombre d'occurrences
    return most_common_num * count





