from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresItemDefCampItem, ETresItemDefBattleItem, ETresItemDefAccessory, ETresItemDefMaterial, ETresItemDefProtector
from worlds.kh3.Locations import TresLuckyMarkDataLocation

checks: dict[str, BaseWorldLocationData] = {
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_1_AP_UP: BaseWorldLocationData('LuckyMarky_1', value=ETresItemDefCampItem.ITEM_APUP),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_3_ITEM_MEGAPOTION: BaseWorldLocationData('LuckyMarky_3', value=ETresItemDefBattleItem.ITEM_MEGAPOTION),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_5_ACC_ITEM09: BaseWorldLocationData('LuckyMarky_5', value=ETresItemDefAccessory.ACC_ITEM09),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_10_PRT_ITEM40: BaseWorldLocationData('LuckyMarky_10', value=ETresItemDefProtector.PRT_ITEM40),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_15_ACC_ITEM36: BaseWorldLocationData('LuckyMarky_15', value=ETresItemDefAccessory.ACC_ITEM36),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_20_ITEM_MAGICUP: BaseWorldLocationData('LuckyMarky_20', value=ETresItemDefCampItem.ITEM_MAGICUP),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_25_ACC_ITEM37: BaseWorldLocationData('LuckyMarky_25', value=ETresItemDefAccessory.ACC_ITEM37),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_30_PRT_ITEM37: BaseWorldLocationData('LuckyMarky_30', value=ETresItemDefProtector.PRT_ITEM37),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_35_PRT_ITEM08: BaseWorldLocationData('LuckyMarky_35', value=ETresItemDefProtector.PRT_ITEM08),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_40_ITEM_POWERUP: BaseWorldLocationData('LuckyMarky_40', value=ETresItemDefCampItem.ITEM_POWERUP),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_45_ACC_ITEM24: BaseWorldLocationData('LuckyMarky_45', value=ETresItemDefAccessory.ACC_ITEM24),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_50_ACC_ITEM21: BaseWorldLocationData('LuckyMarky_50', value=ETresItemDefAccessory.ACC_ITEM21),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_55_ITEM_GUARDUP: BaseWorldLocationData('LuckyMarky_55', value=ETresItemDefCampItem.ITEM_GUARDUP),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_60_ACC_ITEM16: BaseWorldLocationData('LuckyMarky_60', value=ETresItemDefAccessory.ACC_ITEM16),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_65_PRT_ITEM10: BaseWorldLocationData('LuckyMarky_65', value=ETresItemDefProtector.PRT_ITEM10),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_70_PRT_ITEM44: BaseWorldLocationData('LuckyMarky_70', value=ETresItemDefProtector.PRT_ITEM44),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_80_MAT_ITEM57: BaseWorldLocationData('LuckyMarky_80', value=ETresItemDefMaterial.MAT_ITEM57),
    TresLuckyMarkDataLocation.LUCKY_MARK_COLLECT_90_ACC_ITEM31: BaseWorldLocationData('LuckyMarky_90', value=ETresItemDefAccessory.ACC_ITEM31),
}