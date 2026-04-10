import typing

from BaseClasses import Location
from worlds.kh3.Constants import KINGDOM_HEARTS_III
from worlds.kh3.Items import *

class LocationData(typing.NamedTuple):
    loc_name: str
    kh3_id: str
    world_name: str
    # world_id: str
    area_name: str
    # area_id: str
    type: str

class KingdomHeartsIIILocation(Location):
    game: str = KINGDOM_HEARTS_III

class TresWorldData():
    OLYMPUS = 'Olympus'
    TWILIGHT_TOWN = 'Twilight Town'
    TOY_BOX = 'Toy Box'
    KINGDOM_OF_CORONA = 'Kingdom of Corona'
    MONSTROPOLIS = 'Monstropolis'
    ARENDELLE = 'Arendelle'
    THE_CARIBBEAN = 'The Caribbean'
    SAN_FRANSOKYO = 'San Fransokyo'
    KEYBLADE_GRAVEYARD = 'Keyblade Graveyard'
    SCALA_AD_CAELUM = 'Scala ad Caelum'
    DARK_WORLD = 'Dark World'
    THE_FINAL_WORLD = 'The Final World'
    STATION_OF_AWAKENING = 'Station of Awakening'
    MYSTERIOUS_TOWER = 'Mysterious Tower'
    GUMMI_OCEAN = 'Gummi Ocean'

    INITIAL = 'INITIAL'
    UNKNOWN = 'UNKNOWN'
    MANY = 'MANY'
    ANY = 'ANY'
    
class TresAreaData():
    # Olympus
    CLIFF_ASCENT_INITIAL = 'Initial Cliff Ascent'
    AGORA_RUIN = 'Ruined Agora'
    OVERLOOK_RUIN = 'Ruined Overlook'
    GARDENS_RUIN = 'Ruined Gardens'
    THE_BIG_OLIVE_RUIN = 'The Big Olive (Ruined)'
    AGORA_GOLEM = 'Agora (Golem Fight)'
    RAVINE = 'Ravine'
    CLIFF_ASCENT = 'Cliff Ascent'
    MOUNTAINSIDE = 'Mountainside'
    SUMMIT = 'Summit'
    ALLEYWAY = 'Alleyway'
    AGORA = 'Agora'
    THE_BIG_OLIVE = 'The Big Olive'
    GARDENS = 'Gardens'
    OVERLOOK = 'Overlook'
    COURTYARD = 'Courtyard'
    CLOUD_RIDGE = 'Cloud Ridge'
    CORRIDORS = 'Corridors'

    # Twilight Town
    TRAM_COMMON = 'Tram Common'
    UNDERGROUND_CONDUIT = 'Underground Conduit'
    THE_WOODS = 'The Woods'
    THE_OLD_MANSION = 'The Old Mansion'

    # Toy Box
    ANDYS_HOUSE = 'Andy\'s House'
    MAIN_FLOOR_1F = 'Main Floor: 1F'
    MAIN_FLOOR_2F = 'Main Floor: 2F'
    MAIN_FLOOR_3F = 'Main Floor: 3F'
    ACTION_FIGURES = 'Action Figures'
    LOWER_VENTS = 'Lower Vents'
    BABIES_AND_TODDLERS_DOLLS = 'Babies & Toddlers (Dolls)'
    BABIES_AND_TODDLERS_OUTDOORS = 'Babies & Toddlers (Outdoors)'
    VIDEO_GAMES = 'Video Games'
    KID_KORRAL = 'Kid Korral'
    REST_AREA = 'Rest Area'

    # Kingdom of Corona
    HILLS = 'Hills'
    TOWER = 'Tower'
    MARSH = 'Marsh'
    CAMPSITE = 'Campsite'
    WETLANDS = 'Wetlands'
    WILDFLOWER_CLEARING = 'Wildflower Clearing'
    SHORE = 'Shore'
    THOROUGHFARE = 'Thoroughfare'
    WHARF = 'Wharf'

    # Monstropolis
    LOBBY_AND_OFFICES = 'Lobby & Offices'
    LAUGH_FLOOR = 'Laugh Floor'
    DOOR_VAULT_UPPER_LEVEL = 'Door Vault Upper Level'
    DOOR_VAULT_LOWER_LEVEL = 'Door Vault Lower Level'
    DOOR_VAULT_SERVICE_AREA = 'Door Vault Service Area'
    FACTORY_BASEMENT = 'Factory Basement'
    FACTORY_GROUND_FLOOR = 'Factory Ground Floor'
    FACTORY_SECOND_FLOOR = 'Factory Second Floor'
    POWER_PLANT_ACCESSWAY = 'Power Plant Accessway'
    POWER_PLANT_TANK_YARD = 'Power Plant Tank Yard'
    POWER_PLANT_VAULT_PASSAGE = 'Power Plant Vault Passage'

    # Arendelle
    TREESCAPE = 'Treescape'
    THE_LABYRINTH_OF_ICE_LOWER_TIER = 'The Labyrinth of Ice Lower Tier'
    THE_LABYRINTH_OF_ICE_MIDDLE_TIER = 'The Labyrinth of Ice Middle Tier'
    THE_LABYRINTH_OF_ICE_UPPER_TIER = 'The Labyrinth of Ice Upper Tier'
    GORGE = 'Gorge'
    FROZEN_WALL = 'Frozen Wall'
    VALLEY_OF_ICE = 'Valley of Ice'
    SNOWFIELD = 'Snowfield'
    FOOTHILLS = 'Foothills'

    # Caribbean
    DAVY_JONES_LOCKER = 'Davy Jones\'s Locker'
    THE_HIGH_SEAS = 'The High Seas'
    ISLA_DE_LOS_MASTILES = 'Isla de los Mástiles'
    SHIPS_END = 'Ship\'s End'
    SANDBAR_ISLE = 'Sandbar Isle'
    HUDDLED_ISLES = 'Huddled Isles'
    LEVIATHAN = 'The Leviathan'
    PORT_ROYAL_SEAPORT = 'Port Royal Seaport'
    PORT_ROYAL_DOCKS = 'Port Royal Docks'
    PORT_ROYAL_SETTLEMENT = 'Port Royal Settlement'
    PORT_ROYAL_FORT = 'Port Royal Fort'
    PORT_ROYAL_WATERS = 'Port Royal Waters'
    ISLA_VERDEMONTANA = 'Isla Verdemontaña'
    EXILE_ISLAND = 'Exile Island'
    CONFINEMENT_ISLE = 'Confinement Isle'
    HORSESHOE_ISLAND = 'Horseshoe Island'

    # San Fransokyo
    BRIDGE = 'Bridge'
    THE_CITY_NORTH_DISTRICT = 'The City North District'
    THE_CITY_SOUTH_DISTRICT = 'The City South District'
    THE_CITY_CENTRAL_DISTRICT = 'The City Central District'

    # Dark World
    DARK_MARGIN = 'Dark Margin'

    # Keyblade Graveyard
    THE_BADLANDS = 'The Badlands'
    THE_SKEIN_OF_SEVERANCE = 'The Skein of Severance'

    # Scala ad Caelum
    THE_STAIRWAY_TO_THE_SKY = 'The Stairway to the Sky'
    BREEZY_QUARTER = 'Breezy Quarter'

    # Misc.
    MOOGLE_SYNTHESIS = 'Moogle Synthesis'
    MOOGLE_WORKSHOP = 'Moogle Worshop'
    LE_GRAND_BISTROT = 'Le Grand Bistrot'
    BOSS_ARENA = 'Boss Arena'
    END_SCREEN = 'End Screen'

    INITIAL = 'INITIAL'
    UNKNOWN = 'UNKNOWN'
    MANY = 'MANY'
    ANY = 'ANY'


class TresChrInitDataLocation(KingdomHeartsIIILocation):
    """
    """
    CHARACTER_INITIALIZATION = 'Character Initialization'
    WEAPON_PREFIX = 'Weapon Slot'
    EQUIP_ABILITY_PREFIX = 'Equip Ability Slot'
    HAVE_ABILITY_PREFIX = 'Have Ability Slot'
    CRITICAL_EQUIP_ABILITY_PREFIX = 'Equip Ability Slot'
    CRITICAL_HAVE_ABILITY_PREFIX = 'Have Ability Slot'

    WEAPON_KEYBLADE = f'{WEAPON_PREFIX} {ETresItemDefWeapon.WEP_KEYBLADE_SO_00}'

    EQUIP_ABILITY_LIBRA = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.LIBRA}'
    EQUIP_ABILITY_DODGE = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.DODGE}'
    EQUIP_ABILITY_AIRSLIDE = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.AIRSLIDE}'
    EQUIP_ABILITY_AIRDODGE = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.AIRDODGE}'
    EQUIP_ABILITY_REFLECT_GUARD = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.REFLECT_GUARD}'
    EQUIP_ABILITY_SUPERSLIDE = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.SUPERSLIDE}'
    EQUIP_ABILITY_FRIEND_AID = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.FRIEND_AID}'
    EQUIP_ABILITY_SONIC_SLASH = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.SONIC_SLASH}'
    EQUIP_ABILITY_SONIC_DOWN = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.SONIC_DOWN}'
    EQUIP_ABILITY_TURN_CUTTER = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.TURN_CUTTER}'
    EQUIP_ABILITY_SUMMERSALT = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.SUMMERSALT}'
    EQUIP_ABILITY_POLE_SPIN = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.POLE_SPIN}'
    EQUIP_ABILITY_POLE_SWING = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.POLE_SWING}'
    EQUIP_ABILITY_WALL_KICK = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.WALL_KICK}'
    EQUIP_ABILITY_CRITICAL_HALF = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.CRITICAL_HALF}'
    EQUIP_ABILITY_AUTO_LOCK_MAGIC = f'{EQUIP_ABILITY_PREFIX} {ETresAbilityKind.AUTO_LOCK_MAGIC}'

    HAVE_ABILITY_EXPZERO = f'{HAVE_ABILITY_PREFIX} {ETresAbilityKind.EXPZERO}'

    CRITICAL_EQUIP_ABILITY_CRITICAL_COUNTER = f'{CRITICAL_EQUIP_ABILITY_PREFIX} {ETresAbilityKind.CRITICAL_COUNTER}'
    CRITICAL_EQUIP_ABILITY_CRITICAL_CHARGE = f'{CRITICAL_EQUIP_ABILITY_PREFIX} {ETresAbilityKind.CRITICAL_CHARGE}'

    CRITICAL_HAVE_ABILITY_CRITICAL_CONVERTER = f'{CRITICAL_HAVE_ABILITY_PREFIX} {ETresAbilityKind.CRITICAL_CONVERTER}'

    @classmethod
    def generate_locations(cls):
        locations = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue
            
            locations.append(LocationData(value, key, TresWorldData.INITIAL, TresAreaData.INITIAL, cls.CHARACTER_INITIALIZATION))
        return locations

class TresEquipItemDataLocation(KingdomHeartsIIILocation):
    """
    """
    WEAPON_ABILITY = 'Weapon Initial Ability'
    ARMOR_ABILITY = 'Armor Initial Ability'
    ACCESSOR_ABILITY = 'Accessory Initial Ability'

    WEP_KEYBLADE_SO_00_ABILITY_1_PRIZE_DRAW = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_00} {WEAPON_ABILITY} 1 ({ETresAbilityKind.PRIZE_DRAW})'
    WEP_KEYBLADE_SO_01_ABILITY_1_DEFENDER = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_01} {WEAPON_ABILITY} 1 ({ETresAbilityKind.DEFENDER})'
    WEP_KEYBLADE_SO_02_ABILITY_1_MAGIC_DRAW = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_02} {WEAPON_ABILITY} 1 ({ETresAbilityKind.MAGIC_DRAW})'
    WEP_KEYBLADE_SO_03_ABILITY_1_LUCK_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_02} {WEAPON_ABILITY} 1 ({ETresAbilityKind.LUCK_UP})'
    WEP_KEYBLADE_SO_04_ABILITY_1_LEAF_VEIL = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_04} {WEAPON_ABILITY} 1 ({ETresAbilityKind.LEAF_VEIL})'
    WEP_KEYBLADE_SO_05_ABILITY_1_FP_CONVERTER = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_05} {WEAPON_ABILITY} 1 ({ETresAbilityKind.FP_CONVERTER})'
    WEP_KEYBLADE_SO_06_ABILITY_1_FREEZE_GUARD = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_06} {WEAPON_ABILITY} 1 ({ETresAbilityKind.FREEZE_GUARD})'
    WEP_KEYBLADE_SO_07_ABILITY_1_HARVEST = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_07} {WEAPON_ABILITY} 1 ({ETresAbilityKind.HARVEST})'
    WEP_KEYBLADE_SO_08_ABILITY_1_STUN_GUARD = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_08} {WEAPON_ABILITY} 1 ({ETresAbilityKind.STUN_GUARD})'
    WEP_KEYBLADE_SO_09_ABILITY_1_WATAGAN = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_09} {WEAPON_ABILITY} 1 ({ETresAbilityKind.WATAGAN})'
    WEP_KEYBLADE_SO_11_ABILITY_1_WIZZARD_STAR = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_11} {WEAPON_ABILITY} 1 ({ETresAbilityKind.WIZZARD_STAR})'
    WEP_KEYBLADE_SO_12_ABILITY_1_MP_HASTE = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_12} {WEAPON_ABILITY} 1 ({ETresAbilityKind.MP_HASTE})'
    WEP_KEYBLADE_SO_13_ABILITY_1_MP_CONVERTER = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_13} {WEAPON_ABILITY} 1 ({ETresAbilityKind.MP_CONVERTER})'
    WEP_KEYBLADE_SO_14_ABILITY_1_HP_CONVERTER = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_14} {WEAPON_ABILITY} 1 ({ETresAbilityKind.HP_CONVERTER})'
    WEP_KEYBLADE_SO_15_ABILITY_1_FORM_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_15} {WEAPON_ABILITY} 1 ({ETresAbilityKind.FORM_UP})'
    WEP_KEYBLADE_SO_15_ABILITY_2_COMBO_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_15} {WEAPON_ABILITY} 2 ({ETresAbilityKind.COMBO_UP})'
    WEP_KEYBLADE_SO_15_ABILITY_3_AIRCOMBO_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_15} {WEAPON_ABILITY} 3 ({ETresAbilityKind.AIRCOMBO_UP})'
    WEP_KEYBLADE_SO_18_ABILITY_1_MP_HASTE = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_18} {WEAPON_ABILITY} 1 ({ETresAbilityKind.MP_HASTE})'
    WEP_KEYBLADE_SO_19_ABILITY_1_LUCK_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_19} {WEAPON_ABILITY} 1 ({ETresAbilityKind.LUCK_UP})'
    WEP_KEYBLADE_SO_19_ABILITY_2_MAGIC_ROULETTE = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_19} {WEAPON_ABILITY} 2 ({ETresAbilityKind.MAGIC_ROULETTE})'
    
    PRT_ITEM01_ABILITY_1_BATTLE_GRAPHER = f'{ETresItemDefProtector.PRT_ITEM01} {ARMOR_ABILITY} 1 ({ETresAbilityKind.BATTLE_GRAPHER})'
    PRT_ITEM02_ABILITY_1_ITEM_UP = f'{ETresItemDefProtector.PRT_ITEM02} {ARMOR_ABILITY} 1 ({ETresAbilityKind.ITEM_UP})'
    PRT_ITEM11_ABILITY_1_FIRE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM11} {ARMOR_ABILITY} 1 ({ETresAbilityKind.FIRE_ASPIR})'
    PRT_ITEM12_ABILITY_1_FIRE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM12} {ARMOR_ABILITY} 1 ({ETresAbilityKind.FIRE_ASPIR})'
    PRT_ITEM13_ABILITY_1_FIRE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM13} {ARMOR_ABILITY} 1 ({ETresAbilityKind.FIRE_ASPIR})'
    PRT_ITEM14_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM14} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    PRT_ITEM15_ABILITY_1_BLIZZARD_ASPIR = f'{ETresItemDefProtector.PRT_ITEM15} {ARMOR_ABILITY} 1 ({ETresAbilityKind.BLIZZARD_ASPIR})'
    PRT_ITEM16_ABILITY_1_BLIZZARD_ASPIR = f'{ETresItemDefProtector.PRT_ITEM16} {ARMOR_ABILITY} 1 ({ETresAbilityKind.BLIZZARD_ASPIR})'
    PRT_ITEM17_ABILITY_1_BLIZZARD_ASPIR = f'{ETresItemDefProtector.PRT_ITEM17} {ARMOR_ABILITY} 1 ({ETresAbilityKind.BLIZZARD_ASPIR})'
    PRT_ITEM18_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM18} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    PRT_ITEM19_ABILITY_1_THUNDER_ASPIR = f'{ETresItemDefProtector.PRT_ITEM19} {ARMOR_ABILITY} 1 ({ETresAbilityKind.THUNDER_ASPIR})'
    PRT_ITEM20_ABILITY_1_THUNDER_ASPIR = f'{ETresItemDefProtector.PRT_ITEM20} {ARMOR_ABILITY} 1 ({ETresAbilityKind.THUNDER_ASPIR})'
    PRT_ITEM21_ABILITY_1_THUNDER_ASPIR = f'{ETresItemDefProtector.PRT_ITEM21} {ARMOR_ABILITY} 1 ({ETresAbilityKind.THUNDER_ASPIR})'
    PRT_ITEM22_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM22} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    PRT_ITEM23_ABILITY_1_DARK_ASPIR = f'{ETresItemDefProtector.PRT_ITEM23} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DARK_ASPIR})'
    PRT_ITEM24_ABILITY_1_DARK_ASPIR = f'{ETresItemDefProtector.PRT_ITEM24} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DARK_ASPIR})'
    PRT_ITEM25_ABILITY_1_DARK_ASPIR = f'{ETresItemDefProtector.PRT_ITEM25} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DARK_ASPIR})'
    PRT_ITEM26_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM26} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    PRT_ITEM27_ABILITY_1_WATER_ASPIR = f'{ETresItemDefProtector.PRT_ITEM27} {ARMOR_ABILITY} 1 ({ETresAbilityKind.WATER_ASPIR})'
    PRT_ITEM28_ABILITY_1_WATER_ASPIR = f'{ETresItemDefProtector.PRT_ITEM28} {ARMOR_ABILITY} 1 ({ETresAbilityKind.WATER_ASPIR})'
    PRT_ITEM29_ABILITY_1_WATER_ASPIR = f'{ETresItemDefProtector.PRT_ITEM29} {ARMOR_ABILITY} 1 ({ETresAbilityKind.WATER_ASPIR})'
    PRT_ITEM30_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM30} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    PRT_ITEM31_ABILITY_1_AERO_ASPIR = f'{ETresItemDefProtector.PRT_ITEM31} {ARMOR_ABILITY} 1 ({ETresAbilityKind.AERO_ASPIR})'
    PRT_ITEM32_ABILITY_1_AERO_ASPIR = f'{ETresItemDefProtector.PRT_ITEM32} {ARMOR_ABILITY} 1 ({ETresAbilityKind.AERO_ASPIR})'
    PRT_ITEM33_ABILITY_1_AERO_ASPIR = f'{ETresItemDefProtector.PRT_ITEM33} {ARMOR_ABILITY} 1 ({ETresAbilityKind.AERO_ASPIR})'
    PRT_ITEM34_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM34} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    PRT_ITEM38_ABILITY_1_FIRE_ASPIR = f'{ETresItemDefProtector.PRT_ITEM38} {ARMOR_ABILITY} 1 ({ETresAbilityKind.FIRE_ASPIR})'
    PRT_ITEM39_ABILITY_1_BLIZZARD_ASPIR = f'{ETresItemDefProtector.PRT_ITEM39} {ARMOR_ABILITY} 1 ({ETresAbilityKind.BLIZZARD_ASPIR})'
    PRT_ITEM40_ABILITY_1_THUNDER_ASPIR = f'{ETresItemDefProtector.PRT_ITEM40} {ARMOR_ABILITY} 1 ({ETresAbilityKind.THUNDER_ASPIR})'
    PRT_ITEM41_ABILITY_1_DARK_ASPIR = f'{ETresItemDefProtector.PRT_ITEM41} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DARK_ASPIR})'
    PRT_ITEM45_ABILITY_1_BURN_GUARD = f'{ETresItemDefProtector.PRT_ITEM45} {ARMOR_ABILITY} 1 ({ETresAbilityKind.BURN_GUARD})'
    PRT_ITEM46_ABILITY_1_CLOUD_GUARD = f'{ETresItemDefProtector.PRT_ITEM46} {ARMOR_ABILITY} 1 ({ETresAbilityKind.CLOUD_GUARD})'
    PRT_ITEM47_ABILITY_1_SNEEZE_GUARD = f'{ETresItemDefProtector.PRT_ITEM47} {ARMOR_ABILITY} 1 ({ETresAbilityKind.SNEEZE_GUARD})'
    PRT_ITEM48_ABILITY_1_FREEZE_GUARD = f'{ETresItemDefProtector.PRT_ITEM48} {ARMOR_ABILITY} 1 ({ETresAbilityKind.FREEZE_GUARD})'
    PRT_ITEM49_ABILITY_1_DISCHARGE_GUARD = f'{ETresItemDefProtector.PRT_ITEM49} {ARMOR_ABILITY} 1 ({ETresAbilityKind.DISCHARGE_GUARD})'

    ACC_ITEM01_ABILITY_1_WALK_REGENE = f'{ETresItemDefAccessory.ACC_ITEM01} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WALK_REGENE})'
    ACC_ITEM02_ABILITY_1_WALK_HEALING = f'{ETresItemDefAccessory.ACC_ITEM02} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WALK_HEALING})'
    ACC_ITEM13_ABILITY_1_POWER_CURE = f'{ETresItemDefAccessory.ACC_ITEM13} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.POWER_CURE})'
    ACC_ITEM14_ABILITY_1_POWER_CURE = f'{ETresItemDefAccessory.ACC_ITEM14} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.POWER_CURE})'
    ACC_ITEM15_ABILITY_1_POWER_CURE = f'{ETresItemDefAccessory.ACC_ITEM15} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.POWER_CURE})'
    ACC_ITEM16_ABILITY_1_POWER_CURE = f'{ETresItemDefAccessory.ACC_ITEM16} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.POWER_CURE})'
    ACC_ITEM18_ABILITY_1_MP_LEAVE = f'{ETresItemDefAccessory.ACC_ITEM18} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_LEAVE})'
    ACC_ITEM19_ABILITY_1_FULLMP_BURST = f'{ETresItemDefAccessory.ACC_ITEM19} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.FULLMP_BURST})'
    ACC_ITEM20_ABILITY_1_MP_HASTE = f'{ETresItemDefAccessory.ACC_ITEM20} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_HASTE})'
    ACC_ITEM21_ABILITY_1_WIZZARD_STAR = f'{ETresItemDefAccessory.ACC_ITEM21} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WIZZARD_STAR})'
    ACC_ITEM22_ABILITY_1_MP_HASTE = f'{ETresItemDefAccessory.ACC_ITEM22} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_HASTE})'
    ACC_ITEM23_ABILITY_1_MP_HASTE = f'{ETresItemDefAccessory.ACC_ITEM23} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_HASTE})'
    ACC_ITEM24_ABILITY_1_MP_HASTE = f'{ETresItemDefAccessory.ACC_ITEM24} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_HASTE})'
    ACC_ITEM25_ABILITY_1_HP_CONVERTER = f'{ETresItemDefAccessory.ACC_ITEM25} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.HP_CONVERTER})'
    ACC_ITEM26_ABILITY_1_MP_CONVERTER = f'{ETresItemDefAccessory.ACC_ITEM26} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_CONVERTER})'
    ACC_ITEM27_ABILITY_1_MUNNY_CONVERTER = f'{ETresItemDefAccessory.ACC_ITEM27} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MUNNY_CONVERTER})'
    ACC_ITEM28_ABILITY_1_PRIZE_DRAW = f'{ETresItemDefAccessory.ACC_ITEM28} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.PRIZE_DRAW})'
    ACC_ITEM29_ABILITY_1_FIRE_UP = f'{ETresItemDefAccessory.ACC_ITEM29} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.FIRE_UP})'
    ACC_ITEM30_ABILITY_1_THUNDER_UP = f'{ETresItemDefAccessory.ACC_ITEM30} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.THUNDER_UP})'
    ACC_ITEM31_ABILITY_1_ENDLESS_MAGIC = f'{ETresItemDefAccessory.ACC_ITEM31} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.ENDLESS_MAGIC})'
    ACC_ITEM31_ABILITY_2_MP_HASTEGA = f'{ETresItemDefAccessory.ACC_ITEM31} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.MP_HASTEGA})'
    ACC_ITEM32_ABILITY_1_DEFENDER = f'{ETresItemDefAccessory.ACC_ITEM32} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DEFENDER})'
    ACC_ITEM33_ABILITY_1_DEFENDER = f'{ETresItemDefAccessory.ACC_ITEM33} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DEFENDER})'
    ACC_ITEM34_ABILITY_1_MAGIC_DRAW = f'{ETresItemDefAccessory.ACC_ITEM34} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MAGIC_DRAW})'
    ACC_ITEM35_ABILITY_1_MAGIC_DRAW = f'{ETresItemDefAccessory.ACC_ITEM35} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MAGIC_DRAW})'
    ACC_ITEM36_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM36} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    ACC_ITEM37_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM37} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    ACC_ITEM38_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM38} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    ACC_ITEM39_ABILITY_1_MP_HASTEGA = f'{ETresItemDefAccessory.ACC_ITEM39} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_HASTEGA})'
    ACC_ITEM40_ABILITY_1_WATER_UP = f'{ETresItemDefAccessory.ACC_ITEM40} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WATER_UP})'
    ACC_ITEM40_ABILITY_2_WATAGAN = f'{ETresItemDefAccessory.ACC_ITEM40} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.WATAGAN})'
    ACC_ITEM41_ABILITY_1_THUNDER_UP = f'{ETresItemDefAccessory.ACC_ITEM41} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WATER_UP})'
    ACC_ITEM41_ABILITY_2_THUNDAGAN = f'{ETresItemDefAccessory.ACC_ITEM41} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.THUNDAGAN})'
    ACC_ITEM42_ABILITY_1_FIRE_UP = f'{ETresItemDefAccessory.ACC_ITEM42} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.FIRE_UP})'
    ACC_ITEM42_ABILITY_2_FIRAGAN = f'{ETresItemDefAccessory.ACC_ITEM42} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.FIRAGAN})'
    ACC_ITEM43_ABILITY_1_AERO_UP = f'{ETresItemDefAccessory.ACC_ITEM43} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.AERO_UP})'
    ACC_ITEM43_ABILITY_2_AEROGAN = f'{ETresItemDefAccessory.ACC_ITEM43} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.AEROGAN})'
    ACC_ITEM44_ABILITY_1_BLIZZARD_UP = f'{ETresItemDefAccessory.ACC_ITEM44} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.BLIZZARD_UP})'
    ACC_ITEM44_ABILITY_2_BLIZZAGAN = f'{ETresItemDefAccessory.ACC_ITEM44} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.BLIZZAGAN})'
    ACC_ITEM45_ABILITY_1_FIRE_UP = f'{ETresItemDefAccessory.ACC_ITEM45} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.FIRE_UP})'
    ACC_ITEM45_ABILITY_2_BLIZZARD_UP = f'{ETresItemDefAccessory.ACC_ITEM45} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.BLIZZARD_UP})'
    ACC_ITEM45_ABILITY_3_THUNDER_UP = f'{ETresItemDefAccessory.ACC_ITEM45} {ACCESSOR_ABILITY} 3 ({ETresAbilityKind.THUNDER_UP})'
    ACC_ITEM46_ABILITY_1_WATER_UP = f'{ETresItemDefAccessory.ACC_ITEM46} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WATER_UP})'
    ACC_ITEM46_ABILITY_2_AERO_UP = f'{ETresItemDefAccessory.ACC_ITEM46} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.AERO_UP})'
    ACC_ITEM46_ABILITY_3_MP_HASTE = f'{ETresItemDefAccessory.ACC_ITEM46} {ACCESSOR_ABILITY} 3 ({ETresAbilityKind.MP_HASTE})'
    ACC_ITEM47_ABILITY_1_HARVEST = f'{ETresItemDefAccessory.ACC_ITEM47} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.HARVEST})'
    ACC_ITEM47_ABILITY_2_CHARISMA_CHEF = f'{ETresItemDefAccessory.ACC_ITEM47} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.CHARISMA_CHEF})'
    ACC_ITEM48_ABILITY_1_MASTER_DRAW = f'{ETresItemDefAccessory.ACC_ITEM48} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MASTER_DRAW})'
    ACC_ITEM49_ABILITY_1_LUCK_UP = f'{ETresItemDefAccessory.ACC_ITEM49} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.LUCK_UP})'
    ACC_ITEM50_ABILITY_1_MP_SAVE = f'{ETresItemDefAccessory.ACC_ITEM50} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_SAVE})'
    ACC_ITEM50_ABILITY_2_MP_HASTERA = f'{ETresItemDefAccessory.ACC_ITEM50} {ACCESSOR_ABILITY} 2 ({ETresAbilityKind.MP_HASTERA})'
    ACC_ITEM81_ABILITY_1_DEFENDER = f'{ETresItemDefAccessory.ACC_ITEM81} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DEFENDER})'
    ACC_ITEM82_ABILITY_1_MP_LEAVE = f'{ETresItemDefAccessory.ACC_ITEM82} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_LEAVE})'
    ACC_ITEM83_ABILITY_1_FULLMP_BURST = f'{ETresItemDefAccessory.ACC_ITEM83} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.FULLMP_BURST})'
    ACC_ITEM84_ABILITY_1_LUCK_UP = f'{ETresItemDefAccessory.ACC_ITEM84} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.LUCK_UP})'
    ACC_ITEM88_ABILITY_1_BURN_GUARD = f'{ETresItemDefAccessory.ACC_ITEM88} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.BURN_GUARD})'
    ACC_ITEM89_ABILITY_1_CLOUD_GUARD = f'{ETresItemDefAccessory.ACC_ITEM89} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.CLOUD_GUARD})'
    ACC_ITEM90_ABILITY_1_SNEEZE_GUARD = f'{ETresItemDefAccessory.ACC_ITEM90} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.SNEEZE_GUARD})'
    ACC_ITEM91_ABILITY_1_FREEZE_GUARD = f'{ETresItemDefAccessory.ACC_ITEM91} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.FREEZE_GUARD})'
    ACC_ITEM92_ABILITY_1_DISCHARGE_GUARD = f'{ETresItemDefAccessory.ACC_ITEM92} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DISCHARGE_GUARD})'
    ACC_ITEM93_ABILITY_1_BLIZZARD_UP = f'{ETresItemDefAccessory.ACC_ITEM93} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.BLIZZARD_UP})'
    ACC_ITEM94_ABILITY_1_WATER_UP = f'{ETresItemDefAccessory.ACC_ITEM94} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WATER_UP})'
    ACC_ITEM95_ABILITY_1_MAGIC_DRAW = f'{ETresItemDefAccessory.ACC_ITEM95} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MAGIC_DRAW})'
    ACC_ITEM96_ABILITY_1_LAST_LEAVE = f'{ETresItemDefAccessory.ACC_ITEM96} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.LAST_LEAVE})'
    ACC_ITEM97_ABILITY_1_STUN_GUARD = f'{ETresItemDefAccessory.ACC_ITEM97} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.STUN_GUARD})'
    ACC_ITEM98_ABILITY_1_ITEM_UP = f'{ETresItemDefAccessory.ACC_ITEM98} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.ITEM_UP})'
    ACC_ITEM99_ABILITY_1_FIRE_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM99} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.FIRE_ASPIR})'
    ACC_ITEM100_ABILITY_1_BLIZZARD_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM100} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.BLIZZARD_ASPIR})'
    ACC_ITEM101_ABILITY_1_THUNDER_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM101} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.THUNDER_ASPIR})'
    ACC_ITEM102_ABILITY_1_WATER_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM102} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WATER_ASPIR})'
    ACC_ITEM103_ABILITY_1_AERO_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM103} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.AERO_ASPIR})'
    ACC_ITEM104_ABILITY_1_AERO_UP = f'{ETresItemDefAccessory.ACC_ITEM104} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.AERO_UP})'
    ACC_ITEM105_ABILITY_1_WIZZARD_STAR = f'{ETresItemDefAccessory.ACC_ITEM105} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.WIZZARD_STAR})'
    ACC_ITEM106_ABILITY_1_COMBO_LEAVE = f'{ETresItemDefAccessory.ACC_ITEM106} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.COMBO_LEAVE})'
    ACC_ITEM107_ABILITY_1_DAMAGE_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM107} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DAMAGE_ASPIR})'
    ACC_ITEM110_ABILITY_1_DARK_ASPIR = f'{ETresItemDefAccessory.ACC_ITEM110} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.DARK_ASPIR})'
    ACC_ITEM111_ABILITY_1_POWER_CURE = f'{ETresItemDefAccessory.ACC_ITEM111} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.POWER_CURE})'
    ACC_ITEM112_ABILITY_1_MP_HASTEGA = f'{ETresItemDefAccessory.ACC_ITEM112} {ACCESSOR_ABILITY} 1 ({ETresAbilityKind.MP_HASTEGA})'
    
    @classmethod
    def generate_locations(cls):
        locations = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue
            
            if key.startswith("WEP_KEYBLADE_SO"):
                locations.append(LocationData(value, key, TresWorldData.INITIAL, TresAreaData.INITIAL, cls.WEAPON_ABILITY))
            elif key.startswith("PRT_ITEM"):
                locations.append(LocationData(value, key, TresWorldData.INITIAL, TresAreaData.INITIAL, cls.ARMOR_ABILITY))
            elif key.startswith("ACC_ITEM"):
                locations.append(LocationData(value, key, TresWorldData.INITIAL, TresAreaData.INITIAL, cls.ACCESSOR_ABILITY))

        return locations

class TresEventDataLocation(KingdomHeartsIIILocation):
    """
    """
    PREFIX = 'gameflow_'
    EVENT = 'Event'

    # THESE ARE KIND OF NOT NEEDED SINCE WE TRIGGER OFF THE ITEM NAME WINDOW
    #   BUT FOR DOCUMENTATION SAKE WILL LIST HERE
    HE_HEV_FACTORY = 'Solve Secluded Forge Puzzle' # Boolean = 1
    HE_Sub_Got_GoldenHeracules_01 = 'Obtain 1 Golden Hercules Statue' # Boolean = 1
    HE_Sub_Got_GoldenHeracules_02 = 'Obtain 2 Golden Hercules Statues' # Boolean = 1
    HE_Sub_Got_GoldenHeracules_03 = 'Obtain 3 Golden Hercules Statues' # Boolean = 1
    HE_Sub_Got_GoldenHeracules_04 = 'Obtain 4 Golden Hercules Statues' # Boolean = 1
    HE_Sub_Got_GoldenHeracules_05 = 'Obtain 5 Golden Hercules Statues' # Boolean = 1
    HE_Sub_HeraculesBoy_End = 'Find All Golden Hercules Statues' # String Flag = HE_Sub_HeraculesBoy_End
    # TODO: How is this going to work? These all need to be completed before reward received
    # BX_CE_SAVE_GOGO = 'Save GoGo from Darkubes'
    # BX_CE_SAVE_HONEY = 'Save Honey from Darkubes'
    # BX_CE_SAVE_WASABI = 'Save Wasabi from Darkubes'
    # BX_CE_SAVE_FRED = 'Save Fred from Darkubes'
    BX_SAVE_FRIENDS = 'Save GoGo, Honey, Wasabi and Fred from Darkubes'
    MI_Sub_mi_02_COMICAL_02 = 'Complete Making Boo Laugh' # Boolean = 1
    HE_END = 'Complete Olympus World' # String Flag = HE_END
    TT_LSI_GAME_MICKEY_PILOT = 'Scan code to receive Mickey, the Mail Pilot (Classic Kingdom)'
    TT_LSI_GAME_MUSICAL_FARMER = 'Scan code to receive The Musical Farmer (Classic Kingdom)'
    TT_LSI_GAME_BUILDING = 'Scan code to receive Building a Building (Classic Kingdom)'
    TT_LSI_GAME_MAD_DOCTOR = 'Scan code to receive Mad Doctor (Classic Kingdom)'
    TT_END_KEYBLADE = 'Complete Twilight Town World (Keyblade)' # String Flag = TT_END
    TT_END_LSI = 'Complete Twilight Town World (Classic Kingdom)'
    TS_END = 'Complete Toy Box World' # String Flag = TS_END
    RA_END = 'Complete Kingdom of Corona World' # String Flag = RA_END
    MI_END = 'Complete Monstropolis World' # String Flag = MI_END
    FZ_END = 'Complete Arendelle World' # String Flag = FZ_END
    PO_END = 'Complete 100 Acre Wood World' # String Flag = PO_END
    BX_END = 'Complete San Fransokyo World' # String Flag = BX_END
    CA_END = 'Complete Caribbean World' # String Flag = CA_END
    EX_minigame_Remy = 'Obtain 5 Star Rating at Le Grand Bistro' # String Flag = CA_END
    # TODO: Not sure this event name
    EX_GET_CLASSIC_TONE = 'Get a High Score in Each Classic Kingdom Game'
    # TODO: Not sure this event name + This probably would not occur
    # GET_OATHKEEPER = 'Complete Game After Finding All Lucky Emblems'
    # TODO: Not sure this event name + This cannot happen
    # GET_OBLIVION = 'Complete Game On Critical'
    KG_got_Starlight = 'Meet Ephemer in The Keyblade Graveyard'
    YT_EVENT2_KEY_ITEM06 = 'Obtain After First Mysterious Tower Visit' # Flag = [One of YT_EVENT2, YT_EVENT3, YT_EVENT4]
    TS_Sub_GAM1_EVENT9 = 'Complete Verum Rex: Beat of Lead'
    BX_BRIDGE_MISSION1 = 'Defend the San Fransokyo Bridge'
    MI_PLANT_BATTLE3 = 'Put Out the Fires in Monstropolis'
    # TODO: Need to determine which battle portals are used
    HE_BATTLEPORTAL_ex_21_CLEARED_ACC_ITEM42 = f'(Mount Olympus - Lobby) Battle Portal 1 Clear ({ETresItemDefAccessory.ACC_ITEM42})'
    HE_BATTLEPORTAL_ex_21_CLEARED_REPORT_ITEM01 = f'(Mount Olympus - Lobby) Battle Portal 1 Clear ({ETresItemDefReport.REPORT_ITEM01})'
    HE_BATTLEPORTAL_ex_22_CLEARED_PRT_ITEM10 = f'(Mount Olympus - Boss Arena) Battle Portal 2 Clear ({ETresItemDefProtector.PRT_ITEM10})'
    HE_BATTLEPORTAL_ex_22_CLEARED_REPORT_ITEM02 = f'(Mount Olympus - Boss Arena) Battle Portal 2 Clear ({ETresItemDefReport.REPORT_ITEM02})'
    TT_BATTLEPORTAL_ex_23_CLEARED_MAT_ITEM59 = f'(Twilight Town - Old Mansion) Battle Portal 3 Clear ({ETresItemDefMaterial.MAT_ITEM59})'
    TT_BATTLEPORTAL_ex_23_CLEARED_REPORT_ITEM03 = f'(Twilight Town - Old Mansion) Battle Portal 3 Clear ({ETresItemDefReport.REPORT_ITEM03})'
    TT_BATTLEPORTAL_ex_24_CLEARED_ITEM_LASTELIXIR = f'(Toy Box - Kid Korral Vent) Battle Portal 4 Clear ({ETresItemDefBattleItem.ITEM_LASTELIXIR})'
    TT_BATTLEPORTAL_ex_24_CLEARED_REPORT_ITEM04 = f'(Toy Box - Kid Korral Vent) Battle Portal 4 Clear ({ETresItemDefReport.REPORT_ITEM04})'
    TT_BATTLEPORTAL_ex_25_CLEARED_ACC_ITEM41 = f'(Toy Box - Lobby Ground Floor) Battle Portal 5 Clear ({ETresItemDefAccessory.ACC_ITEM41})'
    TT_BATTLEPORTAL_ex_25_CLEARED_REPORT_ITEM05 = f'(Toy Box - Lobby Ground Floor) Battle Portal 5 Clear ({ETresItemDefReport.REPORT_ITEM05})'
    RA_BATTLEPORTAL_ex_26_CLEARED_MAT_ITEM60 = f'(Kingdom of Corona - Mini-boss Area) Battle Portal 6 Clear ({ETresItemDefMaterial.MAT_ITEM60})'
    RA_BATTLEPORTAL_ex_26_CLEARED_REPORT_ITEM06 = f'(Kingdom of Corona - Mini-boss Area) Battle Portal 6 Clear ({ETresItemDefReport.REPORT_ITEM06})'
    RA_BATTLEPORTAL_ex_27_CLEARED_ACC_ITEM43 = f'(Kingdom of Corona - The Forest) Battle Portal 7 Clear ({ETresItemDefAccessory.ACC_ITEM43})'
    RA_BATTLEPORTAL_ex_27_CLEARED_REPORT_ITEM07 = f'(Kingdom of Corona - The Forest) Battle Portal 7 Clear ({ETresItemDefReport.REPORT_ITEM07})'
    # BATTLEPORTAL_ex_28_CLEARED = 'Battle Portal 8 Clear'
    MI_BATTLEPORTAL_ex_29_CLEARED_MAT_ITEM60 = f'(Monstropolis - Tank Yard) Battle Portal 8 Clear ({ETresItemDefMaterial.MAT_ITEM60})'
    MI_BATTLEPORTAL_ex_29_CLEARED_REPORT_ITEM08 = f'(Monstropolis - Tank Yard) Battle Portal 8 Clear ({ETresItemDefReport.REPORT_ITEM08})'
    # BATTLEPORTAL_ex_30_CLEARED = 'Battle Portal 10 Clear'
    FZ_BATTLEPORTAL_ex_31_CLEARED_MAT_ITEM59 = f'(Arendelle - The Gorge) Battle Portal 9 Clear ({ETresItemDefMaterial.MAT_ITEM59})'
    FZ_BATTLEPORTAL_ex_31_CLEARED_REPORT_ITEM09 = f'(Arendelle - The Gorge) Battle Portal 9 Clear ({ETresItemDefReport.REPORT_ITEM09})'
    # BATTLEPORTAL_ex_32_CLEARED = 'Battle Portal 12 Clear'
    CA_BATTLEPORTAL_ex_33_CLEARED_ACC_ITEM40 = f'(Caribbean - The Huddled Isles) Battle Portal 10 Clear ({ETresItemDefAccessory.ACC_ITEM40})'
    CA_BATTLEPORTAL_ex_33_CLEARED_REPORT_ITEM10 = f'(Caribbean - The Huddled Isles) Battle Portal 10 Clear ({ETresItemDefReport.REPORT_ITEM10})'
    BX_BATTLEPORTAL_ex_34_CLEARED_ACC_ITEM46 = f'(San Fransokyo - North District [Day]) Battle Portal 11 Clear ({ETresItemDefAccessory.ACC_ITEM46})'
    BX_BATTLEPORTAL_ex_34_CLEARED_REPORT_ITEM11 = f'(San Fransokyo - North District [Day]) Battle Portal 11 Clear ({ETresItemDefReport.REPORT_ITEM11})'
    BX_BATTLEPORTAL_ex_35_CLEARED_ACC_ITEM44 = f'(San Fransokyo - Central District) Battle Portal 12 Clear ({ETresItemDefAccessory.ACC_ITEM44})'
    BX_BATTLEPORTAL_ex_35_CLEARED_REPORT_ITEM12 = f'(San Fransokyo - Central District) Battle Portal 12 Clear ({ETresItemDefReport.REPORT_ITEM12})'
    # BATTLEPORTAL_ex_36_CLEARED = 'Battle Portal 16 Clear'
    KG_BATTLEPORTAL_ex_37_CLEARED_ACC_ITEM45 = f'(Keyblade Graveyard - Badlands Entrance) Battle Portal 13 Clear ({ETresItemDefAccessory.ACC_ITEM45})'
    KG_BATTLEPORTAL_ex_37_CLEARED_REPORT_ITEM13 = f'(Keyblade Graveyard - Badlands Entrance) Battle Portal 13 Clear ({ETresItemDefReport.REPORT_ITEM13})'
    KG_BATTLEPORTAL_ex_38_CLEARED_ACC_ITEM39 = f'(Keyblade Graveyard - Badlands Exit) Boss Battle Portal Clear ({ETresItemDefAccessory.ACC_ITEM39})'
    # KG_BATTLEPORTAL_ex_39_CLEARED = '(Keyblade Graveyard - Skein of Severance) Tutorial Battle Portal Clear'
    # BATTLEPORTAL_ex_40_CLEARED = 'Battle Portal 20 Clear'

    GM_EVENT2_KEY_ITEM02 = 'Obtain Gummiphone'

    SS_DLC_SUB_TRUEEND_END_ACC_ITEM112 = f'Defeat Yozora ({ETresItemDefAccessory.ACC_ITEM112})'
    SS_DLC_SUB_TRUEEND_END_KEY_ITEM14 = f'Defeat Yozora ({ETresItemDefKeyItem.KEY_ITEM14})'
    
    RG_DLC_SHU_BATTLE_10 = 'Defeat Data Battle 1'
    RG_DLC_SHU_BATTLE_11 = 'Defeat Data Battle 2'
    RG_DLC_SHU_BATTLE_12 = 'Defeat Data Battle 3'
    RG_DLC_SHU_BATTLE_13 = 'Defeat Data Battle 4'
    RG_DLC_SHU_BATTLE_14 = 'Defeat Data Battle 5'
    RG_DLC_SHU_BATTLE_15 = 'Defeat Data Battle 6'
    RG_DLC_SHU_BATTLE_16 = 'Defeat Data Battle 7'
    RG_DLC_SHU_BATTLE_17 = 'Defeat Data Battle 8'
    RG_DLC_SHU_BATTLE_18 = 'Defeat Data Battle 9'
    RG_DLC_SHU_BATTLE_19 = 'Defeat Data Battle 10'
    RG_DLC_SHU_BATTLE_20 = 'Defeat Data Battle 11'
    RG_DLC_SHU_BATTLE_21 = 'Defeat Data Battle 12'
    RG_DLC_SHU_BATTLE_22 = 'Defeat Data Battle 13'

    COMPLETE_GAME = 'Complete Game'
    
    @classmethod
    def generate_locations(cls):
        locations = []

        world_code_map = {
            "bt": TresWorldData.SCALA_AD_CAELUM,
            "bx": TresWorldData.SAN_FRANSOKYO,
            "ca": TresWorldData.THE_CARIBBEAN,
            "ew": TresWorldData.THE_FINAL_WORLD,
            "fz": TresWorldData.ARENDELLE,
            "he": TresWorldData.OLYMPUS,
            "kg": TresWorldData.KEYBLADE_GRAVEYARD,
            "mi": TresWorldData.MONSTROPOLIS,
            "ra": TresWorldData.KINGDOM_OF_CORONA,
            "ts": TresWorldData.TOY_BOX,
            "tt": TresWorldData.TWILIGHT_TOWN,
            "init": TresWorldData.UNKNOWN,
            "yt": TresWorldData.MYSTERIOUS_TOWER,
            "gm": TresWorldData.GUMMI_OCEAN
        }

        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue

            lowered_key = key.lower()

            for code, world in world_code_map.items():
                if code in lowered_key:
                    locations.append(LocationData(value, key, world, '', cls.EVENT))
                    break
        
        for location in locations:
            for key, value in TresAreaData.__dict__.items():
                if key.startswith("__"):
                    continue

                if value in location.loc_name:
                    location = location._replace(area_name=value)
                    break
        
        return locations

class TresFullcourseAbilityDataLocation(KingdomHeartsIIILocation):
    """
    """
    PREFIX = 'Food Ability'
    CUISINE_FULL_COURSE_BONUS = 'Cuisine Full Course Bonus'

    FOOD_ABILITY_LUNCH_TIME = f'{PREFIX} {ETresAbilityKind.LUNCH_TIME}'
    FOOD_ABILITY_POWER_LUNCH = f'{PREFIX} {ETresAbilityKind.POWER_LUNCH}'
    FOOD_ABILITY_OVER_TIME = f'{PREFIX} {ETresAbilityKind.OVER_TIME}'
    FOOD_ABILITY_PRIZE_FEEVER = f'{PREFIX} {ETresAbilityKind.PRIZE_FEEVER}'
    FOOD_ABILITY_FIRAGAN = f'{PREFIX} {ETresAbilityKind.FIRAGAN}'
    FOOD_ABILITY_BLIZZAGAN = f'{PREFIX} {ETresAbilityKind.BLIZZAGAN}'
    FOOD_ABILITY_BEST_CONDITION = f'{PREFIX} {ETresAbilityKind.BEST_CONDITION}'
    FOOD_ABILITY_EXP_BARGAIN = f'{PREFIX} {ETresAbilityKind.EXP_BARGAIN}'
    FOOD_ABILITY_THUNDAGAN = f'{PREFIX} {ETresAbilityKind.THUNDAGAN}'
    FOOD_ABILITY_WATAGAN = f'{PREFIX} {ETresAbilityKind.WATAGAN}'
    FOOD_ABILITY_AEROGAN = f'{PREFIX} {ETresAbilityKind.AEROGAN}'
    FOOD_ABILITY_MILLIONAIRE = f'{PREFIX} {ETresAbilityKind.MILLIONAIRE}'
    FOOD_ABILITY_CHARGE_BERSERK = f'{PREFIX} {ETresAbilityKind.CHARGE_BERSERK}'
    FOOD_ABILITY_GRAND_MAGIC = f'{PREFIX} {ETresAbilityKind.GRAND_MAGIC}'
    FOOD_ABILITY_CURAGAN = f'{PREFIX} {ETresAbilityKind.CURAGAN}'
    
    @classmethod
    def generate_locations(cls):
        locations = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue
            
            locations.append(LocationData(value, key, TresWorldData.TWILIGHT_TOWN, TresAreaData.LE_GRAND_BISTROT, cls.CUISINE_FULL_COURSE_BONUS))

        return locations

class TresSynthesisDataLocation(KingdomHeartsIIILocation):
    """
    """
    SYNTHESIS_ITEM = 'Synthesis Item'

    ITEM_SYNTHESIS_ITEM_ETHER = f'{SYNTHESIS_ITEM} {ETresItemDefBattleItem.ITEM_ETHER}'
    ITEM_SYNTHESIS_PRT_ITEM11 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM11}'
    ITEM_SYNTHESIS_PRT_ITEM38 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM38}'
    ITEM_SYNTHESIS_PRT_ITEM41 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM41}'
    ITEM_SYNTHESIS_ACC_ITEM04 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM04}'
    ITEM_SYNTHESIS_PRT_ITEM28 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM28}'
    ITEM_SYNTHESIS_PRT_ITEM19 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM19}'
    ITEM_SYNTHESIS_PRT_ITEM40 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM40}'
    ITEM_SYNTHESIS_ITEM_FOCUSSUPPLY = f'{SYNTHESIS_ITEM} {ETresItemDefBattleItem.ITEM_FOCUSSUPPLY}'
    ITEM_SYNTHESIS_MAT_ITEM33 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM33}'
    ITEM_SYNTHESIS_PRT_ITEM30 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM30}'
    ITEM_SYNTHESIS_ITEM_APUP = f'{SYNTHESIS_ITEM} {ETresItemDefCampItem.ITEM_APUP}'
    ITEM_SYNTHESIS_WEP_DONALD_03 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_DONALD_03}'
    ITEM_SYNTHESIS_WEP_GOOFY_03 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_GOOFY_03}'
    ITEM_SYNTHESIS_ACC_ITEM06 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM06}'
    ITEM_SYNTHESIS_ITEM_HIGHETHER = f'{SYNTHESIS_ITEM} {ETresItemDefBattleItem.ITEM_HIGHETHER}'
    ITEM_SYNTHESIS_ITEM_MEGAPOTION = f'{SYNTHESIS_ITEM} {ETresItemDefBattleItem.ITEM_MEGAPOTION}'
    ITEM_SYNTHESIS_PRT_ITEM23 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM23}'
    ITEM_SYNTHESIS_MAT_ITEM34 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM34}'
    ITEM_SYNTHESIS_WEP_GOOFY_07 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_GOOFY_07}'
    ITEM_SYNTHESIS_PRT_ITEM15 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM15}'
    ITEM_SYNTHESIS_PRT_ITEM16 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM16}'
    ITEM_SYNTHESIS_ACC_ITEM08 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM08}'
    ITEM_SYNTHESIS_ITEM_MEGAETHER = f'{SYNTHESIS_ITEM} {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    ITEM_SYNTHESIS_ITEM_POWERUP = f'{SYNTHESIS_ITEM} {ETresItemDefCampItem.ITEM_POWERUP}'
    ITEM_SYNTHESIS_ITEM_MAGICUP = f'{SYNTHESIS_ITEM} {ETresItemDefCampItem.ITEM_MAGICUP}'
    ITEM_SYNTHESIS_ITEM_GUARDUP = f'{SYNTHESIS_ITEM} {ETresItemDefCampItem.ITEM_GUARDUP}'
    ITEM_SYNTHESIS_PRT_ITEM12 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM12}'
    ITEM_SYNTHESIS_PRT_ITEM17 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM17}'
    ITEM_SYNTHESIS_PRT_ITEM20 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM20}'
    ITEM_SYNTHESIS_PRT_ITEM27 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM27}'
    ITEM_SYNTHESIS_PRT_ITEM31 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM31}'
    ITEM_SYNTHESIS_PRT_ITEM24 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM24}'
    ITEM_SYNTHESIS_WEP_DONALD_09 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_DONALD_09}'
    ITEM_SYNTHESIS_ITEM_HIGHFOCUSSUPPLY = f'{SYNTHESIS_ITEM} {ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY}'
    ITEM_SYNTHESIS_MAT_ITEM35 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM35}'
    ITEM_SYNTHESIS_ACC_ITEM15 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM15}'
    ITEM_SYNTHESIS_ACC_ITEM20 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM20}'
    ITEM_SYNTHESIS_PRT_ITEM13 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM13}'
    ITEM_SYNTHESIS_PRT_ITEM39 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM39}'
    ITEM_SYNTHESIS_PRT_ITEM21 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM21}'
    ITEM_SYNTHESIS_PRT_ITEM25 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM25}'
    ITEM_SYNTHESIS_PRT_ITEM38 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM38}'
    ITEM_SYNTHESIS_ITEM_ELIXIR = f'{SYNTHESIS_ITEM} {ETresItemDefBattleItem.ITEM_ELIXIR}'
    ITEM_SYNTHESIS_MAT_ITEM36 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM36}'
    ITEM_SYNTHESIS_PRT_ITEM07 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM07}'
    ITEM_SYNTHESIS_ACC_ITEM16 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM16}'
    ITEM_SYNTHESIS_ACC_ITEM21 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM21}'
    ITEM_SYNTHESIS_WEP_DONALD_11 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_DONALD_11}'
    ITEM_SYNTHESIS_WEP_GOOFY_11 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_GOOFY_11}'
    ITEM_SYNTHESIS_PRT_ITEM08 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM08}'
    ITEM_SYNTHESIS_PRT_ITEM43 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM43}'
    ITEM_SYNTHESIS_ITEM_LASTELIXIR = f'{SYNTHESIS_ITEM} {ETresItemDefBattleItem.ITEM_LASTELIXIR}'
    ITEM_SYNTHESIS_WEP_DONALD_12 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_DONALD_12}'
    ITEM_SYNTHESIS_WEP_GOOFY_12 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_GOOFY_12}'
    ITEM_SYNTHESIS_WEP_DONALD_13 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_DONALD_13}'
    ITEM_SYNTHESIS_WEP_GOOFY_13 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_GOOFY_13}'
    ITEM_SYNTHESIS_PRT_ITEM35 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM35}'
    ITEM_SYNTHESIS_WEP_KEYBLADE_SO_15 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_KEYBLADE_SO_15}'
    ITEM_SYNTHESIS_WEP_DONALD_14 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_DONALD_14}'
    ITEM_SYNTHESIS_WEP_GOOFY_14 = f'{SYNTHESIS_ITEM} {ETresItemDefWeapon.WEP_GOOFY_14}'
    ITEM_SYNTHESIS_PRT_ITEM45 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM45}'
    ITEM_SYNTHESIS_PRT_ITEM46 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM46}'
    ITEM_SYNTHESIS_ACC_ITEM32 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM32}'
    ITEM_SYNTHESIS_ACC_ITEM34 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM34}'
    ITEM_SYNTHESIS_PRT_ITEM47 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM47}'
    ITEM_SYNTHESIS_PRT_ITEM49 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM49}'
    ITEM_SYNTHESIS_ACC_ITEM11 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM11}'
    ITEM_SYNTHESIS_ACC_ITEM36 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM36}'
    ITEM_SYNTHESIS_PRT_ITEM14 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM14}'
    ITEM_SYNTHESIS_PRT_ITEM18 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM18}'
    ITEM_SYNTHESIS_PRT_ITEM22 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM22}'
    ITEM_SYNTHESIS_PRT_ITEM48 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM48}'
    ITEM_SYNTHESIS_ACC_ITEM37 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM37}'
    ITEM_SYNTHESIS_ACC_ITEM48 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM48}'
    ITEM_SYNTHESIS_PRT_ITEM29 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM29}'
    ITEM_SYNTHESIS_PRT_ITEM32 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM32}'
    ITEM_SYNTHESIS_ACC_ITEM33 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM33}'
    ITEM_SYNTHESIS_ACC_ITEM35 = f'{SYNTHESIS_ITEM} {ETresItemDefAccessory.ACC_ITEM35}'
    ITEM_SYNTHESIS_PRT_ITEM26 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM26}'
    ITEM_SYNTHESIS_PRT_ITEM36 = f'{SYNTHESIS_ITEM} {ETresItemDefProtector.PRT_ITEM36}'
    ITEM_SYNTHESIS_MAT_ITEM16 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM16}'
    ITEM_SYNTHESIS_MAT_ITEM44 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM44}'
    ITEM_SYNTHESIS_MAT_ITEM24 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM24}'
    ITEM_SYNTHESIS_MAT_ITEM20 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM20}'
    ITEM_SYNTHESIS_MAT_ITEM04 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM04}'
    ITEM_SYNTHESIS_MAT_ITEM08 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM08}'
    ITEM_SYNTHESIS_MAT_ITEM12 = f'{SYNTHESIS_ITEM} {ETresItemDefMaterial.MAT_ITEM12}'
    
    @classmethod
    def generate_locations(cls):
        locations = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue
            
            locations.append(LocationData(value, key, TresWorldData.TWILIGHT_TOWN, TresAreaData.MOOGLE_SYNTHESIS, cls.SYNTHESIS_ITEM))

        return locations

class TresLevelUpDataLocation(KingdomHeartsIIILocation):
    """
    """
    LEVEL_UP = 'Level Up'

    WARRIOR = '(Warrior)' # 1
    MYSTIC = '(Mystic)' # 2
    GUARDIAN = '(Guardian)' # 3

    # WE ONLY WANT 1 SET HERE SINCE ONLY ONE DECISION CAN BE MADE HERE THAT DISTRIBUTES THE REST

    LEVELUP_2_WARRIOR_COMBO_PLUS = f'{LEVEL_UP}  2 {WARRIOR} {ETresAbilityKind.COMBO_PLUS}'
    LEVELUP_2_MYSTIC_MAGIC_COMBO_SAVE = f'{LEVEL_UP}  2 {MYSTIC} {ETresAbilityKind.MAGIC_COMBO_SAVE}'
    LEVELUP_2_GUARDIAN_CRITICAL_HALF = f'{LEVEL_UP}   {MYSTIC} {ETresAbilityKind.CRITICAL_HALF}'
    
    LEVELUP_3_WARRIOR_PRIZE_DRAW = f'{LEVEL_UP}  3 {WARRIOR} {ETresAbilityKind.PRIZE_DRAW}'
    LEVELUP_3_MYSTIC_PRIZE_DRAW = f'{LEVEL_UP}  3 {MYSTIC} {ETresAbilityKind.PRIZE_DRAW}'
    LEVELUP_3_GUARDIAN_PRIZE_DRAW = f'{LEVEL_UP}  3 {MYSTIC} {ETresAbilityKind.PRIZE_DRAW}'

    LEVELUP_4_WARRIOR_AIRCOMBO_PLUS = f'{LEVEL_UP}  4 {WARRIOR} {ETresAbilityKind.AIRCOMBO_PLUS}'
    LEVELUP_4_MYSTIC_MP_HASTE = f'{LEVEL_UP} 4 {MYSTIC} {ETresAbilityKind.MP_HASTE}'
    LEVELUP_4_GUARDIAN_COMBO_LEAVE = f'{LEVEL_UP} 4 {MYSTIC} {ETresAbilityKind.COMBO_LEAVE}'

    LEVELUP_5_WARRIOR_AUTO_FINISH = f'{LEVEL_UP} 5 {WARRIOR} {ETresAbilityKind.AUTO_FINISH}'
    LEVELUP_5_MYSTIC_AUTO_FINISH = f'{LEVEL_UP} 5 {MYSTIC} {ETresAbilityKind.AUTO_FINISH}'
    LEVELUP_5_GUARDIAN_AUTO_FINISH = f'{LEVEL_UP} 5 {MYSTIC} {ETresAbilityKind.AUTO_FINISH}'

    LEVELUP_6_WARRIOR_MP_HASTE = f'{LEVEL_UP} 6 {WARRIOR} {ETresAbilityKind.MP_HASTE}'
    LEVELUP_6_MYSTIC_COMBO_PLUS = f'{LEVEL_UP} 6 {MYSTIC} {ETresAbilityKind.COMBO_PLUS}'
    LEVELUP_6_GUARDIAN_COMBO_PLUS = f'{LEVEL_UP} 6 {MYSTIC} {ETresAbilityKind.COMBO_PLUS}'

    LEVELUP_8_WARRIOR_UNISON_FIRE = f'{LEVEL_UP} 8 {WARRIOR} {ETresAbilityKind.UNISON_FIRE}'
    LEVELUP_8_MYSTIC_UNISON_FIRE = f'{LEVEL_UP} 8 {MYSTIC} {ETresAbilityKind.UNISON_FIRE}'
    LEVELUP_8_GUARDIAN_UNISON_FIRE = f'{LEVEL_UP} 8 {MYSTIC} {ETresAbilityKind.UNISON_FIRE}'

    LEVELUP_9_WARRIOR_COMBO_PLUS = f'{LEVEL_UP} 9 {WARRIOR} {ETresAbilityKind.COMBO_PLUS}'
    LEVELUP_9_MYSTIC_FIRE_UP = f'{LEVEL_UP} 9 {MYSTIC} {ETresAbilityKind.FIRE_UP}'
    LEVELUP_9_GUARDIAN_GUARD_REGENE = f'{LEVEL_UP} 9 {MYSTIC} {ETresAbilityKind.GUARD_REGENE}'

    LEVELUP_10_WARRIOR_FUSION_SPIN = f'{LEVEL_UP} 10 {WARRIOR} {ETresAbilityKind.FUSION_SPIN}'
    LEVELUP_10_MYSTIC_FUSION_SPIN = f'{LEVEL_UP} 10 {MYSTIC} {ETresAbilityKind.FUSION_SPIN}'
    LEVELUP_10_GUARDIAN_FUSION_SPIN = f'{LEVEL_UP} 10 {MYSTIC} {ETresAbilityKind.FUSION_SPIN}'

    LEVELUP_12_WARRIOR_ATTRACTION_UP = f'{LEVEL_UP} 12 {WARRIOR} {ETresAbilityKind.ATTRACTION_UP}'
    LEVELUP_12_MYSTIC_WATER_UP = f'{LEVEL_UP} 12 {MYSTIC} {ETresAbilityKind.WATER_UP}'
    LEVELUP_12_GUARDIAN_MP_HASTE = f'{LEVEL_UP} 12 {MYSTIC} {ETresAbilityKind.MP_HASTE}'

    LEVELUP_14_WARRIOR_FIRE_UP = f'{LEVEL_UP} 14 {WARRIOR} {ETresAbilityKind.FIRE_UP}'
    LEVELUP_14_MYSTIC_LEAF_VEIL = f'{LEVEL_UP} 14 {MYSTIC} {ETresAbilityKind.LEAF_VEIL}'
    LEVELUP_14_GUARDIAN_AIRCOMBO_PLUS = f'{LEVEL_UP} 14 {MYSTIC} {ETresAbilityKind.AIRCOMBO_PLUS}'

    LEVELUP_16_WARRIOR_AIRCOMBO_PLUS = f'{LEVEL_UP} 16 {WARRIOR} {ETresAbilityKind.AIRCOMBO_PLUS}'
    LEVELUP_16_MYSTIC_AIRCOMBO_PLUS = f'{LEVEL_UP} 16 {MYSTIC} {ETresAbilityKind.AIRCOMBO_PLUS}'
    LEVELUP_16_GUARDIAN_FIRE_UP = f'{LEVEL_UP} 16 {MYSTIC} {ETresAbilityKind.FIRE_UP}'

    LEVELUP_18_WARRIOR_WATER_UP = f'{LEVEL_UP} 18 {WARRIOR} {ETresAbilityKind.WATER_UP}'
    LEVELUP_18_MYSTIC_BLIZZARD_UP = f'{LEVEL_UP} 18 {MYSTIC} {ETresAbilityKind.BLIZZARD_UP}'
    LEVELUP_18_GUARDIAN_ATTRACTION_UP = f'{LEVEL_UP} 18 {MYSTIC} {ETresAbilityKind.ATTRACTION_UP}'

    LEVELUP_20_WARRIOR_COMBO_UP = f'{LEVEL_UP} 20 {WARRIOR} {ETresAbilityKind.COMBO_UP}'
    LEVELUP_20_MYSTIC_MAGIC_TIME = f'{LEVEL_UP} 20 {MYSTIC} {ETresAbilityKind.MAGIC_TIME}'
    LEVELUP_20_GUARDIAN_COUNTER_UP = f'{LEVEL_UP} 20 {MYSTIC} {ETresAbilityKind.COUNTER_UP}'

    LEVELUP_22_WARRIOR_ATTRACTION_TIME = f'{LEVEL_UP} 22 {WARRIOR} {ETresAbilityKind.ATTRACTION_TIME}'
    LEVELUP_22_MYSTIC_ATTRACTION_TIME = f'{LEVEL_UP} 22 {MYSTIC} {ETresAbilityKind.ATTRACTION_TIME}'
    LEVELUP_22_GUARDIAN_ATTRACTION_TIME = f'{LEVEL_UP} 22 {MYSTIC} {ETresAbilityKind.ATTRACTION_TIME}'

    LEVELUP_24_WARRIOR_AIRCOMBO_UP = f'{LEVEL_UP} 24 {WARRIOR} {ETresAbilityKind.AIRCOMBO_UP}'
    LEVELUP_24_MYSTIC_COUNTER_UP = f'{LEVEL_UP} 24 {MYSTIC} {ETresAbilityKind.COUNTER_UP}'
    LEVELUP_24_GUARDIAN_COMBO_PLUS = f'{LEVEL_UP} 24 {MYSTIC} {ETresAbilityKind.COMBO_PLUS}'

    LEVELUP_26_WARRIOR_COMBO_LEAVE = f'{LEVEL_UP} 26 {WARRIOR} {ETresAbilityKind.COMBO_LEAVE}'
    LEVELUP_26_MYSTIC_MAGIC_COMBO_UP = f'{LEVEL_UP} 26 {MYSTIC} {ETresAbilityKind.MAGIC_COMBO_UP}'
    LEVELUP_26_GUARDIAN_LEAF_VEIL = f'{LEVEL_UP} 26 {MYSTIC} {ETresAbilityKind.LEAF_VEIL}'

    LEVELUP_28_WARRIOR_LEAF_VEIL = f'{LEVEL_UP} 28 {WARRIOR} {ETresAbilityKind.LEAF_VEIL}'
    LEVELUP_28_MYSTIC_COMBO_LEAVE = f'{LEVEL_UP} 28 {MYSTIC} {ETresAbilityKind.COMBO_LEAVE}'
    LEVELUP_28_GUARDIAN_WATER_UP = f'{LEVEL_UP} 28 {MYSTIC} {ETresAbilityKind.WATER_UP}'

    LEVELUP_30_WARRIOR_BLIZZARD_UP = f'{LEVEL_UP} 30 {WARRIOR} {ETresAbilityKind.BLIZZARD_UP}'
    LEVELUP_30_MYSTIC_COMBO_PLUS = f'{LEVEL_UP} 30 {MYSTIC} {ETresAbilityKind.COMBO_PLUS}'
    LEVELUP_30_GUARDIAN_LAST_LEAVE = f'{LEVEL_UP} 30 {MYSTIC} {ETresAbilityKind.LAST_LEAVE}'

    LEVELUP_32_WARRIOR_LINK_BOOST = f'{LEVEL_UP} 32 {WARRIOR} {ETresAbilityKind.LINK_BOOST}'
    LEVELUP_32_MYSTIC_CRITICAL_HALF = f'{LEVEL_UP} 32 {MYSTIC} {ETresAbilityKind.CRITICAL_HALF}'
    LEVELUP_32_GUARDIAN_AIRCOMBO_PLUS = f'{LEVEL_UP} 32 {MYSTIC} {ETresAbilityKind.AIRCOMBO_PLUS}'

    LEVELUP_34_WARRIOR_THUNDER_UP = f'{LEVEL_UP} 34 {WARRIOR} {ETresAbilityKind.THUNDER_UP}'
    LEVELUP_34_MYSTIC_THUNDER_UP = f'{LEVEL_UP} 34 {MYSTIC} {ETresAbilityKind.THUNDER_UP}'
    LEVELUP_34_GUARDIAN_LINK_BOOST = f'{LEVEL_UP} 34 {MYSTIC} {ETresAbilityKind.LINK_BOOST}'

    LEVELUP_36_WARRIOR_GUARD_REGENE = f'{LEVEL_UP} 36 {WARRIOR} {ETresAbilityKind.GUARD_REGENE}'
    LEVELUP_36_MYSTIC_GUARD_REGENE = f'{LEVEL_UP} 36 {MYSTIC} {ETresAbilityKind.GUARD_REGENE}'
    LEVELUP_36_GUARDIAN_COMBO_UP = f'{LEVEL_UP} 36 {MYSTIC} {ETresAbilityKind.COMBO_UP}'

    LEVELUP_38_WARRIOR_AERO_UP = f'{LEVEL_UP} 38 {WARRIOR} {ETresAbilityKind.AERO_UP}'
    LEVELUP_38_MYSTIC_AERO_UP = f'{LEVEL_UP} 38 {MYSTIC} {ETresAbilityKind.AERO_UP}'
    LEVELUP_38_GUARDIAN_BLIZZARD_UP = f'{LEVEL_UP} 38 {MYSTIC} {ETresAbilityKind.BLIZZARD_UP}'

    LEVELUP_40_WARRIOR_COUNTER_UP = f'{LEVEL_UP} 40 {WARRIOR} {ETresAbilityKind.COUNTER_UP}'
    LEVELUP_40_MYSTIC_AIRCOMBO_PLUS = f'{LEVEL_UP} 40 {MYSTIC} {ETresAbilityKind.AIRCOMBO_PLUS}'
    LEVELUP_40_GUARDIAN_THUNDER_UP = f'{LEVEL_UP} 40 {MYSTIC} {ETresAbilityKind.THUNDER_UP}'

    LEVELUP_42_WARRIOR_MAGIC_TIME = f'{LEVEL_UP} 42 {WARRIOR} {ETresAbilityKind.MAGIC_TIME}'
    LEVELUP_42_MYSTIC_LAST_LEAVE = f'{LEVEL_UP} 42 {MYSTIC} {ETresAbilityKind.LAST_LEAVE}'
    LEVELUP_42_GUARDIAN_AIRCOMBO_UP = f'{LEVEL_UP} 42 {MYSTIC} {ETresAbilityKind.AIRCOMBO_UP}'

    LEVELUP_44_WARRIOR_MAGIC_COMBO_SAVE = f'{LEVEL_UP} 44 {WARRIOR} {ETresAbilityKind.MAGIC_COMBO_SAVE}'
    LEVELUP_44_MYSTIC_ATTRACTION_UP = f'{LEVEL_UP} 44 {MYSTIC} {ETresAbilityKind.ATTRACTION_UP}'
    LEVELUP_44_GUARDIAN_MAGIC_TIME = f'{LEVEL_UP} 44 {MYSTIC} {ETresAbilityKind.MAGIC_TIME}'

    LEVELUP_46_WARRIOR_MAGIC_COMBO_UP = f'{LEVEL_UP} 46 {WARRIOR} {ETresAbilityKind.MAGIC_COMBO_UP}'
    LEVELUP_46_MYSTIC_COMBO_UP = f'{LEVEL_UP} 46 {MYSTIC} {ETresAbilityKind.COMBO_UP}'
    LEVELUP_46_GUARDIAN_MAGIC_COMBO_SAVE = f'{LEVEL_UP} 46 {MYSTIC} {ETresAbilityKind.MAGIC_COMBO_SAVE}'

    LEVELUP_48_WARRIOR_LAST_LEAVE = f'{LEVEL_UP} 48 {WARRIOR} {ETresAbilityKind.LAST_LEAVE}'
    LEVELUP_48_MYSTIC_LINK_BOOST = f'{LEVEL_UP} 48 {MYSTIC} {ETresAbilityKind.LINK_BOOST}'
    LEVELUP_48_GUARDIAN_AERO_UP = f'{LEVEL_UP} 48 {MYSTIC} {ETresAbilityKind.AERO_UP}'

    LEVELUP_50_WARRIOR_CRITICAL_HALF = f'{LEVEL_UP} 50 {WARRIOR} {ETresAbilityKind.CRITICAL_HALF}'
    LEVELUP_50_MYSTIC_AIRCOMBO_UP = f'{LEVEL_UP} 50 {MYSTIC} {ETresAbilityKind.AIRCOMBO_UP}'
    LEVELUP_50_GUARDIAN_MAGIC_COMBO_UP = f'{LEVEL_UP} 50 {MYSTIC} {ETresAbilityKind.MAGIC_COMBO_UP}'
    
    @classmethod
    def generate_locations(cls):
        locations = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue
            
            locations.append(LocationData(value, key, TresWorldData.ANY, TresAreaData.ANY, cls.LEVEL_UP))

        return locations

class TresLuckyMarkDataLocation(KingdomHeartsIIILocation):
    """
    """
    PREFIX = 'Lucky Emblem Collect'
    LUCKY_EMBLEM = 'Lucky Emblem'

    LUCKY_MARK_COLLECT_1_AP_UP = f'{PREFIX} 1 {ETresItemDefCampItem.ITEM_APUP}'
    LUCKY_MARK_COLLECT_3_ITEM_MEGAPOTION = f'{PREFIX} 3 {ETresItemDefBattleItem.ITEM_MEGAPOTION}'
    LUCKY_MARK_COLLECT_5_ACC_ITEM09 = f'{PREFIX} 5 {ETresItemDefAccessory.ACC_ITEM09}'
    LUCKY_MARK_COLLECT_10_PRT_ITEM40 = f'{PREFIX} 10 {ETresItemDefProtector.PRT_ITEM40}'
    LUCKY_MARK_COLLECT_15_ACC_ITEM36 = f'{PREFIX} 15 {ETresItemDefAccessory.ACC_ITEM36}'
    LUCKY_MARK_COLLECT_20_ITEM_MAGICUP = f'{PREFIX} 20 {ETresItemDefCampItem.ITEM_MAGICUP}'
    LUCKY_MARK_COLLECT_25_ACC_ITEM37 = f'{PREFIX} 25 {ETresItemDefAccessory.ACC_ITEM37}'
    LUCKY_MARK_COLLECT_30_PRT_ITEM37 = f'{PREFIX} 30 {ETresItemDefProtector.PRT_ITEM37}'
    LUCKY_MARK_COLLECT_35_PRT_ITEM08 = f'{PREFIX} 35 {ETresItemDefProtector.PRT_ITEM08}'
    LUCKY_MARK_COLLECT_40_ITEM_POWERUP = f'{PREFIX} 40 {ETresItemDefCampItem.ITEM_POWERUP}'
    LUCKY_MARK_COLLECT_45_ACC_ITEM24 = f'{PREFIX} 45 {ETresItemDefAccessory.ACC_ITEM24}'
    LUCKY_MARK_COLLECT_50_ACC_ITEM21 = f'{PREFIX} 50 {ETresItemDefAccessory.ACC_ITEM21}'
    LUCKY_MARK_COLLECT_55_ITEM_GUARDUP = f'{PREFIX} 55 {ETresItemDefCampItem.ITEM_GUARDUP}'
    LUCKY_MARK_COLLECT_60_ACC_ITEM16 = f'{PREFIX} 60 {ETresItemDefAccessory.ACC_ITEM16}'
    LUCKY_MARK_COLLECT_65_PRT_ITEM10 = f'{PREFIX} 65 {ETresItemDefProtector.PRT_ITEM10}'
    LUCKY_MARK_COLLECT_70_PRT_ITEM44 = f'{PREFIX} 70 {ETresItemDefProtector.PRT_ITEM44}'
    LUCKY_MARK_COLLECT_80_MAT_ITEM57 = f'{PREFIX} 80 {ETresItemDefMaterial.MAT_ITEM57}'
    LUCKY_MARK_COLLECT_90_ACC_ITEM31 = f'{PREFIX} 90 {ETresItemDefAccessory.ACC_ITEM31}'
    
    @classmethod
    def generate_locations(cls):
        locations = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue
            
            locations.append(LocationData(value, key, TresWorldData.MANY, TresAreaData.MANY, cls.LUCKY_EMBLEM))

        return locations

class TresMooglePostPresentsDataLocation(KingdomHeartsIIILocation):
    """
    """

class TresSynthesisCollectionDataLocation(KingdomHeartsIIILocation):
    """
    """

class TresTreasureDataLocation(KingdomHeartsIIILocation):
    """
    """
    LARGE_TREASURE = 'Large Treasure'
    SMALL_TREASURE = 'Small Treasure'
    TREASURE_CHEST = 'Treasure Chest'

    SCALA_AD_CAELUM_LARGE_TREASURE_001_NAVI_MAP_BT01 = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.THE_STAIRWAY_TO_THE_SKY} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_BT01}'
    SCALA_AD_CAELUM_LARGE_TREASURE_002_NAVI_MAP_BT02 = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.BREEZY_QUARTER} {LARGE_TREASURE} 2 {ETresItemDefNavimap.NAVI_MAP_BT02}'
    SCALA_AD_CAELUM_SMALL_TREASURE_001_ITEM_LASTELIXIR = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.BREEZY_QUARTER} {SMALL_TREASURE} 1 {ETresItemDefBattleItem.ITEM_LASTELIXIR}'
    SCALA_AD_CAELUM_SMALL_TREASURE_002_FOOD_ITEM56 = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.BREEZY_QUARTER} {SMALL_TREASURE} 2 {ETresItemDefFood.FOOD_ITEM56}'
    SCALA_AD_CAELUM_SMALL_TREASURE_003_MAT_ITEM48 = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.BREEZY_QUARTER} {SMALL_TREASURE} 3 {ETresItemDefMaterial.MAT_ITEM48}'
    SCALA_AD_CAELUM_SMALL_TREASURE_004_MAT_ITEM47 = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.BREEZY_QUARTER} {SMALL_TREASURE} 4 {ETresItemDefMaterial.MAT_ITEM47}'
    SCALA_AD_CAELUM_SMALL_TREASURE_005_ITEM_MEGAETHER = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.BREEZY_QUARTER} {SMALL_TREASURE} 5 {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    SCALA_AD_CAELUM_SMALL_TREASURE_006_MAT_ITEM58 = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.BREEZY_QUARTER} {SMALL_TREASURE} 6 {ETresItemDefMaterial.MAT_ITEM58}'
    SCALA_AD_CAELUM_SMALL_TREASURE_007_MAT_ITEM52 = f'{TresWorldData.SCALA_AD_CAELUM} {TresAreaData.BREEZY_QUARTER} {SMALL_TREASURE} 7 {ETresItemDefMaterial.MAT_ITEM52}'

    SAN_FRANSOKYO_LARGE_TREASURE_001_NAVI_MAP_BX01 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_BX01}'
    SAN_FRANSOKYO_LARGE_TREASURE_005_LSIGAME19 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {LARGE_TREASURE} 2 {ETresItemDefLSIGameItem.LSIGAME19}'
    SAN_FRANSOKYO_LARGE_TREASURE_006_LSIGAME12 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {LARGE_TREASURE} 3 {ETresItemDefLSIGameItem.LSIGAME12}'
    SAN_FRANSOKYO_LARGE_TREASURE_007_LSIGAME23 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {LARGE_TREASURE} 4 {ETresItemDefLSIGameItem.LSIGAME23}'
    SAN_FRANSOKYO_SMALL_TREASURE_001_PRT_ITEM33 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 1 {ETresItemDefProtector.PRT_ITEM33}'
    SAN_FRANSOKYO_SMALL_TREASURE_002_ACC_ITEM08 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 2 {ETresItemDefAccessory.ACC_ITEM08}'
    SAN_FRANSOKYO_SMALL_TREASURE_003_ITEM_HIGHFOCUSSUPPLY = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 3 {ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY}'
    SAN_FRANSOKYO_SMALL_TREASURE_004_ITEM_APUP = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 4 {ETresItemDefCampItem.ITEM_APUP}'
    SAN_FRANSOKYO_SMALL_TREASURE_005_MAT_ITEM58 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 5 {ETresItemDefMaterial.MAT_ITEM58}'
    SAN_FRANSOKYO_SMALL_TREASURE_006_ACC_ITEM15 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 6 {ETresItemDefAccessory.ACC_ITEM15}'
    SAN_FRANSOKYO_SMALL_TREASURE_007_ITEM_APUP = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 7 {ETresItemDefCampItem.ITEM_APUP}'
    SAN_FRANSOKYO_SMALL_TREASURE_008_ITEM_MEGAETHER = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 8 {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    SAN_FRANSOKYO_SMALL_TREASURE_009_MAT_ITEM55 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 9 {ETresItemDefMaterial.MAT_ITEM55}'
    SAN_FRANSOKYO_SMALL_TREASURE_010_ITEM_MEGAPOTION = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 10 {ETresItemDefBattleItem.ITEM_MEGAPOTION}'
    SAN_FRANSOKYO_SMALL_TREASURE_011_PRT_ITEM20 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 11 {ETresItemDefProtector.PRT_ITEM20}'
    SAN_FRANSOKYO_SMALL_TREASURE_012_ITEM_ELIXIR = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 12 {ETresItemDefBattleItem.ITEM_ELIXIR}'
    SAN_FRANSOKYO_SMALL_TREASURE_013_PRT_ITEM31 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 13 {ETresItemDefProtector.PRT_ITEM31}'
    SAN_FRANSOKYO_SMALL_TREASURE_014_ITEM_APUP = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 14 {ETresItemDefCampItem.ITEM_APUP}'
    SAN_FRANSOKYO_SMALL_TREASURE_015_ITEM_MAGICUP = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 15 {ETresItemDefCampItem.ITEM_MAGICUP}'
    SAN_FRANSOKYO_SMALL_TREASURE_016_ITEM_HIGHETHER = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 16 {ETresItemDefBattleItem.ITEM_HIGHETHER}'
    SAN_FRANSOKYO_SMALL_TREASURE_017_ITEM_MEGAETHER = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 17 {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    SAN_FRANSOKYO_SMALL_TREASURE_018_WEP_DONALD_07 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 18 {ETresItemDefWeapon.WEP_DONALD_07}'
    SAN_FRANSOKYO_SMALL_TREASURE_019_ITEM_APUP = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 19 {ETresItemDefCampItem.ITEM_APUP}'
    SAN_FRANSOKYO_SMALL_TREASURE_020_MAT_ITEM54 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 20 {ETresItemDefMaterial.MAT_ITEM54}'
    SAN_FRANSOKYO_SMALL_TREASURE_021_MAT_ITEM55 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 21 {ETresItemDefMaterial.MAT_ITEM55}'
    SAN_FRANSOKYO_SMALL_TREASURE_022_PRT_ITEM27 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 22 {ETresItemDefProtector.PRT_ITEM27}'
    SAN_FRANSOKYO_SMALL_TREASURE_023_ITEM_HIGHFOCUSSUPPLY = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 23 {ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY}'
    SAN_FRANSOKYO_SMALL_TREASURE_024_ACC_ITEM37 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 24 {ETresItemDefAccessory.ACC_ITEM37}'
    SAN_FRANSOKYO_SMALL_TREASURE_025_MAT_ITEM58 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 25 {ETresItemDefMaterial.MAT_ITEM58}'
    SAN_FRANSOKYO_SMALL_TREASURE_026_PRT_ITEM07 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 26 {ETresItemDefProtector.PRT_ITEM07}'
    SAN_FRANSOKYO_SMALL_TREASURE_027_ITEM_MAGICUP = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 27 {ETresItemDefCampItem.ITEM_MAGICUP}'
    SAN_FRANSOKYO_SMALL_TREASURE_028_ITEM_POWERUP = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 28 {ETresItemDefCampItem.ITEM_POWERUP}'
    SAN_FRANSOKYO_SMALL_TREASURE_029_PRT_ITEM24 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {SMALL_TREASURE} 29 {ETresItemDefProtector.PRT_ITEM24}'
    SAN_FRANSOKYO_SMALL_TREASURE_030_ITEM_MEGAPOTION = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {SMALL_TREASURE} 30 {ETresItemDefBattleItem.ITEM_MEGAPOTION}'
    SAN_FRANSOKYO_SMALL_TREASURE_031_MAT_ITEM54 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 31 {ETresItemDefMaterial.MAT_ITEM54}'
    SAN_FRANSOKYO_SMALL_TREASURE_032_ITEM_APUP = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_NORTH_DISTRICT} {SMALL_TREASURE} 32 {ETresItemDefCampItem.ITEM_APUP}'
    
    THE_CARIBBEAN_LARGE_TREASURE_001_NAVI_MAP_CA01 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_DOCKS} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_CA01}'
    THE_CARIBBEAN_LARGE_TREASURE_002_NAVI_MAP_CA04 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.ISLA_DE_LOS_MASTILES} {LARGE_TREASURE} 2 {ETresItemDefNavimap.NAVI_MAP_CA04}'
    THE_CARIBBEAN_LARGE_TREASURE_003_NAVI_MAP_CA03 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SHIPS_END} {LARGE_TREASURE} 3 {ETresItemDefNavimap.NAVI_MAP_CA03}'
    THE_CARIBBEAN_LARGE_TREASURE_004_NAVI_MAP_CA05 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {LARGE_TREASURE} 4 {ETresItemDefNavimap.NAVI_MAP_CA05}'
    THE_CARIBBEAN_LARGE_TREASURE_005_NAVI_MAP_CA02 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {LARGE_TREASURE} 5 {ETresItemDefNavimap.NAVI_MAP_CA02}'
    THE_CARIBBEAN_LARGE_TREASURE_006_LSIGAME11 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_FORT} {LARGE_TREASURE} 6 {ETresItemDefLSIGameItem.LSIGAME11}'
    THE_CARIBBEAN_LARGE_TREASURE_007_LSIGAME08 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {LARGE_TREASURE} 7 {ETresItemDefLSIGameItem.LSIGAME08}'
    THE_CARIBBEAN_LARGE_TREASURE_008_LSIGAME21 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.ISLA_VERDEMONTANA} {LARGE_TREASURE} 8 {ETresItemDefLSIGameItem.LSIGAME21}'
    THE_CARIBBEAN_LARGE_TREASURE_009_LSIGAME17 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.CONFINEMENT_ISLE} {LARGE_TREASURE} 9 {ETresItemDefLSIGameItem.LSIGAME17}'
    THE_CARIBBEAN_LARGE_TREASURE_010_KEY_ITEM10 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {LARGE_TREASURE} 10 {ETresItemDefKeyItem.KEY_ITEM10}'
    THE_CARIBBEAN_LARGE_TREASURE_011_ACC_ITEM23 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.ISLA_DE_LOS_MASTILES} {LARGE_TREASURE} 11 {ETresItemDefAccessory.ACC_ITEM23}'
    THE_CARIBBEAN_SMALL_TREASURE_001_ITEM_HIGHFOCUSSUPPLY = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_FORT} {SMALL_TREASURE} 1 {ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY}'
    THE_CARIBBEAN_SMALL_TREASURE_002_ACC_ITEM20 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_SEAPORT} {SMALL_TREASURE} 2 {ETresItemDefAccessory.ACC_ITEM20}'
    THE_CARIBBEAN_SMALL_TREASURE_003_ITEM_HIGHPOTION = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_SEAPORT} {SMALL_TREASURE} 3 {ETresItemDefBattleItem.ITEM_HIGHPOTION}'
    THE_CARIBBEAN_SMALL_TREASURE_004_ITEM_MEGAETHER = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_SEAPORT} {SMALL_TREASURE} 4 {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    THE_CARIBBEAN_SMALL_TREASURE_005_ITEM_TENT = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_SETTLEMENT} {SMALL_TREASURE} 5 {ETresItemDefCampItem.ITEM_TENT}'
    THE_CARIBBEAN_SMALL_TREASURE_006_ITEM_HIGHETHER = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_DOCKS} {SMALL_TREASURE} 6 {ETresItemDefBattleItem.ITEM_HIGHETHER}'
    THE_CARIBBEAN_SMALL_TREASURE_007_ITEM_ELIXIR = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_FORT} {SMALL_TREASURE} 7 {ETresItemDefBattleItem.ITEM_ELIXIR}'
    THE_CARIBBEAN_SMALL_TREASURE_008_ITEM_MEGAPOTION = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_SETTLEMENT} {SMALL_TREASURE} 8 {ETresItemDefBattleItem.ITEM_MEGAPOTION}'
    THE_CARIBBEAN_SMALL_TREASURE_009_ITEM_ETHER = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_SEAPORT} {SMALL_TREASURE} 9 {ETresItemDefBattleItem.ITEM_ETHER}'
    THE_CARIBBEAN_SMALL_TREASURE_010_ACC_ITEM10 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {SMALL_TREASURE} 10 {ETresItemDefAccessory.ACC_ITEM10}'
    THE_CARIBBEAN_SMALL_TREASURE_011_MAT_ITEM55 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {SMALL_TREASURE} 11 {ETresItemDefMaterial.MAT_ITEM55}'
    THE_CARIBBEAN_SMALL_TREASURE_012_MAT_ITEM56 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {SMALL_TREASURE} 12 {ETresItemDefMaterial.MAT_ITEM56}'
    THE_CARIBBEAN_SMALL_TREASURE_013_MAT_ITEM54 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {SMALL_TREASURE} 13 {ETresItemDefMaterial.MAT_ITEM54}'
    THE_CARIBBEAN_SMALL_TREASURE_014_ACC_ITEM38 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SHIPS_END} {SMALL_TREASURE} 14 {ETresItemDefAccessory.ACC_ITEM38}'
    THE_CARIBBEAN_SMALL_TREASURE_015_ITEM_MEGAETHER = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SHIPS_END} {SMALL_TREASURE} 15 {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    THE_CARIBBEAN_SMALL_TREASURE_016_MAT_ITEM58 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.ISLA_VERDEMONTANA} {SMALL_TREASURE} 16 {ETresItemDefMaterial.MAT_ITEM58}'
    THE_CARIBBEAN_SMALL_TREASURE_017_MAT_ITEM58 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 17 {ETresItemDefMaterial.MAT_ITEM58}'
    THE_CARIBBEAN_SMALL_TREASURE_018_MAT_ITEM57 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.EXILE_ISLAND} {SMALL_TREASURE} 18 {ETresItemDefMaterial.MAT_ITEM57}'
    THE_CARIBBEAN_SMALL_TREASURE_019_ACC_ITEM46 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_WATERS} {SMALL_TREASURE} 19 {ETresItemDefAccessory.ACC_ITEM46}'
    THE_CARIBBEAN_SMALL_TREASURE_020_PRT_ITEM34 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HORSESHOE_ISLAND} {SMALL_TREASURE} 20 {ETresItemDefProtector.PRT_ITEM34}'
    THE_CARIBBEAN_SMALL_TREASURE_021_ITEM_ALLCURE = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {SMALL_TREASURE} 21 {ETresItemDefBattleItem.ITEM_ALLCURE}'
    THE_CARIBBEAN_SMALL_TREASURE_022_ITEM_MEGAPOTION = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {SMALL_TREASURE} 22 {ETresItemDefBattleItem.ITEM_MEGAPOTION}'
    THE_CARIBBEAN_SMALL_TREASURE_023_PRT_ITEM49 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.ISLA_DE_LOS_MASTILES} {SMALL_TREASURE} 23 {ETresItemDefProtector.PRT_ITEM49}'
    THE_CARIBBEAN_SMALL_TREASURE_024_MAT_ITEM55 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.ISLA_DE_LOS_MASTILES} {SMALL_TREASURE} 24 {ETresItemDefMaterial.MAT_ITEM55}'
    THE_CARIBBEAN_SMALL_TREASURE_025_ACC_ITEM45 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.LEVIATHAN} {SMALL_TREASURE} 25 {ETresItemDefAccessory.ACC_ITEM45}'
    THE_CARIBBEAN_SMALL_TREASURE_026_MAT_ITEM56 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.ISLA_VERDEMONTANA} {SMALL_TREASURE} 26 {ETresItemDefMaterial.MAT_ITEM56}'
    THE_CARIBBEAN_SMALL_TREASURE_027_MAT_ITEM52 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 27 {ETresItemDefMaterial.MAT_ITEM52}'
    THE_CARIBBEAN_SMALL_TREASURE_028_MAT_ITEM55 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 28 {ETresItemDefMaterial.MAT_ITEM55}'
    THE_CARIBBEAN_SMALL_TREASURE_029_MAT_ITEM54 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 29 {ETresItemDefMaterial.MAT_ITEM54}'
    THE_CARIBBEAN_SMALL_TREASURE_030_MAT_ITEM56 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 30 {ETresItemDefMaterial.MAT_ITEM56}'
    THE_CARIBBEAN_SMALL_TREASURE_031_MAT_ITEM55 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 31 {ETresItemDefMaterial.MAT_ITEM55}'
    THE_CARIBBEAN_SMALL_TREASURE_032_MAT_ITEM58 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 32 {ETresItemDefMaterial.MAT_ITEM58}'
    THE_CARIBBEAN_SMALL_TREASURE_033_MAT_ITEM55 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 33 {ETresItemDefMaterial.MAT_ITEM55}'
    THE_CARIBBEAN_SMALL_TREASURE_034_MAT_ITEM56 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 34 {ETresItemDefMaterial.MAT_ITEM56}'
    THE_CARIBBEAN_SMALL_TREASURE_035_WEP_GOOFY_09 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 35 {ETresItemDefWeapon.WEP_GOOFY_09}'
    THE_CARIBBEAN_SMALL_TREASURE_036_MAT_ITEM58 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 36 {ETresItemDefMaterial.MAT_ITEM58}'
    THE_CARIBBEAN_SMALL_TREASURE_037_MAT_ITEM56 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 37 {ETresItemDefMaterial.MAT_ITEM56}'
    THE_CARIBBEAN_SMALL_TREASURE_038_MAT_ITEM55 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 38 {ETresItemDefMaterial.MAT_ITEM55}'
    THE_CARIBBEAN_SMALL_TREASURE_039_MAT_ITEM58 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 39 {ETresItemDefMaterial.MAT_ITEM58}'
    THE_CARIBBEAN_SMALL_TREASURE_040_MAT_ITEM55 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 40 {ETresItemDefMaterial.MAT_ITEM55}'
    THE_CARIBBEAN_SMALL_TREASURE_041_MAT_ITEM52 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.SANDBAR_ISLE} {SMALL_TREASURE} 41 {ETresItemDefMaterial.MAT_ITEM52}'
    THE_CARIBBEAN_SMALL_TREASURE_042_MAT_ITEM54 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HORSESHOE_ISLAND} {SMALL_TREASURE} 42 {ETresItemDefMaterial.MAT_ITEM54}'
    THE_CARIBBEAN_SMALL_TREASURE_043_PRT_ITEM12 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HORSESHOE_ISLAND} {SMALL_TREASURE} 43 {ETresItemDefProtector.PRT_ITEM12}'
    THE_CARIBBEAN_SMALL_TREASURE_044_PRT_ITEM17 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HORSESHOE_ISLAND} {SMALL_TREASURE} 44 {ETresItemDefProtector.PRT_ITEM17}'
    THE_CARIBBEAN_SMALL_TREASURE_045_PRT_ITEM25 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HORSESHOE_ISLAND} {SMALL_TREASURE} 45 {ETresItemDefProtector.PRT_ITEM25}'

    THE_FINAL_WORLD_LARGE_TREASURE_001_MAT_ITEM57 = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.UNKNOWN} {LARGE_TREASURE} 1 {ETresItemDefMaterial.MAT_ITEM57}'

    ARENDELLE_LARGE_TREASURE_001_NAVI_MAP_FZ01 = f'{TresWorldData.ARENDELLE} {TresAreaData.TREESCAPE} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_FZ01}'
    ARENDELLE_LARGE_TREASURE_002_NAVI_MAP_FZ02 = f'{TresWorldData.ARENDELLE} {TresAreaData.THE_LABYRINTH_OF_ICE_MIDDLE_TIER} {LARGE_TREASURE} 2 {ETresItemDefNavimap.NAVI_MAP_FZ02}'
    ARENDELLE_LARGE_TREASURE_003_LSIGAME07 = f'{TresWorldData.ARENDELLE} {TresAreaData.TREESCAPE} {LARGE_TREASURE} 3 {ETresItemDefLSIGameItem.LSIGAME07}'
    ARENDELLE_LARGE_TREASURE_004_LSIGAME06 = f'{TresWorldData.ARENDELLE} {TresAreaData.SNOWFIELD} {LARGE_TREASURE} 4 {ETresItemDefLSIGameItem.LSIGAME06}'
    ARENDELLE_LARGE_TREASURE_005_LSIGAME22 = f'{TresWorldData.ARENDELLE} {TresAreaData.THE_LABYRINTH_OF_ICE_LOWER_TIER} {LARGE_TREASURE} 5 {ETresItemDefLSIGameItem.LSIGAME22}'
    ARENDELLE_LARGE_TREASURE_006_MAT_ITEM56 = f'{TresWorldData.ARENDELLE} {TresAreaData.SNOWFIELD} {LARGE_TREASURE} 6 {ETresItemDefMaterial.MAT_ITEM56}'
    ARENDELLE_SMALL_TREASURE_001_PRT_ITEM15 = f'{TresWorldData.ARENDELLE} {TresAreaData.TREESCAPE} {SMALL_TREASURE} 1 {ETresItemDefProtector.PRT_ITEM15}'
    ARENDELLE_SMALL_TREASURE_002_MAT_ITEM54 = f'{TresWorldData.ARENDELLE} {TresAreaData.TREESCAPE} {SMALL_TREASURE} 2 {ETresItemDefMaterial.MAT_ITEM54}'
    ARENDELLE_SMALL_TREASURE_004_ITEM_ELIXIR = f'{TresWorldData.ARENDELLE} {TresAreaData.GORGE} {SMALL_TREASURE} 3 {ETresItemDefBattleItem.ITEM_ELIXIR}'
    ARENDELLE_SMALL_TREASURE_005_PRT_ITEM05 = f'{TresWorldData.ARENDELLE} {TresAreaData.GORGE} {SMALL_TREASURE} 4 {ETresItemDefProtector.PRT_ITEM05}'
    ARENDELLE_SMALL_TREASURE_007_ACC_ITEM19 = f'{TresWorldData.ARENDELLE} {TresAreaData.SNOWFIELD} {SMALL_TREASURE} 5 {ETresItemDefAccessory.ACC_ITEM19}'
    ARENDELLE_SMALL_TREASURE_011_PRT_ITEM23 = f'{TresWorldData.ARENDELLE} {TresAreaData.THE_LABYRINTH_OF_ICE_UPPER_TIER} {SMALL_TREASURE} 6 {ETresItemDefProtector.PRT_ITEM23}'
    ARENDELLE_SMALL_TREASURE_012_PRT_ITEM48 = f'{TresWorldData.ARENDELLE} {TresAreaData.THE_LABYRINTH_OF_ICE_MIDDLE_TIER} {SMALL_TREASURE} 7 {ETresItemDefProtector.PRT_ITEM48}'
    ARENDELLE_SMALL_TREASURE_013_MAT_ITEM54 = f'{TresWorldData.ARENDELLE} {TresAreaData.THE_LABYRINTH_OF_ICE_UPPER_TIER} {SMALL_TREASURE} 8 {ETresItemDefMaterial.MAT_ITEM54}'
    ARENDELLE_SMALL_TREASURE_015_ACC_ITEM44 = f'{TresWorldData.ARENDELLE} {TresAreaData.THE_LABYRINTH_OF_ICE_MIDDLE_TIER} {SMALL_TREASURE} 9 {ETresItemDefAccessory.ACC_ITEM44}'
    ARENDELLE_SMALL_TREASURE_016_ITEM_HIGHPOTION = f'{TresWorldData.ARENDELLE} {TresAreaData.VALLEY_OF_ICE} {SMALL_TREASURE} 10 {ETresItemDefBattleItem.ITEM_HIGHPOTION}'
    ARENDELLE_SMALL_TREASURE_017_ITEM_FOCUSSUPPLY = f'{TresWorldData.ARENDELLE} {TresAreaData.VALLEY_OF_ICE} {SMALL_TREASURE} 11 {ETresItemDefBattleItem.ITEM_FOCUSSUPPLY}'
    ARENDELLE_SMALL_TREASURE_019_ITEM_HIGHETHER = f'{TresWorldData.ARENDELLE} {TresAreaData.VALLEY_OF_ICE} {SMALL_TREASURE} 12 {ETresItemDefBattleItem.ITEM_HIGHETHER}'
    ARENDELLE_SMALL_TREASURE_020_PRT_ITEM16 = f'{TresWorldData.ARENDELLE} {TresAreaData.VALLEY_OF_ICE} {SMALL_TREASURE} 13 {ETresItemDefProtector.PRT_ITEM16}'
    ARENDELLE_SMALL_TREASURE_022_ITEM_APUP = f'{TresWorldData.ARENDELLE} {TresAreaData.VALLEY_OF_ICE} {SMALL_TREASURE} 14 {ETresItemDefCampItem.ITEM_APUP}'
    ARENDELLE_SMALL_TREASURE_023_ITEM_MEGAETHER = f'{TresWorldData.ARENDELLE} {TresAreaData.FROZEN_WALL} {SMALL_TREASURE} 15 {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    ARENDELLE_SMALL_TREASURE_024_ACC_ITEM26 = f'{TresWorldData.ARENDELLE} {TresAreaData.FROZEN_WALL} {SMALL_TREASURE} 16 {ETresItemDefAccessory.ACC_ITEM26}'
    ARENDELLE_SMALL_TREASURE_025_WEP_DONALD_05 = f'{TresWorldData.ARENDELLE} {TresAreaData.FROZEN_WALL} {SMALL_TREASURE} 17 {ETresItemDefWeapon.WEP_DONALD_05}'
    ARENDELLE_SMALL_TREASURE_027_ACC_ITEM35 = f'{TresWorldData.ARENDELLE} {TresAreaData.FOOTHILLS} {SMALL_TREASURE} 18 {ETresItemDefAccessory.ACC_ITEM35}'
    ARENDELLE_SMALL_TREASURE_029_MAT_ITEM54 = f'{TresWorldData.ARENDELLE} {TresAreaData.FOOTHILLS} {SMALL_TREASURE} 19 {ETresItemDefMaterial.MAT_ITEM54}'
    
    OLYMPUS_LARGE_TREASURE_001_NAVI_MAP_HE01 = f'{TresWorldData.OLYMPUS} {TresAreaData.CLIFF_ASCENT} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_HE01}'
    OLYMPUS_LARGE_TREASURE_002_NAVI_MAP_HE02 = f'{TresWorldData.OLYMPUS} {TresAreaData.OVERLOOK} {LARGE_TREASURE} 2 {ETresItemDefNavimap.NAVI_MAP_HE02}'
    OLYMPUS_LARGE_TREASURE_003_ITEM_ELIXIR = f'{TresWorldData.OLYMPUS} {TresAreaData.CORRIDORS} {LARGE_TREASURE} 3 {ETresItemDefBattleItem.ITEM_ELIXIR}'
    OLYMPUS_LARGE_TREASURE_004_NAVI_MAP_HE03 = f'{TresWorldData.OLYMPUS} {TresAreaData.CORRIDORS} {LARGE_TREASURE} 4 {ETresItemDefNavimap.NAVI_MAP_HE03}'
    OLYMPUS_SMALL_TREASURE_001_MAT_ITEM53 = f'{TresWorldData.OLYMPUS} {TresAreaData.COURTYARD} {SMALL_TREASURE} 1 {ETresItemDefMaterial.MAT_ITEM53}'
    OLYMPUS_SMALL_TREASURE_002_ITEM_FOCUSSUPPLY = f'{TresWorldData.OLYMPUS} {TresAreaData.COURTYARD} {SMALL_TREASURE} 2 {ETresItemDefBattleItem.ITEM_FOCUSSUPPLY}'
    OLYMPUS_SMALL_TREASURE_003_ITEM_POTION = f'{TresWorldData.OLYMPUS} {TresAreaData.COURTYARD} {SMALL_TREASURE} 3 {ETresItemDefBattleItem.ITEM_POTION}'
    OLYMPUS_SMALL_TREASURE_004_MAT_ITEM33 = f'{TresWorldData.OLYMPUS} {TresAreaData.COURTYARD} {SMALL_TREASURE} 4 {ETresItemDefMaterial.MAT_ITEM33}'
    OLYMPUS_SMALL_TREASURE_005_ITEM_FOCUSSUPPLY = f'{TresWorldData.OLYMPUS} {TresAreaData.CLOUD_RIDGE} {SMALL_TREASURE} 5 {ETresItemDefBattleItem.ITEM_FOCUSSUPPLY}'
    OLYMPUS_SMALL_TREASURE_006_ITEM_POTION = f'{TresWorldData.OLYMPUS} {TresAreaData.CORRIDORS} {SMALL_TREASURE} 6 {ETresItemDefBattleItem.ITEM_POTION}'
    OLYMPUS_SMALL_TREASURE_007_ACC_ITEM12 = f'{TresWorldData.OLYMPUS} {TresAreaData.RAVINE} {SMALL_TREASURE} 7 {ETresItemDefAccessory.ACC_ITEM12}'
    OLYMPUS_SMALL_TREASURE_008_ACC_ITEM40 = f'{TresWorldData.OLYMPUS} {TresAreaData.RAVINE} {SMALL_TREASURE} 8 {ETresItemDefAccessory.ACC_ITEM40}'
    OLYMPUS_SMALL_TREASURE_009_ITEM_POTION = f'{TresWorldData.OLYMPUS} {TresAreaData.CLIFF_ASCENT} {SMALL_TREASURE} 9 {ETresItemDefBattleItem.ITEM_POTION}'
    OLYMPUS_SMALL_TREASURE_010_ITEM_ALLCURE = f'{TresWorldData.OLYMPUS} {TresAreaData.CLIFF_ASCENT} {SMALL_TREASURE} 10 {ETresItemDefBattleItem.ITEM_ALLCURE}'
    OLYMPUS_SMALL_TREASURE_011_ACC_ITEM03 = f'{TresWorldData.OLYMPUS} {TresAreaData.CLIFF_ASCENT} {SMALL_TREASURE} 11 {ETresItemDefAccessory.ACC_ITEM03}'
    OLYMPUS_SMALL_TREASURE_012_ACC_ITEM22 = f'{TresWorldData.OLYMPUS} {TresAreaData.CLIFF_ASCENT} {SMALL_TREASURE} 12 {ETresItemDefAccessory.ACC_ITEM22}'
    OLYMPUS_SMALL_TREASURE_013_ITEM_POTION = f'{TresWorldData.OLYMPUS} {TresAreaData.CLIFF_ASCENT} {SMALL_TREASURE} 13 {ETresItemDefBattleItem.ITEM_POTION}'
    OLYMPUS_SMALL_TREASURE_014_ITEM_APUP = f'{TresWorldData.OLYMPUS} {TresAreaData.CLIFF_ASCENT} {SMALL_TREASURE} 14 {ETresItemDefCampItem.ITEM_APUP}'
    OLYMPUS_SMALL_TREASURE_015_ITEM_APUP = f'{TresWorldData.OLYMPUS} {TresAreaData.MOUNTAINSIDE} {SMALL_TREASURE} 15 {ETresItemDefCampItem.ITEM_APUP}'
    OLYMPUS_SMALL_TREASURE_016_MAT_ITEM53 = f'{TresWorldData.OLYMPUS} {TresAreaData.SUMMIT} {SMALL_TREASURE} 16 {ETresItemDefMaterial.MAT_ITEM53}'
    OLYMPUS_SMALL_TREASURE_017_ITEM_HIGHETHER = f'{TresWorldData.OLYMPUS} {TresAreaData.MOUNTAINSIDE} {SMALL_TREASURE} 17 {ETresItemDefBattleItem.ITEM_HIGHETHER}'
    OLYMPUS_SMALL_TREASURE_018_ITEM_APUP = f'{TresWorldData.OLYMPUS} {TresAreaData.ALLEYWAY} {SMALL_TREASURE} 18 {ETresItemDefCampItem.ITEM_APUP}'
    OLYMPUS_SMALL_TREASURE_019_ITEM_POTION = f'{TresWorldData.OLYMPUS} {TresAreaData.ALLEYWAY} {SMALL_TREASURE} 19 {ETresItemDefBattleItem.ITEM_POTION}'
    OLYMPUS_SMALL_TREASURE_020_MAT_ITEM53 = f'{TresWorldData.OLYMPUS} {TresAreaData.AGORA} {SMALL_TREASURE} 20 {ETresItemDefMaterial.MAT_ITEM53}'
    OLYMPUS_SMALL_TREASURE_021_ITEM_ETHER = f'{TresWorldData.OLYMPUS} {TresAreaData.THE_BIG_OLIVE} {SMALL_TREASURE} 21 {ETresItemDefBattleItem.ITEM_ETHER}'
    OLYMPUS_SMALL_TREASURE_022_ITEM_MEGAPOTION = f'{TresWorldData.OLYMPUS} {TresAreaData.THE_BIG_OLIVE} {SMALL_TREASURE} 22 {ETresItemDefBattleItem.ITEM_MEGAPOTION}'
    OLYMPUS_SMALL_TREASURE_023_ACC_ITEM17 = f'{TresWorldData.OLYMPUS} {TresAreaData.GARDENS} {SMALL_TREASURE} 23 {ETresItemDefAccessory.ACC_ITEM17}'
    OLYMPUS_SMALL_TREASURE_024_ITEM_ETHER = f'{TresWorldData.OLYMPUS} {TresAreaData.OVERLOOK} {SMALL_TREASURE} 24 {ETresItemDefBattleItem.ITEM_ETHER}'
    OLYMPUS_SMALL_TREASURE_025_PRT_ITEM03 = f'{TresWorldData.OLYMPUS} {TresAreaData.OVERLOOK} {SMALL_TREASURE} 25 {ETresItemDefProtector.PRT_ITEM03}'
    OLYMPUS_SMALL_TREASURE_026_ITEM_POTION = f'{TresWorldData.OLYMPUS} {TresAreaData.OVERLOOK} {SMALL_TREASURE} 26 {ETresItemDefBattleItem.ITEM_POTION}'
    OLYMPUS_SMALL_TREASURE_027_ITEM_APUP = f'{TresWorldData.OLYMPUS} {TresAreaData.OVERLOOK} {SMALL_TREASURE} 27 {ETresItemDefCampItem.ITEM_APUP}'
    OLYMPUS_SMALL_TREASURE_028_ITEM_POTION = f'{TresWorldData.OLYMPUS} {TresAreaData.OVERLOOK} {SMALL_TREASURE} 28 {ETresItemDefBattleItem.ITEM_POTION}'
    
    KEYBLADE_GRAVEYARD_LARGE_TREASURE_001_NAVI_MAP_KG01 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_BADLANDS} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_KG01}'
    KEYBLADE_GRAVEYARD_LARGE_TREASURE_002_NAVI_MAP_KG02 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {LARGE_TREASURE} 2 {ETresItemDefNavimap.NAVI_MAP_KG02}'
    KEYBLADE_GRAVEYARD_SMALL_TREASURE_001_ITEM_LASTELIXIR = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {SMALL_TREASURE} 1 {ETresItemDefBattleItem.ITEM_LASTELIXIR}'
    KEYBLADE_GRAVEYARD_SMALL_TREASURE_002_ITEM_MEGAPOTION = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {SMALL_TREASURE} 2 {ETresItemDefBattleItem.ITEM_MEGAPOTION}'
    KEYBLADE_GRAVEYARD_SMALL_TREASURE_003_ITEM_MEGAETHER = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {SMALL_TREASURE} 3 {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    KEYBLADE_GRAVEYARD_SMALL_TREASURE_004_PRT_ITEM09 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_BADLANDS} {SMALL_TREASURE} 4 {ETresItemDefProtector.PRT_ITEM09}'
    
    MONSTROPOLIS_LARGE_TREASURE_001_NAVI_MAP_MI01 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.LOBBY_AND_OFFICES} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_MI01}'
    MONSTROPOLIS_LARGE_TREASURE_002_NAVI_MAP_MI02 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.FACTORY_BASEMENT} {LARGE_TREASURE} 2 {ETresItemDefNavimap.NAVI_MAP_MI02}'
    MONSTROPOLIS_LARGE_TREASURE_003_LSIGAME14 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_TANK_YARD} {LARGE_TREASURE} 3 {ETresItemDefLSIGameItem.LSIGAME14}'
    MONSTROPOLIS_LARGE_TREASURE_004_LSIGAME13 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.FACTORY_GROUND_FLOOR} {LARGE_TREASURE} 4 {ETresItemDefLSIGameItem.LSIGAME13}'
    MONSTROPOLIS_SMALL_TREASURE_001_ITEM_HIGHPOTION = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.LOBBY_AND_OFFICES} {SMALL_TREASURE} 1 {ETresItemDefBattleItem.ITEM_HIGHPOTION}'
    MONSTROPOLIS_SMALL_TREASURE_002_ACC_ITEM06 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.LAUGH_FLOOR} {SMALL_TREASURE} 2 {ETresItemDefAccessory.ACC_ITEM06}'
    MONSTROPOLIS_SMALL_TREASURE_003_ITEM_FOCUSSUPPLY = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.LAUGH_FLOOR} {SMALL_TREASURE} 3 {ETresItemDefBattleItem.ITEM_FOCUSSUPPLY}'
    MONSTROPOLIS_SMALL_TREASURE_005_MAT_ITEM54 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.FACTORY_GROUND_FLOOR} {SMALL_TREASURE} 4 {ETresItemDefMaterial.MAT_ITEM54}'
    MONSTROPOLIS_SMALL_TREASURE_006_PRT_ITEM46 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.FACTORY_GROUND_FLOOR} {SMALL_TREASURE} 5 {ETresItemDefProtector.PRT_ITEM46}'
    MONSTROPOLIS_SMALL_TREASURE_007_ITEM_HIGHPOTION = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.FACTORY_SECOND_FLOOR} {SMALL_TREASURE} 6 {ETresItemDefBattleItem.ITEM_HIGHPOTION}'
    MONSTROPOLIS_SMALL_TREASURE_008_ACC_ITEM14 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.FACTORY_SECOND_FLOOR} {SMALL_TREASURE} 7 {ETresItemDefAccessory.ACC_ITEM14}'
    MONSTROPOLIS_SMALL_TREASURE_009_PRT_ITEM45 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_ACCESSWAY} {SMALL_TREASURE} 8 {ETresItemDefProtector.PRT_ITEM45}'
    MONSTROPOLIS_SMALL_TREASURE_010_PRT_ITEM38 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_ACCESSWAY} {SMALL_TREASURE} 9 {ETresItemDefProtector.PRT_ITEM38}'
    MONSTROPOLIS_SMALL_TREASURE_011_MAT_ITEM54 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_ACCESSWAY} {SMALL_TREASURE} 10 {ETresItemDefMaterial.MAT_ITEM54}'
    MONSTROPOLIS_SMALL_TREASURE_012_ITEM_ETHER = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_TANK_YARD} {SMALL_TREASURE} 11 {ETresItemDefBattleItem.ITEM_ETHER}'
    MONSTROPOLIS_SMALL_TREASURE_013_ITEM_MEGAETHER = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_VAULT_PASSAGE} {SMALL_TREASURE} 12 {ETresItemDefBattleItem.ITEM_MEGAETHER}'
    MONSTROPOLIS_SMALL_TREASURE_014_ITEM_LASTELIXIR = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_VAULT_PASSAGE} {SMALL_TREASURE} 13 {ETresItemDefBattleItem.ITEM_LASTELIXIR}'
    MONSTROPOLIS_SMALL_TREASURE_015_ITEM_HIGHFOCUSSUPPLY = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_ACCESSWAY} {SMALL_TREASURE} 14 {ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY}'
    MONSTROPOLIS_SMALL_TREASURE_016_ACC_ITEM33 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.DOOR_VAULT_UPPER_LEVEL} {SMALL_TREASURE} 15 {ETresItemDefAccessory.ACC_ITEM33}'
    MONSTROPOLIS_SMALL_TREASURE_017_WEP_GOOFY_05 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.DOOR_VAULT_LOWER_LEVEL} {SMALL_TREASURE} 16 {ETresItemDefWeapon.WEP_GOOFY_05}'
    MONSTROPOLIS_SMALL_TREASURE_018_ITEM_HIGHPOTION = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.DOOR_VAULT_SERVICE_AREA} {SMALL_TREASURE} 17 {ETresItemDefBattleItem.ITEM_HIGHPOTION}'
    MONSTROPOLIS_SMALL_TREASURE_019_ACC_ITEM41 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.DOOR_VAULT_SERVICE_AREA} {SMALL_TREASURE} 18 {ETresItemDefAccessory.ACC_ITEM41}'
    
    KINGDOM_OF_CORONA_LARGE_TREASURE_001_NAVI_MAP_RA01 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_RA01}'
    KINGDOM_OF_CORONA_LARGE_TREASURE_002_NAVI_MAP_RA02 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {LARGE_TREASURE} 2 {ETresItemDefNavimap.NAVI_MAP_RA02}'
    KINGDOM_OF_CORONA_LARGE_TREASURE_003_LSIGAME15 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {LARGE_TREASURE} 3 {ETresItemDefLSIGameItem.LSIGAME15}'
    KINGDOM_OF_CORONA_LARGE_TREASURE_004_LSIGAME18 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WILDFLOWER_CLEARING} {LARGE_TREASURE} 4 {ETresItemDefLSIGameItem.LSIGAME18}'
    KINGDOM_OF_CORONA_LARGE_TREASURE_005_LSIGAME09 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.THOROUGHFARE} {LARGE_TREASURE} 5 {ETresItemDefLSIGameItem.LSIGAME09}'
    KINGDOM_OF_CORONA_LARGE_TREASURE_006_ACC_ITEM43 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WETLANDS} {LARGE_TREASURE} 6 {ETresItemDefAccessory.ACC_ITEM43}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_001_PRT_ITEM47 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.TOWER} {SMALL_TREASURE} 1 {ETresItemDefProtector.PRT_ITEM47}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_002_PRT_ITEM28 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {SMALL_TREASURE} 2 {ETresItemDefProtector.PRT_ITEM28}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_003_PRT_ITEM30 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {SMALL_TREASURE} 3 {ETresItemDefProtector.PRT_ITEM30}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_004_ACC_ITEM25 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {SMALL_TREASURE} 4 {ETresItemDefAccessory.ACC_ITEM25}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_005_ITEM_ALLCURE = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {SMALL_TREASURE} 5 {ETresItemDefBattleItem.ITEM_ALLCURE}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_006_ITEM_POTION = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {SMALL_TREASURE} 6 {ETresItemDefBattleItem.ITEM_POTION}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_007_ITEM_FOCUSSUPPLY = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {SMALL_TREASURE} 7 {ETresItemDefBattleItem.ITEM_FOCUSSUPPLY}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_008_ITEM_POTION = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {SMALL_TREASURE} 8 {ETresItemDefBattleItem.ITEM_POTION}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_009_PRT_ITEM41 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {SMALL_TREASURE} 9 {ETresItemDefProtector.PRT_ITEM41}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_010_ACC_ITEM34 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {SMALL_TREASURE} 10 {ETresItemDefAccessory.ACC_ITEM34}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_011_PRT_ITEM04 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {SMALL_TREASURE} 11 {ETresItemDefProtector.PRT_ITEM04}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_012_MAT_ITEM54 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {SMALL_TREASURE} 12 {ETresItemDefMaterial.MAT_ITEM54}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_013_MAT_ITEM34 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {SMALL_TREASURE} 13 {ETresItemDefMaterial.MAT_ITEM34}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_014_ITEM_ETHER = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {SMALL_TREASURE} 14 {ETresItemDefBattleItem.ITEM_ETHER}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_015_MAT_ITEM54 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.MARSH} {SMALL_TREASURE} 15 {ETresItemDefMaterial.MAT_ITEM54}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_016_ITEM_APUP = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.SHORE} {SMALL_TREASURE} 16 {ETresItemDefCampItem.ITEM_APUP}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_017_ITEM_HIGHETHER = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WILDFLOWER_CLEARING} {SMALL_TREASURE} 17 {ETresItemDefBattleItem.ITEM_HIGHETHER}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_018_ITEM_MAGICUP = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.THOROUGHFARE} {SMALL_TREASURE} 18 {ETresItemDefCampItem.ITEM_MAGICUP}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_019_ITEM_ETHER = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.THOROUGHFARE} {SMALL_TREASURE} 19 {ETresItemDefBattleItem.ITEM_ETHER}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_020_FOOD_ITEM41 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WHARF} {SMALL_TREASURE} 20 {ETresItemDefFood.FOOD_ITEM41}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_021_ACC_ITEM18 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WHARF} {SMALL_TREASURE} 21 {ETresItemDefAccessory.ACC_ITEM18}'
    KINGDOM_OF_CORONA_SMALL_TREASURE_022_ITEM_HIGHPOTION = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WHARF} {SMALL_TREASURE} 22 {ETresItemDefBattleItem.ITEM_HIGHPOTION}'
    
    TOY_BOX_LARGE_TREASURE_001_NAVI_MAP_TS01 = f'{TresWorldData.TOY_BOX} {TresAreaData.ANDYS_HOUSE} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_TS01}'
    TOY_BOX_LARGE_TREASURE_002_ITEM_ELIXIR = f'{TresWorldData.TOY_BOX} {TresAreaData.ANDYS_HOUSE} {LARGE_TREASURE} 2 {ETresItemDefBattleItem.ITEM_ELIXIR}'
    TOY_BOX_LARGE_TREASURE_003_NAVI_MAP_TS02 = f'{TresWorldData.TOY_BOX} {TresAreaData.MAIN_FLOOR_1F} {LARGE_TREASURE} 3 {ETresItemDefNavimap.NAVI_MAP_TS02}'
    TOY_BOX_LARGE_TREASURE_004_LSIGAME16 = f'{TresWorldData.TOY_BOX} {TresAreaData.LOWER_VENTS} {LARGE_TREASURE} 4 {ETresItemDefLSIGameItem.LSIGAME16}'
    TOY_BOX_LARGE_TREASURE_005_LSIGAME20 = f'{TresWorldData.TOY_BOX} {TresAreaData.KID_KORRAL} {LARGE_TREASURE} 5 {ETresItemDefLSIGameItem.LSIGAME20}'
    TOY_BOX_LARGE_TREASURE_006_LSIGAME10 = f'{TresWorldData.TOY_BOX} {TresAreaData.MAIN_FLOOR_3F} {LARGE_TREASURE} 6 {ETresItemDefLSIGameItem.LSIGAME10}'
    TOY_BOX_SMALL_TREASURE_001_MAT_ITEM35 = f'{TresWorldData.TOY_BOX} {TresAreaData.ANDYS_HOUSE} {SMALL_TREASURE} 1 {ETresItemDefMaterial.MAT_ITEM35}'
    TOY_BOX_SMALL_TREASURE_002_MAT_ITEM53 = f'{TresWorldData.TOY_BOX} {TresAreaData.ANDYS_HOUSE} {SMALL_TREASURE} 2 {ETresItemDefMaterial.MAT_ITEM53}'
    TOY_BOX_SMALL_TREASURE_003_PRT_ITEM36 = f'{TresWorldData.TOY_BOX} {TresAreaData.MAIN_FLOOR_2F} {SMALL_TREASURE} 3 {ETresItemDefProtector.PRT_ITEM36}'
    TOY_BOX_SMALL_TREASURE_004_ITEM_POTION = f'{TresWorldData.TOY_BOX} {TresAreaData.MAIN_FLOOR_3F} {SMALL_TREASURE} 4 {ETresItemDefBattleItem.ITEM_POTION}'
    TOY_BOX_SMALL_TREASURE_005_ITEM_POWERUP = f'{TresWorldData.TOY_BOX} {TresAreaData.ACTION_FIGURES} {SMALL_TREASURE} 5 {ETresItemDefCampItem.ITEM_POWERUP}'
    TOY_BOX_SMALL_TREASURE_006_ITEM_ETHER = f'{TresWorldData.TOY_BOX} {TresAreaData.ACTION_FIGURES} {SMALL_TREASURE} 6 {ETresItemDefBattleItem.ITEM_ETHER}'
    TOY_BOX_SMALL_TREASURE_007_ACC_ITEM32 = f'{TresWorldData.TOY_BOX} {TresAreaData.ACTION_FIGURES} {SMALL_TREASURE} 7 {ETresItemDefAccessory.ACC_ITEM32}'
    TOY_BOX_SMALL_TREASURE_008_ITEM_FOCUSSUPPLY = f'{TresWorldData.TOY_BOX} {TresAreaData.LOWER_VENTS} {SMALL_TREASURE} 8 {ETresItemDefBattleItem.ITEM_FOCUSSUPPLY}'
    TOY_BOX_SMALL_TREASURE_009_ITEM_ETHER = f'{TresWorldData.TOY_BOX} {TresAreaData.LOWER_VENTS} {SMALL_TREASURE} 9 {ETresItemDefBattleItem.ITEM_ETHER}'
    TOY_BOX_SMALL_TREASURE_010_ACC_ITEM27 = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_DOLLS} {SMALL_TREASURE} 10 {ETresItemDefAccessory.ACC_ITEM27}'
    TOY_BOX_SMALL_TREASURE_011_WEP_DONALD_01 = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_DOLLS} {SMALL_TREASURE} 11 {ETresItemDefWeapon.WEP_DONALD_01}'
    TOY_BOX_SMALL_TREASURE_012_MAT_ITEM53 = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_DOLLS} {SMALL_TREASURE} 12 {ETresItemDefMaterial.MAT_ITEM53}'
    TOY_BOX_SMALL_TREASURE_013_PRT_ITEM11 = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_DOLLS} {SMALL_TREASURE} 13 {ETresItemDefProtector.PRT_ITEM11}'
    TOY_BOX_SMALL_TREASURE_014_ITEM_HIGHETHER = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_OUTDOORS} {SMALL_TREASURE} 14 {ETresItemDefBattleItem.ITEM_HIGHETHER}'
    TOY_BOX_SMALL_TREASURE_015_PRT_ITEM42 = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_OUTDOORS} {SMALL_TREASURE} 15 {ETresItemDefProtector.PRT_ITEM42}'
    TOY_BOX_SMALL_TREASURE_016_ACC_ITEM04 = f'{TresWorldData.TOY_BOX} {TresAreaData.VIDEO_GAMES} {SMALL_TREASURE} 16 {ETresItemDefAccessory.ACC_ITEM04}'
    TOY_BOX_SMALL_TREASURE_017_MAT_ITEM53 = f'{TresWorldData.TOY_BOX} {TresAreaData.KID_KORRAL} {SMALL_TREASURE} 17 {ETresItemDefMaterial.MAT_ITEM53}'
    TOY_BOX_SMALL_TREASURE_018_ITEM_POTION = f'{TresWorldData.TOY_BOX} {TresAreaData.KID_KORRAL} {SMALL_TREASURE} 18 {ETresItemDefBattleItem.ITEM_POTION}'
    TOY_BOX_SMALL_TREASURE_019_ACC_ITEM13 = f'{TresWorldData.TOY_BOX} {TresAreaData.KID_KORRAL} {SMALL_TREASURE} 19 {ETresItemDefAccessory.ACC_ITEM13}'
    TOY_BOX_SMALL_TREASURE_020_PRT_ITEM19 = f'{TresWorldData.TOY_BOX} {TresAreaData.KID_KORRAL} {SMALL_TREASURE} 20 {ETresItemDefProtector.PRT_ITEM19}'
    TOY_BOX_SMALL_TREASURE_021_ACC_ITEM42 = f'{TresWorldData.TOY_BOX} {TresAreaData.REST_AREA} {SMALL_TREASURE} 21 {ETresItemDefAccessory.ACC_ITEM42}'
    TOY_BOX_SMALL_TREASURE_022_ITEM_HIGHFOCUSSUPPLY = f'{TresWorldData.TOY_BOX} {TresAreaData.MAIN_FLOOR_1F} {SMALL_TREASURE} 22 {ETresItemDefBattleItem.ITEM_HIGHFOCUSSUPPLY}'
    TOY_BOX_SMALL_TREASURE_023_MAT_ITEM34 = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_OUTDOORS} {SMALL_TREASURE} 23 {ETresItemDefMaterial.MAT_ITEM34}'

    TWILIGHT_TOWN_LARGE_TREASURE_001_NAVI_MAP_TT01 = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.TRAM_COMMON} {LARGE_TREASURE} 1 {ETresItemDefNavimap.NAVI_MAP_TT01}'
    TWILIGHT_TOWN_SMALL_TREASURE_001_MAT_ITEM33 = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.TRAM_COMMON} {SMALL_TREASURE} 1 {ETresItemDefMaterial.MAT_ITEM33}'
    TWILIGHT_TOWN_SMALL_TREASURE_002_MAT_ITEM53 = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.TRAM_COMMON} {SMALL_TREASURE} 2 {ETresItemDefMaterial.MAT_ITEM53}'
    TWILIGHT_TOWN_SMALL_TREASURE_003_MAT_ITEM53 = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.TRAM_COMMON} {SMALL_TREASURE} 3 {ETresItemDefMaterial.MAT_ITEM53}'
    TWILIGHT_TOWN_SMALL_TREASURE_004_ITEM_HIGHPOTION = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.TRAM_COMMON} {SMALL_TREASURE} 4 {ETresItemDefBattleItem.ITEM_HIGHPOTION}'
    TWILIGHT_TOWN_SMALL_TREASURE_005_ITEM_FOCUSSUPPLY = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.UNDERGROUND_CONDUIT} {SMALL_TREASURE} 5 {ETresItemDefBattleItem.ITEM_FOCUSSUPPLY}'
    TWILIGHT_TOWN_SMALL_TREASURE_006_ITEM_APUP = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.THE_WOODS} {SMALL_TREASURE} 6 {ETresItemDefCampItem.ITEM_APUP}'
    TWILIGHT_TOWN_SMALL_TREASURE_007_ITEM_ETHER = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.THE_WOODS} {SMALL_TREASURE} 7 {ETresItemDefBattleItem.ITEM_ETHER}'
    TWILIGHT_TOWN_SMALL_TREASURE_008_MAT_ITEM53 = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.THE_WOODS} {SMALL_TREASURE} 8 {ETresItemDefMaterial.MAT_ITEM53}'
    TWILIGHT_TOWN_SMALL_TREASURE_009_ITEM_GUARDUP = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.THE_OLD_MANSION} {SMALL_TREASURE} 9 {ETresItemDefCampItem.ITEM_GUARDUP}'
    
    @classmethod
    def generate_locations(cls):
        locations: LocationData = []

        world_mapping = {
            "SCALA_AD_CAELUM": TresWorldData.SCALA_AD_CAELUM,
            "SAN_FRANSOKYO": TresWorldData.SAN_FRANSOKYO,
            "THE_CARIBBEAN": TresWorldData.THE_CARIBBEAN,
            "THE_FINAL_WORLD": TresWorldData.THE_FINAL_WORLD,
            "ARENDELLE": TresWorldData.ARENDELLE,
            "OLYMPUS": TresWorldData.OLYMPUS,
            "KEYBLADE_GRAVEYARD": TresWorldData.KEYBLADE_GRAVEYARD,
            "MONSTROPOLIS": TresWorldData.MONSTROPOLIS,
            "KINGDOM_OF_CORONA": TresWorldData.KINGDOM_OF_CORONA,
            "TOY_BOX": TresWorldData.TOY_BOX,
            "TWILIGHT_TOWN": TresWorldData.TWILIGHT_TOWN,
        }

        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue
            
            for prefix, world in world_mapping.items():
                if key.startswith(prefix):
                    locations.append(LocationData(value, key, world, '', cls.TREASURE_CHEST))
                    break
        
        for location in locations:
            for key, value in TresAreaData.__dict__.items():
                if key.startswith("__"):
                    continue

                if value in location.loc_name:
                    location = location._replace(area_name=value)
                    break

        return locations

class TresVictoryBonusDataLocation(KingdomHeartsIIILocation):
    """
    """
    VICTORY_BONUS = 'Victory Bonus'
    BONUS_SORA = 'Bonus Sora'
    ABILITY_SORA = 'Ability Sora'

    VBONUS_001_he_001_BONUSSORA1_HP_UP10 = f'{TresWorldData.OLYMPUS} {TresAreaData.AGORA_RUIN} {VICTORY_BONUS} Initial Battle ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'
    VBONUS_005_he_005_BONUSSORA1_HP_UP10 = f'{TresWorldData.OLYMPUS} {TresAreaData.OVERLOOK_RUIN} {VICTORY_BONUS} Fire Core Battle (Thebes) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'
    VBONUS_006_he_006_BONUSSORA1_HP_UP10 = f'{TresWorldData.OLYMPUS} {TresAreaData.GARDENS_RUIN} {VICTORY_BONUS} Fire Core Battle (Gardens) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'
    VBONUS_008_he_008_BONUSSORA1_HP_UP10 = f'{TresWorldData.OLYMPUS} {TresAreaData.AGORA_GOLEM} {VICTORY_BONUS} Defeat the Rock Troll ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'
    VBONUS_010_he_010_BONUSSORA1_MP_UP5 = f'{TresWorldData.OLYMPUS} {TresAreaData.SUMMIT} {VICTORY_BONUS} Defeat the Rock Titan ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP5})'
    VBONUS_013_he_013_BONUSSORA1_HP_UP10 = f'{TresWorldData.OLYMPUS} {TresAreaData.BOSS_ARENA} {VICTORY_BONUS} Defeat the Tornado Titan ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'
    
    VBONUS_014_tt_001_BONUSSORA1_MELEM_CURE = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.TRAM_COMMON} {VICTORY_BONUS} Defeat the Demon Tide ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_CURE})'
    VBONUS_014_tt_001_ABILITYSORA1_MP_SAFETY = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.TRAM_COMMON} {VICTORY_BONUS} Defeat the Demon Tide ({ABILITY_SORA} 1 - {ETresAbilityKind.MP_SAFETY})'
    VBONUS_016_tt_003_BONUSSORA1_MELEM_BLIZZARD = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.THE_OLD_MANSION} {VICTORY_BONUS} Defeat Dusks and Neoshadows ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_BLIZZARD})'
    VBONUS_016_tt_003_BONUSSORA2_HP_UP10 = f'{TresWorldData.TWILIGHT_TOWN} {TresAreaData.THE_OLD_MANSION} {VICTORY_BONUS} Defeat Dusks and Neoshadows ({BONUS_SORA} 2 - {ETresVictoryBonusKind.HP_UP10})'

    VBONUS_017_ts_001_ABILITYSORA1_AIR_RECOVERY = f'{TresWorldData.TOY_BOX} {TresAreaData.ANDYS_HOUSE} {VICTORY_BONUS} Defeat Heartless in Andy\'s Room ({ABILITY_SORA} 1 - {ETresAbilityKind.AIR_RECOVERY})'
    VBONUS_019_ts_003_ABILITYSORA1_TRIPPLE_SLASH = f'{TresWorldData.TOY_BOX} {TresAreaData.ACTION_FIGURES} {VICTORY_BONUS} Defeat the Monsterous Monsters ({ABILITY_SORA} 1 - {ETresAbilityKind.TRIPPLE_SLASH})'
    VBONUS_020_ts_004_ABILITYSORA1_HIGHJUMP = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_DOLLS} {VICTORY_BONUS} Defeat Angelic Amber ({ABILITY_SORA} 1 - {ETresAbilityKind.HIGHJUMP})'
    VBONUS_020_ts_004_BONUSSORA2_MP_UP5 = f'{TresWorldData.TOY_BOX} {TresAreaData.BABIES_AND_TODDLERS_DOLLS} {VICTORY_BONUS} Defeat Angelic Amber ({BONUS_SORA} 2 - {ETresVictoryBonusKind.MP_UP5})'
    VBONUS_021_ts_005_BONUSSORA1_MELEM_THUNDER = f'{TresWorldData.TOY_BOX} {TresAreaData.KID_KORRAL} {VICTORY_BONUS} Defeat the UFO ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_THUNDER})'
    VBONUS_022_ts_006_BONUSSORA1_ACC_SLOT_UP1 = f'{TresWorldData.TOY_BOX} {TresAreaData.VIDEO_GAMES} {VICTORY_BONUS} Complete Verum Rex: Beat of Lead ({BONUS_SORA} 1 - {ETresVictoryBonusKind.ACC_SLOT_UP1})'
    VBONUS_023_ts_007_BONUSSORA1_HP_UP10 = f'{TresWorldData.TOY_BOX} {TresAreaData.BOSS_ARENA} {VICTORY_BONUS} Defeat King of Toys ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'
    VBONUS_023_ts_007_ABILITYSORA1_AIR_DOWN = f'{TresWorldData.TOY_BOX} {TresAreaData.BOSS_ARENA} {VICTORY_BONUS} Defeat King of Toys ({ABILITY_SORA} 1 - {ETresAbilityKind.AIR_DOWN})'

    VBONUS_024_ra_001_BONUSSORA1_MELEM_AERO = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {VICTORY_BONUS} Initial Battle ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_AERO})'
    VBONUS_026_ra_003_ABILITYSORA1_GUARD_COUNTER = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {VICTORY_BONUS} Defeat the Reapears (Initial) ({ABILITY_SORA} 1 - {ETresAbilityKind.GUARD_COUNTER})'
    VBONUS_027_ra_004_BONUSSORA1_MP_UP5 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WETLANDS} {VICTORY_BONUS} Defeat the Chaos Carriage ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP5})'
    VBONUS_027_ra_004_ABILITYSORA1_SUPERJUMP = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WETLANDS} {VICTORY_BONUS} Defeat the Chaos Carriage ({ABILITY_SORA} 1 - {ETresAbilityKind.SUPERJUMP})'
    VBONUS_028_ra_005_ABILITYSORA1_SLASH_UPPER = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.WHARF} {VICTORY_BONUS} Defeat the Reapears (Wharf) ({ABILITY_SORA} 1 - {ETresAbilityKind.SLASH_UPPER})'
    VBONUS_029_ra_006_BONUSSORA1_DEF_SLOT_UP1 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.TOWER} {VICTORY_BONUS} Defeat Heartless (Tower) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.DEF_SLOT_UP1})'
    VBONUS_030_ra_007_BONUSSORA1_HP_UP10 = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.TOWER} {VICTORY_BONUS} Defeat the Grim Guardianess ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'

    VBONUS_032_mi_001_ABILITYSORA1_REVENGEIMPACT = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.LOBBY_AND_OFFICES} {VICTORY_BONUS} Initial Battle ({ABILITY_SORA} 1 - {ETresAbilityKind.REVENGEIMPACT})'
    VBONUS_034_mi_003_BONUSSORA1_MELEM_FIRE = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.DOOR_VAULT_LOWER_LEVEL} {VICTORY_BONUS} Laughter Battle 1 ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_FIRE})'
    VBONUS_036_mi_005_ABILITYSORA1_COMBO_MASTER = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.FACTORY_SECOND_FLOOR} {VICTORY_BONUS} Laughter Battle 2 ({ABILITY_SORA} 1 - {ETresAbilityKind.COMBO_MASTER})'
    VBONUS_037_mi_006_BONUSSORA1_MELEM_WATER = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_TANK_YARD} {VICTORY_BONUS} Fire Battle 1 ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_WATER})'
    VBONUS_038_mi_007_BONUSSORA1_ITEM_SLOT_UP1 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_TANK_YARD} {VICTORY_BONUS} Fire Battle 2 ({BONUS_SORA} 1 - {ETresVictoryBonusKind.ITEM_SLOT_UP1})'
    VBONUS_039_mi_008_ABILITYSORA1_CHARGE_THRUST = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_ACCESSWAY} {VICTORY_BONUS} Defeat the Spiked Turtletoad ({ABILITY_SORA} 1 - {ETresAbilityKind.CHARGE_THRUST})'
    VBONUS_040_mi_009_BONUSSORA1_MELEM_CURE = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_VAULT_PASSAGE} {VICTORY_BONUS} Defeat the Lump of Horror ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_CURE})'
    VBONUS_040_mi_009_BONUSSORA2_HP_UP10 = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.POWER_PLANT_VAULT_PASSAGE} {VICTORY_BONUS} Defeat the Lump of Horror ({BONUS_SORA} 2 - {ETresVictoryBonusKind.HP_UP10})'
    
    VBONUS_041_fz_001_ABILITYSORA1_AIR_ROLL_BEAT = f'{TresWorldData.ARENDELLE} {TresAreaData.TREESCAPE} {VICTORY_BONUS} Defeat the Rock Troll ({ABILITY_SORA} 1 - {ETresAbilityKind.AIR_ROLL_BEAT})'
    VBONUS_043_fz_003_BONUSSORA1_MELEM_THUNDER = f'{TresWorldData.ARENDELLE} {TresAreaData.THE_LABYRINTH_OF_ICE_LOWER_TIER} {VICTORY_BONUS} Defeat the Ninjas 2 ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_THUNDER})'
    VBONUS_045_fz_005_BONUSSORA1_RISKDODGE = f'{TresWorldData.ARENDELLE} {TresAreaData.THE_LABYRINTH_OF_ICE_MIDDLE_TIER} {VICTORY_BONUS} Defeat the Ninjas 4 ({ABILITY_SORA} 1 - {ETresVictoryBonusKind.MELEM_BLIZZARD})'
    VBONUS_047_fz_007_BONUSSORA1_MELEM_BLIZZARD = f'{TresWorldData.ARENDELLE} {TresAreaData.BOSS_ARENA} {VICTORY_BONUS} Defeat Marshmallow ({BONUS_SORA} 1)'
    VBONUS_048_fz_008_ABILITYSORA1_DOUBLEFLIGHT = f'{TresWorldData.ARENDELLE} {TresAreaData.BOSS_ARENA} {VICTORY_BONUS} Defeat Frost Serpents ({ABILITY_SORA} 1 - {ETresAbilityKind.DOUBLEFLIGHT})'
    VBONUS_049_fz_009_ABILITYSORA1_AIRSLIDE = f'{TresWorldData.ARENDELLE} {TresAreaData.VALLEY_OF_ICE} {VICTORY_BONUS} Defeat Heartless (Frozen Lake) ({ABILITY_SORA} 1 - {ETresAbilityKind.AIRSLIDE})'
    VBONUS_049_fz_009_BONUSSORA1_ACC_SLOT_UP1 = f'{TresWorldData.ARENDELLE} {TresAreaData.VALLEY_OF_ICE} {VICTORY_BONUS} Defeat Heartless (Frozen Lake) ({ABILITY_SORA} 1 - {ETresVictoryBonusKind.ACC_SLOT_UP1})'
    VBONUS_050_fz_010_ABILITYSORA1_SUPERSLIDE = f'{TresWorldData.ARENDELLE} {TresAreaData.FOOTHILLS} {VICTORY_BONUS} Defeat Sköll ({ABILITY_SORA} 1 - {ETresAbilityKind.SUPERSLIDE})'
    VBONUS_050_fz_010_BONUSSORA1_MP_UP5 = f'{TresWorldData.ARENDELLE} {TresAreaData.FOOTHILLS} {VICTORY_BONUS} Defeat Sköll ({ABILITY_SORA} 1 - {ETresVictoryBonusKind.MP_UP5})'
    
    VBONUS_052_bx_002_ABILITYSORA1_FOCUS_ASPIR = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.BRIDGE} {VICTORY_BONUS} Meet Big Hero 6 ({ABILITY_SORA} 1 - {ETresAbilityKind.FOCUS_ASPIR})'
    VBONUS_054_bx_004_BONUSSORA1_MELEM_FIRE = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {VICTORY_BONUS} Defeat the Catastrochorus ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_FIRE})'
    VBONUS_055_bx_005_BONUSSORA1_SUPERSLIDE = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {VICTORY_BONUS} Rescue Big Hero 6 ({ABILITY_SORA} 1 - {ETresAbilityKind.SUPERSLIDE})'
    VBONUS_056_bx_006_BONUSSORA1_DEF_SLOT_UP1 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {VICTORY_BONUS} Defeat the Darkubes ({BONUS_SORA} 1 - {ETresVictoryBonusKind.DEF_SLOT_UP1})'
    VBONUS_057_bx_007_BONUSSORA1_MELEM_AERO = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {VICTORY_BONUS} Defeat Dark Baymax ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_AERO})'
    VBONUS_057_bx_007_BONUSSORA2_HP_UP10 = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {VICTORY_BONUS} Defeat Dark Baymax ({BONUS_SORA} 2 - {ETresVictoryBonusKind.HP_UP10})'
    
    VBONUS_058_ca_001_ABILITYSORA1_REVENGEDIVE = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.DAVY_JONES_LOCKER} {VICTORY_BONUS} Defeat the Anchor Raiders ({ABILITY_SORA} 1 - {ETresAbilityKind.REVENGEDIVE})'
    VBONUS_060_ca_003_ABILITYSORA1_AIRSLIDE = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.THE_HIGH_SEAS} {VICTORY_BONUS} Defeat the Raging Vulture ({ABILITY_SORA} 1 - {ETresAbilityKind.AIRSLIDE})'
    VBONUS_061_ca_004_BONUSSORA1_MELEM_THUNDER = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.HUDDLED_ISLES} {VICTORY_BONUS} Defeat the Lightning Angler ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_THUNDER})'
    VBONUS_062_ca_005_BONUSSORA1_ITEM_SLOT_UP1 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.THE_HIGH_SEAS} {VICTORY_BONUS} Beat Luxord Ship Race ({BONUS_SORA} 1 - {ETresVictoryBonusKind.ITEM_SLOT_UP1})'
    VBONUS_063_ca_006_ABILITYSORA1_MAGICFLUSH = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.THE_HIGH_SEAS} {VICTORY_BONUS} Defeat Heartless and Nobodies (Luxord\'s Ship) ({ABILITY_SORA} 1 - {ETresAbilityKind.MAGICFLUSH})'
    VBONUS_064_ca_007_BONUSSORA1_MELEM_WATER = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.THE_HIGH_SEAS} {VICTORY_BONUS} Defeat Pirate Ships ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_WATER})'
    VBONUS_066_ca_009_ABILITYSORA1_BLOW_COUNTER = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.BOSS_ARENA} {VICTORY_BONUS} Defeat Davy Jones ({ABILITY_SORA} 1 - {ETresAbilityKind.BLOW_COUNTER})'
    VBONUS_066_ca_009_BONUSSORA2_HP_UP10 = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.BOSS_ARENA} {VICTORY_BONUS} Defeat Davy Jones ({BONUS_SORA} 2 - {ETresVictoryBonusKind.HP_UP10})'

    VBONUS_067_dw_001_BONUSSORA1_MELEM_BLIZZARD = f'{TresWorldData.DARK_WORLD} {TresAreaData.DARK_MARGIN} {VICTORY_BONUS} Defeat Anti-Aqua ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_BLIZZARD})'
    VBONUS_067_dw_001_BONUSSORA2_HP_UP10 = f'{TresWorldData.DARK_WORLD} {TresAreaData.DARK_MARGIN} {VICTORY_BONUS} Defeat Anti-Aqua ({BONUS_SORA} 2 - {ETresVictoryBonusKind.HP_UP10})'

    VBONUS_068_ew_001_BONUSSORA1_MELEM_AERO = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {VICTORY_BONUS} Defeat the Lich ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_AERO})'
    VBONUS_068_ew_001_BONUSSORA2_MP_UP5 = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.THE_CITY_CENTRAL_DISTRICT} {VICTORY_BONUS} Defeat the Lich ({BONUS_SORA} 2 - {ETresVictoryBonusKind.MP_UP5})'

    VBONUS_069_kg_001_ABILITYSORA1_REVENGE_EX = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_BADLANDS} {VICTORY_BONUS} Defeat the 10,000 Heartless ({ABILITY_SORA} 1 - {ETresAbilityKind.REVENGE_EX})'
    VBONUS_069_kg_001_BONUSSORA2_ITEM_SLOT_UP1 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_BADLANDS} {VICTORY_BONUS} Defeat the 10,000 Heartless ({BONUS_SORA} 2 - {ETresVictoryBonusKind.ITEM_SLOT_UP1})'
    VBONUS_070_kg_002_BONUSSORA1_MELEM_CURE = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_BADLANDS} {VICTORY_BONUS} Defeat the Demon Tide ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_CURE})'
    VBONUS_071_kg_003_BONUSSORA1_MP_UP5 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Xigbar and Replica Riku ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP5})'
    VBONUS_072_kg_004_BONUSSORA1_HP_UP10 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Luxord, Marluxia, and Larxene ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'
    VBONUS_073_kg_005_BONUSSORA1_MP_UP5 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Vanitas and Terra-Xehanort ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP5})'
    VBONUS_074_kg_006_BONUSSORA1_HP_UP10 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Saix ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP10})'
    VBONUS_075_kg_007_BONUSSORA1_HP_UP10 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Young Xehanort, Ansem and Xemnas ({BONUS_SORA} 1)'
    
    VBONUS_076_ew_002_ABILITYSORA1_GLIDE = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.UNKNOWN} {VICTORY_BONUS} Received before Sora Collection ({ABILITY_SORA} 1 - {ETresAbilityKind.GLIDE})'
    
    # TODO: Only one of these can ever be selected... So I think we leave them out of our pool
    # VBONUS_079_Select_HP_BONUSSORA1_HP_UP30 = f'{TresWorldData.STATION_OF_AWAKENING} {VICTORY_BONUS} Selected Vitality ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP30})'
    # VBONUS_080_Select_NT_BONUSSORA1_HP_UP15 = f'{TresWorldData.TOY_BOX} {VICTORY_BONUS} Selected Balanced ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP15})'
    # VBONUS_080_Select_NT_BONUSSORA2_MP_UP10 = f'{TresWorldData.TOY_BOX} {VICTORY_BONUS} Selected Balanced ({BONUS_SORA} 2 - {ETresVictoryBonusKind.MP_UP10})'
    # VBONUS_081_Select_MP_BONUSSORA1_MP_UP20 = f'{TresWorldData.TOY_BOX} {VICTORY_BONUS} Selected Wisdom ({BONUS_SORA} 1) - {ETresVictoryBonusKind.MP_UP20}'

    VBONUS_082_ew_001_BONUSSORA1_MELEM_FIRE = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.UNKNOWN} {VICTORY_BONUS} Defeat the Darkside ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_FIRE})'
    VBONUS_082_ew_001_BONUSSORA1_MELEM_WATER = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.UNKNOWN} {VICTORY_BONUS} Defeat the Darkside ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MELEM_WATER})'
    VBONUS_083_ew_002_BONUSSORA1_HP_UP5 = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.UNKNOWN} {VICTORY_BONUS} Collect 200 Soras ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP5})'
    VBONUS_084_ew_003_BONUSSORA1_HP_UP5 = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.UNKNOWN} {VICTORY_BONUS} Collect 300 Soras ({BONUS_SORA} 1 - {ETresVictoryBonusKind.HP_UP5})'

    TS_Sub_Minigame_CLEAR_A_ABILITYSORA1_FOCUS_ASPIR = f'{TresWorldData.TOY_BOX} {TresAreaData.VIDEO_GAMES} {VICTORY_BONUS} Get A Rank on Verum Rex: Beat of Lead ({ABILITY_SORA} 1 - {ETresAbilityKind.FOCUS_ASPIR})'
    RA_AfterDance_CLEAR_A_ABILITYSORA1_UNISON_THUNDER = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.THOROUGHFARE} {VICTORY_BONUS} Get A Rank on Festival Dance ({ABILITY_SORA} 1 - {ETresAbilityKind.UNISON_THUNDER})'
    FZ_Sub_RESULT_RANK_A_ABILITYSORA1_FUSION_ROCKET = f'{TresWorldData.ARENDELLE} {TresAreaData.SUMMIT} {VICTORY_BONUS} Get A Rank on Frozen Slider ({ABILITY_SORA} 1 - {ETresAbilityKind.FUSION_ROCKET})'
    FZ_Sub_RESULT_TREASURECOMPLETE_ABILITYSORA1_MASTER_DRAW = f'{TresWorldData.ARENDELLE} {TresAreaData.SUMMIT} {VICTORY_BONUS} Collect 10 Treasures in Frozen Slider ({ABILITY_SORA} 1 - {ETresAbilityKind.MASTER_DRAW})'
    BX_FLASHTRACER_01_RANK_A_ABILITYSORA1_ATTRACTION_UP = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {VICTORY_BONUS} Get A Rank in Flash Tracer course 1 ({ABILITY_SORA} 1 - {ETresAbilityKind.ATTRACTION_TIME})'
    BX_FLASHTRACER_02_RANK_A_ABILITYSORA1_MAGIC_TIME = f'{TresWorldData.THE_FINAL_WORLD} {TresAreaData.THE_CITY_NORTH_DISTRICT} {VICTORY_BONUS} Get A Rank in Flash Tracer course 2 ({ABILITY_SORA} 1 - {ETresAbilityKind.MAGIC_TIME})'

    HE_Sub_Pudding_CLEAR_A_ABILITYSORA1_FORM_TIME = f'{TresWorldData.OLYMPUS} {TresAreaData.OVERLOOK} {VICTORY_BONUS} Cherry Flan (20,000+ points) ({ABILITY_SORA} 1 - {ETresAbilityKind.FORM_TIME})'
    TS_Sub_Pudding_CLEAR_A_ABILITYSORA1_ATTRACTION_UP = f'{TresWorldData.TOY_BOX} {TresAreaData.REST_AREA} {VICTORY_BONUS} Cherry Flan (17,000+ points) ({ABILITY_SORA} 1 - {ETresAbilityKind.ATTRACTION_UP})'
    RA_Sub_Pudding_CLEAR_A_ABILITYSORA1_PRIZE_DRAW = f'{TresWorldData.KINGDOM_OF_CORONA} {TresAreaData.HILLS} {VICTORY_BONUS} Orange Flan (23,000+ points) ({ABILITY_SORA} 1 - {ETresAbilityKind.PRIZE_DRAW})'
    MI_Sub_Pudding_CLEAR_A_ABILITYSORA1_MAGIC_TIME = f'{TresWorldData.MONSTROPOLIS} {TresAreaData.DOOR_VAULT_UPPER_LEVEL} {VICTORY_BONUS} Banana Flan (20,000+ points) ({ABILITY_SORA} 1 - {ETresAbilityKind.MAGIC_TIME})'
    FZ_Sub_Pudding_CLEAR_A_ABILITYSORA1_UNISON_BLIZZARD = f'{TresWorldData.ARENDELLE} {TresAreaData.MOUNTAINSIDE} {VICTORY_BONUS} Grape Flan (20,000+ points) ({ABILITY_SORA} 1 - {ETresAbilityKind.UNISON_BLIZZARD})'
    CA_Sub_Pudding_CLEAR_A_ABILITYSORA1_FOCUS_ASPIR = f'{TresWorldData.THE_CARIBBEAN} {TresAreaData.PORT_ROYAL_FORT} {VICTORY_BONUS} Watermelon Flan (28,000+ points) ({ABILITY_SORA} 1 - {ETresAbilityKind.FOCUS_ASPIR})'
    BX_Sub_Pudding_CLEAR_A_ABILITYSORA1_ATTRACTION_TIME = f'{TresWorldData.SAN_FRANSOKYO} {TresAreaData.THE_CITY_SOUTH_DISTRICT} {VICTORY_BONUS} Melon Flan (15,000+ points) ({ABILITY_SORA} 1 - {ETresAbilityKind.ATTRACTION_TIME})'
    
    VBONUS_DLC_001_kg_001_BONUSSORA1_ITEM_SLOT_UP1 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_BADLANDS} {VICTORY_BONUS} Defeat Dark Inferno χ (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.ITEM_SLOT_UP1})'

    VBONUS_DLC_002_kg_002_BONUSSORA1_MP_UP3 = f'{TresWorldData.DARK_WORLD} {TresAreaData.DARK_MARGIN} {VICTORY_BONUS} Defeat Anti-Aqua (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP3})'

    VBONUS_DLC_003_kg_003_BONUSSORA1_MP_UP3 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Terra-Xehanort (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP3})'
    VBONUS_DLC_004_kg_004_BONUSSORA1_MP_UP3 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Xigbar and Replica Riku (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP3})'
    VBONUS_DLC_005_kg_005_BONUSSORA1_MP_UP3 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Luxord, Marluxia, and Larxene (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP3})'
    VBONUS_DLC_006_kg_006_BONUSSORA1_MP_UP3 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Vanitas and Terra-Xehanort (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP3})'
    VBONUS_DLC_007_kg_007_BONUSSORA1_MP_UP3 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Saix (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP3})'
    VBONUS_DLC_008_kg_008_BONUSSORA1_MP_UP3 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.THE_SKEIN_OF_SEVERANCE} {VICTORY_BONUS} Defeat Young Xehanort, Ansem and Xemnas (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP3})'
    
    VBONUS_DLC_010_bt_002_BONUSSORA1_MP_UP3 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.BREEZY_QUARTER} {VICTORY_BONUS} Defeat Heart Piece Darkside (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.MP_UP3})'

    VBONUS_DLC_015_kg_012_BONUSSORA1_ITEM_SLOT_UP1 = f'{TresWorldData.KEYBLADE_GRAVEYARD} {TresAreaData.BOSS_ARENA} {VICTORY_BONUS} Armored Xehanort (DLC) ({BONUS_SORA} 1 - {ETresVictoryBonusKind.ITEM_SLOT_UP1})'
    
    # TODO: POTENTIALLY DEBUG VBONUSES?
    # VBONUS_DLC_init_01_ABILITYSORA1_QUICK_SHAFT = f'{TresWorldData.INITIAL} {TresAreaData.INITIAL} {VICTORY_BONUS} Initial 1 (DLC) ({ABILITY_SORA} 1 - {ETresAbilityKind.QUICK_SHAFT})'
    # VBONUS_DLC_init_01_ABILITYSORA2_FLASH_STEP = f'{TresWorldData.INITIAL} {TresAreaData.INITIAL} {VICTORY_BONUS} Initial 1 (DLC) ({ABILITY_SORA} 2 - {ETresAbilityKind.FLASH_STEP})'
    # VBONUS_DLC_init_02_ABILITYSORA1_RADIAL_CUT = f'{TresWorldData.INITIAL} {TresAreaData.INITIAL} {VICTORY_BONUS} Initial 2 (DLC) ({ABILITY_SORA} 1 - {ETresAbilityKind.RADIAL_CUT})'
    # VBONUS_DLC_init_02_ABILITYSORA2_AERIAL_SWEEP = f'{TresWorldData.INITIAL} {TresAreaData.INITIAL} {VICTORY_BONUS} Initial 2 (DLC) ({ABILITY_SORA} 2 - {ETresAbilityKind.AERIAL_SWEEP})'
    # VBONUS_DLC_init_03_ABILITYSORA1_AERIAL_DIVE = f'{TresWorldData.INITIAL} {TresAreaData.INITIAL} {VICTORY_BONUS} Initial 3 (DLC) ({ABILITY_SORA} 1 - {ETresAbilityKind.AERIAL_DIVE})'
    # VBONUS_DLC_init_03_ABILITYSORA2_FINAL_HEAVEN = f'{TresWorldData.INITIAL} {TresAreaData.INITIAL} {VICTORY_BONUS} Initial 3 (DLC) ({ABILITY_SORA} 2 - {ETresAbilityKind.FINAL_HEAVEN})'
    
    @classmethod
    def generate_locations(cls):
        locations = []

        world_code_map = {
            "bt": TresWorldData.SCALA_AD_CAELUM,
            "bx": TresWorldData.SAN_FRANSOKYO,
            "ca": TresWorldData.THE_CARIBBEAN,
            "ew": TresWorldData.THE_FINAL_WORLD,
            "fz": TresWorldData.ARENDELLE,
            "he": TresWorldData.OLYMPUS,
            "kg": TresWorldData.KEYBLADE_GRAVEYARD,
            "mi": TresWorldData.MONSTROPOLIS,
            "ra": TresWorldData.KINGDOM_OF_CORONA,
            "ts": TresWorldData.TOY_BOX,
            "tt": TresWorldData.TWILIGHT_TOWN,
            "init": TresWorldData.UNKNOWN,
        }

        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue

            lowered_key = key.lower()

            for code, world in world_code_map.items():
                if code in lowered_key:
                    locations.append(LocationData(value, key, world, '', cls.VICTORY_BONUS))
                    break
        
        for location in locations:
            for key, value in TresAreaData.__dict__.items():
                if key.startswith("__"):
                    continue

                if value in location.loc_name:
                    location = location._replace(area_name=value)
                    break
        
        return locations

class TresWeaponEnhanceDataLocation(KingdomHeartsIIILocation):
    """
    """
    WEAPON_ENHANCE = 'Weapon Enhance'

    WEP_KEYBLADE00_WEAPON_ENHANCE_4_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_00} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.FORM_TIME})'

    WEP_KEYBLADE01_WEAPON_ENHANCE_4_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_01} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.FORM_TIME})'

    WEP_KEYBLADE02_WEAPON_ENHANCE_4_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_02} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.FORM_TIME})'

    WEP_KEYBLADE03_WEAPON_ENHANCE_4_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_03} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.FORM_TIME})'

    WEP_KEYBLADE04_WEAPON_ENHANCE_4_AEROGAN = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_04} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.AEROGAN})'
    WEP_KEYBLADE04_WEAPON_ENHANCE_10_AERO_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_04} {WEAPON_ENHANCE} 10 ({ETresAbilityKind.AERO_UP})'

    # In code as 09?
    WEP_KEYBLADE05_WEAPON_ENHANCE_6_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_09} {WEAPON_ENHANCE} 6 ({ETresAbilityKind.FULLMP_BURST})'

    WEP_KEYBLADE06_WEAPON_ENHANCE_9_BLIZZARD_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_06} {WEAPON_ENHANCE} 9 ({ETresAbilityKind.BLIZZARD_UP})'

    WEP_KEYBLADE07_WEAPON_ENHANCE_6_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_07} {WEAPON_ENHANCE} 6 ({ETresAbilityKind.FORM_TIME})'

    WEP_KEYBLADE08_WEAPON_ENHANCE_6_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_08} {WEAPON_ENHANCE} 6 ({ETresAbilityKind.FORM_TIME})'

    # In code as 05?
    WEP_KEYBLADE09_WEAPON_ENHANCE_6_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_05} {WEAPON_ENHANCE} 6 ({ETresAbilityKind.FORM_TIME})'

    # In code as 10?
    WEP_KEYBLADE10_WEAPON_ENHANCE_6_MP_HASTE = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_12} {WEAPON_ENHANCE} 6 ({ETresAbilityKind.MP_HASTE})'
    WEP_KEYBLADE10_WEAPON_ENHANCE_9_MP_HASTE = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_12} {WEAPON_ENHANCE} 9 ({ETresAbilityKind.MP_HASTE})'

    # In code as 11?
    WEP_KEYBLADE11_WEAPON_ENHANCE_3_CHARISMA_CHEF = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_11} {WEAPON_ENHANCE} 3 ({ETresAbilityKind.CHARISMA_CHEF})'

    WEP_KEYBLADE12_WEAPON_ENHANCE_4_FORM_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_13} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.FORM_UP})'
    WEP_KEYBLADE12_WEAPON_ENHANCE_9_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_13} {WEAPON_ENHANCE} 9 ({ETresAbilityKind.FORM_TIME})'

    WEP_KEYBLADE13_WEAPON_ENHANCE_4_FORM_UP = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_14} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.FORM_UP})'
    WEP_KEYBLADE13_WEAPON_ENHANCE_9_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_14} {WEAPON_ENHANCE} 9 ({ETresAbilityKind.FORM_TIME})'

    # In code as 18?
    WEP_KEYBLADE17_WEAPON_ENHANCE_4_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_18} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.FORM_TIME})'

    # In code as 17?
    WEP_KEYBLADE18_WEAPON_ENHANCE_4_FORM_TIME = f'{ETresItemDefWeapon.WEP_KEYBLADE_SO_19} {WEAPON_ENHANCE} 4 ({ETresAbilityKind.FORM_TIME})'

    @classmethod
    def generate_locations(cls):
        locations = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue
            
            locations.append(LocationData(value, key, TresWorldData.ANY, '', cls.WEAPON_ENHANCE))

        return locations

# Variables
tres_chr_init_data_locations =  TresChrInitDataLocation.generate_locations()
tres_equip_item_data_locations = TresEquipItemDataLocation.generate_locations()
tres_event_data_locations = TresEventDataLocation.generate_locations()
tres_fullcourse_ability_data_locations = TresFullcourseAbilityDataLocation.generate_locations()
tres_synthesis_data_locations = TresSynthesisDataLocation.generate_locations()
tres_level_up_data_locations = TresLevelUpDataLocation.generate_locations()
tres_lucky_mark_data_locations = TresLuckyMarkDataLocation.generate_locations()
tres_treasure_data_locations = TresTreasureDataLocation.generate_locations()
tres_victory_bonus_data_locations = TresVictoryBonusDataLocation.generate_locations()
tres_weapon_enhance_data_locations = TresWeaponEnhanceDataLocation.generate_locations()

all_kh3_locations = (
    tres_chr_init_data_locations +
    tres_equip_item_data_locations +
    tres_event_data_locations +
    tres_fullcourse_ability_data_locations +
    tres_synthesis_data_locations +
    tres_level_up_data_locations +
    tres_lucky_mark_data_locations +
    tres_treasure_data_locations +
    tres_victory_bonus_data_locations +
    tres_weapon_enhance_data_locations
)

# Mapping: group_name -> { all_location_names_in_group }
kh3_location_name_groups = {
    f'{location.world_name} {location.area_name}'.strip(): location.loc_name for location in all_kh3_locations
}