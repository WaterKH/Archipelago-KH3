from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefBattleItem, ETresItemDefKeyItem, ETresItemDefLSIGameItem, ETresItemDefMaterial, ETresItemDefNavimap, ETresItemDefProtector, ETresAbilityKind, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.MONSTROPOLIS_LARGE_TREASURE_001_NAVI_MAP_MI01: BaseWorldLocationData('MI_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_MI01),
    TresTreasureDataLocation.MONSTROPOLIS_LARGE_TREASURE_002_NAVI_MAP_MI02: BaseWorldLocationData('MI_LBOX_002', value=ETresItemDefNavimap.NAVI_MAP_MI02),
    TresTreasureDataLocation.MONSTROPOLIS_LARGE_TREASURE_003_LSIGAME14: BaseWorldLocationData('MI_LBOX_003', value=ETresItemDefLSIGameItem.LSIGAME14),
    TresTreasureDataLocation.MONSTROPOLIS_LARGE_TREASURE_004_LSIGAME13: BaseWorldLocationData('MI_LBOX_004', value=ETresItemDefLSIGameItem.LSIGAME13),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_001_ITEM_HIGHPOTION: BaseWorldLocationData('MI_SBOX_001', value=ETresItemDefBattleItem.ITEM_HIGHPOTION),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_002_ACC_ITEM06: BaseWorldLocationData('MI_SBOX_002', value=ETresItemDefAccessory.ACC_ITEM06),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_003_ITEM_FOCUSSUPPLY: BaseWorldLocationData('MI_SBOX_003', value=ETresItemDefBattleItem.ITEM_FOCUSSUPPLY),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_005_MAT_ITEM54: BaseWorldLocationData('MI_SBOX_005', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_006_PRT_ITEM46: BaseWorldLocationData('MI_SBOX_006', value=ETresItemDefProtector.PRT_ITEM46),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_007_ITEM_HIGHPOTION: BaseWorldLocationData('MI_SBOX_007', value=ETresItemDefBattleItem.ITEM_HIGHPOTION),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_008_ACC_ITEM14: BaseWorldLocationData('MI_SBOX_008', value=ETresItemDefAccessory.ACC_ITEM14),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_009_PRT_ITEM45: BaseWorldLocationData('MI_SBOX_009', value=ETresItemDefProtector.PRT_ITEM45),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_010_PRT_ITEM38: BaseWorldLocationData('MI_SBOX_010', value=ETresItemDefProtector.PRT_ITEM38),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_011_MAT_ITEM54: BaseWorldLocationData('MI_SBOX_011', value=ETresItemDefMaterial.MAT_ITEM54),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_012_ITEM_ETHER: BaseWorldLocationData('MI_SBOX_012', value=ETresItemDefBattleItem.ITEM_ETHER),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_013_ITEM_MEGAETHER: BaseWorldLocationData('MI_SBOX_013', value=ETresItemDefBattleItem.ITEM_MEGAETHER),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_014_ITEM_LASTELIXIR: BaseWorldLocationData('MI_SBOX_014', value=ETresItemDefBattleItem.ITEM_LASTELIXIR),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_015_ITEM_HIGHFOCUSSUPPLY: BaseWorldLocationData('MI_SBOX_015', value=ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_016_ACC_ITEM33: BaseWorldLocationData('MI_SBOX_016', value=ETresItemDefAccessory.ACC_ITEM33),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_017_WEP_GOOFY_05: BaseWorldLocationData('MI_SBOX_017', value=ETresItemDefWeapon.WEP_GOOFY_05),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_018_ITEM_HIGHPOTION: BaseWorldLocationData('MI_SBOX_018', value=ETresItemDefBattleItem.ITEM_HIGHPOTION),
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_019_ACC_ITEM41: BaseWorldLocationData('MI_SBOX_019', value=ETresItemDefAccessory.ACC_ITEM41),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.MI_Sub_mi_02_COMICAL_02: BaseWorldLocationData('gameflow_MI_Sub_mi_02_COMICAL_02', value=ETresItemDefAccessory.ACC_ITEM01, label='gameflow_MI_Sub_mi_02_COMICAL_02'),
    TresEventDataLocation.MI_PLANT_BATTLE3: BaseWorldLocationData('gameflow_MI', value=ETresItemDefKeyItem.KEY_ITEM09, label='MI_PLANT_BATTLE3'),
    TresEventDataLocation.MI_BATTLEPORTAL_ex_29_CLEARED_MAT_ITEM60: BaseWorldLocationData('MI_BATTLEPORTAL_ex_29_CLEARED_MAT_ITEM60', value=ETresItemDefMaterial.MAT_ITEM60, label='global_BATTLEPORTAL_ex_29_CLEARED'),
    TresEventDataLocation.MI_BATTLEPORTAL_ex_29_CLEARED_REPORT_ITEM08: BaseWorldLocationData('MI_BATTLEPORTAL_ex_29_CLEARED_REPORT_ITEM08', value=ETresItemDefReport.REPORT_ITEM08, label='global_BATTLEPORTAL_ex_29_CLEARED'),
    TresEventDataLocation.MI_END: BaseWorldLocationData('gameflow_MI', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_05, label='MI_END'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_032_mi_001_ABILITYSORA1_REVENGEIMPACT: BaseWorldLocationData('Vbonus_032', value=ETresAbilityKind.REVENGEIMPACT, label='gameflow_VBONUS_032_mi_001'),
    TresVictoryBonusDataLocation.VBONUS_034_mi_003_BONUSSORA1_MELEM_FIRE: BaseWorldLocationData('Vbonus_034', value=ETresVictoryBonusKind.MELEM_FIRE, label='gameflow_VBONUS_034_mi_003'),
    TresVictoryBonusDataLocation.VBONUS_036_mi_005_ABILITYSORA1_COMBO_MASTER: BaseWorldLocationData('Vbonus_036', value=ETresAbilityKind.COMBO_MASTER, label='gameflow_VBONUS_036_mi_005'),
    TresVictoryBonusDataLocation.VBONUS_037_mi_006_BONUSSORA1_MELEM_WATER: BaseWorldLocationData('Vbonus_037', value=ETresVictoryBonusKind.MELEM_WATER, label='gameflow_VBONUS_037_mi_006'),
    TresVictoryBonusDataLocation.VBONUS_038_mi_007_BONUSSORA1_ITEM_SLOT_UP1: BaseWorldLocationData('Vbonus_038', value=ETresVictoryBonusKind.ITEM_SLOT_UP1, label='gameflow_VBONUS_038_mi_007'),
    TresVictoryBonusDataLocation.VBONUS_039_mi_008_ABILITYSORA1_CHARGE_THRUST: BaseWorldLocationData('Vbonus_039', value=ETresAbilityKind.CHARGE_THRUST, label='gameflow_VBONUS_039_mi_008'),
    TresVictoryBonusDataLocation.VBONUS_040_mi_009_BONUSSORA1_MELEM_CURE: BaseWorldLocationData('Vbonus_040a', value=ETresVictoryBonusKind.MELEM_CURE, label='gameflow_VBONUS_040_mi_009'),
    TresVictoryBonusDataLocation.VBONUS_040_mi_009_BONUSSORA2_HP_UP10: BaseWorldLocationData('Vbonus_040b', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_040_mi_009'),
    TresVictoryBonusDataLocation.MI_Sub_Pudding_CLEAR_A_ABILITYSORA1_MAGIC_TIME: BaseWorldLocationData('VBonus_Minigame010', value=ETresAbilityKind.MAGIC_TIME, label='gameflow_MI_Sub_Pudding_CLEAR_A')
}


# LOCATION NAMES
MONSTROPOLIS_LOBBY_AND_OFFICES_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_LARGE_TREASURE_001_NAVI_MAP_MI01,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_001_ITEM_HIGHPOTION,
    TresVictoryBonusDataLocation.VBONUS_032_mi_001_ABILITYSORA1_REVENGEIMPACT
]

MONSTROPOLIS_LAUGH_FLOOR_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_002_ACC_ITEM06,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_003_ITEM_FOCUSSUPPLY
]

MONSTROPOLIS_DOOR_VAULT_UPPER_LEVEL_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_016_ACC_ITEM33,
    TresVictoryBonusDataLocation.MI_Sub_Pudding_CLEAR_A_ABILITYSORA1_MAGIC_TIME
]

MONSTROPOLIS_DOOR_VAULT_LOWER_LEVEL_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_017_WEP_GOOFY_05,
    TresVictoryBonusDataLocation.VBONUS_034_mi_003_BONUSSORA1_MELEM_FIRE
]

MONSTROPOLIS_DOOR_VAULT_SERVICE_AREA_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_018_ITEM_HIGHPOTION,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_019_ACC_ITEM41,
    TresEventDataLocation.MI_END
]

MONSTROPOLIS_FACTORY_BASEMENT_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_LARGE_TREASURE_002_NAVI_MAP_MI02
]

MONSTROPOLIS_FACTORY_GROUND_FLOOR_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_LARGE_TREASURE_004_LSIGAME13,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_005_MAT_ITEM54,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_006_PRT_ITEM46
]

MONSTROPOLIS_FACTORY_SECOND_FLOOR_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_007_ITEM_HIGHPOTION,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_008_ACC_ITEM14,
    TresVictoryBonusDataLocation.VBONUS_036_mi_005_ABILITYSORA1_COMBO_MASTER,
    TresEventDataLocation.MI_Sub_mi_02_COMICAL_02
]

MONSTROPOLIS_POWER_PLANT_ACCESSWAY_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_009_PRT_ITEM45,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_010_PRT_ITEM38,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_011_MAT_ITEM54,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_015_ITEM_HIGHFOCUSSUPPLY,
    TresVictoryBonusDataLocation.VBONUS_039_mi_008_ABILITYSORA1_CHARGE_THRUST
]

MONSTROPOLIS_POWER_PLANT_TANK_YARD_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_LARGE_TREASURE_003_LSIGAME14,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_012_ITEM_ETHER,
    TresVictoryBonusDataLocation.VBONUS_037_mi_006_BONUSSORA1_MELEM_WATER,
    TresVictoryBonusDataLocation.VBONUS_038_mi_007_BONUSSORA1_ITEM_SLOT_UP1,
    TresEventDataLocation.MI_PLANT_BATTLE3
]

MONSTROPOLIS_POWER_PLANT_VAULT_PASSAGE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_013_ITEM_MEGAETHER,
    TresTreasureDataLocation.MONSTROPOLIS_SMALL_TREASURE_014_ITEM_LASTELIXIR,
    TresVictoryBonusDataLocation.VBONUS_040_mi_009_BONUSSORA1_MELEM_CURE,
    TresVictoryBonusDataLocation.VBONUS_040_mi_009_BONUSSORA2_HP_UP10,
    TresEventDataLocation.MI_BATTLEPORTAL_ex_29_CLEARED_MAT_ITEM60,
    TresEventDataLocation.MI_BATTLEPORTAL_ex_29_CLEARED_REPORT_ITEM08
]
