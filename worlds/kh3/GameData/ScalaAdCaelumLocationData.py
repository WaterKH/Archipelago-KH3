from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefBattleItem, ETresItemDefFood, ETresItemDefMaterial, ETresItemDefNavimap, ETresVictoryBonusKind
from worlds.kh3.Locations import TresTreasureDataLocation, TresVictoryBonusDataLocation, TresEventDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.SCALA_AD_CAELUM_LARGE_TREASURE_001_NAVI_MAP_BT01: BaseWorldLocationData('BT_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_BT01),
    TresTreasureDataLocation.SCALA_AD_CAELUM_LARGE_TREASURE_002_NAVI_MAP_BT02: BaseWorldLocationData('BT_LBOX_002', value=ETresItemDefNavimap.NAVI_MAP_BT02),
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_001_ITEM_LASTELIXIR: BaseWorldLocationData('BT_SBOX_001', value=ETresItemDefBattleItem.ITEM_ELIXIR),
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_002_FOOD_ITEM56: BaseWorldLocationData('BT_SBOX_002', value=ETresItemDefFood.FOOD_ITEM56),
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_003_MAT_ITEM48: BaseWorldLocationData('BT_SBOX_003', value=ETresItemDefMaterial.MAT_ITEM48),
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_004_MAT_ITEM47: BaseWorldLocationData('BT_SBOX_004', value=ETresItemDefMaterial.MAT_ITEM47),
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_005_ITEM_MEGAETHER: BaseWorldLocationData('BT_SBOX_005', value=ETresItemDefBattleItem.ITEM_MEGAETHER),
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_006_MAT_ITEM58: BaseWorldLocationData('BT_SBOX_006', value=ETresItemDefMaterial.MAT_ITEM58),
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_007_MAT_ITEM52: BaseWorldLocationData('BT_SBOX_007', value=ETresItemDefMaterial.MAT_ITEM52),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    #TresEventDataLocation.COMPLETE_GAME: BaseWorldLocationData('COMPLETE_GAME', value='COMPLETE_GAME'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_DLC_010_bt_002_BONUSSORA1_MP_UP3: BaseWorldLocationData('VBonus_DLC_010', value=ETresVictoryBonusKind.MP_UP3, label='gameflow_VBONUS_DLC_010_bt_002')
}


# LOCATION NAMES
SCALA_AD_CAELUM_THE_STAIRWAY_TO_THE_SKY_LOCATIONS: list[str] = [
    TresTreasureDataLocation.SCALA_AD_CAELUM_LARGE_TREASURE_001_NAVI_MAP_BT01
]

SCALA_AD_CAELUM_BREEZY_QUARTER_LOCATIONS: list[str] = [
    TresTreasureDataLocation.SCALA_AD_CAELUM_LARGE_TREASURE_002_NAVI_MAP_BT02,
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_001_ITEM_LASTELIXIR,
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_002_FOOD_ITEM56,
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_003_MAT_ITEM48,
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_004_MAT_ITEM47,
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_005_ITEM_MEGAETHER,
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_006_MAT_ITEM58,
    TresTreasureDataLocation.SCALA_AD_CAELUM_SMALL_TREASURE_007_MAT_ITEM52,
    TresVictoryBonusDataLocation.VBONUS_DLC_010_bt_002_BONUSSORA1_MP_UP3
]

# END_SCREEN_LOCATIONS: list[str] = [
#     TresEventDataLocation.COMPLETE_GAME
# ]