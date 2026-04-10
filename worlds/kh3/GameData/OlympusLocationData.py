from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefBattleItem, ETresItemDefCampItem, ETresItemDefKeyItem, ETresItemDefMaterial, ETresItemDefProtector, ETresItemDefNavimap, ETresAbilityKind, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.OLYMPUS_LARGE_TREASURE_001_NAVI_MAP_HE01: BaseWorldLocationData('HE_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_HE01),
    TresTreasureDataLocation.OLYMPUS_LARGE_TREASURE_002_NAVI_MAP_HE02: BaseWorldLocationData('HE_LBOX_002', value=ETresItemDefNavimap.NAVI_MAP_HE02),
    TresTreasureDataLocation.OLYMPUS_LARGE_TREASURE_003_ITEM_ELIXIR: BaseWorldLocationData('HE_LBOX_003', value=ETresItemDefBattleItem.ITEM_ELIXIR),
    TresTreasureDataLocation.OLYMPUS_LARGE_TREASURE_004_NAVI_MAP_HE03: BaseWorldLocationData('HE_LBOX_004', value=ETresItemDefNavimap.NAVI_MAP_HE03),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_001_MAT_ITEM53: BaseWorldLocationData('HE_SBOX_001', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_002_ITEM_FOCUSSUPPLY: BaseWorldLocationData('HE_SBOX_002', value=ETresItemDefBattleItem.ITEM_FOCUSSUPPLY),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_003_ITEM_POTION: BaseWorldLocationData('HE_SBOX_003', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_004_MAT_ITEM33: BaseWorldLocationData('HE_SBOX_004', value=ETresItemDefMaterial.MAT_ITEM33),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_005_ITEM_FOCUSSUPPLY: BaseWorldLocationData('HE_SBOX_005', value=ETresItemDefBattleItem.ITEM_FOCUSSUPPLY),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_006_ITEM_POTION: BaseWorldLocationData('HE_SBOX_006', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_007_ACC_ITEM12: BaseWorldLocationData('HE_SBOX_007', value=ETresItemDefAccessory.ACC_ITEM12),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_008_ACC_ITEM40: BaseWorldLocationData('HE_SBOX_008', value=ETresItemDefAccessory.ACC_ITEM40),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_009_ITEM_POTION: BaseWorldLocationData('HE_SBOX_009', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_010_ITEM_ALLCURE: BaseWorldLocationData('HE_SBOX_010', value=ETresItemDefBattleItem.ITEM_ALLCURE),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_011_ACC_ITEM03: BaseWorldLocationData('HE_SBOX_011', value=ETresItemDefAccessory.ACC_ITEM03),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_012_ACC_ITEM22: BaseWorldLocationData('HE_SBOX_012', value=ETresItemDefAccessory.ACC_ITEM22),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_013_ITEM_POTION: BaseWorldLocationData('HE_SBOX_013', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_014_ITEM_APUP: BaseWorldLocationData('HE_SBOX_014', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_015_ITEM_APUP: BaseWorldLocationData('HE_SBOX_015', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_016_MAT_ITEM53: BaseWorldLocationData('HE_SBOX_016', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_017_ITEM_HIGHETHER: BaseWorldLocationData('HE_SBOX_017', value=ETresItemDefBattleItem.ITEM_HIGHETHER),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_018_ITEM_APUP: BaseWorldLocationData('HE_SBOX_018', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_019_ITEM_POTION: BaseWorldLocationData('HE_SBOX_019', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_020_MAT_ITEM53: BaseWorldLocationData('HE_SBOX_020', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_021_ITEM_ETHER: BaseWorldLocationData('HE_SBOX_021', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_022_ITEM_MEGAPOTION: BaseWorldLocationData('HE_SBOX_022', value=ETresItemDefBattleItem.ITEM_MEGAPOTION),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_023_ACC_ITEM17: BaseWorldLocationData('HE_SBOX_023', value=ETresItemDefAccessory.ACC_ITEM17),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_024_ITEM_ETHER: BaseWorldLocationData('HE_SBOX_024', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_025_PRT_ITEM03: BaseWorldLocationData('HE_SBOX_025', value=ETresItemDefProtector.PRT_ITEM03),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_026_ITEM_POTION: BaseWorldLocationData('HE_SBOX_026', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_027_ITEM_APUP: BaseWorldLocationData('HE_SBOX_027', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_028_ITEM_POTION: BaseWorldLocationData('HE_SBOX_028', value=ETresItemDefBattleItem.ITEM_POTION),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.HE_HEV_FACTORY: BaseWorldLocationData('gameflow_HE_HEV_FACTORY', value=ETresItemDefWeapon.WEP_GOOFY_01, label='gameflow_HE_HEV_FACTORY'),
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_01: BaseWorldLocationData('gameflow_HE_Sub_Got_GoldenHeracules_01', value=ETresItemDefKeyItem.KEY_ITEM11, label='gameflow_HE_Sub_Got_GoldenHeracules_01'),
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_02: BaseWorldLocationData('gameflow_HE_Sub_Got_GoldenHeracules_02', value=ETresItemDefKeyItem.KEY_ITEM11, label='gameflow_HE_Sub_Got_GoldenHeracules_02'),
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_03: BaseWorldLocationData('gameflow_HE_Sub_Got_GoldenHeracules_03', value=ETresItemDefKeyItem.KEY_ITEM11, label='gameflow_HE_Sub_Got_GoldenHeracules_03'),
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_04: BaseWorldLocationData('gameflow_HE_Sub_Got_GoldenHeracules_04', value=ETresItemDefKeyItem.KEY_ITEM11, label='gameflow_HE_Sub_Got_GoldenHeracules_04'),
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_05: BaseWorldLocationData('gameflow_HE_Sub_Got_GoldenHeracules_05', value=ETresItemDefKeyItem.KEY_ITEM11, label='gameflow_HE_Sub_Got_GoldenHeracules_05'),
    TresEventDataLocation.HE_Sub_HeraculesBoy_End: BaseWorldLocationData('gameflow_HE_Sub_HeraculesBoy', value=ETresItemDefProtector.PRT_ITEM01, label='HE_Sub_HeraculesBoy_End'),
    TresEventDataLocation.HE_BATTLEPORTAL_ex_21_CLEARED_ACC_ITEM42: BaseWorldLocationData('HE_BATTLEPORTAL_ex_21_CLEARED_ACC_ITEM42', value=ETresItemDefAccessory.ACC_ITEM42, label='global_BATTLEPORTAL_ex_21_CLEARED'),
    TresEventDataLocation.HE_BATTLEPORTAL_ex_21_CLEARED_REPORT_ITEM01: BaseWorldLocationData('HE_BATTLEPORTAL_ex_21_CLEARED_REPORT_ITEM01', value=ETresItemDefReport.REPORT_ITEM01, label='global_BATTLEPORTAL_ex_21_CLEARED'),
    TresEventDataLocation.HE_BATTLEPORTAL_ex_22_CLEARED_PRT_ITEM10: BaseWorldLocationData('global_BATTLEPORTAL_ex_22_CLEARED_PRT_ITEM10', value=ETresItemDefProtector.PRT_ITEM10, label='global_BATTLEPORTAL_ex_22_CLEARED'),
    TresEventDataLocation.HE_BATTLEPORTAL_ex_22_CLEARED_REPORT_ITEM02: BaseWorldLocationData('global_BATTLEPORTAL_ex_22_CLEARED_REPORT_ITEM02', value=ETresItemDefReport.REPORT_ITEM02, label='global_BATTLEPORTAL_ex_22_CLEARED'),
    TresEventDataLocation.HE_END: BaseWorldLocationData('gameflow_HE', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_01, label='HE_END'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_001_he_001_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_001', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_001_he_001'),
    TresVictoryBonusDataLocation.VBONUS_005_he_005_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_005', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_005_he_005'),
    TresVictoryBonusDataLocation.VBONUS_006_he_006_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_006', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_006_he_006'),
    TresVictoryBonusDataLocation.VBONUS_008_he_008_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_008', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_008_he_008'),
    TresVictoryBonusDataLocation.VBONUS_010_he_010_BONUSSORA1_MP_UP5: BaseWorldLocationData('Vbonus_010', value=ETresVictoryBonusKind.MP_UP5, label='gameflow_VBONUS_010_he_010'),
    TresVictoryBonusDataLocation.VBONUS_013_he_013_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_013', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_013_he_013'),
    TresVictoryBonusDataLocation.HE_Sub_Pudding_CLEAR_A_ABILITYSORA1_FORM_TIME: BaseWorldLocationData('VBonus_Minigame007', value=ETresAbilityKind.FORM_TIME, label='gameflow_HE_Sub_Pudding_CLEAR_A')
}


# LOCATION NAMES
OLYMPUS_RAVINE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_007_ACC_ITEM12,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_008_ACC_ITEM40
]

OLYMPUS_CLIFF_ASCENT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_LARGE_TREASURE_001_NAVI_MAP_HE01,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_009_ITEM_POTION,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_010_ITEM_ALLCURE,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_011_ACC_ITEM03,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_012_ACC_ITEM22,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_013_ITEM_POTION,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_014_ITEM_APUP
]

OLYMPUS_MOUNTAINSIDE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_015_ITEM_APUP,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_017_ITEM_HIGHETHER
]

OLYMPUS_SUMMIT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_016_MAT_ITEM53,
    TresVictoryBonusDataLocation.VBONUS_010_he_010_BONUSSORA1_MP_UP5
]

OLYMPUS_ALLEYWAY_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_018_ITEM_APUP,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_019_ITEM_POTION,
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_05
]

OLYMPUS_AGORA_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_020_MAT_ITEM53,
    TresVictoryBonusDataLocation.VBONUS_001_he_001_BONUSSORA1_HP_UP10,
    TresVictoryBonusDataLocation.VBONUS_008_he_008_BONUSSORA1_HP_UP10,
    TresEventDataLocation.HE_Sub_HeraculesBoy_End
]

OLYMPUS_THE_BIG_OLIVE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_021_ITEM_ETHER,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_022_ITEM_MEGAPOTION
]

OLYMPUS_GARDENS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_023_ACC_ITEM17,
    TresVictoryBonusDataLocation.VBONUS_006_he_006_BONUSSORA1_HP_UP10,
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_03,
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_04
]

OLYMPUS_OVERLOOK_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_LARGE_TREASURE_002_NAVI_MAP_HE02,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_024_ITEM_ETHER,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_025_PRT_ITEM03,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_026_ITEM_POTION,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_027_ITEM_APUP,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_028_ITEM_POTION,
    TresVictoryBonusDataLocation.VBONUS_005_he_005_BONUSSORA1_HP_UP10,
    TresVictoryBonusDataLocation.HE_Sub_Pudding_CLEAR_A_ABILITYSORA1_FORM_TIME,
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_01,
    TresEventDataLocation.HE_Sub_Got_GoldenHeracules_02
]

OLYMPUS_COURTYARD_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_001_MAT_ITEM53,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_002_ITEM_FOCUSSUPPLY,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_003_ITEM_POTION,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_004_MAT_ITEM33
]

OLYMPUS_CLOUD_RIDGE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_005_ITEM_FOCUSSUPPLY
]

OLYMPUS_CORRIDORS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.OLYMPUS_LARGE_TREASURE_003_ITEM_ELIXIR,
    TresTreasureDataLocation.OLYMPUS_LARGE_TREASURE_004_NAVI_MAP_HE03,
    TresTreasureDataLocation.OLYMPUS_SMALL_TREASURE_006_ITEM_POTION,
    TresEventDataLocation.HE_HEV_FACTORY,
    TresEventDataLocation.HE_BATTLEPORTAL_ex_21_CLEARED_ACC_ITEM42,
    TresEventDataLocation.HE_BATTLEPORTAL_ex_21_CLEARED_REPORT_ITEM01,
    TresEventDataLocation.HE_BATTLEPORTAL_ex_22_CLEARED_PRT_ITEM10,
    TresEventDataLocation.HE_BATTLEPORTAL_ex_22_CLEARED_REPORT_ITEM02
]

OLYMPUS_BOSS_ARENA_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_013_he_013_BONUSSORA1_HP_UP10,
    TresEventDataLocation.HE_BATTLEPORTAL_ex_22_CLEARED_PRT_ITEM10,
    TresEventDataLocation.HE_BATTLEPORTAL_ex_22_CLEARED_REPORT_ITEM02,
    TresEventDataLocation.HE_END
]