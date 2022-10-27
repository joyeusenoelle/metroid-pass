# Metroid (NES) Random Password Generator
# Author: Noëlle Anthony
# License: MIT
# Date: October 2022
# This uses http://games.technoplaza.net/mpg/password.txt as a basis for its password algorithm
# You can see the original Metroid password system in action at https://www.truepeacein.space/

import logging

from dataclasses import dataclass
from string import ascii_letters, digits
from types import NoneType

logger = logging.getLogger(__name__)

@dataclass
class PasswordItem:
    """A single entry in the password."""
    name: str
    item_type: type
    value: str | int | bool
    maximum: int | NoneType

class PasswordMgr:
    """
    Builds a password out of the values passed in. Intended to be imported
    into your own projects.

    Metroid stores most of the values it cares about as booleans, with three 
    exceptions: current missile count, game age, and start location, which it
    converts to binary. This password manager allows three types: booleans
    (True/False), integers, and strings. Integers are always stored with one
    extra leftmost bit to indicate positive or negative (0=+, 1=-).
    
    Each value is then stored into a long string of bits. Through a fairly 
    convoluted process, that string of bits is then turned into a series 
    of six-bit decimal numbers, and each number corresponds to one of the 
    valid characters in the list below.
    """
    # 0-9A-Za-z plus question mark (?), dash (-), and space ( )
    valid_chars = digits + ascii_letters + "?- "

    def __init__(self):
        """Create the password manager."""
        self.items = {}

    def add_item(self, name: str, value: str|int|bool, maximum: int|NoneType):
        """Add a new item to the password.
        
        Parameters:
            - name (str): The name of the item.
            - type (str): The type of the item ("str", "int", "bool")

        """
        if name not in self.items:
            item_type = type(value)
            curItem = PasswordItem(
                name, item_type, value, maximum
            )
            self.items[name] = curItem
            logger.debug(f"Added to password: {name=}, {value=!s}, {maximum=!s}")
        else:
            raise ValueError(f"Item {name} already exists in the password.")

    def modify_item(self, name: str, value: str|int|bool):
        if name not in self.items:
            raise ValueError(f"Item {name} has not been added to the password yet.")
        else:
            curItem = self.items[name]
            item_max = curItem.maximum
            item_type = curItem.item_type
            if type(value) == item_type:
                if type(value) is int and maximum is not None and value > maximum):
                    raise ValueError(f"Item {name} has a maximum of {maximum} (you wanted to set it to {value}).")
                else:
                    curItem.value = value
                    self.items[name] = curItem
            else:
                raise TypeError(f"Item {name} has a type of {item_type} (you wanted to set it to {type(value)}).")
                    

if __name__ == "__main__":
    help(PasswordMgr)