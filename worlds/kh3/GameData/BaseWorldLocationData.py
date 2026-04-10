import typing

class BaseWorldLocationData(typing.NamedTuple):
    # lookup id of value in KH3 datatable (event/ treasure/ etc.)
    location: str
    # value that is used for items
    value: str = ""
    # label that is used for event, ability and victory bonuses
    label: str = ""