"Hero Monkey"

# Standard
import logging

# Third Party
import numpy as np
from numpy.typing import NDArray

# Local
from constants import MonkeySize, Difficulty

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
        self.purchase_cost = base_costs[difficulty.value]
        self.hotkey = "u"
        self.size = size

    def purchase_monkey(self, position: tuple[int, int]):
        """Purchase the monkey"""
        self.position = position


# pylint: disable=C0413
from monkeys.heroes.obyn import Obyn
