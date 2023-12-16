""""""

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


class Monkey(BaseMonkey):
    """"""

    def __init__(self, difficulty: Difficulty) -> None:
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
        super().__init__(difficulty, upgrade_costs, MonkeySize.SMALL, "")
