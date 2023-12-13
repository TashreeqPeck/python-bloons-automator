"""Global Constants"""
# Standard
import logging
import os

# Third Party

# Local

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------
ROUND_START = os.path.join("resources", "start_round.png")
ENABLE_FAST_FORWARD = os.path.join("resources", "enable_fast_forward.png")
DISABLE_FAST_FORWARD = os.path.join("resources", "disable_fast_forward.png")
