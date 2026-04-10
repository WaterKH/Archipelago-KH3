from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefMaterial, ETresAbilityKind, ETresVictoryBonusKind
from worlds.kh3.Locations import TresTreasureDataLocation, TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Treasures
    TresTreasureDataLocation.THE_FINAL_WORLD_LARGE_TREASURE_001_MAT_ITEM57: BaseWorldLocationData('EW_LBOX_001', value=ETresItemDefMaterial.MAT_ITEM57),

    # Events - If label starts with gameflow/ global, this is a boolean, otherwise it is a flag/ label

    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_068_ew_001_BONUSSORA1_MELEM_AERO: BaseWorldLocationData('Vbonus_068a', value=ETresVictoryBonusKind.MELEM_AERO),
    TresVictoryBonusDataLocation.VBONUS_068_ew_001_BONUSSORA2_MP_UP5: BaseWorldLocationData('Vbonus068b', value=ETresVictoryBonusKind.MP_UP5),
    TresVictoryBonusDataLocation.VBONUS_076_ew_002_ABILITYSORA1_GLIDE: BaseWorldLocationData('Vbonus_076', value=ETresAbilityKind.GLIDE),
    TresVictoryBonusDataLocation.VBONUS_082_ew_001_BONUSSORA1_MELEM_FIRE: BaseWorldLocationData('Vbonus_082a', value=ETresVictoryBonusKind.MELEM_FIRE),
    TresVictoryBonusDataLocation.VBONUS_082_ew_001_BONUSSORA1_MELEM_WATER: BaseWorldLocationData('Vbonus_82b', value=ETresVictoryBonusKind.MELEM_WATER),
    TresVictoryBonusDataLocation.VBONUS_083_ew_002_BONUSSORA1_HP_UP5: BaseWorldLocationData('Vbonus_083', value=ETresVictoryBonusKind.HP_UP5),
    TresVictoryBonusDataLocation.VBONUS_084_ew_003_BONUSSORA1_HP_UP5: BaseWorldLocationData('Vbonus_084', value=ETresVictoryBonusKind.HP_UP5)
}


# LOCATION NAMES
THE_FINAL_WORLD_THE_SEA_OF_STARS_LOCATIONS: list[str] = [
    TresTreasureDataLocation.THE_FINAL_WORLD_LARGE_TREASURE_001_MAT_ITEM57,
    TresVictoryBonusDataLocation.VBONUS_082_ew_001_BONUSSORA1_MELEM_FIRE,
    TresVictoryBonusDataLocation.VBONUS_082_ew_001_BONUSSORA1_MELEM_WATER
]

THE_FINAL_WORLD_LABYRINTH_OF_PILLARS_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_076_ew_002_ABILITYSORA1_GLIDE,
    TresVictoryBonusDataLocation.VBONUS_083_ew_002_BONUSSORA1_HP_UP5,
    TresVictoryBonusDataLocation.VBONUS_084_ew_003_BONUSSORA1_HP_UP5
]

THE_FINAL_WORLD_FALLEN_SAN_FRANSOKYO_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_068_ew_001_BONUSSORA1_MELEM_AERO,
    TresVictoryBonusDataLocation.VBONUS_068_ew_001_BONUSSORA2_MP_UP5
]