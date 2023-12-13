"""BloonsTD6 UI control"""

# Standard
import logging
import time

# Third Party
import pyautogui
from pyautogui import ImageNotFoundException
import keyboard

# Local
from constants import (
    CANCEL_PLACEMENT,
    ROUND_START,
    ENABLE_FAST_FORWARD,
    DISABLE_FAST_FORWARD,
    UPGRADE_HOTKEYS,
)
from monkeys.base_monkey import BaseMonkey, UpgradeException, UpgradePath
from ocr import grab_int

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class ActionFailedException(Exception):
    """Exception for failed UI Actions"""


class RoundAlreadyStartedException(ActionFailedException):
    """Exception for round already started"""


class UIController:
    """Bloons TD6 UI Controller"""

    def start_round(self, speed_up: bool = False) -> None:
        """Start the round"""
        try:
            x, y = pyautogui.locateCenterOnScreen(ROUND_START, confidence=0.9)  # type: ignore
            pyautogui.click(x, y)
            logger.info("Round started")
            if speed_up:
                pyautogui.click(x, y)
                logger.info("Round fast forward enabled")
        except ImageNotFoundException as error:
            try:
                pyautogui.locateOnScreen(ENABLE_FAST_FORWARD, confidence=0.9)
                logger.info("Round already started")
                raise RoundAlreadyStartedException  # pylint: disable=W0707
            except ImageNotFoundException:
                pass
            try:
                pyautogui.locateOnScreen(DISABLE_FAST_FORWARD, confidence=0.9)
                logger.info("Round already started")
                raise RoundAlreadyStartedException  # pylint: disable=W0707
            except ImageNotFoundException:
                pass
            logger.error("Failed to start round")
            raise ActionFailedException("Could not start the round") from error

    def get_health(self) -> int:
        """Gets the player's health (using ocr)"""
        return grab_int((180, 20, 110, 60))

    def get_money(self) -> int:
        """Gets the player's money (using ocr)"""
        return grab_int((490, 20, 270, 60))

    def place_monkey(self, monkey: BaseMonkey, position: tuple[int, int]):
        """Place a monkey on the map"""
        # if not monkey.can_afford(self.get_money()):
        #     raise ActionFailedException("Insufficient funds")

        x, y = position
        pyautogui.click(x, y)
        keyboard.press_and_release(monkey.hotkey)
        pyautogui.click(x, y)
        try:
            pyautogui.locateOnScreen(CANCEL_PLACEMENT)
            raise ActionFailedException("Failed to place monkey")
        except ImageNotFoundException:
            monkey.position = (x, y)

    def upgrade_monkey(self, monkey: BaseMonkey, path: UpgradePath):
        """Upgrades a monkey"""
        if not monkey.can_upgrade(path, self.get_money()):
            raise UpgradeException("Monkey not upgradable")
        if monkey.position is None:
            raise ActionFailedException("Monkey is not placed")

        x, y = monkey.position
        pyautogui.click(x, y)
        keyboard.press_and_release(UPGRADE_HOTKEYS[path])
        monkey.increment_upgrade(path)
        pyautogui.click(x, y)
