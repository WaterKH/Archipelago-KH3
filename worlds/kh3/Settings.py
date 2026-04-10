import typing

import settings

class KingdomHeartsIIISettings(settings.Group):
    class Executable(settings.UserFilePath):
        is_exe = True

    class FilterConnectionChanges(settings.Bool):
        """Whether to filter connection changes displayed in-game."""

    class FilterItemSends(settings.Bool):
        """Whether to filter item send messages displayed in-game to only those that involve you."""    

    class ServerSettings(settings.OptionalUserFilePath):
        """
        Required for other settings.
        server_settings: "KH_3/data/server-settings.json"
        """

    executable: Executable = Executable("KH_3/KINGDOM HEARTS III/Binaries/Win64")
    filter_connection_changes: typing.Union[FilterConnectionChanges, bool] = False
    filter_item_sends: typing.Union[FilterItemSends, bool] = False
    server_settings: typing.Optional[ServerSettings] = None