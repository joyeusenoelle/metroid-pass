# Metroid (NES) Random Password Generator
# Author: Noëlle Anthony
# License: MIT
# Date: October 2022
# This uses http://games.technoplaza.net/mpg/password.txt as a basis for its password algorithm
# You can see the original Metroid password system in action at https://www.truepeacein.space/

from dataclasses import dataclass
from string import ascii_letters, digits
from typing import TypedDict

@dataclass
class PasswordItem:
    """A single entry in the password."""
    name: str
    value: str | int | bool


class PasswordMgr:
    """
    Builds a password out of the values passed in. Intended to be imported
    into your own projects.

    Metroid stores most of the values it cares about as booleans, with three 
    exceptions: current missile count, game age, and start location, which it
    converts to binary. Each value is then stored into a long string of bits,
    Through a fairly convoluted process, that string of bits is then turned 
    into a series of six-bit decimal numbers, and each number corresponds to
    one of the valid characters in the list below.
    """
    # 0-9A-Za-z plus question mark (?), dash (-), and space ( )
    valid_chars = digits + ascii_letters + "?- "

    def __init__(self):
        """Create the password manager."""
        self.items = {}

if __name__ == "__main__":
    help(PasswordMgr)