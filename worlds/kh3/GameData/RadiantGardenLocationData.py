from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefCampItem, ETresItemDefKeyItem, ETresItemDefProtector
from worlds.kh3.Locations import TresEventDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    
    # TODO: Verify these rewards
    TresEventDataLocation.RG_DLC_SHU_BATTLE_10: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_10', value=ETresItemDefProtector.PRT_ITEM52, label='gameflow_RG_DLC_SHU_BATTLE_10'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_11: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_11', value=ETresItemDefCampItem.ITEM_GUARDUP, label='gameflow_RG_DLC_SHU_BATTLE_11'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_12: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_12', value=ETresItemDefProtector.PRT_ITEM50, label='gameflow_RG_DLC_SHU_BATTLE_12'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_13: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_13', value=ETresItemDefCampItem.ITEM_APUP, label='gameflow_RG_DLC_SHU_BATTLE_13'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_14: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_14', value=ETresItemDefProtector.PRT_ITEM51, label='gameflow_RG_DLC_SHU_BATTLE_14'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_15: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_15', value=ETresItemDefCampItem.ITEM_MAGICUP, label='gameflow_RG_DLC_SHU_BATTLE_15'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_16: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_16', value=ETresItemDefProtector.PRT_ITEM51, label='gameflow_RG_DLC_SHU_BATTLE_16'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_17: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_17', value=ETresItemDefProtector.PRT_ITEM50, label='gameflow_RG_DLC_SHU_BATTLE_17'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_18: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_18', value=ETresItemDefCampItem.ITEM_POWERUP, label='gameflow_RG_DLC_SHU_BATTLE_18'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_19: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_19', value=ETresItemDefProtector.PRT_ITEM50, label='gameflow_RG_DLC_SHU_BATTLE_19'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_20: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_20', value=ETresItemDefCampItem.ITEM_APUP, label='gameflow_RG_DLC_SHU_BATTLE_20'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_21: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_21', value=ETresItemDefProtector.PRT_ITEM51, label='gameflow_RG_DLC_SHU_BATTLE_21'),
    TresEventDataLocation.RG_DLC_SHU_BATTLE_22: BaseWorldLocationData('gameflow_RG_DLC_SHU_BATTLE_22', value=ETresItemDefAccessory.ACC_ITEM111, label='gameflow_RG_DLC_SHU_BATTLE_22'),
}


# LOCATION NAMES
RADIANT_GARDEN_DATA_BATTLES_LOCATIONS: list[str] = [
    TresEventDataLocation.RG_DLC_SHU_BATTLE_10,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_11,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_12,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_13,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_14,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_15,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_16,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_17,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_18,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_19,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_20,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_21,
    TresEventDataLocation.RG_DLC_SHU_BATTLE_22
]