import re

## This function calculates the average roll of a dice string in D&D 5e format.
def get_dice_average(dice_str):
    """
    Parses a dice string like '2d8 + 3' and returns the average roll.
    """
    pattern = r'(\d+)d(\d+)(?:\s*([+-])\s*(\d+))?'
    match = re.match(pattern, dice_str.strip())

    if not match:
        raise ValueError(f"Invalid dice string: {dice_str}")

    num_dice = int(match.group(1))
    dice_sides = int(match.group(2))
    modifier = int(match.group(4)) if match.group(4) else 0
    if match.group(3) == '-':
        modifier *= -1

    average = num_dice * ((dice_sides + 1) / 2) + modifier
    return round(average)



## This function calculates the valid challenge ratings (CR) for a given character level in D&D 5e.
def calculate_valid_cr_to_level(character_level):
    """
    Calculates the valid challenge ratings (CR) for a given character level.
    """
    # This list contains valid challenge ratings (CR) for monsters in D&D 5e.
    valid_crs = [
        0, 0.125, 0.25, 0.5, 1, 2, 3, 4, 5,
        6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24,
        25, 26, 27, 28, 29, 30
    ]
    
    # This scale is used to determine the challenge rating (CR) for solo encounters based on player levels.
    solo_cr_scale = [
        {"level_range": (1, 2), "cr_min": 0, "cr_max": 0.25},
        {"level_range": (3, 4), "cr_min": 0.25, "cr_max": 0.5},
        {"level_range": (5, 6), "cr_min": 0.5, "cr_max": 1},
        {"level_range": (7, 8), "cr_min": 1, "cr_max": 2},
        {"level_range": (9, 10), "cr_min": 2, "cr_max": 3},
        {"level_range": (11, 13), "cr_min": 3, "cr_max": 5},
        {"level_range": (14, 16), "cr_min": 5, "cr_max": 8},
        {"level_range": (17, 20), "cr_min": 8, "cr_max": 10}
    ]
    
    # Determine the valid challenge ratings (CR) based on the character level.
    for entry in solo_cr_scale:
        min_level, max_level = entry["level_range"]
        if min_level <= character_level <= max_level:
            cr_min = entry["cr_min"]
            cr_max = entry["cr_max"]
            return [cr for cr in valid_crs if cr_min <= cr <= cr_max] # List of valid CRs for the character level
