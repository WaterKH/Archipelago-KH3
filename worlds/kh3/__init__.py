import dataclasses
import hashlib
import logging
import pathlib
import sys
import time
from collections.abc import Callable, Iterable, Mapping
from typing import (Any, ClassVar, Dict, FrozenSet, List, Optional, Self, Set, TextIO, Tuple,
                    TYPE_CHECKING, Type, Union)

from BaseClasses import CollectionRule, CollectionState, Item,  Location, Entrance, ItemClassification, MultiWorld, Region, Tutorial
from Options import item_and_loc_options, ItemsAccessibility, OptionGroup, PerGameCommonOptions
from rule_builder.rules import CustomRuleRegister, Rule
from worlds.LauncherComponents import Component, components, icon_paths, Type, launch as launch_component
from worlds.AutoWorld import WebWorld, World
from worlds.kh3.Container import generate_kh3_output
from worlds.kh3.Rules import KingdomHeartsIIIRules

if TYPE_CHECKING:
    from NetUtils import GamesPackage, MultiData
    from settings import Group

from worlds.kh3.Constants import KEYBLADE_CROSSROADS_REGION, KINGDOM_HEARTS_III, MENU_REGION, SCALA_AD_CAELUM_BOSS_ARENA_REGION
from worlds.kh3.Items import all_kh3_items, filler_items, kh3_items_by_name, kh3_item_name_groups, kh3_item_id_to_name
from worlds.kh3.Locations import all_kh3_locations, kh3_location_name_groups
from worlds.kh3.Options import KingdomHeartsIIIOptions, kh3_option_groups, kh3_options_presets
from worlds.kh3.Regions import KH3_REGION_CONNECTIONS, KingdomHeartsIIIRegion, create_kh3_regions
from worlds.kh3.Settings import KingdomHeartsIIISettings

def launch_client():
    from worlds.kh3.Client import launch
    launch_component(launch, name="KH3Client")

components.append(Component("KH3 Client", func=launch_client, component_type=Type.CLIENT)) #, icon='kh3apicon'))


class KingdomHeartsIIIWebWorld(WebWorld):
    option_groups = kh3_option_groups
    options_presets = kh3_options_presets 

    theme = "ocean"
    
    tutorials = [Tutorial(
        "Archipelago Setup Guide",
        "Archipelago setup guide for Kingdom Hearts III.",
        "English",
        "setup_en.md",
        "setup/en",
        ["waterkh"]
    )]

class KingdomHeartsIIIWorld(World):
    """
    KINGDOM HEARTS III tells the story of the power of friendship as Sora and his friends embark on a perilous adventure. 
    Set in a vast array of Disney and Pixar worlds, KINGDOM HEARTS follows the journey of Sora, a young boy and unknowing 
    heir to a spectacular power. Sora is joined by Donald Duck and Goofy to stop an evil force known as the Heartless from 
    invading and overtaking the universe.

    Through the power of friendship, Sora, Donald and Goofy unite with iconic Disney-Pixar characters old and new to 
    overcome tremendous challenges and persevere against the darkness threatening their worlds.
    """
    game = KINGDOM_HEARTS_III
    web = KingdomHeartsIIIWebWorld()

    options_dataclass = KingdomHeartsIIIOptions
    options: KingdomHeartsIIIOptions

    settings: ClassVar[KingdomHeartsIIISettings]
    
    topology_present = True  # show path to required location checks in spoiler

    base_id = 1000 # I don't see how this is used really?

    item_name_to_id = { item.item_name: kh3_id for kh3_id, item in enumerate(all_kh3_items, base_id) }

    item_name_to_data = kh3_items_by_name

    location_name_to_id = { location.loc_name: kh3_id for kh3_id, location in enumerate(all_kh3_locations, base_id) }
    

    item_name_groups = kh3_item_name_groups

    location_name_groups = kh3_location_name_groups


    # def convert_ap_options_to_kh3_logic(self):
    #     # store a dict of ladxr settings as a middle step so that we can also create a
    #     # ladxr settings object on the other side of the patch
    #     options_dict = dataclasses.asdict(self.options)
    #     self.kh3_settings_dict = {}
    #     for option in options_dict.values():
    #         if not hasattr(option, 'to_kh3_option'):
    #             continue
    #         name, value = option.to_kh3_option(options_dict)
    #         if name:
    #             self.kh3_settings_dict[name] = value
    #     self.kh3_settings = KingdomHeartsIIISettings(self.kh3_settings_dict)

    #     self.kh3_settings.validate()
    #     world_setup = KingdomHeartsIIIWorldSetup()
    #     world_setup.randomize(self.kh3_settings, self.random)
    #     self.kh3_logic = KingdomHeartsIIILogic(configuration_options=self.kh3_settings, world_setup=world_setup)
    #     self.kh3_itempool = KingdomHeartsIIIItemPool(self.kh3_logic, self.kh3_settings, self.random, bool(self.options.stabilize_item_pool)).toDict()

    def generate_early(self) -> None:
        """
        Run before any general steps of the MultiWorld other than options. Useful for getting and adjusting option
        results and determining layouts for entrance rando etc. start inventory gets pushed after this step.
        """
        pass

    def create_regions(self) -> None:
        """Method for creating and connecting regions for the World."""
        # Initialize
        # self.convert_ap_options_to_kh3_logic()

        regions = create_kh3_regions()
        self.multiworld.regions += regions

        # Connect Menu -> Start
        start = None
        for region in regions:
            if region.name == KEYBLADE_CROSSROADS_REGION:
                start = region
                break

        assert(start)

        menu_region = KingdomHeartsIIIRegion(MENU_REGION, MENU_REGION, self.player, self.multiworld)        
        menu_region.exits = [Entrance(self.player, KEYBLADE_CROSSROADS_REGION, menu_region)]
        menu_region.exits[0].connect(start)
        
        self.multiworld.regions.append(menu_region)

        # Connect Scala ad Caelum Boss Arena -> Victory
        scala_ad_caelum_boss_arena = self.multiworld.get_region(SCALA_AD_CAELUM_BOSS_ARENA_REGION, self.player)
        location = Location(self.player, SCALA_AD_CAELUM_BOSS_ARENA_REGION, parent=scala_ad_caelum_boss_arena)
        scala_ad_caelum_boss_arena.locations = [location]
        
        x_blade_key = "The X-Blade"
        location.place_locked_item(self.create_event(x_blade_key))
        
        self.multiworld.completion_condition[self.player] = lambda state: state.has(x_blade_key, player=self.player)

    def create_event(self, event: str):
        return Item(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        """
        Method for creating and submitting items to the itempool. Items and Regions must *not* be created and submitted
        to the MultiWorld after this step. If items need to be placed during pre_fill use `get_pre_fill_items`.
        """
        itempool = []

        for kh3_item_id, count in self.kh3_itempool.items():
            if kh3_item_id not in kh3_item_id_to_name:
                continue
            item_name = kh3_item_id_to_name[kh3_item_id]
            for _ in range(count):
                item = self.create_item(item_name)
                
                itempool.append(item)

        self.multiworld.itempool += itempool

        for source, target in KH3_REGION_CONNECTIONS.items():
            source_region = self.multiworld.get_region(source, self.player)
            source_region.add_exits(target)

    def set_rules(self) -> None:
        """Method for setting the rules on the World's regions and locations."""
        rules = KingdomHeartsIIIRules(self)

        rules.set_kh3_rules()

    def connect_entrances(self) -> None:
        """Method to finalize the source and target regions of the World's entrances"""
        # TODO
        pass

    def generate_basic(self) -> None:
        """
        Useful for randomizing things that don't affect logic but are better to be determined before the output stage.
        i.e. checking what the player has marked as priority or randomizing enemies
        """
        pass

    def pre_fill(self) -> None:
        """Optional method that is supposed to be used for special fill stages. This is run *after* plando."""
        pass

    def fill_hook(self,
                  progitempool: List["Item"],
                  usefulitempool: List["Item"],
                  filleritempool: List["Item"],
                  fill_locations: List["Location"]) -> None:
        """Special method that gets called as part of distribute_items_restrictive (main fill)."""
        pass

    def post_fill(self) -> None:
        """
        Optional Method that is called after regular fill. Can be used to do adjustments before output generation.
        This happens before progression balancing, so the items may not be in their final locations yet.
        """

    def finalize_multiworld(self) -> None:
        """
        Optional Method that is called after fill and progression balancing.
        This is the last stage of generation where worlds may change logically relevant data,
        such as item placements and connections. To not break assumptions,
        only ever increase accessibility, never decrease it.
        """
        pass

    def pre_output(self):
        """
        Optional method that is called before output generation.
        Items and connections are not meant to be moved anymore,
        anything that would affect logical spheres is forbidden at this point.
        """
        pass

    def generate_output(self, output_directory: str) -> None:
        """
        This method gets called from a threadpool, do not use multiworld.random here.
        If you need any last-second randomization, use self.random instead.
        """
        generate_kh3_output(self, output_directory)

    def fill_slot_data(self) -> Mapping[str, Any]:  # json of WebHostLib.models.Slot
        """
        What is returned from this function will be in the `slot_data` field
        in the `Connected` network package.
        It should be a `dict` with `str` keys, and should be serializable with json.

        This is a way the generator can give custom data to the client.
        The client will receive this as JSON in the `Connected` response.

        The generation does not wait for `generate_output` to complete before calling this.
        `threading.Event` can be used if you need to wait for something from `generate_output`.
        """
        # The reason for the `Mapping` type annotation, rather than `dict`
        # is so that type checkers won't worry about the mutability of `dict`,
        # so you can have more specific typing in your world implementation.
        return {}

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        """
        Fill in additional entrance information text into locations, which is displayed when hinted.
        structure is {player_id: {location_id: text}} You will need to insert your own player_id.
        """
        pass

    def modify_multidata(self, multidata: "MultiData") -> None:
        """For deeper modification of server multidata."""
        pass

    # Spoiler writing is optional, these may not get called.
    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        """
        Write to the spoiler header. If individual it's right at the end of that player's options,
        if as stage it's right under the common header before per-player options.
        """
        pass

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        """
        Write to the spoiler "middle", this is after the per-player options and before locations,
        meant for useful or interesting info.
        """
        pass

    def write_spoiler_end(self, spoiler_handle: TextIO) -> None:
        """Write to the end of the spoiler"""
        pass

    # end of ordered Main.py calls

    def create_item(self, name: str) -> "Item":
        """
        Create an item for this world type and player.
        Warning: this may be called with self.world = None, for example by MultiServer
        """
        return kh3_items_by_name[name]

    def get_filler_item_name(self) -> str:
        """
        Called when the item pool needs to be filled with additional items to match location count.

        Any returned item name must be for a "repeatable" item, i.e. one that it's okay to generate arbitrarily many of.
        For most worlds this will be one or more of your filler items, but the classification of these items
        does not need to be ItemClassification.filler.
        The item name returned can be for a trap, useful, and/or progression item as long as it's repeatable.
        """
        return self.random.choice(filler_items)

    @classmethod
    def create_group(cls, multiworld: "MultiWorld", new_player_id: int, players: Set[int]) -> World:
        """
        Creates a group, which is an instance of World that is responsible for multiple others.
        An example case is ItemLinks creating these.
        """
        group = cls(multiworld, new_player_id)
        group.options = cls.options_dataclass(**{option_key: option.from_any(option.default)
                                                 for option_key, option in cls.options_dataclass.type_hints.items()})
        group.options.accessibility = ItemsAccessibility(ItemsAccessibility.option_items)

        return group

    # decent place to implement progressive items, in most cases can stay as-is
    def collect_item(self, state: "CollectionState", item: "Item", remove: bool = False) -> Optional[str]:
        """
        Collect an item name into state. For speed reasons items that aren't logically useful get skipped.
        Collect None to skip item.
        :param state: CollectionState to collect into
        :param item: Item to decide on if it should be collected into state
        :param remove: indicate if this is meant to remove from state instead of adding.
        """
        if item.advancement:
            return item.name
        return None

    def get_pre_fill_items(self) -> List["Item"]:
        """
        Used to return items that need to be collected when creating a fresh all_state, but don't exist in the
        multiworld itempool.
        """
        return []

    # these two methods can be extended for pseudo-items on state
    def collect(self, state: "CollectionState", item: "Item") -> bool:
        """Called when an item is collected in to state. Useful for things such as progressive items or currency."""
        name = self.collect_item(state, item)
        if name:
            state.add_item(name, self.player)
            return True
        return False

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        """Called when an item is removed from to state. Useful for things such as progressive items or currency."""
        name = self.collect_item(state, item, True)
        if name:
            state.remove_item(name, self.player)
            return True
        return False

    def reached_region(self, state: "CollectionState", region: "Region") -> None:
        """Called when a region is newly reachable by the state."""
        pass

    # convenience methods
    def get_location(self, location_name: str) -> "Location":
        return self.multiworld.get_location(location_name, self.player)

    def get_locations(self) -> "Iterable[Location]":
        return self.multiworld.get_locations(self.player)

    def get_entrance(self, entrance_name: str) -> "Entrance":
        return self.multiworld.get_entrance(entrance_name, self.player)

    def get_entrances(self) -> "Iterable[Entrance]":
        return self.multiworld.get_entrances(self.player)

    def get_region(self, region_name: str) -> "Region":
        return self.multiworld.get_region(region_name, self.player)

    def get_regions(self) -> "Iterable[Region]":
        return self.multiworld.get_regions(self.player)

    def push_precollected(self, item: Item) -> None:
        self.multiworld.push_precollected(item)

    @property
    def player_name(self) -> str:
        return self.multiworld.get_player_name(self.player)

    @classmethod
    def get_data_package_data(cls) -> "GamesPackage":
        sorted_item_name_groups = {
            name: sorted(cls.item_name_groups[name]) for name in sorted(cls.item_name_groups)
        }
        sorted_location_name_groups = {
            name: sorted(cls.location_name_groups[name]) for name in sorted(cls.location_name_groups)
        }
        res: "GamesPackage" = {
            # sorted alphabetically
            "item_name_groups": sorted_item_name_groups,
            "item_name_to_id": cls.item_name_to_id,
            "location_name_groups": sorted_location_name_groups,
            "location_name_to_id": cls.location_name_to_id,
        }
        res["checksum"] = data_package_checksum(res)
        return res

    @classmethod
    def get_rule_cls(cls, name: str) -> type[Rule[Self]]:
        """Returns the world-registered or default rule with the given name"""
        return CustomRuleRegister.get_rule_cls(cls.game, name)

    @classmethod
    def rule_from_dict(cls, data: Mapping[str, Any]) -> Rule[Self]:
        """Create a rule instance from a serialized dict representation"""
        name = data.get("rule", "")
        rule_class = cls.get_rule_cls(name)
        return rule_class.from_dict(data, cls)

    def set_rule(self, spot: Location | Entrance, rule: CollectionRule | Rule[Any]) -> None:
        """Sets an access rule for a location or entrance"""
        if isinstance(rule, Rule):
            rule = rule.resolve(self)
            self.register_rule_dependencies(rule)
            if isinstance(spot, Entrance):
                self._register_rule_indirects(rule, spot)
        spot.access_rule = rule

    def set_completion_rule(self, rule: CollectionRule | Rule[Any]) -> None:
        """Set the completion rule for this world"""
        if isinstance(rule, Rule):
            rule = rule.resolve(self)
            self.register_rule_dependencies(rule)
        self.multiworld.completion_condition[self.player] = rule

    def create_entrance(
        self,
        from_region: Region,
        to_region: Region,
        rule: CollectionRule | Rule[Any] | None = None,
        name: str | None = None,
        force_creation: bool = False,
    ) -> Entrance | None:
        """Try to create an entrance between regions with the given rule,
        skipping it if the rule resolves to False (unless force_creation is True)"""
        if rule is not None and isinstance(rule, Rule):
            rule = rule.resolve(self)
            if rule.always_false and not force_creation:
                return None
            self.register_rule_dependencies(rule)

        entrance = from_region.connect(to_region, name, rule=rule)
        if rule and isinstance(rule, Rule.Resolved):
            self._register_rule_indirects(rule, entrance)
        return entrance

    def register_rule_dependencies(self, resolved_rule: Rule.Resolved) -> None:
        """Hook for registering dependencies when a rule is assigned for this world"""
        pass

    def _register_rule_indirects(self, resolved_rule: Rule.Resolved, entrance: Entrance) -> None:
        if self.explicit_indirect_conditions:
            for indirect_region in resolved_rule.region_dependencies().keys():
                self.multiworld.register_indirect_condition(self.get_region(indirect_region), entrance)


def data_package_checksum(data: "GamesPackage") -> str:
    """Calculates the data package checksum for a game from a dict"""
    assert "checksum" not in data, "Checksum already in data"
    assert sorted(data) == list(data), "Data not ordered"
    from NetUtils import encode
    return hashlib.sha1(encode(data).encode()).hexdigest()