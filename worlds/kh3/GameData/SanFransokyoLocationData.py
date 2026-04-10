from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefBattleItem, ETresItemDefCampItem, ETresItemDefKeyItem, ETresItemDefLSIGameItem, ETresItemDefMaterial, ETresItemDefProtector, ETresItemDefNavimap, ETresAbilityKind, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.SAN_FRANSOKYO_LARGE_TREASURE_001_NAVI_MAP_BX01: BaseWorldLocationData('BX_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_BX01),
    TresTreasureDataLocation.SAN_FRANSOKYO_LARGE_TREASURE_005_LSIGAME19: BaseWorldLocationData('BX_LBOX_005', value=ETresItemDefLSIGameItem.LSIGAME19),
    TresTreasureDataLocation.SAN_FRANSOKYO_LARGE_TREASURE_006_LSIGAME12: BaseWorldLocationData('BX_LBOX_006', value=ETresItemDefLSIGameItem.LSIGAME12),
    TresTreasureDataLocation.SAN_FRANSOKYO_LARGE_TREASURE_007_LSIGAME23: BaseWorldLocationData('BX_LBOX_007', value=ETresItemDefLSIGameItem.LSIGAME23),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_001_PRT_ITEM33: BaseWorldLocationData('BX_SBOX_001', value=ETresItemDefProtector.PRT_ITEM33),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_002_ACC_ITEM08: BaseWorldLocationData('BX_SBOX_002', value=ETresItemDefAccessory.ACC_ITEM08),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_003_ITEM_HIGHFOCUSSUPPLY: BaseWorldLocationData('BX_SBOX_003', value=ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_004_ITEM_APUP: BaseWorldLocationData('BX_SBOX_004', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_005_MAT_ITEM58: BaseWorldLocationData('BX_SBOX_005', value=ETresItemDefMaterial.MAT_ITEM58),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_006_ACC_ITEM15: BaseWorldLocationData('BX_SBOX_006', value=ETresItemDefAccessory.ACC_ITEM15),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_007_ITEM_APUP: BaseWorldLocationData('BX_SBOX_007', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_008_ITEM_MEGAETHER: BaseWorldLocationData('BX_SBOX_008', value=ETresItemDefBattleItem.ITEM_MEGAETHER),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_009_MAT_ITEM55: BaseWorldLocationData('BX_SBOX_009', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_010_ITEM_MEGAPOTION: BaseWorldLocationData('BX_SBOX_010', value=ETresItemDefBattleItem.ITEM_MEGAPOTION),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_011_PRT_ITEM20: BaseWorldLocationData('BX_SBOX_011', value=ETresItemDefProtector.PRT_ITEM20),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_012_ITEM_ELIXIR: BaseWorldLocationData('BX_SBOX_012', value=ETresItemDefBattleItem.ITEM_ELIXIR),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_013_PRT_ITEM31: BaseWorldLocationData('BX_SBOX_013', value=ETresItemDefProtector.PRT_ITEM31),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_014_ITEM_APUP: BaseWorldLocationData('BX_SBOX_014', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_015_ITEM_MAGICUP: BaseWorldLocationData('BX_SBOX_015', value=ETresItemDefCampItem.ITEM_MAGICUP),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_016_ITEM_HIGHETHER: BaseWorldLocationData('BX_SBOX_016', value=ETresItemDefBattleItem.ITEM_HIGHETHER),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_017_ITEM_MEGAETHER: BaseWorldLocationData('BX_SBOX_017', value=ETresItemDefBattleItem.ITEM_MEGAETHER),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_018_WEP_DONALD_07: BaseWorldLocationData('BX_SBOX_018', value=ETresItemDefWeapon.WEP_DONALD_07),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_019_ITEM_APUP: BaseWorldLocationData('BX_SBOX_019', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_020_MAT_ITEM54: BaseWorldLocationData('BX_SBOX_020', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_021_MAT_ITEM55: BaseWorldLocationData('BX_SBOX_021', value=ETresItemDefMaterial.MAT_ITEM55),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_022_PRT_ITEM27: BaseWorldLocationData('BX_SBOX_022', value=ETresItemDefProtector.PRT_ITEM27),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_023_ITEM_HIGHFOCUSSUPPLY: BaseWorldLocationData('BX_SBOX_023', value=ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_024_ACC_ITEM37: BaseWorldLocationData('BX_SBOX_024', value=ETresItemDefAccessory.ACC_ITEM37),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_025_MAT_ITEM58: BaseWorldLocationData('BX_SBOX_025', value=ETresItemDefMaterial.MAT_ITEM58),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_026_PRT_ITEM07: BaseWorldLocationData('BX_SBOX_026', value=ETresItemDefProtector.PRT_ITEM07),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_027_ITEM_MAGICUP: BaseWorldLocationData('BX_SBOX_027', value=ETresItemDefCampItem.ITEM_MAGICUP),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_028_ITEM_POWERUP: BaseWorldLocationData('BX_SBOX_028', value=ETresItemDefCampItem.ITEM_POWERUP),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_029_PRT_ITEM24: BaseWorldLocationData('BX_SBOX_029', value=ETresItemDefProtector.PRT_ITEM24),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_030_ITEM_MEGAPOTION: BaseWorldLocationData('BX_SBOX_030', value=ETresItemDefBattleItem.ITEM_MEGAPOTION),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_031_MAT_ITEM54: BaseWorldLocationData('BX_SBOX_031', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_032_ITEM_APUP: BaseWorldLocationData('BX_SBOX_032', value=ETresItemDefCampItem.ITEM_APUP),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.BX_BRIDGE_MISSION1: BaseWorldLocationData('gameflow_BX', value=ETresItemDefKeyItem.KEY_ITEM03, label='BX_BRIDGE_MISSION1'), # TODO: Double check this label... may be incorrect
    TresEventDataLocation.BX_SAVE_FRIENDS: BaseWorldLocationData('gameflow_BX', value=ETresItemDefProtector.PRT_ITEM02, label='BX_CENTRAL_EVENT5'), # TODO: Double check this label... may be incorrect
    TresEventDataLocation.BX_BATTLEPORTAL_ex_34_CLEARED_ACC_ITEM46: BaseWorldLocationData('BX_BATTLEPORTAL_ex_34_CLEARED_ACC_ITEM46', value=ETresItemDefAccessory.ACC_ITEM46, label='global_BATTLEPORTAL_ex_35_CLEARED'),
    TresEventDataLocation.BX_BATTLEPORTAL_ex_34_CLEARED_REPORT_ITEM11: BaseWorldLocationData('BX_BATTLEPORTAL_ex_34_CLEARED_REPORT_ITEM11', value=ETresItemDefReport.REPORT_ITEM11, label='global_BATTLEPORTAL_ex_35_CLEARED'),
    TresEventDataLocation.BX_BATTLEPORTAL_ex_35_CLEARED_ACC_ITEM44: BaseWorldLocationData('BX_BATTLEPORTAL_ex_35_CLEARED_ACC_ITEM44', value=ETresItemDefAccessory.ACC_ITEM44, label='global_BATTLEPORTAL_ex_36_CLEARED'),
    TresEventDataLocation.BX_BATTLEPORTAL_ex_35_CLEARED_REPORT_ITEM12: BaseWorldLocationData('BX_BATTLEPORTAL_ex_36_CLEARED_REPORT_ITEM12', value=ETresItemDefReport.REPORT_ITEM12, label='global_BATTLEPORTAL_ex_36_CLEARED'),
    TresEventDataLocation.BX_END: BaseWorldLocationData('gameflow_BX', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_08, label='BX_END'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_052_bx_002_ABILITYSORA1_FOCUS_ASPIR: BaseWorldLocationData('Vbonus_052', value=ETresAbilityKind.FOCUS_ASPIR, label='gameflow_VBONUS_052_bx_002'),
    TresVictoryBonusDataLocation.VBONUS_054_bx_004_BONUSSORA1_MELEM_FIRE: BaseWorldLocationData('Vbonus_054', value=ETresVictoryBonusKind.MELEM_FIRE, label='gameflow_VBONUS_054_bx_004'),
    TresVictoryBonusDataLocation.VBONUS_055_bx_005_BONUSSORA1_SUPERSLIDE: BaseWorldLocationData('Vbonus_055', value=ETresAbilityKind.SUPERSLIDE, label='gameflow_VBONUS_055_bx_005'),
    TresVictoryBonusDataLocation.VBONUS_056_bx_006_BONUSSORA1_DEF_SLOT_UP1: BaseWorldLocationData('Vbonus_056', value=ETresVictoryBonusKind.DEF_SLOT_UP1, label='gameflow_VBONUS_056_bx_006'),
    TresVictoryBonusDataLocation.VBONUS_057_bx_007_BONUSSORA1_MELEM_AERO: BaseWorldLocationData('Vbonus_057a', value=ETresVictoryBonusKind.MELEM_AERO, label='gameflow_VBONUS_057_bx_007'),
    TresVictoryBonusDataLocation.VBONUS_057_bx_007_BONUSSORA2_HP_UP10: BaseWorldLocationData('Vbonus_057b', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_057_bx_007'),
    TresVictoryBonusDataLocation.BX_FLASHTRACER_01_RANK_A_ABILITYSORA1_ATTRACTION_UP: BaseWorldLocationData('VBonus_Minigame005', value=ETresAbilityKind.ATTRACTION_UP, label='gameflow_BX_FLASHTRACER_01_RANK_A'),
    TresVictoryBonusDataLocation.BX_FLASHTRACER_02_RANK_A_ABILITYSORA1_MAGIC_TIME: BaseWorldLocationData('VBonus_Minigame006', value=ETresAbilityKind.MAGIC_TIME, label='gameflow_BX_FLASHTRACER_02_RANK_A'),
    TresVictoryBonusDataLocation.BX_Sub_Pudding_CLEAR_A_ABILITYSORA1_ATTRACTION_TIME: BaseWorldLocationData('VBonus_Minigame013', value=ETresAbilityKind.ATTRACTION_TIME, label='gameflow_BX_Sub_Pudding_CLEAR_A'),
}


# LOCATION NAMES
SAN_FRANSOKYO_BRIDGE_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_052_bx_002_ABILITYSORA1_FOCUS_ASPIR
]

SAN_FRANSOKYO_THE_CITY_NORTH_DISTRICT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_004_ITEM_APUP,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_005_MAT_ITEM58,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_009_MAT_ITEM55,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_012_ITEM_ELIXIR,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_013_PRT_ITEM31,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_014_ITEM_APUP,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_018_WEP_DONALD_07,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_021_MAT_ITEM55,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_027_ITEM_MAGICUP,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_028_ITEM_POWERUP,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_031_MAT_ITEM54,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_032_ITEM_APUP,
    TresVictoryBonusDataLocation.BX_FLASHTRACER_02_RANK_A_ABILITYSORA1_MAGIC_TIME,
    TresEventDataLocation.BX_BATTLEPORTAL_ex_34_CLEARED_ACC_ITEM46,
    TresEventDataLocation.BX_BATTLEPORTAL_ex_34_CLEARED_REPORT_ITEM11
]

SAN_FRANSOKYO_THE_CITY_SOUTH_DISTRICT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.SAN_FRANSOKYO_LARGE_TREASURE_001_NAVI_MAP_BX01,
    TresTreasureDataLocation.SAN_FRANSOKYO_LARGE_TREASURE_006_LSIGAME12,
    TresTreasureDataLocation.SAN_FRANSOKYO_LARGE_TREASURE_007_LSIGAME23,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_002_ACC_ITEM08,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_003_ITEM_HIGHFOCUSSUPPLY,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_006_ACC_ITEM15,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_010_ITEM_MEGAPOTION,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_011_PRT_ITEM20,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_017_ITEM_MEGAETHER,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_019_ITEM_APUP,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_020_MAT_ITEM54,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_026_PRT_ITEM07,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_030_ITEM_MEGAPOTION,
    TresVictoryBonusDataLocation.BX_FLASHTRACER_01_RANK_A_ABILITYSORA1_ATTRACTION_UP,
    TresVictoryBonusDataLocation.BX_Sub_Pudding_CLEAR_A_ABILITYSORA1_ATTRACTION_TIME
]

SAN_FRANSOKYO_THE_CITY_CENTRAL_DISTRICT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.SAN_FRANSOKYO_LARGE_TREASURE_005_LSIGAME19,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_001_PRT_ITEM33,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_007_ITEM_APUP,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_008_ITEM_MEGAETHER,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_015_ITEM_MAGICUP,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_016_ITEM_HIGHETHER,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_022_PRT_ITEM27,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_023_ITEM_HIGHFOCUSSUPPLY,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_024_ACC_ITEM37,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_025_MAT_ITEM58,
    TresTreasureDataLocation.SAN_FRANSOKYO_SMALL_TREASURE_029_PRT_ITEM24,
    TresVictoryBonusDataLocation.VBONUS_054_bx_004_BONUSSORA1_MELEM_FIRE,
    TresVictoryBonusDataLocation.VBONUS_055_bx_005_BONUSSORA1_SUPERSLIDE,
    TresVictoryBonusDataLocation.VBONUS_056_bx_006_BONUSSORA1_DEF_SLOT_UP1,
    TresVictoryBonusDataLocation.VBONUS_057_bx_007_BONUSSORA1_MELEM_AERO,
    TresVictoryBonusDataLocation.VBONUS_057_bx_007_BONUSSORA2_HP_UP10,
    TresEventDataLocation.BX_SAVE_FRIENDS,
    TresEventDataLocation.BX_BATTLEPORTAL_ex_35_CLEARED_ACC_ITEM44,
    TresEventDataLocation.BX_BATTLEPORTAL_ex_35_CLEARED_REPORT_ITEM12,
    TresEventDataLocation.BX_END
]
