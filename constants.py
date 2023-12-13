"""Global Constants"""
# Standard
import logging
import os

# Third Party

# Local
from monkeys.base_monkey import UpgradePath

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------
ROUND_START = os.path.join("resources", "start_round.png")
ENABLE_FAST_FORWARD = os.path.join("resources", "enable_fast_forward.png")
DISABLE_FAST_FORWARD = os.path.join("resources", "disable_fast_forward.png")
CANCEL_PLACEMENT = os.path.join("resources", "cancel_placement.png")

UPGRADE_HOTKEYS = {
    UpgradePath.TOP: ",",
    UpgradePath.MIDDLE: ".",
    UpgradePath.BOTTOM: "/",
}
