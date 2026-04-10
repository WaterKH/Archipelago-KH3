from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefBattleItem, ETresItemDefCampItem, ETresItemDefKeyItem, ETresItemDefLSIGameItem, ETresItemDefMaterial, ETresItemDefNavimap, ETresItemDefProtector, ETresAbilityKind, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_001_NAVI_MAP_CA01: BaseWorldLocationData('CA_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_CA01),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_002_NAVI_MAP_CA04: BaseWorldLocationData('CA_LBOX_002', value=ETresItemDefNavimap.NAVI_MAP_CA04),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_003_NAVI_MAP_CA03: BaseWorldLocationData('CA_LBOX_003', value=ETresItemDefNavimap.NAVI_MAP_CA03),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_004_NAVI_MAP_CA05: BaseWorldLocationData('CA_LBOX_004', value=ETresItemDefNavimap.NAVI_MAP_CA05),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_005_NAVI_MAP_CA02: BaseWorldLocationData('CA_LBOX_005', value=ETresItemDefNavimap.NAVI_MAP_CA02),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_006_LSIGAME11: BaseWorldLocationData('CA_LBOX_006', value=ETresItemDefLSIGameItem.LSIGAME11),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_007_LSIGAME08: BaseWorldLocationData('CA_LBOX_007', value=ETresItemDefLSIGameItem.LSIGAME08),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_008_LSIGAME21: BaseWorldLocationData('CA_LBOX_008', value=ETresItemDefLSIGameItem.LSIGAME21),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_009_LSIGAME17: BaseWorldLocationData('CA_LBOX_009', value=ETresItemDefLSIGameItem.LSIGAME17),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_010_KEY_ITEM10: BaseWorldLocationData('CA_LBOX_010', value=ETresItemDefKeyItem.KEY_ITEM10),
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_011_ACC_ITEM23: BaseWorldLocationData('CA_LBOX_011', value=ETresItemDefAccessory.ACC_ITEM23),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_001_ITEM_HIGHFOCUSSUPPLY: BaseWorldLocationData('CA_SBOX_001', value=ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_002_ACC_ITEM20: BaseWorldLocationData('CA_SBOX_002', value=ETresItemDefAccessory.ACC_ITEM20),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_003_ITEM_HIGHPOTION: BaseWorldLocationData('CA_SBOX_003', value=ETresItemDefBattleItem.ITEM_HIGHPOTION),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_004_ITEM_MEGAETHER: BaseWorldLocationData('CA_SBOX_004', value=ETresItemDefBattleItem.ITEM_MEGAETHER),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_005_ITEM_TENT: BaseWorldLocationData('CA_SBOX_005', value=ETresItemDefCampItem.ITEM_TENT),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_006_ITEM_HIGHETHER: BaseWorldLocationData('CA_SBOX_006', value=ETresItemDefBattleItem.ITEM_HIGHETHER),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_007_ITEM_ELIXIR: BaseWorldLocationData('CA_SBOX_007', value=ETresItemDefBattleItem.ITEM_ELIXIR),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_008_ITEM_MEGAPOTION: BaseWorldLocationData('CA_SBOX_008', value=ETresItemDefBattleItem.ITEM_MEGAPOTION),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_009_ITEM_ETHER: BaseWorldLocationData('CA_SBOX_008', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_010_ACC_ITEM10: BaseWorldLocationData('CA_SBOX_010', value=ETresItemDefAccessory.ACC_ITEM10),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_011_MAT_ITEM55: BaseWorldLocationData('CA_SBOX_011', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_012_MAT_ITEM56: BaseWorldLocationData('CA_SBOX_012', value=ETresItemDefMaterial.MAT_ITEM56),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_013_MAT_ITEM54: BaseWorldLocationData('CA_SBOX_013', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_014_ACC_ITEM38: BaseWorldLocationData('CA_SBOX_014', value=ETresItemDefAccessory.ACC_ITEM38),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_015_ITEM_MEGAETHER: BaseWorldLocationData('CA_SBOX_015', value=ETresItemDefBattleItem.ITEM_MEGAETHER),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_016_MAT_ITEM58: BaseWorldLocationData('CA_SBOX_016', value=ETresItemDefMaterial.MAT_ITEM58),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_017_MAT_ITEM58: BaseWorldLocationData('CA_SBOX_017', value=ETresItemDefMaterial.MAT_ITEM58),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_018_MAT_ITEM57: BaseWorldLocationData('CA_SBOX_018', value=ETresItemDefMaterial.MAT_ITEM57),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_019_ACC_ITEM46: BaseWorldLocationData('CA_SBOX_019', value=ETresItemDefAccessory.ACC_ITEM46),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_020_PRT_ITEM34: BaseWorldLocationData('CA_SBOX_020', value=ETresItemDefProtector.PRT_ITEM34),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_021_ITEM_ALLCURE: BaseWorldLocationData('CA_SBOX_021', value=ETresItemDefBattleItem.ITEM_ALLCURE),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_022_ITEM_MEGAPOTION: BaseWorldLocationData('CA_SBOX_022', value=ETresItemDefBattleItem.ITEM_MEGAPOTION),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_023_PRT_ITEM49: BaseWorldLocationData('CA_SBOX_023', value=ETresItemDefProtector.PRT_ITEM49),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_024_MAT_ITEM55: BaseWorldLocationData('CA_SBOX_024', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_025_ACC_ITEM45: BaseWorldLocationData('CA_SBOX_025', value=ETresItemDefAccessory.ACC_ITEM45),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_026_MAT_ITEM56: BaseWorldLocationData('CA_SBOX_026', value=ETresItemDefMaterial.MAT_ITEM56),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_027_MAT_ITEM52: BaseWorldLocationData('CA_SBOX_027', value=ETresItemDefMaterial.MAT_ITEM52),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_028_MAT_ITEM55: BaseWorldLocationData('CA_SBOX_028', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_029_MAT_ITEM54: BaseWorldLocationData('CA_SBOX_029', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_030_MAT_ITEM56: BaseWorldLocationData('CA_SBOX_030', value=ETresItemDefMaterial.MAT_ITEM56),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_031_MAT_ITEM55: BaseWorldLocationData('CA_SBOX_031', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_032_MAT_ITEM58: BaseWorldLocationData('CA_SBOX_032', value=ETresItemDefMaterial.MAT_ITEM58),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_033_MAT_ITEM55: BaseWorldLocationData('CA_SBOX_033', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_034_MAT_ITEM56: BaseWorldLocationData('CA_SBOX_034', value=ETresItemDefMaterial.MAT_ITEM56),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_035_WEP_GOOFY_09: BaseWorldLocationData('CA_SBOX_035', value=ETresItemDefWeapon.WEP_GOOFY_09),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_036_MAT_ITEM58: BaseWorldLocationData('CA_SBOX_036', value=ETresItemDefMaterial.MAT_ITEM58),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_037_MAT_ITEM56: BaseWorldLocationData('CA_SBOX_037', value=ETresItemDefMaterial.MAT_ITEM56),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_038_MAT_ITEM55: BaseWorldLocationData('CA_SBOX_038', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_039_MAT_ITEM58: BaseWorldLocationData('CA_SBOX_039', value=ETresItemDefMaterial.MAT_ITEM58),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_040_MAT_ITEM55: BaseWorldLocationData('CA_SBOX_040', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_041_MAT_ITEM52: BaseWorldLocationData('CA_SBOX_041', value=ETresItemDefMaterial.MAT_ITEM52),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_042_MAT_ITEM54: BaseWorldLocationData('CA_SBOX_042', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_043_PRT_ITEM12: BaseWorldLocationData('CA_SBOX_043', value=ETresItemDefMaterial.MAT_ITEM12),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_044_PRT_ITEM17: BaseWorldLocationData('CA_SBOX_044', value=ETresItemDefMaterial.MAT_ITEM17),
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_045_PRT_ITEM25: BaseWorldLocationData('CA_SBOX_045', value=ETresItemDefMaterial.MAT_ITEM25),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.CA_BATTLEPORTAL_ex_33_CLEARED_ACC_ITEM40: BaseWorldLocationData('CA_BATTLEPORTAL_ex_33_CLEARED_ACC_ITEM40', value=ETresItemDefAccessory.ACC_ITEM40, label='global_BATTLEPORTAL_ex_33_CLEARED'),
    TresEventDataLocation.CA_BATTLEPORTAL_ex_33_CLEARED_REPORT_ITEM10: BaseWorldLocationData('CA_BATTLEPORTAL_ex_33_CLEARED_REPORT_ITEM10', value=ETresItemDefReport.REPORT_ITEM10, label='global_BATTLEPORTAL_ex_33_CLEARED'),
    TresEventDataLocation.CA_END: BaseWorldLocationData('gameflow_CA', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_09, label='CA_END'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_058_ca_001_ABILITYSORA1_REVENGEDIVE: BaseWorldLocationData('Vbonus_058', value=ETresAbilityKind.REVENGEDIVE, label='gameflow_VBONUS_058_ca_001'),
    TresVictoryBonusDataLocation.VBONUS_060_ca_003_ABILITYSORA1_AIRSLIDE: BaseWorldLocationData('Vbonus_060', value=ETresAbilityKind.AIRSLIDE, label='gameflow_VBONUS_060_ca_003'),
    TresVictoryBonusDataLocation.VBONUS_061_ca_004_BONUSSORA1_MELEM_THUNDER: BaseWorldLocationData('Vbonus_061', value=ETresVictoryBonusKind.MELEM_THUNDER, label='gameflow_VBONUS_061_ca_004'),
    TresVictoryBonusDataLocation.VBONUS_062_ca_005_BONUSSORA1_ITEM_SLOT_UP1: BaseWorldLocationData('Vbonus_062', value=ETresVictoryBonusKind.ITEM_SLOT_UP1, label='gameflow_VBONUS_062_ca_005'),
    TresVictoryBonusDataLocation.VBONUS_063_ca_006_ABILITYSORA1_MAGICFLUSH: BaseWorldLocationData('Vbonus_063', value=ETresAbilityKind.MAGICFLUSH, label='gameflow_VBONUS_063_ca_006'),
    TresVictoryBonusDataLocation.VBONUS_064_ca_007_BONUSSORA1_MELEM_WATER: BaseWorldLocationData('Vbonus_064', value=ETresVictoryBonusKind.MELEM_WATER, label='gameflow_VBONUS_064_ca_007'),
    TresVictoryBonusDataLocation.VBONUS_066_ca_009_ABILITYSORA1_BLOW_COUNTER: BaseWorldLocationData('Vbonus_066a', value=ETresAbilityKind.BLOW_COUNTER, label='gameflow_VBONUS_066_ca_009'),
    TresVictoryBonusDataLocation.VBONUS_066_ca_009_BONUSSORA2_HP_UP10: BaseWorldLocationData('Vbonus_066b', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_066_ca_009'),
    TresVictoryBonusDataLocation.CA_Sub_Pudding_CLEAR_A_ABILITYSORA1_FOCUS_ASPIR: BaseWorldLocationData('VBonus_Minigame012', value=ETresAbilityKind.FOCUS_ASPIR, label='gameflow_CA_Sub_Pudding_CLEAR_A')
}


# LOCATION NAMES
THE_CARIBBEAN_DAVY_JONES_LOCKER_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_058_ca_001_ABILITYSORA1_REVENGEDIVE
]

THE_CARIBBEAN_THE_HIGH_SEAS_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_060_ca_003_ABILITYSORA1_AIRSLIDE,
    TresVictoryBonusDataLocation.VBONUS_062_ca_005_BONUSSORA1_ITEM_SLOT_UP1,
    TresVictoryBonusDataLocation.VBONUS_063_ca_006_ABILITYSORA1_MAGICFLUSH,
    TresVictoryBonusDataLocation.VBONUS_064_ca_007_BONUSSORA1_MELEM_WATER
]

THE_CARIBBEAN_ISLA_DE_LOS_MASTILES_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_002_NAVI_MAP_CA04,
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_011_ACC_ITEM23,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_023_PRT_ITEM49,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_024_MAT_ITEM55
]

THE_CARIBBEAN_SHIPS_END_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_003_NAVI_MAP_CA03,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_014_ACC_ITEM38,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_015_ITEM_MEGAETHER
]

THE_CARIBBEAN_SANDBAR_ISLE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_004_NAVI_MAP_CA05,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_017_MAT_ITEM58,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_027_MAT_ITEM52,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_028_MAT_ITEM55,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_029_MAT_ITEM54,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_030_MAT_ITEM56,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_031_MAT_ITEM55,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_032_MAT_ITEM58,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_033_MAT_ITEM55,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_034_MAT_ITEM56,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_035_WEP_GOOFY_09,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_036_MAT_ITEM58,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_037_MAT_ITEM56,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_038_MAT_ITEM55,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_039_MAT_ITEM58,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_040_MAT_ITEM55,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_041_MAT_ITEM52
]

THE_CARIBBEAN_HUDDLED_ISLES_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_005_NAVI_MAP_CA02,
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_007_LSIGAME08,
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_010_KEY_ITEM10,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_010_ACC_ITEM10,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_011_MAT_ITEM55,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_012_MAT_ITEM56,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_013_MAT_ITEM54,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_021_ITEM_ALLCURE,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_022_ITEM_MEGAPOTION,
    TresVictoryBonusDataLocation.VBONUS_061_ca_004_BONUSSORA1_MELEM_THUNDER,
    TresEventDataLocation.CA_BATTLEPORTAL_ex_33_CLEARED_ACC_ITEM40,
    TresEventDataLocation.CA_BATTLEPORTAL_ex_33_CLEARED_REPORT_ITEM10
]

THE_CARIBBEAN_LEVIATHAN_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_025_ACC_ITEM45
]

THE_CARIBBEAN_PORT_ROYAL_SEAPORT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_002_ACC_ITEM20,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_003_ITEM_HIGHPOTION,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_004_ITEM_MEGAETHER,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_009_ITEM_ETHER
]

THE_CARIBBEAN_PORT_ROYAL_DOCKS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_001_NAVI_MAP_CA01,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_006_ITEM_HIGHETHER
]

THE_CARIBBEAN_PORT_ROYAL_SETTLEMENT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_005_ITEM_TENT,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_008_ITEM_MEGAPOTION
]

THE_CARIBBEAN_PORT_ROYAL_FORT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_006_LSIGAME11,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_001_ITEM_HIGHFOCUSSUPPLY,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_007_ITEM_ELIXIR,
    TresVictoryBonusDataLocation.CA_Sub_Pudding_CLEAR_A_ABILITYSORA1_FOCUS_ASPIR
]

THE_CARIBBEAN_PORT_ROYAL_WATERS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_019_ACC_ITEM46
]

THE_CARIBBEAN_ISLA_VERDEMONTANA_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_008_LSIGAME21,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_016_MAT_ITEM58,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_026_MAT_ITEM56
]

THE_CARIBBEAN_EXILE_ISLAND_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_018_MAT_ITEM57
]

THE_CARIBBEAN_CONFINEMENT_ISLE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_LARGE_TREASURE_009_LSIGAME17
]

THE_CARIBBEAN_HORSESHOE_ISLAND_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_020_PRT_ITEM34,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_042_MAT_ITEM54,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_043_PRT_ITEM12,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_044_PRT_ITEM17,
    TresTreasureDataLocation.THE_CARIBBEAN_SMALL_TREASURE_045_PRT_ITEM25
]

THE_CARIBBEAN_BOSS_ARENA_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_066_ca_009_ABILITYSORA1_BLOW_COUNTER,
    TresVictoryBonusDataLocation.VBONUS_066_ca_009_BONUSSORA2_HP_UP10,
    TresEventDataLocation.CA_END
]