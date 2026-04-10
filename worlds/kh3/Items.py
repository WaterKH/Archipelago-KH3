import typing

from BaseClasses import Item, ItemClassification

from worlds.kh3.Constants import KINGDOM_HEARTS_III

class ItemData(typing.NamedTuple):
    item_name: str
    kh3_id: str
    classification: ItemClassification
    prefix: str

    @property
    def full_id(self):
        return f"{self.prefix}{self.item_name}"

class KingdomHeartsIIIItem(Item):
    game: str = KINGDOM_HEARTS_III


class ETresItemDefAccessory(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefAccessory:'

    ACC_ITEM01 = 'Laughter Pin'
    ACC_ITEM02 = 'Forest Clasp'

    ACC_ITEM03 = 'Ability Ring'
    ACC_ITEM04 = 'Ability Ring+'
    ACC_ITEM05 = 'Technician\'s Ring'
    ACC_ITEM06 = 'Technician\'s Ring+'
    ACC_ITEM07 = 'Skill Ring'
    ACC_ITEM08 = 'Skill Ring+'
    ACC_ITEM09 = 'Expert\'s Ring'
    ACC_ITEM10 = 'Master\'s Ring'
    ACC_ITEM11 = 'Cosmic Ring'
    ACC_ITEM12 = 'Power Ring'
    ACC_ITEM13 = 'Buster Ring'
    ACC_ITEM14 = 'Valor Ring'
    ACC_ITEM15 = 'Phantom Ring'
    ACC_ITEM16 = 'Orichalcum Ring'
    ACC_ITEM17 = 'Magic Ring'
    ACC_ITEM18 = 'Rune Ring'
    ACC_ITEM19 = 'Force Ring'
    ACC_ITEM20 = 'Sorcerer\'s Ring'
    ACC_ITEM21 = 'Wisdom Ring'

    ACC_ITEM22 = 'Bronze Necklace' # NOT USED [Grand Necklace 01 Ability: "Draw" "MP Haste"]
    ACC_ITEM23 = 'Silver Necklace' # NOT USED [Supreme Necklace 01 Ability: "Fire Up" and "MP Haste"]
    ACC_ITEM24 = 'Gold Necklace' # NOT USED [Master Necklace 01 Ability: "Thunder Up" and "MP Haste"]
    
    ACC_ITEM25 = 'Bronze Amulet'
    ACC_ITEM26 = 'Silver Amulet'
    ACC_ITEM27 = 'Gold Amulet'

    ACC_ITEM28 = 'Junior Medal (Treasure Magnet)' # Chance B-Rank Verum Rex
    ACC_ITEM29 = 'Master Medal (Fire Boost)' # Chance A-Rank Verum Rex
    ACC_ITEM30 = 'Star Medal (Thunder Boost)' # Chance A-Rank Flash Tracer (Fred)
    
    ACC_ITEM31 = 'Mickey Clasp'
    ACC_ITEM32 = 'Soldier\'s Earring'
    ACC_ITEM33 = 'Fencer\'s Earring'
    ACC_ITEM34 = 'Mage\'s Earring'
    ACC_ITEM35 = 'Slayer\'s Earring'

    ACC_ITEM36 = 'Moon Amulet'
    ACC_ITEM37 = 'Star Charm'
    ACC_ITEM38 = 'Cosmic Arts'
    ACC_ITEM39 = 'Crystal Regalia'

    ACC_ITEM40 = 'Water Cufflink'
    ACC_ITEM41 = 'Thunder Cufflink'
    ACC_ITEM42 = 'Fire Cufflink'
    ACC_ITEM43 = 'Aero Cufflink'
    ACC_ITEM44 = 'Blizzard Cufflink'
    ACC_ITEM45 = 'Celestriad'
    ACC_ITEM46 = 'Yin-Yang Cufflink'

    ACC_ITEM47 = 'Gourmand\'s Ring'
    ACC_ITEM48 = 'Draw Ring'
    ACC_ITEM49 = 'Lucky Ring'
    ACC_ITEM50 = 'Flanniversary Badge'

    # ACC_ITEM51 = '' # NOT USED [Grand Necklace 02 Ability: "Defender" and "MP Haste"]
    # ACC_ITEM52 = '' # NOT USED [Grand Necklace 03 Ability: "MP Leve" and "MP Haste"]
    # ACC_ITEM53 = '' # NOT USED [Grand Necklace 04 Ability: "Full MP Burst" and "MP Haste"]
    # ACC_ITEM54 = '' # NOT USED [Grand Necklace 05 Ability: "Rack Up" and "MP Haste"]
    # ACC_ITEM55 = '' # NOT USED [Grand Necklace 06 Ability: "HP Converter" and "MP Haste"]
    # ACC_ITEM56 = '' # NOT USED [Grand Necklace 07 Ability: MP Converter, MP Haste]
    # ACC_ITEM57 = '' # NOT USED [Grand Necklace 08 Ability: "Money Converter" and "MP Haste"]
    # ACC_ITEM58 = '' # NOT USED [Grand Necklace 09 Ability: Burn Guard, MP Haste]
    # ACC_ITEM59 = '' # NOT USED [Grand Necklace 10 Ability: Cloud Guard, MP Haste]
    # ACC_ITEM60 = '' # NOT USED [Grand Necklace 11 Ability: "Sneeze Guard" and "MP Haste"]
    # ACC_ITEM61 = '' # NOT USED [Grand Necklace 12 Ability: Freeze Guard, MP Haste]
    # ACC_ITEM62 = '' # NOT USED [Grand Necklace 13 Ability: "Eleki Guard" and "MP Haste"]

    # ACC_ITEM63 = '' # NOT USED [Supreme Necklace 02 Ability: Blizzard Up, MP Haste]
    # ACC_ITEM64 = '' # NOT USED [Supreme Necklace 03 Ability: "Water Up" and "MP Haste"]
    # ACC_ITEM65 = '' # NOT USED [Supreme Necklace 04 Ability: Magic Draw, MP Haste]
    # ACC_ITEM66 = '' # NOT USED [Supreme Necklace 05 Ability: Last Leave, MP Haste]
    # ACC_ITEM67 = '' # NOT USED [Supreme Necklace 06 Ability: "Stun Guard" and "MP Haste"]
    # ACC_ITEM68 = '' # NOT USED [Supreme Necklace 07 Ability: "Item Up" and "MP Haste"]
    # ACC_ITEM69 = '' # NOT USED [Supreme Necklace 08 Ability: "Fire Aspir" and "MP Haste"]
    # ACC_ITEM70 = '' # NOT USED [Supreme Necklace 09 Ability: Blizzard Spill, MP Haste]
    # ACC_ITEM71 = '' # NOT USED [Supreme Necklace 10 Ability: Thunder Aspir, MP Haste]
    # ACC_ITEM72 = '' # NOT USED [Supreme Necklace 11 Ability: "Water Spill" and "MP Haste"]
    # ACC_ITEM73 = '' # NOT USED [Supreme Necklace 12 Ability: Aero Aspir, MP Haste]

    # ACC_ITEM74 = '' # NOT USED [Master Necklace 02 Ability: Aero Up, MP Haste]
    # ACC_ITEM75 = '' # NOT USED [Master Necklace 03 Ability: Wizard Star, MP Haste]
    # ACC_ITEM76 = '' # NOT USED [Master Necklace 04 Ability: "Combo Leave" and "MP Haste"]
    # ACC_ITEM77 = '' # NOT USED [Master Necklace 05 Ability: Damage Aspiration, MP Haste]
    # ACC_ITEM78 = '' # NOT USED [Master Necklace 06 Ability: "MP Save" "MP Haste"]
    # ACC_ITEM79 = '' # NOT USED [Master Necklace 07 Ability: "Charge Berserk" and "MP Haste"]
    # ACC_ITEM80 = '' # NOT USED [Master Necklace 08 Ability: "Dark Aspir" and "MP Haste"]

    ACC_ITEM81 = 'Master Medal (Defender)' # Chance A-Rank Verum Rex [Senior Medal 03 Ability "Defender"]
    ACC_ITEM82 = 'Master Medal (Extra Cast)' # Chance A-Rank Festival Dance [Senior Medal 04 Ability "MP Leve"]

    ACC_ITEM83 = 'Junior Medal (Full MP Blast)' # Chance B-Rank Frozen Slider [Junior Medal 02 Ability "Full MP Burst"]
    
    ACC_ITEM84 = 'Master Medal (Lucky Strike)' # Chance A-Rank Verum Rex [Senior Medal 05 Ability "Luck Up"]

    # ACC_ITEM85 = '' # NOT USED [Junior Medal 03 Ability "HP Converter"]
    # ACC_ITEM86 = '' # NOT USED [Junior Medal 04 Ability "MP Converter"]
    # ACC_ITEM87 = '' # NOT USED [Junior Medal 05 Ability "Money Converter"]
    ACC_ITEM88 = 'Junior Medal (Burn Protection)' # Chance B-Rank Verum Rex [Junior Medal 06 Ability "Burn Guard"]
    ACC_ITEM89 = 'Junior Medal (Cloud Protection)' # Chance B-Rank Verum Rex [Junior Medal 07 Ability "Cloud Guard"]
    ACC_ITEM90 = 'Junior Medal (Sneeze Protection)' # Chance B-Rank Festival Dance [Junior Medal 08 Ability "Sneeze Guard"]
    ACC_ITEM91 = 'Junior Medal (Freeze Protection)' # Chance B-Rank Frozen Slider [Junior Medal 09 Ability "Freeze Guard"]
    ACC_ITEM92 = 'Junior Medal (Electric Protection)' # Chance B-Rank Festival Dance [Junior Medal 10 Ability "Eleki Guard"]

    ACC_ITEM93 = 'Star Medal (Blizzard Boost)' # Chance A-Rank Frozen Slider [Master Medal 02 Ability "Blizzard Up"]

    ACC_ITEM94 = 'Master Medal (Water Boost)' # Chance A-Rank Festival Dance [Senior Medal 02 Ability "Water Up"]
    ACC_ITEM95 = 'Master Medal (Magic Treasure Magnet)' # Chance A-Rank Festival Dance [Senior Medal 06 Ability "Magic Draw"]

    ACC_ITEM96 = 'Star Medal (Second Chance)' # Chance A-Rank Flash Tracer (Fred) [Master Medal 04 Ability "Last Leave"]
    
    ACC_ITEM97 = 'Master Medal (Stun Protection)' # Chance B-Rank Flash Tracer (Fred) [Senior Medal 07 Ability "Stun Guard"]
    
    ACC_ITEM98 = 'Star Medal (Item Boost)' # Chance A-Rank Flash Tracer (Gogo) [Master Medal 05 Ability "Item Up"]

    ACC_ITEM99 = 'Master Medal (Fire Syphon)' # Chance B-Rank Flash Tracer (Gogo) [Senior Medal 08 Ability "Fire Aspill"]
    ACC_ITEM100 = 'Master Medal (Blizzard Syphon)' # Chance B-Rank Frozen Slider [Senior Medal 09 Ability "Blizzard Spill"]
    ACC_ITEM101 = 'Master Medal (Thunder Syphon)' # Chance B-Rank Flash Tracer (Fred) [Senior Medal 10 Ability: "Thunder Aspir"]
    ACC_ITEM102 = 'Master Medal (Water Syphon)' # Chance B-Rank Festival Dance [Senior Medal 11 Ability: "Water Aspill"]
    ACC_ITEM103 = 'Master Medal (Aero Syphon)' # Chance B-Rank Flash Tracer (Gogo) [Senior Medal 12 Ability: Aero Aspir]

    ACC_ITEM104 = 'Star Medal (Aero Boost)' # Chance A-Rank Flash Tracer (Gogo) [Master Medal 03 Ability "Aero Up"]
    ACC_ITEM105 = 'Star Medal (Wizard\'s Ruse)' # Chance A-Rank Frozen Slider [Master Medal 06 Ability "Wizard Star"]
    ACC_ITEM106 = 'Star Medal (Withstand Combo)' # Chance A-Rank Frozen Slider [Master Medal 07 Ability "Combo Leave"]
    ACC_ITEM107 = 'Star Medal (Damage Syphon)' # Chance A-Rank Flash Tracer (Fred) [Master Medal 10 Ability "Damage Aspiration"]
    # ACC_ITEM108 = '' # NOT USED [Master Medal 08 Ability "MP Save"]
    # ACC_ITEM109 = '' # NOT USED [Master Medal 09 Ability "Charge Berserk"]
    ACC_ITEM110 = 'Star Medal (Dark Syphon)' # Chance A-Rank Flash Tracer (Gogo) [Master Medal 11 Ability "Dark Aspir"]

    ACC_ITEM111 = 'Breakthrough'
    ACC_ITEM112 = 'Crystal Regalia+'

    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("ACC_ITEM"):
                items.append(ItemData(value, key, ItemClassification.filler, cls.PREFIX))
        return items
    
class ETresItemDefBattleItem(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefBattleItem:'

    ITEM_POTION = 'Potion'
    ITEM_HIGHPOTION = 'Hi-Potion'
    ITEM_MEGAPOTION = 'Mega-Potion'
    
    ITEM_ETHER = 'Ether'
    ITEM_HIGHETHER = 'Hi-Ether'
    ITEM_MEGAETHER = 'Mega-Ether'
    
    ITEM_ELIXIR = 'Elixir'
    ITEM_LASTELIXIR = 'Megalixir'
    
    ITEM_FOCUSSUPPLY = 'Refocuser'
    ITEM_HIGHFOCUSSUPPLY = 'Hi-Refocuser'
    
    ITEM_ALLCURE = 'Panacea'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("ITEM"):
                items.append(ItemData(value, key, ItemClassification.filler, cls.PREFIX))
        return items
    
class ETresItemDefCampItem(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefCampItem:'

    ITEM_TENT = 'Tent'
    
    ITEM_POWERUP = 'Strength Boost'
    ITEM_MAGICUP = 'Magic Boost'
    ITEM_GUARDUP = 'Defense Boost'
    ITEM_APUP = 'AP Boost'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("ITEM"):
                items.append(ItemData(value, key, ItemClassification.useful, cls.PREFIX))
        return items
    
class ETresItemDefFood(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefFood:'

    FOOD_ITEM01 = 'Pumpkin Velouté'
    FOOD_ITEM02 = 'Consommé'
    FOOD_ITEM03 = 'Carrot Potage'
    FOOD_ITEM04 = 'Crab Bisque'
    FOOD_ITEM05 = 'Cold Tomato Soup'

    FOOD_ITEM06 = 'Scallop Poêlé'
    FOOD_ITEM07 = 'Lobster Mousse'
    FOOD_ITEM08 = 'Mushroom Terrine'
    FOOD_ITEM09 = 'Ratatouille'
    FOOD_ITEM10 = 'Caprese Salad'

    FOOD_ITEM11 = 'Sole Meunière'
    FOOD_ITEM12 = 'Eel Matelote'
    FOOD_ITEM13 = 'Sea Bass en Papillote'
    FOOD_ITEM14 = 'Bouillabaisse'
    FOOD_ITEM15 = 'Seafood Tartare'
    FOOD_ITEM16 = 'Sea Bass Poêlé'

    FOOD_ITEM17 = 'Sweetbread Poêlé'
    FOOD_ITEM18 = 'Beef Sauté'
    FOOD_ITEM19 = 'Beef Bourguignon'
    FOOD_ITEM20 = 'Stuffed Quail'
    FOOD_ITEM21 = 'Filet Mignon Poêlé'

    FOOD_ITEM22 = 'Crêpes Suzette'
    FOOD_ITEM23 = 'Chocolate Mousse'
    FOOD_ITEM24 = 'Fresh Fruit Compote'
    FOOD_ITEM25 = 'Berries au Fromage'
    FOOD_ITEM26 = 'Warm Banana Soufflé'
    FOOD_ITEM27 = 'Fruit Gelée'
    FOOD_ITEM28 = 'Tarte aux Fruits'

    FOOD_ITEM29 = 'Pumpkin Velouté+'
    FOOD_ITEM30 = 'Consommé+'
    FOOD_ITEM31 = 'Carrot Potage+'
    FOOD_ITEM32 = 'Crab Bisque+'
    FOOD_ITEM33 = 'Cold Tomato Soup+'

    FOOD_ITEM34 = 'Scallop Poêlé+'
    FOOD_ITEM35 = 'Lobster Mousse+'
    FOOD_ITEM36 = 'Mushroom Terrine+'
    FOOD_ITEM37 = 'Ratatouille+'
    FOOD_ITEM38 = 'Caprese Salad+'

    FOOD_ITEM39 = 'Sole Meunière+'
    FOOD_ITEM40 = 'Eel Matelote+'
    FOOD_ITEM41 = 'Sea Bass en Papillote+'
    FOOD_ITEM42 = 'Bouillabaisse+'
    FOOD_ITEM43 = 'Seafood Tartare+'
    FOOD_ITEM44 = 'Sea Bass Poêlé+'

    FOOD_ITEM45 = 'Sweetbread Poêlé+'
    FOOD_ITEM46 = 'Beef Sauté+'
    FOOD_ITEM47 = 'Beef Bourguignon+'
    FOOD_ITEM48 = 'Stuffed Quail+'
    FOOD_ITEM49 = 'Filet Mignon Poêlé+'

    FOOD_ITEM50 = 'Crêpes Suzette+'
    FOOD_ITEM51 = 'Chocolate Mousse+'
    FOOD_ITEM52 = 'Fresh Fruit Compote+'
    FOOD_ITEM53 = 'Berries au Fromage+'
    FOOD_ITEM54 = 'Warm Banana Soufflé+'
    FOOD_ITEM55 = 'Fruit Gelée+'
    FOOD_ITEM56 = 'Tarte aux Fruits+'

    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("FOOD_ITEM"):
                items.append(ItemData(value, key, ItemClassification.filler, cls.PREFIX))
        return items

class ETresItemDefFoodstuff(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefFoodstuff:'

    FST_ITEM01 = 'Crab'
    FST_ITEM02 = 'Scallop'
    FST_ITEM03 = 'Lobster'
    FST_ITEM04 = 'Sole'
    FST_ITEM05 = 'Eel'
    FST_ITEM06 = 'Sea Bass'
    FST_ITEM07 = 'Mussel'
    FST_ITEM08 = 'Cod'

    FST_ITEM09 = 'Pumpkin'
    FST_ITEM10 = 'Zucchini'
    FST_ITEM11 = 'Onion'
    FST_ITEM12 = 'Tomato'
    FST_ITEM13 = 'Eggplant'
    FST_ITEM14 = 'Carrot'
    FST_ITEM15 = 'Garlic'
    FST_ITEM16 = 'Celery'

    FST_ITEM17 = 'Morel'
    FST_ITEM18 = 'Porcini'
    FST_ITEM19 = 'Chanterelle'
    FST_ITEM20 = 'Portobello'
    FST_ITEM21 = 'Black Truffle'
    FST_ITEM22 = 'King Oyster Mushroom'
    FST_ITEM23 = 'Black Trumpet'
    FST_ITEM24 = 'Miller Mushroom'

    FST_ITEM25 = 'Cloves'
    FST_ITEM26 = 'Rosemary'
    FST_ITEM27 = 'Thyme'
    FST_ITEM28 = 'Bay Leaf'
    FST_ITEM29 = 'Basil'
    FST_ITEM30 = 'Dill'
    FST_ITEM31 = 'Parsley'
    FST_ITEM32 = 'Saffron'

    FST_ITEM33 = 'Apricot'
    FST_ITEM34 = 'Gooseberry'
    FST_ITEM35 = 'Lemon'
    FST_ITEM36 = 'Orange'
    FST_ITEM37 = 'Raspberry'
    FST_ITEM38 = 'Pear'
    FST_ITEM39 = 'Blackberry'
    FST_ITEM40 = 'Apple'

    FST_ITEM41 = 'Cheese'
    FST_ITEM42 = 'Chocolate'
    FST_ITEM43 = 'Caviar'
    FST_ITEM44 = 'Butter'
    FST_ITEM45 = 'Olive Oil'
    FST_ITEM46 = 'Cornichon'
    FST_ITEM47 = 'Rice'
    FST_ITEM48 = 'Honey'

    FST_ITEM49 = 'Sour Cherry'
    FST_ITEM50 = 'Strawberry'
    FST_ITEM51 = 'Blood Orange'
    FST_ITEM52 = 'Banana'
    FST_ITEM53 = 'Grapes'
    FST_ITEM54 = 'Melon'
    FST_ITEM55 = 'Watermelon'

    FST_ITEM56 = 'Veal'
    FST_ITEM57 = 'Beef'
    FST_ITEM58 = 'Quail'
    FST_ITEM59 = 'Filet Mignon'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("FST_ITEM"):
                items.append(ItemData(value, key, ItemClassification.filler, cls.PREFIX))
        return items
    
class ETresItemDefKeyItem(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefKeyItem:'

    KEY_ITEM01 = '' # NOT USED
    KEY_ITEM02 = 'Gummiphone'
    KEY_ITEM03 = 'AR Device'
    KEY_ITEM04 = 'Prize Postcard'
    KEY_ITEM05 = 'M.O.G. Card'
    KEY_ITEM06 = 'Dream Heartbinder'
    KEY_ITEM07 = 'Pixel Heartbinder'
    KEY_ITEM08 = '\'Ohana Heartbinder'
    KEY_ITEM09 = 'Pride Heartbinder'
    KEY_ITEM10 = 'Ocean Heartbinder'
    KEY_ITEM11 = 'Golden Herc Figure'
    KEY_ITEM12 = 'Proof of Promises'
    KEY_ITEM13 = 'Proof of Times Past'
    KEY_ITEM14 = 'Proof of Fantasies' # Modded in
    KEY_ITEM15 = 'Kairi\'s Heart Piece' # Modded in
    
    # TODO: Add in item names for these
    KEY_ITEM16 = 'Golden Phil Statue' # Modded in - Olympus Unlock Condition
    KEY_ITEM17 = 'Familiar Skateboard' # Modded in - Twilight Town Unlock Condition
    KEY_ITEM18 = 'Dissidia Collector\'s Set' # Modded in - Toy Box Unlock Condition
    KEY_ITEM19 = 'Maximus\'s Crisp Apple' # Modded in - Kingdom of Corona Unlock Condition
    KEY_ITEM20 = 'Pooh\'s Hunny Pot' # Modded in - 100 Acre Woord Unlock Condition
    KEY_ITEM21 = 'Boo\'s Monster Outfit' # Modded in - Monstropolis Unlock Condition
    KEY_ITEM22 = 'Magical Crystalline Snowflake' # Modded in - Arendelle Unlock Condition
    KEY_ITEM23 = 'Weathered Pirate Flag' # Modded in - Caribbean Unlock Condition
    KEY_ITEM24 = '' # Modded in - San Fransokyo Unlock Condition
    KEY_ITEM25 = '' # Modded in - Data Garden of Assemblage Unlock Condition
    KEY_ITEM26 = '' # Modded in - Scala ad Caelum Unlock Condition
    KEY_ITEM27 = 'Ephemer\'s Scarf' # Modded in - Keyblade Graveyard Unlock Condition
    KEY_ITEM27 = 'Guardians of Light Memories' # Modded in - Re:Mind Unlock Condition

    KEY_ITEM28 = 'End Screen Win Condition'

    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("KEY_ITEM"):
                items.append(ItemData(value, key, ItemClassification.progression, cls.PREFIX))
        return items

class ETresItemDefLSIGameItem(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefLSIGameItem:'

    LSIGAME01 = 'Giantland'
    LSIGAME02 = 'Mickey, the Mail Pilot'
    LSIGAME03 = 'The Musical Farmer'
    LSIGAME04 = 'Building a Building'
    LSIGAME05 = 'The Mad Doctor'
    LSIGAME06 = 'Mickey\'s Kitten Catch'
    LSIGAME07 = 'The Klondike Kid' # Mickey's Gold Rush?
    LSIGAME08 = 'Fishin\' Frenzy'
    LSIGAME09 = 'The Karnival Kid'
    LSIGAME10 = 'Mickey Cuts Up'
    LSIGAME11 = 'Mickey\'s Prison Escape'
    LSIGAME12 = 'How to Play Baseball'
    LSIGAME13 = 'How to Play Golf'
    LSIGAME14 = 'Mickey\'s Circus'
    LSIGAME15 = 'Camping Out'
    LSIGAME16 = 'Taxi Troubles'
    LSIGAME17 = 'Beach Party'
    LSIGAME18 = 'The Wayward Canary'
    LSIGAME19 = 'Mickey\'s Mechanical Man'
    LSIGAME20 = 'The Barnyard Battle'
    LSIGAME21 = 'Cast Out to Sea'
    LSIGAME22 = 'Barnyard Sports'
    LSIGAME23 = 'Mickey Steps Out'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("LSIGAME"):
                items.append(ItemData(value, key, ItemClassification.filler, cls.PREFIX))
        return items
    
class ETresItemDefMaterial(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefMaterial:'

    MAT_ITEM01 = 'Blazing Shard'
    MAT_ITEM02 = 'Blazing Stone'
    MAT_ITEM03 = 'Blazing Gem'
    MAT_ITEM04 = 'Blazing Crystal'
    MAT_ITEM05 = 'Frost Shard'
    MAT_ITEM06 = 'Frost Stone'
    MAT_ITEM07 = 'Frost Gem'
    MAT_ITEM08 = 'Frost Crystal'
    MAT_ITEM09 = 'Lightning Shard'
    MAT_ITEM10 = 'Lightning Stone'
    MAT_ITEM11 = 'Lightning Gem'
    MAT_ITEM12 = 'Lightning Crystal'
    MAT_ITEM13 = 'Lucid Shard'
    MAT_ITEM14 = 'Lucid Stone'
    MAT_ITEM15 = 'Lucid Gem'
    MAT_ITEM16 = 'Lucid Crystal'
    MAT_ITEM17 = 'Pulsing Shard'
    MAT_ITEM18 = 'Pulsing Stone'
    MAT_ITEM19 = 'Pulsing Gem'
    MAT_ITEM20 = 'Pulsing Crystal'
    MAT_ITEM21 = 'Writhing Shard'
    MAT_ITEM22 = 'Writhing Stone'
    MAT_ITEM23 = 'Writhing Gem'
    MAT_ITEM24 = 'Writhing Crystal'
    MAT_ITEM25 = 'Betwixt Shard'
    MAT_ITEM26 = 'Betwixt Stone'
    MAT_ITEM27 = 'Betwixt Gem'
    MAT_ITEM28 = 'Betwixt Crystal'
    MAT_ITEM29 = 'Twilight Shard'
    MAT_ITEM30 = 'Twilight Stone'
    MAT_ITEM31 = 'Twilight Gem'
    MAT_ITEM32 = 'Twilight Crystal'
    MAT_ITEM33 = 'Mythril Shard'
    MAT_ITEM34 = 'Mythril Stone'
    MAT_ITEM35 = 'Mythril Gem'
    MAT_ITEM36 = 'Mythril Crystal'
    MAT_ITEM37 = 'Sinister Shard'
    MAT_ITEM38 = 'Sinister Stone'
    MAT_ITEM39 = 'Sinister Gem'
    MAT_ITEM40 = 'Sinister Crystal'
    MAT_ITEM41 = 'Soothing Shard'
    MAT_ITEM42 = 'Soothing Stone'
    MAT_ITEM43 = 'Soothing Gem'
    MAT_ITEM44 = 'Soothing Crystal'
    MAT_ITEM45 = 'Wellspring Shard'
    MAT_ITEM46 = 'Wellspring Stone'
    MAT_ITEM47 = 'Wellspring Gem'
    MAT_ITEM48 = 'Wellspring Crystal'
    MAT_ITEM49 = 'Hungry Shard'
    MAT_ITEM50 = 'Hungry Stone'
    MAT_ITEM51 = 'Hungry Gem'
    MAT_ITEM52 = 'Hungry Crystal'
    MAT_ITEM53 = 'Fluorite'
    MAT_ITEM54 = 'Damascus'
    MAT_ITEM55 = 'Adamantite'
    MAT_ITEM56 = 'Orichalcum'
    MAT_ITEM57 = 'Orichalcum+'
    MAT_ITEM58 = 'Electrum'
    MAT_ITEM59 = 'Evanescent Crystal'
    MAT_ITEM60 = 'Illusory Crystal'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("MAT_ITEM"):
                items.append(ItemData(value, key, ItemClassification.filler, cls.PREFIX))
        return items
    
class ETresItemDefMognetItem(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefMognetItem:'

    ITEM_MOGNETMEDAL = 'Kupo Coin'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("ITEM"):
                items.append(ItemData(value, key, ItemClassification.useful, cls.PREFIX))
        return items
    
class ETresItemDefNavimap(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefNavimap:'

    NAVI_MAP_MI01 = 'Map: Monsters, Inc.'
    NAVI_MAP_MI02 = 'Map: The Factory'

    NAVI_MAP_TS01 = 'Map: Andy\'s House'
    NAVI_MAP_TS02 = 'Map: Galaxy Toys'

    NAVI_MAP_FZ01 = 'Map: The North Mountain'
    NAVI_MAP_FZ02 = 'Map: The Labyrinth of Ice'

    NAVI_MAP_RA01 = 'Map: The Forest (1/2)'
    NAVI_MAP_RA02 = 'Map: The Forest (2/2)'

    NAVI_MAP_CA01 = 'Map: Port Royal Waters'
    NAVI_MAP_CA02 = 'Map: Huddled Isles'
    NAVI_MAP_CA03 = 'Map: Ship\'s End'
    NAVI_MAP_CA04 = 'Map: Isla de los Mástiles'

    NAVI_MAP_HE01 = 'Map: Mount Olympus'
    NAVI_MAP_HE02 = 'Map: Thebes'
    NAVI_MAP_HE03 = 'Map: Realm of the Gods'

    NAVI_MAP_BX01 = 'Map: The City'

    NAVI_MAP_TT01 = 'Map: The Neighborhood'

    NAVI_MAP_KG01 = 'Map: The Badlands'
    NAVI_MAP_KG02 = 'Map: The Skein of Severance'

    NAVI_MAP_BT01 = 'Map: The Stairway to the Sky'
    NAVI_MAP_BT02 = 'Map: Breezy Quarter'

    NAVI_MAP_CA05 = 'Map: Sandbar Isle'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("NAVI_MAP"):
                items.append(ItemData(value, key, ItemClassification.filler, cls.PREFIX))
        return items
    
class ETresItemDefProtector(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefProtector:'

    PRT_ITEM01 = 'Hero\'s Belt'
    PRT_ITEM02 = 'Hero\'s Glove'

    PRT_ITEM03 = 'Shield Belt'
    PRT_ITEM04 = 'Defense Belt'
    PRT_ITEM05 = 'Guardian\'s Belt'
    
    PRT_ITEM06 = 'Power Band'
    PRT_ITEM07 = 'Buster Band'
    PRT_ITEM08 = 'Buster Band+'

    PRT_ITEM09 = 'Cosmic Belt'
    PRT_ITEM10 = 'Cosmic Belt+'
    
    PRT_ITEM11 = 'Fire Bangle'
    PRT_ITEM12 = 'Firaga Bangle'
    PRT_ITEM13 = 'Firaza Bangle'
    PRT_ITEM14 = 'Fire Chain'

    PRT_ITEM15 = 'Blizzard Choker'
    PRT_ITEM16 = 'Blizzara Choker'
    PRT_ITEM17 = 'Blizzaga Choker'
    PRT_ITEM18 = 'Blizzard Chain'

    PRT_ITEM19 = 'Thunder Trinket'
    PRT_ITEM20 = 'Thundara Trinket'
    PRT_ITEM21 = 'Thundaza Trinket'
    PRT_ITEM22 = 'Thunder Chain'

    PRT_ITEM23 = 'Dark Anklet'
    PRT_ITEM24 = 'Midnight Anklet'
    PRT_ITEM25 = 'Chaos Anklet'
    PRT_ITEM26 = 'Dark Chain'

    PRT_ITEM27 = 'Divine Bandana'
    PRT_ITEM28 = 'Elven Bandana'

    PRT_ITEM29 = 'Aqua Chaplet'
    PRT_ITEM30 = 'Wind Fan'
    PRT_ITEM31 = 'Storm Fan'

    PRT_ITEM32 = 'Aero Armlet'
    PRT_ITEM33 = 'Aegis Chain'
    PRT_ITEM34 = 'Acrisius'
    PRT_ITEM35 = 'Cosmic Chain'

    PRT_ITEM36 = 'Petite Ribbon'
    PRT_ITEM37 = 'Ribbon'

    PRT_ITEM38 = 'Fira Bangle'
    PRT_ITEM39 = 'Blizzaza Choker'
    PRT_ITEM40 = 'Thundara Trinket'
    PRT_ITEM41 = 'Shadow Anklet'

    PRT_ITEM42 = 'Abas Chain'
    PRT_ITEM43 = 'Acrisius+'
    PRT_ITEM44 = 'Royal Ribbon'

    PRT_ITEM45 = 'Firefighter Rosette'
    PRT_ITEM46 = 'Umbrella Rosette'
    PRT_ITEM47 = 'Mask Rosette'
    PRT_ITEM48 = 'Snowman Rosette'
    PRT_ITEM49 = 'Insulator Rosette'

    PRT_ITEM50 = 'Power Weight'
    PRT_ITEM51 = 'Magic Weight'
    PRT_ITEM52 = 'Master Belt'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("PRT_ITEM"):
                items.append(ItemData(value, key, ItemClassification.useful, cls.PREFIX))
        return items
    
class ETresItemDefReport(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefReport:'

    REPORT_ITEM01 = 'Secret Report 1'
    REPORT_ITEM02 = 'Secret Report 2'
    REPORT_ITEM03 = 'Secret Report 3'
    REPORT_ITEM04 = 'Secret Report 4'
    REPORT_ITEM05 = 'Secret Report 5'
    REPORT_ITEM06 = 'Secret Report 6'
    REPORT_ITEM07 = 'Secret Report 7'
    REPORT_ITEM08 = 'Secret Report 8'
    REPORT_ITEM09 = 'Secret Report 9'
    REPORT_ITEM10 = 'Secret Report 10'
    REPORT_ITEM11 = 'Secret Report 11'
    REPORT_ITEM12 = 'Secret Report 12'
    REPORT_ITEM13 = 'Secret Report 13'
    REPORT_ITEM14 = 'Secret Report 14'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("REPORT_ITEM"):
                items.append(ItemData(value, key, ItemClassification.useful, cls.PREFIX))
        return items
    
class ETresItemDefWeapon(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresItemDefWeapon:'

    WEP_NOEQUIP = 'No Keyblade'
    WEP_KEYBLADE_SO_00 = 'Kingdom Key'
    WEP_KEYBLADE_SO_01 = 'Hero\'s Origin'
    WEP_KEYBLADE_SO_02 = 'Shooting Star'
    WEP_KEYBLADE_SO_03 = 'Favorite Deputy'
    WEP_KEYBLADE_SO_04 = 'Ever After'
    WEP_KEYBLADE_SO_05 = 'Happy Gear'
    WEP_KEYBLADE_SO_06 = 'Crystal Snow'
    WEP_KEYBLADE_SO_07 = 'Hunny Spout'
    WEP_KEYBLADE_SO_08 = 'Nano Gear'
    WEP_KEYBLADE_SO_09 = 'Wheel of Fate'
    WEP_KEYBLADE_SO_11 = 'Grand Chef'
    WEP_KEYBLADE_SO_12 = 'Classic Tone'
    WEP_KEYBLADE_SO_13 = 'Oathkeeper'
    WEP_KEYBLADE_SO_14 = 'Oblivion'
    WEP_KEYBLADE_SO_15 = 'Ultima Weapon'
    # WEP_KEYBLADE_SO_16 = 'Midnight Blue' # PS Exclusive Keyblade [UNUSED]
    # WEP_KEYBLADE_SO_17 = 'Phantom Green' # XBox Exclusive Keyblade [UNUSED]
    WEP_KEYBLADE_SO_18 = 'Starlight'
    WEP_KEYBLADE_SO_19 = 'Elemental Encoder' # PC Exclusive Keyblade (EGS) [UNUSED IF STEAM]
    WEP_KEYBLADE_SO_20 = 'Dead of Night' # PC Exclusive Keyblade (Steam) [UNUSED IF EGS]
    
    WEP_DONALD_00 = 'Mage\'s Staff'
    WEP_DONALD_01 = 'Mage\'s Staff+'
    WEP_DONALD_02 = 'Warhammer'
    WEP_DONALD_03 = 'Warhammer+'
    WEP_DONALD_04 = 'Magician\'s Wand'
    WEP_DONALD_05 = 'Magician\'s Wand+'
    WEP_DONALD_06 = 'Nirvana'
    WEP_DONALD_07 = 'Nirvana+'
    WEP_DONALD_08 = 'Astrolabe'
    WEP_DONALD_09 = 'Astrolabe+'
    # WEP_DONALD_10 = '' # [UNUSED]
    WEP_DONALD_11 = 'Heartless Maul'
    WEP_DONALD_12 = 'Heartless Maul+'
    WEP_DONALD_13 = 'Save the Queen'
    WEP_DONALD_14 = 'Save the Queen+'
    # WEP_DONALD_15 = '' # [UNUSED]
    # WEP_DONALD_16 = '' # [UNUSED]
    # WEP_DONALD_17 = '' # [UNUSED]
    # WEP_DONALD_18 = '' # [UNUSED]
    # WEP_DONALD_19 = '' # [UNUSED]
    
    WEP_GOOFY_00 = 'Knight\'s Shield'
    WEP_GOOFY_01 = 'Knight\'s Shield+'
    WEP_GOOFY_02 = 'Clockwork Shield'
    WEP_GOOFY_03 = 'Clockwork Shield+'
    WEP_GOOFY_04 = 'Star Shield'
    WEP_GOOFY_05 = 'Star Shield+'
    WEP_GOOFY_06 = 'Aegis Shield'
    WEP_GOOFY_07 = 'Aegis Shield+'
    WEP_GOOFY_08 = 'Storm Anchor'
    WEP_GOOFY_09 = 'Storm Anchor+'
    # WEP_GOOFY_10 = '' [UNUSED]
    WEP_GOOFY_11 = 'Nobody Guard'
    WEP_GOOFY_12 = 'Nobody Guard+'
    WEP_GOOFY_13 = 'Save the King'
    WEP_GOOFY_14 = 'Save the King+'
    # WEP_GOOFY_15 = '' # [UNUSED]
    # WEP_GOOFY_16 = '' # [UNUSED]
    # WEP_GOOFY_17 = '' # [UNUSED]
    # WEP_GOOFY_18 = '' # [UNUSED]
    # WEP_GOOFY_19 = '' # [UNUSED]
    
    # WEP_AQUA_00 = 'Master\'s Defender'
    # WEP_AQUA_01 = 'Rainfell'
    # WEP_AQUA_02 = '' # [UNUSED]
    # WEP_AQUA_03 = '' # [UNUSED]
    
    # WEP_MICKEY_00 = '' # [UNUSED]
    # WEP_MICKEY_01 = 'Kingdom Key D'
    # WEP_MICKEY_02 = 'Star Cluster'
    # WEP_MICKEY_03 = '' # [UNUSED]

    # WEP_HERCULES00 = 'Hercule\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_WOODY00 = 'Woody\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_BUZZ00 = 'Buzz\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_RAPUNZEL00 = 'Rapunzel\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_FLYNN00 = 'Flynn\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_JACK_SPARROW00 = 'Jack Sparrow\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_MARSHMALLOW00 = 'Marshmallow\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_BAYMAX00 = 'Baymax\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_SULLEY00 = 'Sulley\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    # WEP_MIKE00 = 'Mike\'s Unique Weapon' # TODO: FIND ACTUAL NAME
    
    # WEP_RIKU00 = 'Way to the Dawn'
    # WEP_RIKU01 = 'Braveheart'
    # WEP_RIKU02 = '' # [UNUSED]
    # WEP_RIKU03 = '' # [UNUSED]
    # WEP_KAIRI00 = 'Destiny\'s Embrace'
    # WEP_LEA00 = 'Flame Liberator'
    # WEP_TERRA00 = 'Earthshaker'
    # WEP_VENTUS00 = 'Wayward Wind'
    # WEP_ROXAS00 = 'Oathkeeper & Oblivion'
    # WEP_XION00 = '(Xion\'s) Kingdom Key'
    # WEP_FRD_SORA00 = '(Sora\'s Friend) Kingdom Key'
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue

            if key.startswith("WEP_KEYBLADE"):
                items.append(ItemData(value, key, ItemClassification.progression, cls.PREFIX))
            else:
                items.append(ItemData(value, key, ItemClassification.filler, cls.PREFIX))
        return items

class ETresTextAbilityKind(KingdomHeartsIIIItem):
    """
    """
    
class ETresAbilityKind(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresAbilityKind:'

    AIR_RECOVERY = 'Aerial Recovery'
    BLOW_COUNTER = 'Payback Strike'
    REFLECT_GUARD = 'Block'
    GUARD_COUNTER = 'Counter Slash'
    REVENGEIMPACT = 'Counter Impact'
    REVENGEDIVE = 'Counter Kick'
    REVENGE_EX = 'Final Blow'
    RISKDODGE = 'Risk Dodge'
    #RD_COUNTER = 'Risk Dodge Counter' # Not used? Or bundled with RISKDODGE?
    SLASH_UPPER = 'Rising Spiral'
    AIR_ROLL_BEAT = 'Groundbreaker'
    AIR_DOWN = 'Falling Slash'
    TRIPPLE_SLASH = 'Speed Slash'
    CHARGE_THRUST = 'Triple Rush'
    MAGICFLUSH = 'Magic Flash'
    HIGHJUMP = 'High Jump'
    DOUBLEFLIGHT = 'Doubleflight'
    SUPERJUMP = 'Superjump'
    SUPERSLIDE = 'Superslide'
    GLIDE = 'Glide'
    LIBRA = 'Scan'
    DODGE = 'Dodge Roll'
    AIRSLIDE = 'Air Slide'
    AIRDODGE = 'Aerial Dodge'
    MP_SAFETY = 'MP Safety'
    EXPZERO = 'Zero EXP'
    FRIEND_AID = 'Assist Friends'
    COMBO_PLUS = 'Combo Plus'
    AIRCOMBO_PLUS = 'Air Combo Plus'
    COMBO_MASTER = 'Combo Master'
    COMBO_UP = 'Combo Boost'
    AIRCOMBO_UP = 'Air Combo Boost'
    FIRE_UP = 'Fire Boost'
    BLIZZARD_UP = 'Blizzard Boost'
    THUNDER_UP = 'Thunder Boost'
    WATER_UP = 'Water Boost'
    AERO_UP = 'Aero Boost'
    WIZZARD_STAR = 'Wizard\'s Ruse'
    LUCK_UP = 'Lucky Strike'
    ITEM_UP = 'Item Boost'
    PRIZE_DRAW = 'Treasure Magnet'
    #FOCUS_BOOST = 'Focus Boost' # Can't seem to find this
    LEAF_VEIL = 'Leaf Bracer'
    LAST_LEAVE = 'Second Chance'
    COMBO_LEAVE = 'Withstand Combo'
    FOCUS_ASPIR = 'Focus Syphon'
    ATTRACTION_TIME = 'Attraction Extender'
    LINK_BOOST = 'Link Extender'
    FORM_TIME = 'Formchange Extender'
    DEFENDER = 'Defender'
    CRITICAL_HALF = 'Damage Control'
    DAMAGE_ASPIR = 'Damage Syphon'
    MP_HASTE = 'MP Haste'
    MP_HASTERA = 'MP Hastera'
    MP_HASTEGA = 'MP Hastega'
    MAGIC_COMBO_SAVE = 'Magic Combo Thrift'
    MAGIC_COMBO_UP = 'Magic Galvanizer'
    WALK_REGENE = 'MP Walker'
    WALK_HEALING = 'HP Walker'
    MAGIC_DRAW = 'Magic Treasure Magnet'
    MASTER_DRAW = 'Master Treasure Magnet'
    ATTRACTION_UP = 'Attraction Enhancer'
    BURN_GUARD = 'Burn Protection'
    CLOUD_GUARD = 'Cloud Protection'
    SNEEZE_GUARD = 'Sneeze Protection'
    FREEZE_GUARD = 'Freeze Protection'
    DISCHARGE_GUARD = 'Electric Protection'
    STUN_GUARD = 'Stun Protection'
    COUNTER_UP = 'Reprisal Boost'
    AUTO_FINISH = 'Auto-Finish'
    FORM_UP = 'Situation Boost'
    MAGIC_TIME = 'Grand Magic Extender'
    AUTO_LOCK_MAGIC = 'Magic Lock-On'
    GUARD_REGENE = 'Block Replenisher'
    MP_SAVE = 'MP Thrift'
    MP_LEAVE = 'Extra Cast'
    FULLMP_BURST = 'Full MP Blast'
    HARVEST = 'Harvester'
    HP_CONVERTER = 'HP Converter'
    MP_CONVERTER = 'MP Converter'
    MUNNY_CONVERTER = 'Munny Converter'
    ENDLESS_MAGIC = 'Endless Magic'
    FP_CONVERTER = 'Focus Converter'
    FIRE_ASPIR = 'Fire Syphon'
    BLIZZARD_ASPIR = 'Blizzard Syphon'
    THUNDER_ASPIR = 'Thunder Syphon'
    WATER_ASPIR = 'Water Syphon'
    AERO_ASPIR = 'Aero Syphon'
    DARK_ASPIR = 'Dark Syphon'
    BEST_COMBI = 'Team Effort'
    SONIC_SLASH = 'Sonic Slash'
    SONIC_DOWN = 'Sonic Cleave'
    TURN_CUTTER = 'Buzz Saw'
    SUMMERSALT = 'Somersault'
    POLE_SPIN = 'Pole Spin'
    POLE_SWING = 'Pole Swing'
    WALL_KICK = 'Wall Kick'
    BATTLE_GRAPHER = 'Frontline Photographer'
    CHARISMA_CHEF = 'Chef Extraordinaire'
    #JOIN_FORCE = 'Join Forces' # Only used by Allies
    HEARTLESS_BUSTER = 'Heartless Buster'
    NOBODY_BUSTER = 'Nobody Buster'
    POWER_CURE = 'Cure Converter'
    CRITICAL_COUNTER = 'Critical Counter'
    CRITICAL_CHARGE = 'Critical Recharge'
    CRITICAL_CONVERTER = 'Critical Converter'
    QUICK_SHAFT = 'Quick Slash'
    FLASH_STEP = 'Flash Step'
    RADIAL_CUT = 'Radial Blaster'
    FINAL_HEAVEN = 'Last Charge'
    AERIAL_SWEEP = 'Aerial Sweep'
    AERIAL_DIVE = 'Aerial Dive'
    LUNCH_TIME = 'Cuisine Extender'
    POWER_LUNCH = 'Hearty Meal'
    OVER_TIME = 'Overtime'
    BEST_CONDITION = 'Top Condition'
    EXP_BARGAIN = 'EXP Incentive'
    PRIZE_FEEVER = 'Prize Proliferator'
    MILLIONAIRE = 'Rags to Riches'
    CURAGAN = 'Curaza'
    CHARGE_BERSERK = 'Berserk Charge'
    OVERCOME = 'Hidden Potential'
    GRAND_MAGIC = 'Grand Magic'
    FIRAGAN = 'Firaza'
    BLIZZAGAN = 'Blizzaza'
    THUNDAGAN = 'Thundaza'
    WATAGAN = 'Waterza'
    AEROGAN = 'Aeroza'
    MAGIC_ROULETTE = 'Magic Roulette'
    UNISON_FIRE = 'Unison Fire'
    UNISON_BLIZZARD = 'Unison Blizzard'
    UNISON_THUNDER = 'Unison Thunder'
    FUSION_SPIN = 'Fusion Spin'
    FUSION_ROCKET = 'Fusion Rocket'
    HYPER_HEALING = 'Hyper Healing'
    COMBI_UP = 'More Team Attacks'
    COMBI_TIME = 'Team Attack Extender'
    SHARE_PRIZE = 'Share Prizes'
    
    @classmethod
    def generate_items(cls):
        items = []
        progression_prefixes = (cls.POLE_SPIN, cls.SUPERJUMP)
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue

            if key.startswith(progression_prefixes):
                items.append(ItemData(value, key, ItemClassification.progression, cls.PREFIX))
            else:
                items.append(ItemData(value, key, ItemClassification.useful, cls.PREFIX))
        return items
    
class ETresCharWearForm(KingdomHeartsIIIItem):
    """
    """

class ETresDropItemID(KingdomHeartsIIIItem):
    """
    """

class ETresVictoryBonusKind(KingdomHeartsIIIItem):
    """
    """
    PREFIX = 'ETresVictoryBonusKind:'

    HP_UP3 = 'HP Up +3'
    HP_UP5 = 'HP Up +5'
    HP_UP10 = 'HP Up +10'
    HP_UP15 = 'HP Up +15'
    HP_UP30 = 'HP Up +30'
    # _RESERVE6 = ''
    # _RESERVE7 = ''
    MP_UP3 = 'MP Up +3'
    MP_UP5 = 'MP Up +5'
    MP_UP10 = 'MP Up +10'
    MP_UP20 = 'MP Up +20'
    # _RESERVE12 = ''
    # _RESERVE13 = ''
    # _RESERVE14 = ''
    # _RESERVE15 = ''
    DEF_SLOT_UP1 = 'Armor Slot +1'
    ACC_SLOT_UP1 = 'Accessory Slot +1'
    ITEM_SLOT_UP1 = 'Item Slot +1'
    # _RESERVE19 = ''
    # _RESERVE20 = ''
    # _RESERVE21 = ''
    # _RESERVE22 = ''
    # _RESERVE23 = ''
    MELEM_FIRE = 'Fire Spell Upgrade'
    MELEM_BLIZZARD = 'Blizzard Spell Upgrade'
    MELEM_THUNDER = 'Thunder Spell Upgrade'
    MELEM_WATER = 'Water Spell Upgrade'
    MELEM_AERO = 'Aero Spell Upgrade'
    MELEM_CURE = 'Cure Spell Upgrade'
    # _RESERVE30 = ''
    # _RESERVE31 = ''
    
    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue

            if key.startswith("MELEM"):
                items.append(ItemData(value, key, ItemClassification.progression, cls.PREFIX))
            else:
                items.append(ItemData(value, key, ItemClassification.useful, cls.PREFIX))
        return items

class ETresSoraBase(KingdomHeartsIIIItem):
    PREFIX = 'ETresSoraBase:'

    # Command Menu
    ATTACK = 'Attack'
    MAGIC = 'Magic'
    ITEMS = 'Items'
    LIMITS = 'Limits'
    WALL_RUN = 'Wall Run'
    RAIL_GRIND = 'Rail Grind'
    AIR_STEP = 'Air Step'
    SHOTLOCK = 'Shotlock'
    DIVING_STRIKE = 'Diving Strike'

    @classmethod
    def generate_items(cls):
        items = []
        for key, value in cls.__dict__.items():
            if key.startswith("__") or isinstance(value, (classmethod, staticmethod)):
                continue

            items.append(ItemData(value, key, ItemClassification.progression, cls.PREFIX))

        return items

# Variables
etres_item_def_accessories = ETresItemDefAccessory.generate_items()
etres_item_def_battle_items = ETresItemDefBattleItem.generate_items()
etres_item_def_camp_items = ETresItemDefCampItem.generate_items()
etres_item_def_foods = ETresItemDefFood.generate_items()
etres_item_def_foodstuffs = ETresItemDefFoodstuff.generate_items()
etres_item_def_key_items = ETresItemDefKeyItem.generate_items()
etres_item_def_lsi_game_items = ETresItemDefLSIGameItem.generate_items()
etres_item_def_materials = ETresItemDefMaterial.generate_items()
etres_item_def_mognet_items = ETresItemDefMognetItem.generate_items()
etres_item_def_navimaps = ETresItemDefNavimap.generate_items()
etres_item_def_protectors = ETresItemDefProtector.generate_items()
etres_item_def_reports = ETresItemDefReport.generate_items()
etres_item_def_weapons = ETresItemDefWeapon.generate_items()
etres_ability_kinds = ETresAbilityKind.generate_items()
etres_victory_bonus_kinds = ETresVictoryBonusKind.generate_items()
etres_sora_base = ETresSoraBase.generate_items()

all_kh3_items = (
    etres_item_def_accessories + 
    etres_item_def_battle_items + 
    etres_item_def_camp_items + 
    etres_item_def_foods +
    etres_item_def_foodstuffs +
    etres_item_def_key_items +
    etres_item_def_lsi_game_items +
    etres_item_def_materials +
    etres_item_def_mognet_items +
    etres_item_def_navimaps +
    etres_item_def_protectors +
    etres_item_def_reports +
    etres_item_def_weapons + 
    etres_ability_kinds +
    etres_victory_bonus_kinds +
    etres_sora_base
)

# Mapping: kh3_id -> item_name (e.g., 'WEP_KEYBLADE_SO_00': 'Kingdom Key')
kh3_item_id_to_name = {
    item.full_id: item.item_name for item in all_kh3_items
}

# Mapping: item_name -> Full ItemData object
kh3_items_by_name = {
    item.item_name: item for item in all_kh3_items
}

# Mapping: group_name -> { all_item_names_in_group }
kh3_item_name_groups: typing.Dict[str, typing.Set[str]] = {
    'Accessories': { item.item_name for item in etres_item_def_accessories },
    'Battle Items': { item.item_name for item in etres_item_def_battle_items },
    'Camp Items': { item.item_name for item in etres_item_def_camp_items },
    'Food Dishes': { item.item_name for item in etres_item_def_foods },
    'Food Ingredients': { item.item_name for item in etres_item_def_foodstuffs },
    'Key Items': { item.item_name for item in etres_item_def_key_items },
    'Classic Kingdom Items': { item.item_name for item in etres_item_def_lsi_game_items },
    'Materials': { item.item_name for item in etres_item_def_materials },
    'Moogle Items': { item.item_name for item in etres_item_def_mognet_items },
    'Maps': { item.item_name for item in etres_item_def_navimaps },
    'Armor': { item.item_name for item in etres_item_def_protectors },
    'Reports': { item.item_name for item in etres_item_def_reports },
    'Weapons': { item.item_name for item in etres_item_def_weapons },
    'Abilities': { item.item_name for item in etres_ability_kinds },
    'Bonuses': { item.item_name for item in etres_victory_bonus_kinds },
    'Sora Base': { item.item_name for item in etres_sora_base }
}

# Pre-defined lists
filler_items = [ ETresItemDefCampItem.ITEM_TENT, ETresItemDefCampItem.ITEM_POWERUP, 
                 ETresItemDefCampItem.ITEM_MAGICUP, ETresItemDefCampItem.ITEM_GUARDUP,
                 ETresItemDefCampItem.ITEM_APUP, ETresItemDefBattleItem.ITEM_POTION, 
                 ETresItemDefBattleItem.ITEM_ETHER, ETresItemDefBattleItem.ITEM_FOCUSSUPPLY,
                 ETresItemDefBattleItem.ITEM_ALLCURE ]

three_proofs = [ ETresItemDefKeyItem.KEY_ITEM12, ETresItemDefKeyItem.KEY_ITEM13, ETresItemDefKeyItem.KEY_ITEM14 ]
kairis_seven_heart_pieces = [ ETresItemDefKeyItem.KEY_ITEM15, ETresItemDefKeyItem.KEY_ITEM15,
                              ETresItemDefKeyItem.KEY_ITEM15, ETresItemDefKeyItem.KEY_ITEM15,
                              ETresItemDefKeyItem.KEY_ITEM15, ETresItemDefKeyItem.KEY_ITEM15,
                              ETresItemDefKeyItem.KEY_ITEM15 ]
