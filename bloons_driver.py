"""BloonsTD6 UI Driver"""

# Standard
import logging
import time

# Third Party
import pyautogui
from pyautogui import ImageNotFoundException
import keyboard

# Local
from constants import *  # pylint: disable=W0401, W0614
from monkeys.base_monkey import BaseMonkey, UpgradeException
from monkeys.heroes import Hero
from ocr import OCR

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class ActionFailedException(Exception):
    """Exception for failed UI Actions"""


class RoundAlreadyStartedException(ActionFailedException):
    """Exception for round already started"""


class BloonsDriver:
    """Driver for Bloons TD6"""

    def __init__(self, difficulty: Difficulty, ocr_filename: str = "default") -> None:
        self.ocr = OCR(ocr_filename)
        self.round = STARTING_ROUND[difficulty.value]
        self.cash_offset = CUMULATIVE_ROUND_CASH[self.round - 1]

    @property
    def calculated_cash(self):
        """Calculate the expected cash"""
        return CUMULATIVE_ROUND_CASH[self.round - 1] + STARTING_CASH - self.cash_offset

    def _start_round(self, speed_up: bool = False) -> None:
        """Start the round"""
        try:
            x, y = pyautogui.locateCenterOnScreen(ROUND_START, confidence=0.9)  # type: ignore
            pyautogui.click(x, y)
            logger.info("Round started")
            if speed_up:
                try:
                    pyautogui.locateOnScreen(ENABLE_FAST_FORWARD, confidence=0.9)
                    pyautogui.click(x, y)
                    logger.info("Fast forward enabled")
                except ImageNotFoundException:
                    logger.info("Fast forward already enabled")
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

    def complete_round(self):
        """Start the round and wait for it to finish"""
        self._start_round(True)
        self._wait_for_round_end()
        self.round += 1

    def _wait_for_round_end(self):
        """Wait until the round is finished"""
        try:
            pyautogui.locateOnScreen(ROUND_START, confidence=0.9)
            raise ActionFailedException("Round not started")
        except ImageNotFoundException:
            pass
        round_ongoing = True
        logger.info("Waiting for round to end")
        while round_ongoing:
            try:
                pyautogui.locateOnScreen(ROUND_START, confidence=0.9)
                round_ongoing = False
            except ImageNotFoundException:
                time.sleep(1)
        logger.info("Round ended")

    def get_health(self) -> int:
        """Gets the player's health (using ocr)"""
        return self.ocr.grab_int(HEALTH_REGION, self.calculated_cash)

    def get_cash(self) -> int:
        """Gets the player's money (using ocr)"""
        return self.ocr.grab_int(MONEY_REGION, self.calculated_cash)

    def can_afford(self, monkey: BaseMonkey | Hero):
        """Checks if a monkey can be afforded"""
        return monkey.cost < self.get_cash()

    def place_monkey(self, monkey: BaseMonkey | Hero, position: tuple[int, int]):
        """Place a monkey on the map"""
        if self.can_afford(monkey):
            raise ActionFailedException("Insufficient funds")
        if monkey.position is not None:
            raise ActionFailedException("Monkey already placed")
        x, y = position
        pyautogui.click(x, y)
        keyboard.press_and_release(monkey.hotkey)
        time.sleep(0.1)
        pyautogui.click(x, y)
        time.sleep(0.1)
        try:
            pyautogui.locateOnScreen(CANCEL_PLACEMENT, confidence=0.9)
            raise ActionFailedException("Failed to place monkey")
        except ImageNotFoundException:
            monkey.position = (x, y)

        self.cash_offset += monkey.cost
        logger.info("%s placed at (%i, %i)", monkey.__class__.__name__, x, y)

    def can_upgrade(self, monkey: BaseMonkey, path: UpgradePath):
        """Checks if a monkey can upgrade the specified path"""
        return self.can_afford(monkey) and monkey.can_upgrade(path)

    def upgrade_monkey(self, monkey: BaseMonkey, path: UpgradePath):
        """Upgrades a monkey"""
        if not self.can_upgrade(monkey, path):
            raise UpgradeException("Monkey not upgradable")
        if monkey.position is None:
            raise ActionFailedException("Monkey is not placed")

        x, y = monkey.position
        pyautogui.click(x, y)
        keyboard.press_and_release(UPGRADE_HOTKEYS[path])
        self.cash_offset += monkey.next_upgrade_cost(path)
        monkey.increment_upgrade(path)
        pyautogui.click(x, y)
        time.sleep(0.1)  # Wait for box to close

        logger.info(
            "%s at (%i, %i) upgraded %s path",
            monkey.__class__.__name__,
            x,
            y,
            path.name,
        )
