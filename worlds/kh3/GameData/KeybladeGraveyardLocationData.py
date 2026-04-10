from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefAccessory, ETresItemDefBattleItem, ETresItemDefCampItem, ETresItemDefLSIGameItem, ETresItemDefMaterial, ETresItemDefNavimap, ETresItemDefProtector, ETresAbilityKind, ETresItemDefReport, ETresItemDefWeapon, ETresVictoryBonusKind
from worlds.kh3.Locations import TresEventDataLocation, TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_LARGE_TREASURE_001_NAVI_MAP_KG01: BaseWorldLocationData('KG_LBOX_001', value=ETresItemDefNavimap.NAVI_MAP_KG01),
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_LARGE_TREASURE_002_NAVI_MAP_KG02: BaseWorldLocationData('KG_LBOX_002', value=ETresItemDefNavimap.NAVI_MAP_KG02),
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_SMALL_TREASURE_001_ITEM_LASTELIXIR: BaseWorldLocationData('KG_SBOX_001', value=ETresItemDefBattleItem.ITEM_LASTELIXIR),
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_SMALL_TREASURE_002_ITEM_MEGAPOTION: BaseWorldLocationData('KG_SBOX_002', value=ETresItemDefBattleItem.ITEM_MEGAPOTION),
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_SMALL_TREASURE_003_ITEM_MEGAETHER: BaseWorldLocationData('KG_SBOX_003', value=ETresItemDefBattleItem.ITEM_MEGAETHER),
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_SMALL_TREASURE_004_PRT_ITEM09: BaseWorldLocationData('KG_SBOX_004', value=ETresItemDefProtector.PRT_ITEM09),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label
    TresEventDataLocation.KG_got_Starlight: BaseWorldLocationData('KG_got_Starlight', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_18, label='KG_got_Starlight'),
    TresEventDataLocation.KG_BATTLEPORTAL_ex_37_CLEARED_ACC_ITEM45: BaseWorldLocationData('KG_BATTLEPORTAL_ex_37_CLEARED_ACC_ITEM45', value=ETresItemDefAccessory.ACC_ITEM45, label='global_BATTLEPORTAL_ex_37_CLEARED'),
    TresEventDataLocation.KG_BATTLEPORTAL_ex_37_CLEARED_REPORT_ITEM13: BaseWorldLocationData('KG_BATTLEPORTAL_ex_37_CLEARED_REPORT_ITEM13', value=ETresItemDefReport.REPORT_ITEM13, label='global_BATTLEPORTAL_ex_37_CLEARED'),
    TresEventDataLocation.KG_BATTLEPORTAL_ex_38_CLEARED_ACC_ITEM39: BaseWorldLocationData('KG_BATTLEPORTAL_ex_38_CLEARED_ACC_ITEM39', value=ETresItemDefAccessory.ACC_ITEM39, label='global_BATTLEPORTAL_ex_38_CLEARED'),

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_069_kg_001_ABILITYSORA1_REVENGE_EX: BaseWorldLocationData('Vbonus_069a', value=ETresAbilityKind.REVENGE_EX, label='gameflow_VBONUS_069_kg_001'),
    TresVictoryBonusDataLocation.VBONUS_069_kg_001_BONUSSORA2_ITEM_SLOT_UP1: BaseWorldLocationData('Vbonus_066b', value=ETresVictoryBonusKind.ITEM_SLOT_UP1, label='gameflow_VBONUS_069_kg_001'),
    TresVictoryBonusDataLocation.VBONUS_070_kg_002_BONUSSORA1_MELEM_CURE: BaseWorldLocationData('Vbonus_070', value=ETresVictoryBonusKind.MELEM_CURE, label='gameflow_VBONUS_070_kg_002'),
    TresVictoryBonusDataLocation.VBONUS_071_kg_003_BONUSSORA1_MP_UP5: BaseWorldLocationData('Vbonus_071', value=ETresVictoryBonusKind.MP_UP5, label='gameflow_VBONUS_071_kg_003'),
    TresVictoryBonusDataLocation.VBONUS_072_kg_004_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_072', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_072_kg_004'),
    TresVictoryBonusDataLocation.VBONUS_073_kg_005_BONUSSORA1_MP_UP5: BaseWorldLocationData('Vbonus_073', value=ETresVictoryBonusKind.MP_UP5, label='gameflow_VBONUS_073_kg_005'),
    TresVictoryBonusDataLocation.VBONUS_074_kg_006_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_074', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_074_kg_006'),
    TresVictoryBonusDataLocation.VBONUS_075_kg_007_BONUSSORA1_HP_UP10: BaseWorldLocationData('Vbonus_075', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_075_kg_007'),
    TresVictoryBonusDataLocation.VBONUS_DLC_001_kg_001_BONUSSORA1_ITEM_SLOT_UP1: BaseWorldLocationData('VBonus_DLC_001', value=ETresVictoryBonusKind.ITEM_SLOT_UP1, label='gameflow_VBONUS_DLC_001_kg_001'),
    TresVictoryBonusDataLocation.VBONUS_DLC_002_kg_002_BONUSSORA1_MP_UP3: BaseWorldLocationData('VBonus_DLC_002', value=ETresVictoryBonusKind.MP_UP3, label='gameflow_VBONUS_DLC_002_kg_002'),
    TresVictoryBonusDataLocation.VBONUS_DLC_003_kg_003_BONUSSORA1_MP_UP3: BaseWorldLocationData('VBonus_DLC_003', value=ETresVictoryBonusKind.MP_UP3, label='gameflow_VBONUS_DLC_003_kg_003'),
    TresVictoryBonusDataLocation.VBONUS_DLC_004_kg_004_BONUSSORA1_MP_UP3: BaseWorldLocationData('VBonus_DLC_004', value=ETresVictoryBonusKind.MP_UP3, label='gameflow_VBONUS_DLC_004_kg_004'),
    TresVictoryBonusDataLocation.VBONUS_DLC_005_kg_005_BONUSSORA1_MP_UP3: BaseWorldLocationData('VBonus_DLC_005', value=ETresVictoryBonusKind.MP_UP3, label='gameflow_VBONUS_DLC_005_kg_005'),
    TresVictoryBonusDataLocation.VBONUS_DLC_006_kg_006_BONUSSORA1_MP_UP3: BaseWorldLocationData('VBonus_DLC_006', value=ETresVictoryBonusKind.MP_UP3, label='gameflow_VBONUS_DLC_006_kg_006'),
    TresVictoryBonusDataLocation.VBONUS_DLC_007_kg_007_BONUSSORA1_MP_UP3: BaseWorldLocationData('VBonus_DLC_007', value=ETresVictoryBonusKind.MP_UP3, label='gameflow_VBONUS_DLC_007_kg_007'),
    TresVictoryBonusDataLocation.VBONUS_DLC_008_kg_008_BONUSSORA1_MP_UP3: BaseWorldLocationData('VBonus_DLC_008', value=ETresVictoryBonusKind.MP_UP3, label='gameflow_VBONUS_DLC_008_kg_008'),
    TresVictoryBonusDataLocation.VBONUS_DLC_015_kg_012_BONUSSORA1_ITEM_SLOT_UP1: BaseWorldLocationData('VBonus_DLC_012', value=ETresVictoryBonusKind.ITEM_SLOT_UP1, label='gameflow_VBONUS_DLC_012_kg_009')
}


# LOCATION NAMES
KEYBLADE_GRAVEYARD_THE_BADLANDS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_LARGE_TREASURE_001_NAVI_MAP_KG01,
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_SMALL_TREASURE_004_PRT_ITEM09,
    TresVictoryBonusDataLocation.VBONUS_069_kg_001_ABILITYSORA1_REVENGE_EX,
    TresVictoryBonusDataLocation.VBONUS_069_kg_001_BONUSSORA2_ITEM_SLOT_UP1,
    TresVictoryBonusDataLocation.VBONUS_070_kg_002_BONUSSORA1_MELEM_CURE,
    TresEventDataLocation.KG_got_Starlight,
    TresEventDataLocation.KG_BATTLEPORTAL_ex_37_CLEARED_ACC_ITEM45,
    TresEventDataLocation.KG_BATTLEPORTAL_ex_37_CLEARED_REPORT_ITEM13,
    TresEventDataLocation.KG_BATTLEPORTAL_ex_38_CLEARED_ACC_ITEM39
]

KEYBLADE_GRAVEYARD_THE_SKEIN_OF_SEVERANCE_LOCATIONS: list[str] = [
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_LARGE_TREASURE_002_NAVI_MAP_KG02,
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_SMALL_TREASURE_001_ITEM_LASTELIXIR,
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_SMALL_TREASURE_002_ITEM_MEGAPOTION,
    TresTreasureDataLocation.KEYBLADE_GRAVEYARD_SMALL_TREASURE_003_ITEM_MEGAETHER,
    TresVictoryBonusDataLocation.VBONUS_071_kg_003_BONUSSORA1_MP_UP5,
    TresVictoryBonusDataLocation.VBONUS_072_kg_004_BONUSSORA1_HP_UP10,
    TresVictoryBonusDataLocation.VBONUS_073_kg_005_BONUSSORA1_MP_UP5,
    TresVictoryBonusDataLocation.VBONUS_074_kg_006_BONUSSORA1_HP_UP10,
    TresVictoryBonusDataLocation.VBONUS_075_kg_007_BONUSSORA1_HP_UP10,
    TresVictoryBonusDataLocation.VBONUS_DLC_001_kg_001_BONUSSORA1_ITEM_SLOT_UP1,
    TresVictoryBonusDataLocation.VBONUS_DLC_002_kg_002_BONUSSORA1_MP_UP3,
    TresVictoryBonusDataLocation.VBONUS_DLC_003_kg_003_BONUSSORA1_MP_UP3,
    TresVictoryBonusDataLocation.VBONUS_DLC_004_kg_004_BONUSSORA1_MP_UP3,
    TresVictoryBonusDataLocation.VBONUS_DLC_005_kg_005_BONUSSORA1_MP_UP3,
    TresVictoryBonusDataLocation.VBONUS_DLC_006_kg_006_BONUSSORA1_MP_UP3,
    TresVictoryBonusDataLocation.VBONUS_DLC_007_kg_007_BONUSSORA1_MP_UP3,
    TresVictoryBonusDataLocation.VBONUS_DLC_008_kg_008_BONUSSORA1_MP_UP3,
    TresVictoryBonusDataLocation.VBONUS_DLC_015_kg_012_BONUSSORA1_ITEM_SLOT_UP1
]