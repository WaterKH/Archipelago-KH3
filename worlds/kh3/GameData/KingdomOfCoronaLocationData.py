from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefBattleItem, ETresItemDefCampItem, ETresItemDefFood, ETresItemDefLSIGameItem, ETresItemDefMaterial, ETresItemDefNavimap, ETresItemDefProtector, ETresAbilityKind, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_001_NAVI_MAP_RA01: BaseWorldLocationData('RA_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_RA01),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_002_NAVI_MAP_RA02: BaseWorldLocationData('RA_LBOX_002', value=ETresItemDefNavimap.NAVI_MAP_RA02),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_003_LSIGAME15: BaseWorldLocationData('RA_LBOX_003', value=ETresItemDefLSIGameItem.LSIGAME15),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_004_LSIGAME18: BaseWorldLocationData('RA_LBOX_004', value=ETresItemDefLSIGameItem.LSIGAME18),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_005_LSIGAME09: BaseWorldLocationData('RA_LBOX_005', value=ETresItemDefLSIGameItem.LSIGAME09),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_006_ACC_ITEM43: BaseWorldLocationData('RA_SBOX_006', value=ETresItemDefAccessory.ACC_ITEM43),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_001_PRT_ITEM47: BaseWorldLocationData('RA_SBOX_001', value=ETresItemDefProtector.PRT_ITEM47),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_002_PRT_ITEM28: BaseWorldLocationData('RA_SBOX_002', value=ETresItemDefProtector.PRT_ITEM28),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_003_PRT_ITEM30: BaseWorldLocationData('RA_SBOX_003', value=ETresItemDefProtector.PRT_ITEM30),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_004_ACC_ITEM25: BaseWorldLocationData('RA_SBOX_004', value=ETresItemDefAccessory.ACC_ITEM25),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_005_ITEM_ALLCURE: BaseWorldLocationData('RA_SBOX_005', value=ETresItemDefBattleItem.ITEM_ALLCURE),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_006_ITEM_POTION: BaseWorldLocationData('RA_SBOX_006', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_007_ITEM_FOCUSSUPPLY: BaseWorldLocationData('RA_SBOX_007', value=ETresItemDefBattleItem.ITEM_FOCUSSUPPLY),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_008_ITEM_POTION: BaseWorldLocationData('RA_SBOX_008', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_009_PRT_ITEM41: BaseWorldLocationData('RA_SBOX_009', value=ETresItemDefProtector.PRT_ITEM41),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_010_ACC_ITEM34: BaseWorldLocationData('RA_SBOX_010', value=ETresItemDefAccessory.ACC_ITEM34),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_011_PRT_ITEM04: BaseWorldLocationData('RA_SBOX_011', value=ETresItemDefProtector.PRT_ITEM04),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_012_MAT_ITEM54: BaseWorldLocationData('RA_SBOX_012', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_013_MAT_ITEM34: BaseWorldLocationData('RA_SBOX_013', value=ETresItemDefMaterial.MAT_ITEM34),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_014_ITEM_ETHER: BaseWorldLocationData('RA_SBOX_014', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_015_MAT_ITEM54: BaseWorldLocationData('RA_SBOX_015', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_016_ITEM_APUP: BaseWorldLocationData('RA_SBOX_016', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_017_ITEM_HIGHETHER: BaseWorldLocationData('RA_SBOX_017', value=ETresItemDefBattleItem.ITEM_HIGHETHER),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_018_ITEM_MAGICUP: BaseWorldLocationData('RA_SBOX_018', value=ETresItemDefCampItem.ITEM_MAGICUP),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_019_ITEM_ETHER: BaseWorldLocationData('RA_SBOX_019', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_020_FOOD_ITEM41: BaseWorldLocationData('RA_SBOX_020', value=ETresItemDefFood.FOOD_ITEM41),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_021_ACC_ITEM18: BaseWorldLocationData('RA_SBOX_021', value=ETresItemDefAccessory.ACC_ITEM18),
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_022_ITEM_HIGHPOTION: BaseWorldLocationData('RA_SBOX_022', value=ETresItemDefBattleItem.ITEM_HIGHPOTION),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.RA_BATTLEPORTAL_ex_26_CLEARED_MAT_ITEM60: BaseWorldLocationData('RA_BATTLEPORTAL_ex_26_CLEARED_MAT_ITEM60', value=ETresItemDefMaterial.MAT_ITEM60, label='global_BATTLEPORTAL_ex_26_CLEARED'),
    TresEventDataLocation.RA_BATTLEPORTAL_ex_26_CLEARED_REPORT_ITEM06: BaseWorldLocationData('RA_BATTLEPORTAL_ex_26_CLEARED_REPORT_ITEM06', value=ETresItemDefReport.REPORT_ITEM06, label='global_BATTLEPORTAL_ex_26_CLEARED'),
    TresEventDataLocation.RA_BATTLEPORTAL_ex_27_CLEARED_ACC_ITEM43: BaseWorldLocationData('RA_BATTLEPORTAL_ex_27_CLEARED_ACC_ITEM43', value=ETresItemDefAccessory.ACC_ITEM43, label='global_BATTLEPORTAL_ex_27_CLEARED'),
    TresEventDataLocation.RA_BATTLEPORTAL_ex_27_CLEARED_REPORT_ITEM07: BaseWorldLocationData('RA_BATTLEPORTAL_ex_27_CLEARED_REPORT_ITEM07', value=ETresItemDefReport.REPORT_ITEM07, label='global_BATTLEPORTAL_ex_27_CLEARED'),
    TresEventDataLocation.RA_END: BaseWorldLocationData('gameflow_RA', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_04, label='RA_END'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_024_ra_001_BONUSSORA1_MELEM_AERO: BaseWorldLocationData('Vbonus_024', value=ETresVictoryBonusKind.MELEM_AERO, label='gameflow_VBONUS_024_ra_001'),
    TresVictoryBonusDataLocation.VBONUS_026_ra_003_ABILITYSORA1_GUARD_COUNTER: BaseWorldLocationData('Vbonus_026', value=ETresAbilityKind.GUARD_COUNTER, label='gameflow_VBONUS_026_ra_003'),
    TresVictoryBonusDataLocation.VBONUS_027_ra_004_BONUSSORA1_MP_UP5: BaseWorldLocationData('Vbonus_027a', value=ETresVictoryBonusKind.MP_UP5, label='gameflow_VBONUS_027_ra_004'),
    TresVictoryBonusDataLocation.VBONUS_027_ra_004_ABILITYSORA1_SUPERJUMP: BaseWorldLocationData('Vbonus_027b', value=ETresAbilityKind.SUPERJUMP, label='gameflow_VBONUS_027_ra_004'),
    TresVictoryBonusDataLocation.VBONUS_028_ra_005_ABILITYSORA1_SLASH_UPPER: BaseWorldLocationData('Vbonus_028', value=ETresAbilityKind.SLASH_UPPER, label='gameflow_VBONUS_028_ra_005'),
    TresVictoryBonusDataLocation.VBONUS_029_ra_006_BONUSSORA1_DEF_SLOT_UP1: BaseWorldLocationData('Vbonus_029', value=ETresVictoryBonusKind.DEF_SLOT_UP1, label='gameflow_VBONUS_029_ra_006'),
    TresVictoryBonusDataLocation.VBONUS_030_ra_007_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_030', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_030_ra_007')
}


# LOCATION NAMES
KINGDOM_OF_CORONA_HILLS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_001_NAVI_MAP_RA01,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_003_LSIGAME15,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_002_PRT_ITEM28,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_003_PRT_ITEM30,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_004_ACC_ITEM25,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_005_ITEM_ALLCURE,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_006_ITEM_POTION,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_007_ITEM_FOCUSSUPPLY,
    TresVictoryBonusDataLocation.VBONUS_024_ra_001_BONUSSORA1_MELEM_AERO,
    TresVictoryBonusDataLocation.VBONUS_026_ra_003_ABILITYSORA1_GUARD_COUNTER,
    TresVictoryBonusDataLocation.RA_Sub_Pudding_CLEAR_A_ABILITYSORA1_PRIZE_DRAW,
    TresEventDataLocation.RA_BATTLEPORTAL_ex_27_CLEARED_ACC_ITEM43,
    TresEventDataLocation.RA_BATTLEPORTAL_ex_27_CLEARED_REPORT_ITEM07
]

KINGDOM_OF_CORONA_TOWER_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_001_PRT_ITEM47,
    TresVictoryBonusDataLocation.VBONUS_029_ra_006_BONUSSORA1_DEF_SLOT_UP1,
    TresVictoryBonusDataLocation.VBONUS_030_ra_007_BONUSSORA1_HP_UP10,
    TresEventDataLocation.RA_END
]

KINGDOM_OF_CORONA_MARSH_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_002_NAVI_MAP_RA02,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_008_ITEM_POTION,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_009_PRT_ITEM41,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_010_ACC_ITEM34,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_011_PRT_ITEM04,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_012_MAT_ITEM54,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_013_MAT_ITEM34,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_014_ITEM_ETHER,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_015_MAT_ITEM54
]

KINGDOM_OF_CORONA_CAMPSITE_LOCATIONS: list[str] = [

]

KINGDOM_OF_CORONA_WETLANDS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_006_ACC_ITEM43,
    TresVictoryBonusDataLocation.VBONUS_027_ra_004_BONUSSORA1_MP_UP5,
    TresVictoryBonusDataLocation.VBONUS_027_ra_004_ABILITYSORA1_SUPERJUMP,
    TresEventDataLocation.RA_BATTLEPORTAL_ex_26_CLEARED_MAT_ITEM60,
    TresEventDataLocation.RA_BATTLEPORTAL_ex_26_CLEARED_REPORT_ITEM06
]

KINGDOM_OF_CORONA_WILDFLOWER_CLEARING_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_004_LSIGAME18,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_017_ITEM_HIGHETHER
]

KINGDOM_OF_CORONA_SHORE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_016_ITEM_APUP
]

KINGDOM_OF_CORONA_THOROUGHFARE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KINGDOM_OF_CORONA_LARGE_TREASURE_005_LSIGAME09,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_018_ITEM_MAGICUP,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_019_ITEM_ETHER,
    TresVictoryBonusDataLocation.RA_AfterDance_CLEAR_A_ABILITYSORA1_UNISON_THUNDER
]

KINGDOM_OF_CORONA_WHARF_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_020_FOOD_ITEM41,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_021_ACC_ITEM18,
    TresTreasureDataLocation.KINGDOM_OF_CORONA_SMALL_TREASURE_022_ITEM_HIGHPOTION,
    TresVictoryBonusDataLocation.VBONUS_028_ra_005_ABILITYSORA1_SLASH_UPPER
]
