"""Dart Monkey Tests"""

# Standard
import logging

# Third Party

# Local
from monkeys import Difficulty, UpgradePath
from monkeys.dart_monkey import DartMonkey


# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class TestDartMonkey:
    """Dart Monkey Tests"""

    @classmethod
    def setup_class(cls):
        """Setup per suite"""
        cls.dart_monkey = None

    def setup_method(self):
        """Setup per test"""
        logger.debug("Creating Dart Monkey")
        self.dart_monkey = DartMonkey(Difficulty.EASY)
        self.dart_monkey.purchase_monkey((0, 0))
        logger.debug("Dart Monkey created")

    def teardown_method(self):
        """Teardown per test"""
        self.dart_monkey = None

    def test_can_not_upgrade_more_than_five_times(self):
        """Tests if a monkey can not be upgraded more than 5 times"""
        self.dart_monkey.purchase_upgrade(UpgradePath.TOP)
        self.dart_monkey.purchase_upgrade(UpgradePath.TOP)
        self.dart_monkey.purchase_upgrade(UpgradePath.TOP)
        self.dart_monkey.purchase_upgrade(UpgradePath.TOP)
        self.dart_monkey.purchase_upgrade(UpgradePath.TOP)

        can_upgrade = self.dart_monkey.can_upgrade(UpgradePath.TOP)
        assert not can_upgrade, "Upgrade possible when it should not be"

    def test_can_only_two_paths_at_once(self):
        """Tests that only two upgrade paths can be used at once"""
        self.dart_monkey.purchase_upgrade(UpgradePath.TOP)
        self.dart_monkey.purchase_upgrade(UpgradePath.BOTTOM)

        can_upgrade = self.dart_monkey.can_upgrade(UpgradePath.MIDDLE)
        assert not can_upgrade, "Upgrade possible when it should not be"

    def test_can_only_upgrade_one_path_more_than_two_times(self):
        """Tests that only a single path can be upgraded more than 3 times"""
        self.dart_monkey.purchase_upgrade(UpgradePath.MIDDLE)
        self.dart_monkey.purchase_upgrade(UpgradePath.MIDDLE)
        self.dart_monkey.purchase_upgrade(UpgradePath.MIDDLE)
        self.dart_monkey.purchase_upgrade(UpgradePath.TOP)
        self.dart_monkey.purchase_upgrade(UpgradePath.TOP)

        can_upgrade = self.dart_monkey.can_upgrade(UpgradePath.TOP)
        assert not can_upgrade, "Upgrade possible when it should not be"
