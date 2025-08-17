import re

def get_dice_average(dice_str):
    """
    Converts a dice string like '2d6' into its average value.
    Example: '2d6' => (2 * (6 + 1)) / 2 = 7
    """
    if not isinstance(dice_str, str) or 'd' not in dice_str:
        return 0  # Gracefully handle invalid or missing dice strings

    match = re.match(r"(\d+)d(\d+)", dice_str)
    if not match:
        return 0  # Invalid format like '1' or 'd6'

    num_dice, dice_sides = map(int, match.groups())
    return (num_dice * (dice_sides + 1)) / 2
