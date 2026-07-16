# NOTE TO STUDENTS: You can ignore the contents of this file. They're used
# by the starter code in game.py. You do not need to understand this code.
# DO NOT modify this code.

import fcntl
import tty
import termios
from typing import IO, Any
import sys
import os

from coordinates import Coordinates

class HashableCoordinates:
    _coordinates: Coordinates
    def __init__(self, coordinates: Coordinates) -> None:
        self._coordinates = coordinates

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, HashableCoordinates):
            return ((self._coordinates.row == other._coordinates.row) and\
                (self._coordinates.column == other._coordinates.column))
        else:
            return False
    
    def __hash__(self) -> int:
        return hash((self._coordinates.row, self._coordinates.column))

class hidden_cursor(object):
    def __enter__(self) -> None:
        print('\033[?25l', end="") # Hides cursor
        
    def __exit__(
            self,
            exc_type: type,
            exc_value: Any,
            traceback: Any
            ) -> None:
        print('\033[?25h', end="") # Shows cursor

# Modified from Thomas Ballinger's implementation:
# https://ballingt.com/nonblocking-stdin-in-python-3/
class raw(object):
    _stream: IO[Any]
    _fd: Any
    _original_stty: Any
    def __init__(self, stream: IO[Any]) -> None:
        self._stream = stream
        self._fd = self._stream.fileno()
    def __enter__(self) -> None:
        self._original_stty = termios.tcgetattr(self._stream)
        tty.setcbreak(self._stream)
    def __exit__(
            self,
            exc_type: type,
            exc_value: Any,
            traceback: Any
            ) -> None:
        termios.tcsetattr(
            self._stream,
            termios.TCSANOW,
            self._original_stty
        )

class nonblocking(object):
    _stream: IO[Any]
    _fd: Any
    _orig_fl: Any
    def __init__(self, stream: IO[Any]) -> None:
        self._stream = stream
        self._fd = self._stream.fileno()
    def __enter__(self) -> None:
        self._orig_fl = fcntl.fcntl(self._fd, fcntl.F_GETFL)
        fcntl.fcntl(
            self._fd,
            fcntl.F_SETFL,
            self._orig_fl | os.O_NONBLOCK
        )
    def __exit__(
            self,
            exc_type: type,
            exc_value: Any,
            traceback: Any) -> None:
        fcntl.fcntl(
            self._fd,
            fcntl.F_SETFL,
            self._orig_fl
        )

def clear_terminal() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
