"Base Tower"

# Standard
from abc import ABCMeta
import logging

# Third Party
import numpy as np
from numpy.typing import NDArray

# Local
from constants import Difficulty, MonkeySize, UpgradePath

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class UpgradeError(Exception):
    """Exception for upgrading tower"""


class BaseMonkey(metaclass=ABCMeta):
    """Base Monkey"""

    def __init__(
        self,
        difficulty: Difficulty,
        costs: NDArray[np.integer],
        size: MonkeySize,
        hotkey,
    ) -> None:
        self._upgrades = np.array([-1, -1, -1])
        self.position: tuple[int, int] = (-1, -1)
        self._costs = costs[difficulty.value]
        self.size = size
        self.hotkey = hotkey

    def can_upgrade(self, path: UpgradePath) -> np.bool_ | bool:
        """Check if the monkey can be upgraded"""
        path_1, path_2 = [_path.value for _path in UpgradePath if _path is not path]
        path_0 = self._upgrades[path.value]
        path_1 = self._upgrades[path_1]
        path_2 = self._upgrades[path_2]
        # Handle max upgrades
        return (
            np.all(self._upgrades != -1)  # Must be purchased
            and path_0 < 5  # Max of 5 upgrades
            and (path_1 < 1 or path_2 < 1)  # Only 2 can be upgraded at any time
            and (
                path_0 < 2 or (path_1 <= 2 and path_2 <= 2)
            )  # only 1 can be more than 3 times
        )

    @property
    def purchase_cost(self) -> int:
        """Monkey purchase cost"""
        return self._costs[0][0]

    def next_upgrade_cost(self, path: UpgradePath) -> int | None:
        """Get the cost of the next upgrade"""
        if self.can_upgrade(path):
            cost = self._costs[path.value][self._upgrades[path.value] + 1]
        else:
            cost = None
        return cost

    def purchase_upgrade(self, path: UpgradePath) -> None:
        """Upgrade the monkey"""
        if np.any(self._upgrades == -1):
            raise UpgradeError("Tower must be purchased before upgrading")
        if not self.can_upgrade(path):
            raise UpgradeError("Upgrade unsuccessful")

        self._upgrades[path.value] += 1

    def purchase_monkey(self, position: tuple[int, int]) -> None:
        """Purchase the monkey"""
        self.position = position
        self._upgrades = np.array([0, 0, 0])


# pylint: disable=C0413
from monkeys.dart_monkey import DartMonkey
from monkeys.ninja_monkey import NinjaMonkey
from monkeys.sniper_monkey import SniperMonkey
