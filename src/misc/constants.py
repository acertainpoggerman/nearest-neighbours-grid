from typing import Optional

type Point = tuple[int, int]
type NearestPointsIndex = tuple[Optional[int], Optional[int]]


# COLORS
from pygame import Color

WHITE   = Color(255, 255, 255)
BLACK   = Color(0, 0, 0)

GRAY75  = Color(191, 191, 191)
GRAY50  = Color(127, 127, 127)
GRAY25  = Color(63, 63, 63)
GRAY15  = Color(31, 31, 31)
GRAY10  = Color(15, 15, 15)

RED         = Color(255, 0, 0)
RED_ALT1    = Color(232, 49, 79)

GREEN   = Color(0, 255, 0)

BLUE        = Color(0, 0, 255)
BLUE_ALT1   = Color(74, 113, 255)

YELLOW  = Color(255, 255, 0)
MAGENTA = Color(0, 255, 255)
CYAN    = Color(255, 0, 255)