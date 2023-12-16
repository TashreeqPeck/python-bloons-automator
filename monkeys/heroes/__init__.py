"Hero Monkey"

# Standard
import logging

# Third Party
import numpy as np
from numpy.typing import NDArray

# Local
from constants import MonkeySize
from monkeys.base_monkey import Difficulty

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class Hero:
    """Hero Monkey"""

    def __init__(
        self, difficulty: Difficulty, base_costs: NDArray[np.integer], size: MonkeySize
    ) -> None:
        self.position: tuple[int, int] = (-1, -1)
        self.cost = base_costs[difficulty.value]  # pylint: disable=E1101
        self.hotkey = "u"
        self.size = size
