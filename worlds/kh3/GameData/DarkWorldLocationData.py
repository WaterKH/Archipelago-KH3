from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresVictoryBonusKind
from worlds.kh3.Locations import TresVictoryBonusDataLocation

checks: dict[str, BaseWorldLocationData] = {
    # Victory Bonuses
    TresVictoryBonusDataLocation.VBONUS_067_dw_001_BONUSSORA1_MELEM_BLIZZARD: BaseWorldLocationData('Vbonus_067', value=ETresVictoryBonusKind.MELEM_BLIZZARD, label='gameflow_VBONUS_067_dw_001'),
    TresVictoryBonusDataLocation.VBONUS_067_dw_001_BONUSSORA2_HP_UP10: BaseWorldLocationData('Vbonus_067', value=ETresVictoryBonusKind.HP_UP10, label='gameflow_VBONUS_067_dw_001')
}


# LOCATION NAMES
DARK_WORLD_DARK_MARGIN_LOCATIONS: list[str] = [
    TresVictoryBonusDataLocation.VBONUS_067_dw_001_BONUSSORA1_MELEM_BLIZZARD,
    TresVictoryBonusDataLocation.VBONUS_067_dw_001_BONUSSORA2_HP_UP10
]