"Dart Monkey"

# Standard
import logging

# Third Party
import numpy as np

# Local
from monkeys.base_monkey import BaseMonkey, Difficulty
from constants import MonkeySize

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class DartMonkey(BaseMonkey):
    """Dart Monkey"""

    def __init__(self, difficulty: Difficulty) -> None:
        base_costs = np.array([170, 200, 215, 240])
        upgrade_costs = np.array(
            [
                [
                    [120, 185, 225, 1530, 12750],
                    [85, 160, 340, 6800, 38250],
                    [75, 170, 530, 1700, 18275],
                ],
                [
                    [140, 220, 325, 1945, 1500],
                    [100, 190, 430, 8000, 45000],
                    [90, 200, 625, 2000, 21500],
                ],
                [
                    [150, 235, 325, 1945, 16200],
                    [110, 205, 430, 8640, 48600],
                    [95, 215, 675, 2160, 23220],
                ],
                [
                    [170, 265, 360, 2160, 1800],
                    [120, 230, 480, 960, 54000],
                    [110, 240, 750, 2400, 25800],
                ],
            ]
        )
        super().__init__(difficulty, upgrade_costs, base_costs, MonkeySize.SMALL)

    @property
    def hotkey(self) -> str:
        return "q"
