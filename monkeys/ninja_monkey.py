"""Ninja Monkey"""
# Standard
import logging

# Third Party
import numpy as np

# Local
from monkeys import BaseMonkey
from constants import MonkeySize, Difficulty

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class NinjaMonkey(BaseMonkey):
    """Ninja Monkey"""

    def __init__(self, difficulty: Difficulty) -> None:
        upgrade_costs = np.array(
            [
                [
                    [425, 255, 295, 720, 2335, 29750],
                    [425, 295, 425, 765, 4420, 18700],
                    [425, 210, 340, 2335, 2825, 34000],
                ],
                [
                    [500, 300, 350, 850, 2750, 35000],
                    [500, 350, 500, 900, 5200, 22000],
                    [500, 250, 400, 2750, 5400, 43200],
                ],
                [
                    [540, 325, 380, 920, 2970, 37800],
                    [540, 380, 540, 970, 5615, 23760],
                    [540, 270, 430, 2430, 5400, 43200],
                ],
                [
                    [600, 360, 420, 1020, 3300, 42000],
                    [600, 420, 600, 1080, 6240, 26400],
                    [600, 300, 480, 3300, 5400, 48000],
                ],
            ]
        )
        super().__init__(difficulty, upgrade_costs, MonkeySize.SMALL, "d")
