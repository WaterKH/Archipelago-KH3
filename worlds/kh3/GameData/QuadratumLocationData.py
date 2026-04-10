from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefKeyItem
from worlds.kh3.Locations import TresEventDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.SS_DLC_SUB_TRUEEND_END_ACC_ITEM112: BaseWorldLocationData('gameflow_SS_DLC_Sub_TrueEnd', value=ETresItemDefAccessory.ACC_ITEM112, label='SS_DLC_SUB_TRUEEND_END'),
    TresEventDataLocation.SS_DLC_SUB_TRUEEND_END_KEY_ITEM14: BaseWorldLocationData('gameflow_SS_DLC_Sub_TrueEnd', value=ETresItemDefKeyItem.KEY_ITEM14, label='SS_DLC_SUB_TRUEEND_END'),
}


# LOCATION NAMES
QUADRATUM_104_BUILDING_LOCATIONS: list[str] = [
    TresEventDataLocation.SS_DLC_SUB_TRUEEND_END_ACC_ITEM112,
    TresEventDataLocation.SS_DLC_SUB_TRUEEND_END_KEY_ITEM14
]