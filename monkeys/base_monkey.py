"Base Tower"

# Standard
from abc import ABC, abstractmethod
import logging

# Third Party
import numpy as np

# Local
from constants import Difficulty, UpgradePath

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class UpgradeException(Exception):
    """Exception for upgrading tower"""


class BaseMonkey(ABC):
    """Base Monkey"""

    def __init__(self, difficulty: Difficulty) -> None:
        if not hasattr(self, "_upgrade_costs") or not hasattr(self, "_base_costs"):
            raise NotImplementedError(
                "_upgrade_costs and _base_costs must be implemented in derived class"
            )
        self._upgrades = np.array([-1, -1, -1])
        self.position: tuple[int, int] | None = None
        # pylint: disable=E1101
        self._upgrade_cost = self._upgrade_costs[difficulty.value]
        self.cost = self._base_costs[difficulty.value]
        # pylint: enable=E1101

    @property
    @abstractmethod
    def hotkey(self) -> str:
        """Hotkey to place tower"""

    def can_upgrade(self, path: UpgradePath) -> bool:
        """Check if the monkey can be upgraded"""
        path_1, path_2 = [_path for _path in UpgradePath if _path is not path]
        path_0 = self._upgrades[path.value]
        path_1 = self._upgrades[path_1.value]
        path_2 = self._upgrades[path_2.value]
        # Handle max upgrades
        return not (
            # Can't upgrade more than 5 times
            path_0 == 4
            # Can't upgrade more than 2 paths
            or (path_1 >= 0 and path_2 >= 0)  # type: ignore
            # Can't upgrade 1 path more than 2 times
            or (path_0 == 1 and (path_1 > 1 or path_2 > 1))  # type: ignore
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
