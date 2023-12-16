"""Global Constants"""
# Standard
from enum import Enum
import logging
import os

# Third Party

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
CUMULATIVE_ROUND_CASH  # pylint: disable=W0104
STARTING_ROUND = [1, 1, 3, 6]
STARTING_CASH = 650
