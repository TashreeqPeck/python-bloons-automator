"""BloonsTD6 Map"""
# pylint: disable=E1101

# Standard
import logging
import os

# Third Party
import cv2
import numpy as np
from numpy.typing import NDArray
from constants import MAP_MATCHING_THRESHOLD, MONKEY_TEMPLATES

# Local
from monkeys import BaseMonkey
from monkeys.heroes import Hero

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class MapPlacementError(Exception):
    """Exception for invalid map placement"""


class Map:
    """BloonsTD6 Map"""

    def __init__(self, map_path: str, offset: tuple[int, int]) -> None:
        self.img = cv2.imread(map_path)
        self.x_offset, self.y_offset = offset

    def can_place(self, monkey: BaseMonkey | Hero, position: tuple[int, int]) -> bool:
        """Check if a monkey can be placed on the map at the position"""
        template = MONKEY_TEMPLATES[monkey.size]

        left, right, top, bottom = self._get_bounds(monkey, position)
        reference = self.img[top:bottom, left:right]
        result = cv2.matchTemplate(reference, template, cv2.TM_CCORR_NORMED)
        return result[0][0] > MAP_MATCHING_THRESHOLD

    def get_positions(self, monkey: BaseMonkey | Hero) -> NDArray:
        """Get placable locations"""
        template = MONKEY_TEMPLATES[monkey.size]
        height, width, _ = template.shape

        reference = self.img.copy()
        result = cv2.matchTemplate(reference, template, cv2.TM_CCORR_NORMED)
        y_points, x_points = np.where(result > MAP_MATCHING_THRESHOLD)
        locations = np.empty(len(y_points), dtype="2i")
        for _i, (_x, _y) in enumerate(zip(x_points, y_points)):
            locations[_i] = (
                int(_x + width / 2 + self.x_offset),
                int(_y + height / 2 + self.y_offset),
            )
            cv2.circle(
                reference,
                (int(_x + width / 2), int(_y + height / 2)),
                0,
                [0, 0, 255],
                -1,
            )

        cv2.imwrite("available.png", reference)

        return locations

    def _get_bounds(
        self,
        monkey: BaseMonkey | Hero,
        center: tuple[int, int],
    ) -> tuple[int, int, int, int]:
        "Return the left, right, top, bottom bounds of the monkey"
        height, width, _ = MONKEY_TEMPLATES[monkey.size].shape
        x, y = center
        bounds = (
            x - self.x_offset - int(width / 2),
            x - self.x_offset + int(width / 2),
            y - self.y_offset - int(height / 2),
            y - self.y_offset + int(height / 2),
        )

        return bounds

    def place_monkey(self, monkey: BaseMonkey | Hero, position, fuzzy=False) -> None:
        """Place monkey on map"""
        if not fuzzy and not self.can_place(monkey, position):
            raise MapPlacementError("Could not place monkey")
        if fuzzy and not self.can_place(monkey, position):
            positions = self.get_positions(monkey)
            deltas = positions - position
            dist_2 = np.einsum("ij,ij->i", deltas, deltas)
            position = positions[np.argmin(dist_2)]
        positions = self.get_positions(monkey)
        left, right, top, bottom = self._get_bounds(monkey, position)
        cv2.rectangle(self.img, (left, top), (right, bottom), (0, 0, 0), -1)
        monkey.position = position
        cv2.imwrite("unavailable.png", self.img)


class Scrapyard(Map):
    """Scrapyard Map"""

    def __init__(self) -> None:
        super().__init__(
            os.path.join("resources", "maps", "beginner", "scrapyard.png"), (43, 0)
        )
