"Base Tower"

# Standard
from enum import Enum
import logging

# Third Party
import numpy as np

# Local

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class Difficulty(Enum):
    """Map Difficulty"""

    EASY = 0
    MEDIUM = 1
    HARD = 2
    IMPOPPABLE = 3


class UpgradePath(Enum):
    """Upgrade Paths"""

    TOP = 0
    MIDDLE = 1
    BOTTOM = 2


class UpgradeException(Exception):
    """Exception for upgrading tower"""


class BaseMonkey:
    """Base Monkey"""

    def __init__(self, difficulty: Difficulty) -> None:
        if not hasattr(self, "_upgrade_costs") or not hasattr(self, "_base_costs"):
            raise NotImplementedError(
                "_upgrade_costs and _base_costs must be implemented in derived class"
            )
        self._upgrades = np.array([-1, -1, -1])
        # pylint: disable=E1101
        self._upgrade_cost = self._upgrade_costs[difficulty.value]
        self.cost = self._base_costs[difficulty.value]
        # pylint: enable=E1101

    def can_upgrade(self, path: UpgradePath, money: int | None = None) -> bool:
        """Check if the monkey can be upgraded"""
        path_1, path_2 = [_path for _path in UpgradePath if _path is not path]
        path_0 = self._upgrades[path.value]
        path_1 = self._upgrades[path_1.value]
        path_2 = self._upgrades[path_2.value]
        cost = self.next_upgrade_cost(path)
        # Handle max upgrades
        return not (
            # Can't upgrade more than 5 times
            path_0 == 4
            # Can't upgrade more than 2 paths
            or (path_1 >= 0 and path_2 >= 0)  # type: ignore
            # Can't upgrade 1 path more than 2 times
            or (path_0 == 1 and (path_1 > 1 or path_2 > 1))  # type: ignore
            # Can't upgrade if money is not enough
            or (cost is not None and money is not None and money < cost)
        )

    def next_upgrade_cost(self, path: UpgradePath) -> int | None:
        """Get the cost of the next upgrade"""
        current_level = self._upgrades[path.value] + 1
        if current_level >= 5:
            cost = None
        else:
            cost = self._upgrade_cost[path.value][self._upgrades[path.value] + 1]
        return cost

    def increment_upgrade(self, path: UpgradePath) -> None:
        """Upgrade the tower"""
        if not self.can_upgrade(path):
            raise UpgradeException("Upgrade unsuccessful")
        self._upgrades[path.value] += 1

    def can_afford(self, money: int) -> bool:
        """Check if the monkey can be afforded"""
        return self.cost < money
