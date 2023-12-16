""""""

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


class Monkey(BaseMonkey):
    """"""

    def __init__(self, difficulty: Difficulty) -> None:
        base_costs = np.array([])
        upgrade_costs = np.array(
            [
                [
                    [],
                    [],
                    [],
                ],
                [
                    [],
                    [],
                    [],
                ],
                [
                    [],
                    [],
                    [],
                ],
                [
                    [],
                    [],
                    [],
                ],
            ]
        )
        super().__init__(difficulty, upgrade_costs, base_costs, MonkeySize.SMALL)

    @property
    def hotkey(self) -> str:
        return ""
