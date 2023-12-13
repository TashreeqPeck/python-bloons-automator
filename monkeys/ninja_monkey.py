"""Ninja Monkey"""
# Standard
import logging

# Third Party
import numpy as np

# Local
from monkeys.base_monkey import BaseMonkey, Difficulty

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class NinjaMonkey(BaseMonkey):
    """Ninja Monkey"""

    def __init__(self, difficulty: Difficulty) -> None:
        self._base_costs = np.array([425, 500, 540, 600])
        self._upgrade_costs = np.array(
            [
                [
                    [255, 295, 720, 3235, 29750],
                    [295, 425, 765, 4420, 18700],
                    [210, 340, 2335, 2825, 34000],
                ],
                [
                    [300, 350, 850, 2750, 35000],
                    [350, 500, 900, 5200, 22000],
                    [250, 400, 2750, 5400, 43200],
                ],
                [
                    [325, 380, 920, 2970, 37800],
                    [380, 540, 970, 5615, 23760],
                    [270, 430, 2430, 5400, 43200],
                ],
                [
                    [360, 420, 1020, 3300, 42000],
                    [420, 600, 1080, 6240, 26400],
                    [300, 480, 3300, 5400, 48000],
                ],
            ]
        )
        super().__init__(difficulty)

    @property
    def hotkey(self) -> str:
        return "d"
