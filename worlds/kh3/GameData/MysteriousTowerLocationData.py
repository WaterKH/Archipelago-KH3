from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefKeyItem
from worlds.kh3.Locations import TresEventDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.YT_EVENT2_KEY_ITEM06: BaseWorldLocationData('gameflow_YT', value=ETresItemDefKeyItem.KEY_ITEM06, label='YT_EVENT2'),
    TresEventDataLocation.GM_EVENT2_KEY_ITEM02: BaseWorldLocationData('gameflow_GM', value=ETresItemDefKeyItem.KEY_ITEM02, label='GM_EVENT2'),
}


# LOCATION NAMES
MYSTERIOUS_TOWER_STUDY_LOCATIONS: list[str] = [
    TresEventDataLocation.YT_EVENT2_KEY_ITEM06,
    TresEventDataLocation.GM_EVENT2_KEY_ITEM02
]