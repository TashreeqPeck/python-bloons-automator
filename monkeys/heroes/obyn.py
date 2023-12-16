"Hero Monkey"

# Standard
import logging

# Third Party
import numpy as np

# Local
from constants import MonkeySize
from monkeys.base_monkey import Difficulty
from monkeys.heroes import Hero

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class Obyn(Hero):
    """Obyn Greenfoot"""

    def __init__(self, difficulty: Difficulty) -> None:
        base_costs = np.array([550, 650, 700, 780])
        super().__init__(difficulty, base_costs, MonkeySize.MEDIUM)
