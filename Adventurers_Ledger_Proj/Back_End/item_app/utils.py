import re

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
