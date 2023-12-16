"""Dart Monkey Tests"""

# Standard
import logging


# Third Party
import numpy as np
import pytest

# Local
from maps import MapPlacementError, Scrapyard
from monkeys import Difficulty
from monkeys.dart_monkey import DartMonkey
from monkeys.ninja_monkey import NinjaMonkey


# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class TestMap:
    """Dart Monkey Tests"""

    @classmethod
    def setup_class(cls):
        """Setup per suite"""
        cls.dart_monkey = None
        cls.map = None

    def setup_method(self):
        """Setup per test"""
        self.dart_monkey = DartMonkey(Difficulty.EASY)
        self.map = Scrapyard()

    def teardown_method(self):
        """Teardown per test"""
        self.dart_monkey = None
        self.map = None

    def test_can_place_when_position_is_valid_and_not_fuzzy(self):
        """Tests if a monkey can be placed on the map when the position is valid"""
        position = (385, 188)
        result = self.map.can_place(self.dart_monkey, position)
        assert result

    def test_can_not_place_when_position_is_invalid(self):
        """Tests if a monkey can not be placed on the map when the position is invalid"""
        position = (500, 500)
        result = self.map.can_place(self.dart_monkey, position)
        assert not result

    def test_get_locations(self):
        """Tests the get locations function (manual verification)"""
        positions = self.map.get_positions(self.dart_monkey)
        for position in positions:
            assert self.map.can_place(
                self.dart_monkey, position
            ), "Should be possible to place monkey"

    def test_place_monkey_on_same_spot(self):
        """Tests that it is not possible to place two monkeys in the same spot"""
        position = (385, 188)
        self.map.place_monkey(self.dart_monkey, position)
        with pytest.raises(MapPlacementError):
            self.map.place_monkey(self.dart_monkey, (385, 198))

    def test_placing_monkey_reduces_options(self):
        """Tests that after placing a monkey there are less options available"""
        positions = self.map.get_positions(self.dart_monkey)
        position = positions[0]
        self.map.place_monkey(self.dart_monkey, position)
        new_positions = self.map.get_positions(self.dart_monkey)

        assert len(new_positions) < len(
            positions
        ), "Placing monkeys should reduce options"

    def test_can_place_monkey_on_same_spot_when_fuzzy(self):
        "Tests that fuzzy placement works"
        position = (385, 188)
        new_monkey = NinjaMonkey(Difficulty.EASY)
        self.map.place_monkey(self.dart_monkey, position)
        self.map.place_monkey(new_monkey, position, True)

        assert np.all(
            self.dart_monkey.position != new_monkey.position
        ), "Monkey positions should not be the same"
