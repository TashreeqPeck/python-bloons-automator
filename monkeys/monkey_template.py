""""""

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


class Monkey(BaseMonkey):
    """"""

    def __init__(self, difficulty: Difficulty) -> None:
        self._base_costs = np.array([])
        self._upgrade_costs = np.array(
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
        super().__init__(difficulty)

    @property
    def hotkey(self) -> str:
        return ""
