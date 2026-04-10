from CommonClient import logger
from worlds.kh3.GameData.BaseWorldLocationData import *
from typing import TYPE_CHECKING

# I don't know what is going on here, but it works.
if TYPE_CHECKING:
    from worlds.kh3.Client import KingdomHeartsIIIContext
else:
    KingdomHeartsIIIContext = object

def finished_game(ctx: KingdomHeartsIIIContext):
    # if ctx.
    #   return True
    return False