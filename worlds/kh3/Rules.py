from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.kh3.Constants import *
from worlds.kh3.Items import ETresAbilityKind, ETresItemDefKeyItem, ETresSoraBase, three_proofs, kairis_seven_heart_pieces

if TYPE_CHECKING:
    from . import KingdomHeartsIIIWorld
else:
    KingdomHeartsIIIWorld = object

class KingdomHeartsIIIRules():
    world: KingdomHeartsIIIWorld
    player: int

    def __init__(self, kh3world: KingdomHeartsIIIWorld) -> None:
        self.world = kh3world
        self.player = kh3world.player
        self.multiworld = kh3world.multiworld

        self.region_rules: dict[str, bool] = {
            OLYMPUS_CLIFF_ASCENT_INITIAL_REGION: lambda state: self.wall_run_unlock(state, 1),

            TOY_BOX_LOWER_VENTS_REGION: lambda state: self.wall_run_unlock(state, 1),

            KINGDOM_OF_CORONA_TOWER_REGION: lambda state: self.wall_run_unlock(state, 1),
            KINGDOM_OF_CORONA_WETLANDS_REGION: lambda state: self.super_jump_unlock(state, 1),

            MONSTROPOLIS_DOOR_VAULT_UPPER_LEVEL_REGION: lambda state: self.rail_grind_unlock(state, 1),

            ARENDELLE_THE_LABYRINTH_OF_ICE_MIDDLE_TIER_REGION: lambda state: self.pole_spin_unlock(state, 1),
            
            SAN_FRANSOKYO_THE_CITY_NORTH_DISTRICT_REGION: lambda state: self.diving_strike_unlock(state, 1),
            SAN_FRANSOKYO_THE_CITY_SOUTH_DISTRICT_REGION: lambda state: self.diving_strike_unlock(state, 1),
            SAN_FRANSOKYO_THE_CITY_CENTRAL_DISTRICT_REGION: lambda state: self.diving_strike_unlock(state, 1),

            THE_FINAL_WORLD_LABYRINTH_OF_PILLARS_REGION: lambda state: self.wall_run_unlock(state, 1)
        }

    def set_kh3_rules(self) -> None:
        for region_name, rules in self.region_rules.items():
            region = self.multiworld.get_region(region_name, self.player)
            for entrance in region.entrances:
                entrance.access_rule = rules

        self.set_kh3_goal()

    def set_kh3_goal(self):
        final_boss_location = self.multiworld.get_location(SCALA_AD_CAELUM_BOSS_ARENA_REGION, self.player)
        # three proofs win condition
        if self.world.options.Goal == "three_proofs":
            final_boss_location.access_rule = lambda state: state.has_all(set(three_proofs), self.player)
        # heart pieces win condition
        elif self.world.options.Goal == "heart_pieces":
            final_boss_location.access_rule = lambda state: state.has(ETresItemDefKeyItem.KEY_ITEM15, self.player, 7)
        # three proofs and heart pieces win condition
        else:
            final_boss_location.access_rule = lambda state: state.has_all(set(three_proofs), self.player) and \
                                                              state.has(ETresItemDefKeyItem.KEY_ITEM15, self.player, 7)
            
        # Defeat Xehanort
        self.multiworld.completion_condition[self.player] = lambda state: state.has(ETresItemDefKeyItem.END_SCREENKEY_ITEM28, self.player, 1)

    # State checks
    def wall_run_unlock(self, state: CollectionState, Amount) -> bool:
        return state.has(ETresSoraBase.WALL_RUN, self.player, Amount)
    
    def super_jump_unlock(self, state: CollectionState, Amount) -> bool:
        return state.has(ETresAbilityKind.SUPERJUMP, self.player, Amount)
    
    def rail_grind_unlock(self, state: CollectionState, Amount) -> bool:
        return state.has(ETresSoraBase.RAIL_GRIND, self.player, Amount)
    
    def pole_spin_unlock(self, state: CollectionState, Amount) -> bool:
        return state.has(ETresAbilityKind.POLE_SPIN, self.player, Amount)
    
    def diving_strike_unlock(self, state: CollectionState, Amount) -> bool:
        return state.has(ETresSoraBase.DIVING_STRIKE, self.player, Amount)