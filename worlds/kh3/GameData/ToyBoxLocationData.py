from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefBattleItem, ETresItemDefCampItem, ETresItemDefLSIGameItem, ETresItemDefKeyItem, ETresItemDefMaterial, ETresItemDefProtector, ETresItemDefNavimap, ETresAbilityKind, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_001_NAVI_MAP_TS01: BaseWorldLocationData('TS_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_TS01),
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_002_ITEM_ELIXIR: BaseWorldLocationData('TS_LBOX_002', value=ETresItemDefBattleItem.ITEM_ELIXIR),
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_003_NAVI_MAP_TS02: BaseWorldLocationData('TS_LBOX_003', value=ETresItemDefNavimap.NAVI_MAP_TS02),
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_004_LSIGAME16: BaseWorldLocationData('TS_LBOX_004', value=ETresItemDefLSIGameItem.LSIGAME16),
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_005_LSIGAME20: BaseWorldLocationData('TS_LBOX_005', value=ETresItemDefLSIGameItem.LSIGAME20),
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_006_LSIGAME10: BaseWorldLocationData('TS_LBOX_006', value=ETresItemDefLSIGameItem.LSIGAME10),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_001_MAT_ITEM35: BaseWorldLocationData('TS_SBOX_001', value=ETresItemDefMaterial.MAT_ITEM35),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_002_MAT_ITEM53: BaseWorldLocationData('TS_SBOX_002', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_003_PRT_ITEM36: BaseWorldLocationData('TS_SBOX_003', value=ETresItemDefProtector.PRT_ITEM36),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_004_ITEM_POTION: BaseWorldLocationData('TS_SBOX_004', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_005_ITEM_POWERUP: BaseWorldLocationData('TS_SBOX_005', value=ETresItemDefCampItem.ITEM_POWERUP),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_006_ITEM_ETHER: BaseWorldLocationData('TS_SBOX_006', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_007_ACC_ITEM32: BaseWorldLocationData('TS_SBOX_007', value=ETresItemDefAccessory.ACC_ITEM32),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_008_ITEM_FOCUSSUPPLY: BaseWorldLocationData('TS_SBOX_008', value=ETresItemDefBattleItem.ITEM_FOCUSSUPPLY),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_009_ITEM_ETHER: BaseWorldLocationData('TS_SBOX_009', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_010_ACC_ITEM27: BaseWorldLocationData('TS_SBOX_010', value=ETresItemDefAccessory.ACC_ITEM27),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_011_WEP_DONALD_01: BaseWorldLocationData('TS_SBOX_011', value=ETresItemDefWeapon.WEP_DONALD_01),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_012_MAT_ITEM53: BaseWorldLocationData('TS_SBOX_012', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_013_PRT_ITEM11: BaseWorldLocationData('TS_SBOX_013', value=ETresItemDefProtector.PRT_ITEM11),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_014_ITEM_HIGHETHER: BaseWorldLocationData('TS_SBOX_014', value=ETresItemDefBattleItem.ITEM_HIGHETHER),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_015_PRT_ITEM42: BaseWorldLocationData('TS_SBOX_015', value=ETresItemDefProtector.PRT_ITEM42),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_016_ACC_ITEM04: BaseWorldLocationData('TS_SBOX_016', value=ETresItemDefAccessory.ACC_ITEM04),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_017_MAT_ITEM53: BaseWorldLocationData('TS_SBOX_017', value=ETresItemDefMaterial.MAT_ITEM53),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_018_ITEM_POTION: BaseWorldLocationData('TS_SBOX_018', value=ETresItemDefBattleItem.ITEM_POTION),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_019_ACC_ITEM13: BaseWorldLocationData('TS_SBOX_019', value=ETresItemDefAccessory.ACC_ITEM13),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_020_PRT_ITEM19: BaseWorldLocationData('TS_SBOX_020', value=ETresItemDefProtector.PRT_ITEM19),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_021_ACC_ITEM42: BaseWorldLocationData('TS_SBOX_021', value=ETresItemDefAccessory.ACC_ITEM42),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_022_ITEM_HIGHFOCUSSUPPLY: BaseWorldLocationData('TS_SBOX_022', value=ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY),
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_023_MAT_ITEM34: BaseWorldLocationData('TS_SBOX_023', value=ETresItemDefMaterial.MAT_ITEM34),
    
    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.TS_Sub_GAM1_EVENT9: BaseWorldLocationData('gameflow_TS', value=ETresItemDefKeyItem.KEY_ITEM07, label='TS_Sub_GAM1_EVENT9'),
    TresEventDataLocation.TT_BATTLEPORTAL_ex_24_CLEARED_ITEM_LASTELIXIR: BaseWorldLocationData('TT_BATTLEPORTAL_ex_24_CLEARED_ITEM_LASTELIXIR', value=ETresItemDefBattleItem.ITEM_LASTELIXIR, label='global_BATTLEPORTAL_ex_24_CLEARED'),
    TresEventDataLocation.TT_BATTLEPORTAL_ex_24_CLEARED_REPORT_ITEM04: BaseWorldLocationData('HE_BATTLEPORTAL_ex_24_CLEARED_REPORT_ITEM04', value=ETresItemDefReport.REPORT_ITEM04, label='global_BATTLEPORTAL_ex_24_CLEARED'),
    TresEventDataLocation.TT_BATTLEPORTAL_ex_25_CLEARED_ACC_ITEM41: BaseWorldLocationData('TT_BATTLEPORTAL_ex_25_CLEARED_ACC_ITEM41', value=ETresItemDefAccessory.ACC_ITEM41, label='global_BATTLEPORTAL_ex_25_CLEARED'),
    TresEventDataLocation.TT_BATTLEPORTAL_ex_25_CLEARED_REPORT_ITEM05: BaseWorldLocationData('HE_BATTLEPORTAL_ex_25_CLEARED_REPORT_ITEM05', value=ETresItemDefReport.REPORT_ITEM05, label='global_BATTLEPORTAL_ex_25_CLEARED'),
    TresEventDataLocation.TS_END: BaseWorldLocationData('gameflow_TS', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_03, label='TS_END'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_017_ts_001_ABILITYSORA1_AIR_RECOVERY: BaseWorldLocationData('Vbonus_017', value=ETresAbilityKind.AIR_RECOVERY, label='gameflow_VBONUS_017_ts_001'),
    TresVictoryBonusDataLocation.VBONUS_019_ts_003_ABILITYSORA1_TRIPPLE_SLASH: BaseWorldLocationData('Vbonus_019', value=ETresAbilityKind.TRIPPLE_SLASH, label='gameflow_VBONUS_019_ts_003'),
    TresVictoryBonusDataLocation.VBONUS_020_ts_004_ABILITYSORA1_HIGHJUMP: BaseWorldLocationData('Vbonus_020a', value=ETresAbilityKind.HIGHJUMP, label='gameflow_VBONUS_020_ts_004'),
    TresVictoryBonusDataLocation.VBONUS_020_ts_004_BONUSSORA2_MP_UP5: BaseWorldLocationData('Vbonus_020b', value=ETresVictoryBonusKind.MP_UP5, label='gameflow_VBONUS_020_ts_004'),
    TresVictoryBonusDataLocation.VBONUS_021_ts_005_BONUSSORA1_MELEM_THUNDER: BaseWorldLocationData('Vbonus_021', value=ETresVictoryBonusKind.MELEM_THUNDER, label='gameflow_VBONUS_021_ts_005'),
    TresVictoryBonusDataLocation.VBONUS_022_ts_006_BONUSSORA1_ACC_SLOT_UP1: BaseWorldLocationData('Vbonus_022', value=ETresVictoryBonusKind.ACC_SLOT_UP1, label='gameflow_VBONUS_022_ts_006'),
    TresVictoryBonusDataLocation.VBONUS_023_ts_007_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_023a', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_023_ts_007'),
    TresVictoryBonusDataLocation.VBONUS_023_ts_007_ABILITYSORA1_AIR_DOWN: BaseWorldLocationData('Vbonus_023b', value=ETresAbilityKind.AIR_DOWN, label='gameflow_VBONUS_023_ts_007'),
    TresVictoryBonusDataLocation.TS_Sub_Minigame_CLEAR_A_ABILITYSORA1_FOCUS_ASPIR: BaseWorldLocationData('VBonus_Minigame001', value=ETresAbilityKind.AIR_DOWN, label='gameflow_TS_Sub_Minigame_CLEAR_A'),
    TresVictoryBonusDataLocation.TS_Sub_Pudding_CLEAR_A_ABILITYSORA1_ATTRACTION_UP: BaseWorldLocationData('VBonus_Minigame008', value=ETresAbilityKind.AIR_DOWN, label='gameflow_TS_Sub_Pudding_CLEAR_A')
}


# LOCATION NAMES
TOY_BOX_ANDYS_HOUSE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_001_NAVI_MAP_TS01,
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_002_ITEM_ELIXIR,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_001_MAT_ITEM35,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_002_MAT_ITEM53,
    TresVictoryBonusDataLocation.VBONUS_017_ts_001_ABILITYSORA1_AIR_RECOVERY
]

TOY_BOX_MAIN_FLOOR_1F_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_003_NAVI_MAP_TS02,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_022_ITEM_HIGHFOCUSSUPPLY,
    TresEventDataLocation.TT_BATTLEPORTAL_ex_25_CLEARED_ACC_ITEM41,
    TresEventDataLocation.TT_BATTLEPORTAL_ex_25_CLEARED_REPORT_ITEM05
]

TOY_BOX_MAIN_FLOOR_2F_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_003_PRT_ITEM36
]

TOY_BOX_MAIN_FLOOR_3F_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_006_LSIGAME10,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_004_ITEM_POTION
]

TOY_BOX_ACTION_FIGURES_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_005_ITEM_POWERUP,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_006_ITEM_ETHER,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_007_ACC_ITEM32,
    TresVictoryBonusDataLocation.VBONUS_019_ts_003_ABILITYSORA1_TRIPPLE_SLASH
]

TOY_BOX_LOWER_VENTS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_004_LSIGAME16,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_008_ITEM_FOCUSSUPPLY,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_009_ITEM_ETHER
]

TOY_BOX_BABIES_AND_TODDLERS_DOLLS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_010_ACC_ITEM27,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_011_WEP_DONALD_01,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_012_MAT_ITEM53,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_013_PRT_ITEM11,
    TresVictoryBonusDataLocation.VBONUS_020_ts_004_ABILITYSORA1_HIGHJUMP,
    TresVictoryBonusDataLocation.VBONUS_020_ts_004_BONUSSORA2_MP_UP5
]

TOY_BOX_VIDEO_GAMES_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_016_ACC_ITEM04,
    TresVictoryBonusDataLocation.VBONUS_022_ts_006_BONUSSORA1_ACC_SLOT_UP1,
    TresVictoryBonusDataLocation.TS_Sub_Minigame_CLEAR_A_ABILITYSORA1_FOCUS_ASPIR,
    TresEventDataLocation.TS_Sub_GAM1_EVENT9
]

TOY_BOX_KID_KORRAL_OUTDOORS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_014_ITEM_HIGHETHER,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_015_PRT_ITEM42,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_023_MAT_ITEM34
]

TOY_BOX_KID_KORRAL_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_LARGE_TREASURE_005_LSIGAME20,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_017_MAT_ITEM53,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_018_ITEM_POTION,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_019_ACC_ITEM13,
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_020_PRT_ITEM19,
    TresVictoryBonusDataLocation.VBONUS_021_ts_005_BONUSSORA1_MELEM_THUNDER,
    TresEventDataLocation.TT_BATTLEPORTAL_ex_24_CLEARED_ITEM_LASTELIXIR,
    TresEventDataLocation.TT_BATTLEPORTAL_ex_24_CLEARED_REPORT_ITEM04
]

TOY_BOX_REST_AREA_LOCATIONS: list[str] = [
    TresTreasureDataLocation.TOY_BOX_SMALL_TREASURE_021_ACC_ITEM42,
    TresVictoryBonusDataLocation.TS_Sub_Pudding_CLEAR_A_ABILITYSORA1_ATTRACTION_UP
]

TOY_BOX_BOSS_ARENA_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_023_ts_007_BONUSSORA1_HP_UP10,
    TresVictoryBonusDataLocation.VBONUS_023_ts_007_ABILITYSORA1_AIR_DOWN,
    TresEventDataLocation.TS_END
]