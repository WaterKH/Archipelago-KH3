from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefWeapon
from worlds.kh3.Locations import TresEventDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.PO_END: BaseWorldLocationData('gameflow_PO', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_07, label='PO_END'),
}


# LOCATION NAMES
HUNDRED_ACRE_WOOD_RABBITS_HOUSE_LOCATIONS: list[str] = [
    TresEventDataLocation.PO_END
]