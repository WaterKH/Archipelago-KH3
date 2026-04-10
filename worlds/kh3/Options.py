import logging

from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, Range, FreeText, PerGameCommonOptions, OptionGroup, Removed, StartInventoryPool

"""

"""
logger = logging.getLogger('Kingdom Hearts III Logger')


"""

"""
class Goal(Choice):
    """
    The Goal of the game.

    **Proofs:** Scala ad Caelum and the Master Xehanort fight will only open if 
    you have collected all 3 proofs: Promises, Times Past and Fantasies
    

    **Kairi's Heart Pieces:** Scala ad Caelum and the Master Xehanort fight will 
    only open if you have collected all 7 pieces of Kairi's heart

    **Both:** Scala ad Caelum and the Master Xehanort fight will only open if 
    you have all 3 proofs and 7 pieces of Kairi's heart.
    """
    display_name = "Goal"
    rich_text_doc = True

    option_proofs = 0
    option_heart_pieces = 1
    option_both = 2

    default = option_proofs
        
"""

"""
kh3_option_groups = [
    # OptionGroup('Level Limits', [
    #     # Sora, Keyblade and Synthesis Levels
    # ]),
    # OptionGroup('Collectibles', [
    #     # Lucky Emblems, Heartless Pictures and Caribbean/ San Fransokyo Treasures
    # ]),
    # OptionGroup('Battles', [
    #     # Battlegates, Databattles and Yozora
    # ]),
    # OptionGroup('Quality of Life', [
    #     # Skip Crabs, Frozen Slide, UFO, Raging Vulture and Sora Collection
    # ])
]

kh3_options_presets = {
    "": {
        "": []
    }
}


@dataclass
class KingdomHeartsIIIOptions(PerGameCommonOptions):
    Goal: Goal