from worlds.kh3.GameData.BaseWorldLocationData import BaseWorldLocationData
from worlds.kh3.Items import ETresAbilityKind, ETresItemDefWeapon
from worlds.kh3.Locations import TresChrInitDataLocation

checks: dict[str, BaseWorldLocationData] = {
    TresChrInitDataLocation.WEAPON_KEYBLADE: BaseWorldLocationData('WEAPON_KEYBLADE', value=ETresItemDefWeapon.WEP_KEYBLADE_SO_00),
    TresChrInitDataLocation.EQUIP_ABILITY_LIBRA: BaseWorldLocationData('EQUIP_ABILITY_LIBRA', value=ETresAbilityKind.LIBRA),
    TresChrInitDataLocation.EQUIP_ABILITY_DODGE: BaseWorldLocationData('EQUIP_ABILITY_DODGE', value=ETresAbilityKind.DODGE),
    TresChrInitDataLocation.EQUIP_ABILITY_AIRSLIDE: BaseWorldLocationData('EQUIP_ABILITY_AIRSLIDE', value=ETresAbilityKind.AIRSLIDE),
    TresChrInitDataLocation.EQUIP_ABILITY_AIRDODGE: BaseWorldLocationData('EQUIP_ABILITY_AIRDODGE', value=ETresAbilityKind.AIRDODGE),
    TresChrInitDataLocation.EQUIP_ABILITY_REFLECT_GUARD: BaseWorldLocationData('EQUIP_ABILITY_REFLECT_GUARD', value=ETresAbilityKind.REFLECT_GUARD),
    TresChrInitDataLocation.EQUIP_ABILITY_SUPERSLIDE: BaseWorldLocationData('EQUIP_ABILITY_SUPERSLIDE', value=ETresAbilityKind.SUPERSLIDE),
    TresChrInitDataLocation.EQUIP_ABILITY_FRIEND_AID: BaseWorldLocationData('EQUIP_ABILITY_FRIEND_AID', value=ETresAbilityKind.FRIEND_AID),
    TresChrInitDataLocation.EQUIP_ABILITY_SONIC_SLASH: BaseWorldLocationData('EQUIP_ABILITY_SONIC_SLASH', value=ETresAbilityKind.SONIC_SLASH),
    TresChrInitDataLocation.EQUIP_ABILITY_SONIC_DOWN: BaseWorldLocationData('EQUIP_ABILITY_SONIC_DOWN', value=ETresAbilityKind.SONIC_DOWN),
    TresChrInitDataLocation.EQUIP_ABILITY_TURN_CUTTER: BaseWorldLocationData('EQUIP_ABILITY_TURN_CUTTER', value=ETresAbilityKind.TURN_CUTTER),
    TresChrInitDataLocation.EQUIP_ABILITY_SUMMERSALT: BaseWorldLocationData('EQUIP_ABILITY_SUMMERSALT', value=ETresAbilityKind.SUMMERSALT),
    TresChrInitDataLocation.EQUIP_ABILITY_POLE_SPIN: BaseWorldLocationData('EQUIP_ABILITY_POLE_SPIN', value=ETresAbilityKind.POLE_SPIN),
    TresChrInitDataLocation.EQUIP_ABILITY_POLE_SWING: BaseWorldLocationData('EQUIP_ABILITY_POLE_SWING', value=ETresAbilityKind.POLE_SWING),
    TresChrInitDataLocation.EQUIP_ABILITY_WALL_KICK: BaseWorldLocationData('EQUIP_ABILITY_WALL_KICK', value=ETresAbilityKind.WALL_KICK),
    TresChrInitDataLocation.EQUIP_ABILITY_CRITICAL_HALF: BaseWorldLocationData('EQUIP_ABILITY_CRITICAL_HALF', value=ETresAbilityKind.CRITICAL_HALF),
    TresChrInitDataLocation.EQUIP_ABILITY_AUTO_LOCK_MAGIC: BaseWorldLocationData('EQUIP_ABILITY_AUTO_LOCK_MAGIC', value=ETresAbilityKind.AUTO_LOCK_MAGIC),
    TresChrInitDataLocation.HAVE_ABILITY_EXPZERO: BaseWorldLocationData('HAVE_ABILITY_EXPZERO', value=ETresAbilityKind.EXPZERO),
    TresChrInitDataLocation.CRITICAL_EQUIP_ABILITY_CRITICAL_COUNTER: BaseWorldLocationData('CRITICAL_EQUIP_ABILITY_CRITICAL_COUNTER', value=ETresAbilityKind.CRITICAL_COUNTER),
    TresChrInitDataLocation.CRITICAL_EQUIP_ABILITY_CRITICAL_CHARGE: BaseWorldLocationData('CRITICAL_EQUIP_ABILITY_CRITICAL_CHARGE', value=ETresAbilityKind.CRITICAL_CHARGE),
    TresChrInitDataLocation.CRITICAL_HAVE_ABILITY_CRITICAL_CONVERTER: BaseWorldLocationData('CRITICAL_HAVE_ABILITY_CRITICAL_CONVERTER', value=ETresAbilityKind.CRITICAL_CONVERTER)
}