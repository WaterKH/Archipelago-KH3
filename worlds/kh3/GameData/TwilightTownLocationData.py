from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefBattleItem, ETresItemDefCampItem, ETresItemDefLSIGameItem, ETresItemDefMaterial, ETresItemDefNavimap, ETresAbilityKind, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.TWILIGHT_TOWN_LARGE_TREASURE_001_NAVI_MAP_TT01: BaseWorldLocationData('TT_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_TT01),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_001_MAT_ITEM33: BaseWorldLocationData('TT_SBOX_001', value=ETresItemDefMaterial.MAT_ITEM33),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_002_MAT_ITEM53: BaseWorldLocationData('TT_SBOX_002', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_003_MAT_ITEM53: BaseWorldLocationData('TT_SBOX_003', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_004_ITEM_HIGHPOTION: BaseWorldLocationData('TT_SBOX_004', value=ETresItemDefBattleItem.ITEM_HIGHPOTION),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_005_ITEM_FOCUSSUPPLY: BaseWorldLocationData('TT_SBOX_005', value=ETresItemDefBattleItem.ITEM_FOCUSSUPPLY),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_006_ITEM_APUP: BaseWorldLocationData('TT_SBOX_006', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_007_ITEM_ETHER: BaseWorldLocationData('TT_SBOX_007', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_008_MAT_ITEM53: BaseWorldLocationData('TT_SBOX_008', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_009_ITEM_GUARDUP: BaseWorldLocationData('TT_SBOX_009', value=ETresItemDefCampItem.ITEM_GUARDUP),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.TT_LSI_GAME_MICKEY_PILOT: BaseWorldLocationData('TT_LSI_GAME_MICKEY_PILOT', value=ETresItemDefLSIGameItem.LSIGAME02),
    TresEventDataLocation.TT_LSI_GAME_MUSICAL_FARMER: BaseWorldLocationData('TT_LSI_GAME_MUSICAL_FARMER', value=ETresItemDefLSIGameItem.LSIGAME03),
    TresEventDataLocation.TT_LSI_GAME_BUILDING: BaseWorldLocationData('TT_LSI_GAME_BUILDING', value=ETresItemDefLSIGameItem.LSIGAME04),
    TresEventDataLocation.TT_LSI_GAME_MAD_DOCTOR: BaseWorldLocationData('TT_LSI_GAME_MAD_DOCTOR', value=ETresItemDefLSIGameItem.LSIGAME05),
    TresEventDataLocation.TT_BATTLEPORTAL_ex_23_CLEARED_MAT_ITEM59: BaseWorldLocationData('TT_BATTLEPORTAL_ex_23_CLEARED_MAT_ITEM59', value=ETresItemDefMaterial.MAT_ITEM59, label='global_BATTLEPORTAL_ex_23_CLEARED'),
    TresEventDataLocation.TT_BATTLEPORTAL_ex_23_CLEARED_REPORT_ITEM03: BaseWorldLocationData('TT_BATTLEPORTAL_ex_23_CLEARED_REPORT_ITEM03', value=ETresItemDefReport.REPORT_ITEM03, label='global_BATTLEPORTAL_ex_23_CLEARED'),
    TresEventDataLocation.TT_END_KEYBLADE: BaseWorldLocationData('gameflow_TT', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_02, label='TT_END'),
    TresEventDataLocation.TT_END_LSI: BaseWorldLocationData('gameflow_TT', value=ETresItemDefLSIGameItem.LSIGAME01, label='TT_END'),
    
    TresEventDataLocation.EX_minigame_Remy: BaseWorldLocationData('gameflow_EX_minigame_Remy', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_11, label='gameflow_EX_minigame_Remy'),
    TresEventDataLocation.EX_GET_CLASSIC_TONE: BaseWorldLocationData('EX_GET_CLASSIC_TONE', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_12, label='EX_GET_CLASSIC_TONE'), # TODO: Find this trigger

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_014_tt_001_ABILITYSORA1_MP_SAFETY: BaseWorldLocationData('Vbonus_014', value=ETresAbilityKind.MP_SAFETY, label='gameflow_VBONUS_014_tt_001'),
    TresVictoryBonusDataLocation.VBONUS_014_tt_001_BONUSSORA1_MELEM_CURE: BaseWorldLocationData('Vbonus_014', value=ETresVictoryBonusKind.MELEM_CURE, label='gameflow_VBONUS_014_tt_001'),
    TresVictoryBonusDataLocation.VBONUS_016_tt_003_BONUSSORA1_MELEM_BLIZZARD: BaseWorldLocationData('Vbonus_016', value=ETresVictoryBonusKind.MELEM_BLIZZARD, label='gameflow_VBONUS_016_tt_003'),
    TresVictoryBonusDataLocation.VBONUS_016_tt_003_BONUSSORA2_HP_UP10: BaseWorldLocationData('Vbonus_016', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_016_tt_003'),
}


# LOCATION NAMES
TWILIGHT_TOWN_TRAM_COMMON_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TWILIGHT_TOWN_LARGE_TREASURE_001_NAVI_MAP_TT01,
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_001_MAT_ITEM33,
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_002_MAT_ITEM53,
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_003_MAT_ITEM53,
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_004_ITEM_HIGHPOTION,
    TresEventDataLocation.TT_LSI_GAME_MICKEY_PILOT,
    TresEventDataLocation.TT_LSI_GAME_MUSICAL_FARMER,
    TresEventDataLocation.TT_LSI_GAME_BUILDING,
    TresEventDataLocation.TT_LSI_GAME_MAD_DOCTOR,
    TresEventDataLocation.TT_END_KEYBLADE,
    TresEventDataLocation.TT_END_LSI,
    TresVictoryBonusDataLocation.VBONUS_014_tt_001_ABILITYSORA1_MP_SAFETY,
    TresVictoryBonusDataLocation.VBONUS_014_tt_001_BONUSSORA1_MELEM_CURE,
    TresEventDataLocation.EX_minigame_Remy,
    TresEventDataLocation.EX_GET_CLASSIC_TONE
]

TWILIGHT_TOWN_UNDERGROUND_CONDUIT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_005_ITEM_FOCUSSUPPLY
]

TWILIGHT_TOWN_THE_WOODS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_006_ITEM_APUP,
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_007_ITEM_ETHER,
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_008_MAT_ITEM53
]

TWILIGHT_TOWN_THE_OLD_MANSION_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TWILIGHT_TOWN_SMALL_TREASURE_009_ITEM_GUARDUP,
    TresVictoryBonusDataLocation.VBONUS_016_tt_003_BONUSSORA1_MELEM_BLIZZARD,
    TresVictoryBonusDataLocation.VBONUS_016_tt_003_BONUSSORA2_HP_UP10,
    TresEventDataLocation.TT_BATTLEPORTAL_ex_23_CLEARED_MAT_ITEM59,
    TresEventDataLocation.TT_BATTLEPORTAL_ex_23_CLEARED_REPORT_ITEM03
]