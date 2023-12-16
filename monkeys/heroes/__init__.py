"Hero Monkey"

# Standard
import logging

# Third Party

# Local
from monkeys.base_monkey import Difficulty

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class Hero:
    """Hero Monkey"""

    def __init__(self, difficulty: Difficulty) -> None:
        if not hasattr(self, "_base_costs"):
            raise NotImplementedError(
                "_base_costs must be implemented in derived class"
            )
        self.position: tuple[int, int] | None = None
        self.cost = self._base_costs[difficulty.value]  # pylint: disable=E1101
        self.hotkey = "u"
