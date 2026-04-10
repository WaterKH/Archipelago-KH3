from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefBattleItem, ETresItemDefCampItem, ETresItemDefLSIGameItem, ETresItemDefMaterial, ETresItemDefNavimap, ETresAbilityKind, ETresItemDefAccessory, ETresItemDefProtector, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_001_NAVI_MAP_FZ01: BaseWorldLocationData('FZ_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_FZ01),
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_002_NAVI_MAP_FZ02: BaseWorldLocationData('FZ_LBOX_002', value=ETresItemDefNavimap.NAVI_MAP_FZ02),
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_003_LSIGAME07: BaseWorldLocationData('FZ_LBOX_003', value=ETresItemDefLSIGameItem.LSIGAME07),
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_004_LSIGAME06: BaseWorldLocationData('FZ_LBOX_004', value=ETresItemDefLSIGameItem.LSIGAME06),
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_005_LSIGAME22: BaseWorldLocationData('FZ_LBOX_005', value=ETresItemDefLSIGameItem.LSIGAME22),
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_006_MAT_ITEM56: BaseWorldLocationData('FZ_LBOX_006', value=ETresItemDefMaterial.MAT_ITEM56),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_001_PRT_ITEM15: BaseWorldLocationData('FZ_001', value=ETresItemDefProtector.PRT_ITEM15),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_002_MAT_ITEM54: BaseWorldLocationData('FZ_002', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_004_ITEM_ELIXIR: BaseWorldLocationData('FZ_004', value=ETresItemDefBattleItem.ITEM_ELIXIR),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_005_PRT_ITEM05: BaseWorldLocationData('FZ_005', value=ETresItemDefProtector.PRT_ITEM05),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_007_ACC_ITEM19: BaseWorldLocationData('FZ_007', value=ETresItemDefAccessory.ACC_ITEM19),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_011_PRT_ITEM23: BaseWorldLocationData('FZ_011', value=ETresItemDefProtector.PRT_ITEM23),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_012_PRT_ITEM48: BaseWorldLocationData('FZ_012', value=ETresItemDefProtector.PRT_ITEM48),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_013_MAT_ITEM54: BaseWorldLocationData('FZ_013', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_015_ACC_ITEM44: BaseWorldLocationData('FZ_015', value=ETresItemDefAccessory.ACC_ITEM44),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_016_ITEM_HIGHPOTION: BaseWorldLocationData('FZ_016', value=ETresItemDefBattleItem.ITEM_HIGHPOTION),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_017_ITEM_FOCUSSUPPLY: BaseWorldLocationData('FZ_017', value=ETresItemDefBattleItem.ITEM_FOCUSSUPPLY),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_019_ITEM_HIGHETHER: BaseWorldLocationData('FZ_019', value=ETresItemDefBattleItem.ITEM_HIGHETHER),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_020_PRT_ITEM16: BaseWorldLocationData('FZ_020', value=ETresItemDefProtector.PRT_ITEM16),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_022_ITEM_APUP: BaseWorldLocationData('FZ_022', value=ETresItemDefCampItem.ITEM_APUP),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_023_ITEM_MEGAETHER: BaseWorldLocationData('FZ_023', value=ETresItemDefBattleItem.ITEM_MEGAETHER),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_024_ACC_ITEM26: BaseWorldLocationData('FZ_024', value=ETresItemDefAccessory.ACC_ITEM26),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_025_WEP_DONALD_05: BaseWorldLocationData('FZ_25', value=ETresItemDefWeapon.WEP_DONALD_05),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_027_ACC_ITEM35: BaseWorldLocationData('FZ_027', value=ETresItemDefAccessory.ACC_ITEM35),
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_029_MAT_ITEM54: BaseWorldLocationData('FZ_029', value=ETresItemDefMaterial.MAT_ITEM54),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.FZ_BATTLEPORTAL_ex_31_CLEARED_MAT_ITEM59: BaseWorldLocationData('FZ_BATTLEPORTAL_ex_31_CLEARED_MAT_ITEM59', value=ETresItemDefMaterial.MAT_ITEM59, label='global_BATTLEPORTAL_ex_31_CLEARED'),
    TresEventDataLocation.FZ_BATTLEPORTAL_ex_31_CLEARED_REPORT_ITEM09: BaseWorldLocationData('FZ_BATTLEPORTAL_ex_31_CLEARED_REPORT_ITEM09', value=ETresItemDefReport.REPORT_ITEM09, label='global_BATTLEPORTAL_ex_31_CLEARED'),
    TresEventDataLocation.FZ_END: BaseWorldLocationData('gameflow_FZ', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_06, label='FZ_END'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_041_fz_001_ABILITYSORA1_AIR_ROLL_BEAT: BaseWorldLocationData('Vbonus_041', value=ETresAbilityKind.AIR_ROLL_BEAT, label='gameflow_VBONUS_041_fz_001'),
    TresVictoryBonusDataLocation.VBONUS_043_fz_003_BONUSSORA1_MELEM_THUNDER: BaseWorldLocationData('Vbonus_043', value=ETresVictoryBonusKind.MELEM_THUNDER, label='gameflow_VBONUS_043_fz_003'),
    TresVictoryBonusDataLocation.VBONUS_045_fz_005_BONUSSORA1_RISKDODGE: BaseWorldLocationData('Vbonus_045', value=ETresAbilityKind.RISKDODGE, label='gameflow_VBONUS_045_fz_005'),
    TresVictoryBonusDataLocation.VBONUS_047_fz_007_BONUSSORA1_MELEM_BLIZZARD: BaseWorldLocationData('Vbonus_047', value=ETresVictoryBonusKind.MELEM_BLIZZARD, label='gameflow_VBONUS_047_fz_007'),
    TresVictoryBonusDataLocation.VBONUS_048_fz_008_ABILITYSORA1_DOUBLEFLIGHT: BaseWorldLocationData('Vbonus_048', value=ETresAbilityKind.DOUBLEFLIGHT, label='gameflow_VBONUS_048_fz_008'),
    TresVictoryBonusDataLocation.VBONUS_049_fz_009_ABILITYSORA1_AIRSLIDE: BaseWorldLocationData('Vbonus_049a', value=ETresAbilityKind.AIRSLIDE, label='gameflow_VBONUS_049_fz_009'),
    TresVictoryBonusDataLocation.VBONUS_049_fz_009_BONUSSORA1_ACC_SLOT_UP1: BaseWorldLocationData('Vbonus_049b', value=ETresVictoryBonusKind.ACC_SLOT_UP1, label='gameflow_VBONUS_049_fz_009'),
    TresVictoryBonusDataLocation.VBONUS_050_fz_010_ABILITYSORA1_SUPERSLIDE: BaseWorldLocationData('Vbonus_50a', value=ETresAbilityKind.SUPERSLIDE, label='gameflow_VBONUS_050_fz_010'),
    TresVictoryBonusDataLocation.VBONUS_050_fz_010_BONUSSORA1_MP_UP5: BaseWorldLocationData('Vbonus_50b', value=ETresVictoryBonusKind.MP_UP5, label='gameflow_VBONUS_050_fz_010'),
    TresVictoryBonusDataLocation.FZ_Sub_RESULT_RANK_A_ABILITYSORA1_FUSION_ROCKET: BaseWorldLocationData('VBonus_Minigame003', value=ETresAbilityKind.FUSION_ROCKET, label='gameflow_FZ_Sub_RESULT_RANK_A'),
    TresVictoryBonusDataLocation.FZ_Sub_RESULT_TREASURECOMPLETE_ABILITYSORA1_MASTER_DRAW: BaseWorldLocationData('VBonus_Minigame004', value=ETresAbilityKind.MASTER_DRAW, label='gameflow_FZ_Sub_RESULT_TREASURECOMPLETE'),
    TresVictoryBonusDataLocation.FZ_Sub_Pudding_CLEAR_A_ABILITYSORA1_UNISON_BLIZZARD: BaseWorldLocationData('VBonus_Minigame011', value=ETresAbilityKind.UNISON_BLIZZARD, label='gameflow_FZ_Sub_Pudding_CLEAR_A')
}


# LOCATION NAMES
ARENDELLE_TREESCAPE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_001_NAVI_MAP_FZ01,
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_003_LSIGAME07,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_001_PRT_ITEM15,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_002_MAT_ITEM54,
    TresVictoryBonusDataLocation.VBONUS_041_fz_001_ABILITYSORA1_AIR_ROLL_BEAT
]

ARENDELLE_THE_LABYRINTH_OF_ICE_LOWER_TIER_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_005_LSIGAME22,
    TresVictoryBonusDataLocation.VBONUS_043_fz_003_BONUSSORA1_MELEM_THUNDER
]

ARENDELLE_THE_LABYRINTH_OF_ICE_MIDDLE_TIER_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_002_NAVI_MAP_FZ02,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_012_PRT_ITEM48,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_015_ACC_ITEM44,
    TresVictoryBonusDataLocation.VBONUS_045_fz_005_BONUSSORA1_RISKDODGE
]

ARENDELLE_THE_LABYRINTH_OF_ICE_UPPER_TIER_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_011_PRT_ITEM23,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_013_MAT_ITEM54
]

ARENDELLE_GORGE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_004_ITEM_ELIXIR,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_005_PRT_ITEM05,
    TresEventDataLocation.FZ_BATTLEPORTAL_ex_31_CLEARED_MAT_ITEM59,
    TresEventDataLocation.FZ_BATTLEPORTAL_ex_31_CLEARED_REPORT_ITEM09
]

ARENDELLE_FROZEN_WALL_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_023_ITEM_MEGAETHER,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_024_ACC_ITEM26,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_025_WEP_DONALD_05
]

ARENDELLE_VALLEY_OF_ICE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_016_ITEM_HIGHPOTION,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_017_ITEM_FOCUSSUPPLY,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_019_ITEM_HIGHETHER,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_020_PRT_ITEM16,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_022_ITEM_APUP,
    TresVictoryBonusDataLocation.VBONUS_049_fz_009_ABILITYSORA1_AIRSLIDE,
    TresVictoryBonusDataLocation.VBONUS_049_fz_009_BONUSSORA1_ACC_SLOT_UP1
]

ARENDELLE_SNOWFIELD_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_004_LSIGAME06,
    TresTreasureDataLocation.ARENDELLE_LARGE_TREASURE_006_MAT_ITEM56,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_007_ACC_ITEM19
]

ARENDELLE_FOOTHILLS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_027_ACC_ITEM35,
    TresTreasureDataLocation.ARENDELLE_SMALL_TREASURE_029_MAT_ITEM54,
    TresVictoryBonusDataLocation.VBONUS_050_fz_010_ABILITYSORA1_SUPERSLIDE,
    TresVictoryBonusDataLocation.VBONUS_050_fz_010_BONUSSORA1_MP_UP5
]

ARENDELLE_SUMMIT_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.FZ_Sub_RESULT_RANK_A_ABILITYSORA1_FUSION_ROCKET,
    TresVictoryBonusDataLocation.FZ_Sub_RESULT_TREASURECOMPLETE_ABILITYSORA1_MASTER_DRAW
]

ARENDELLE_MOUNTAINSIDE_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.FZ_Sub_Pudding_CLEAR_A_ABILITYSORA1_UNISON_BLIZZARD
]

ARENDELLE_MINI_BOSS_ARENA_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_047_fz_007_BONUSSORA1_MELEM_BLIZZARD
]

ARENDELLE_BOSS_ARENA_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_048_fz_008_ABILITYSORA1_DOUBLEFLIGHT,
    TresEventDataLocation.FZ_END
]