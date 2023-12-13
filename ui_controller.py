"""BloonsTD6 UI control"""

# Standard
import logging

# Third Party
import pyautogui
from pyautogui import ImageNotFoundException

# Local
from constants import ROUND_START, ENABLE_FAST_FORWARD, DISABLE_FAST_FORWARD
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


