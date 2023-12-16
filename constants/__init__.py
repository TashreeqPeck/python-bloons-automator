"""Global Constants"""
# pylint: disable=E1101
# Standard
from enum import Enum
import logging
import os

# Third Party
import cv2

# Local
from constants.cash import CUMULATIVE_ROUND_CASH

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


# General Constants
class Difficulty(Enum):
    """Map Difficulty"""

    EASY = 0
    MEDIUM = 1
    HARD = 2
    IMPOPPABLE = 3


# Image resources
ROUND_START = os.path.join("resources", "start_round.png")
ENABLE_FAST_FORWARD = os.path.join("resources", "enable_fast_forward.png")
DISABLE_FAST_FORWARD = os.path.join("resources", "disable_fast_forward.png")
CANCEL_PLACEMENT = os.path.join("resources", "cancel_placement.png")


# Upgrade Constants
class UpgradePath(Enum):
    """Upgrade Paths"""

    TOP = 0
    MIDDLE = 1
    BOTTOM = 2


UPGRADE_HOTKEYS = {
    UpgradePath.TOP: ",",
    UpgradePath.MIDDLE: ".",
    UpgradePath.BOTTOM: "/",
}

# Screen capture regions
MONEY_REGION = (486, 30, 220, 57)
HEALTH_REGION = (180, 20, 110, 60)

# Round Cash Constants
STARTING_ROUND = [1, 1, 3, 6]
STARTING_CASH = 650


# Monkey Size Constants
class MonkeySize(Enum):
    """Monkey Sizes"""

    SMALL = os.path.join("resources", "footprints", "small.png")
    MEDIUM = os.path.join("resources", "footprints", "medium.png")
    LARGE = os.path.join("resources", "footprints", "large.png")
    EXTRA_LARGE = os.path.join("resources", "footprints", "xlarge.png")
    HELI_PILOT = os.path.join("resources", "footprints", "heli.png")
    MONKEY_ACE = os.path.join("resources", "footprints", "ace.png")


MONKEY_TEMPLATES = {
    MonkeySize.SMALL: cv2.imread(MonkeySize.SMALL.value),
    MonkeySize.MEDIUM: cv2.imread(MonkeySize.MEDIUM.value),
    MonkeySize.LARGE: cv2.imread(MonkeySize.LARGE.value),
    MonkeySize.EXTRA_LARGE: cv2.imread(MonkeySize.EXTRA_LARGE.value),
    MonkeySize.HELI_PILOT: cv2.imread(MonkeySize.HELI_PILOT.value),
    MonkeySize.MONKEY_ACE: cv2.imread(MonkeySize.MONKEY_ACE.value),
}

# Map Offsets
MAP_REGION_OFFSET = 40
MAP_MATCHING_THRESHOLD = 0.97
