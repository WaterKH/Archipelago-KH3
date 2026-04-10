

from datetime import UTC, datetime

import yaml
import os
import zipfile

import Utils
from worlds.Files import APPlayerContainer
from worlds.kh3.Locations import all_kh3_locations
from worlds.kh3.Items import kh3_items_by_name


class KingdomHeartsIIIContainer(APPlayerContainer):
    game: str = 'Kingdom Hearts III'
    patch_file_ending = ".zip"

    def __init__(self, patch_data: dict, base_path: str, output_directory: str, player=None, player_name: str = "", server: str = ""):
        self.patch_data = patch_data
        self.file_path = base_path

        container_path = os.path.join(output_directory, base_path + ".zip")
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        for filename, yml in self.patch_data.items():
            opened_zipfile.writestr(filename, yml)
        
        super().write_contents(opened_zipfile)

def generate_kh3_output(self, output_directory):
    curr_timestamp = datetime.strftime(datetime.now(UTC), "%d%b%Y-%H%M%S")
    player_name = self.multiworld.get_file_safe_player_name(self.player)
    seed_name = self.multiworld.seed_name
    mod_name = f"AP-{seed_name}-P{self.player}-{player_name}-{curr_timestamp}"
    mod_dir = os.path.join(output_directory, mod_name + "_" + Utils.__version__)

    self.mod_yml = { }

    self.mod_yml["title"] = f"Archipelago Seed - {player_name}"
    self.mod_yml["originalAuthor"] = "waterkh"
    self.mod_yml["description"] = f"Seed {seed_name} was generated for {player_name} - Player {self.player} at {curr_timestamp} UTC."

    all_valid_locations = {location for location, data in all_kh3_locations.items()}

    for location in self.multiworld.get_filled_locations(self.player):
        if location.name not in all_valid_locations:
            continue

        data = all_valid_locations[location.name]

        if not location.item:
            continue
        if location.item.player != self.player:
            continue

        itemcode = kh3_items_by_name[location.item.name].kh3id
        
        self.mod_yml["data"].append(itemcode)


    kh3_mod = {
        "mod.yml": yaml.dump(self.mod_yml, line_break="\n")
    }

    mod = KingdomHeartsIIIContainer(kh3_mod, mod_dir, output_directory, self.player, player_name)
    mod.write()