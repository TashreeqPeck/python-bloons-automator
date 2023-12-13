"""Sniper Monkey"""

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


class SniperMonkey(BaseMonkey):
    """Sniper Monkey"""

    def __init__(self, difficulty: Difficulty) -> None:
        self._base_costs = np.array([300, 350, 380, 420])
        self._upgrade_costs = np.array(
            [
                [
                    [295, 1275, 2550, 4250, 28900],
                    [255, 380, 2720, 6120, 11050],
                    [340, 340, 2975, 3610, 11900],
                ],
                [
                    [350, 1500, 3000, 5000, 34000],
                    [300, 450, 3200, 7200, 13000],
                    [400, 400, 3500, 4250, 14000],
                ],
                [
                    [380, 1620, 3240, 4500, 36720],
                    [325, 485, 3455, 7775, 14040],
                    [430, 430, 3780, 4590, 15120],
                ],
                [
                    [420, 1800, 3600, 6000, 4080],
                    [360, 540, 3840, 8640, 15600],
                    [480, 480, 4200, 5100, 16800],
                ],
            ]
        )
        super().__init__(difficulty)

    @property
    def hotkey(self) -> str:
        return "z"
