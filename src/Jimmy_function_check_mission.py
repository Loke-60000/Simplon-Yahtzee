from main import *
from collections import Counter


checked_missions = {} 


def is_mission_checked(mission):
    return checked_missions.get(mission, False)

def check_mission(mission):
    checked_missions[mission] = True

def calculate_mission(dice_values, round_number):
    frequency = Counter(dice_values)
    most_common_num, count = frequency.most_common(1)[0]

    if is_mission_checked(round_number):
        print(f"La mission {round_number} a déjà été cochée.")
        return 0

    if round_number > 6:
        check_mission(round_number)
        return score
 
    else:
        check_mission(round_number)
        return score

score = calculate_mission()
