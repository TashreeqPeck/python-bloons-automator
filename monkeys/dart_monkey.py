"Dart Monkey"

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


class DartMonkey(BaseMonkey):
    """Dart Monkey"""

    def __init__(self, difficulty: Difficulty) -> None:
        costs = np.array(
            [
                [
                    [170, 120, 185, 225, 1530, 12750],
                    [170, 85, 160, 340, 6800, 38250],
                    [170, 75, 170, 530, 1700, 18275],
                ],
                [
                    [200, 140, 220, 325, 1945, 1500],
                    [200, 100, 190, 430, 8000, 45000],
                    [200, 90, 200, 625, 2000, 21500],
                ],
                [
                    [215, 150, 235, 325, 1945, 16200],
                    [215, 110, 205, 430, 8640, 48600],
                    [215, 95, 215, 675, 2160, 23220],
                ],
                [
                    [245, 170, 265, 360, 2160, 1800],
                    [245, 120, 230, 480, 960, 54000],
                    [245, 110, 240, 750, 2400, 25800],
                ],
            ]
        )
        super().__init__(difficulty, costs, MonkeySize.SMALL, "q")
