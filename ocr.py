"""OCR functions for capturing money and health"""
# pylint: disable=E1101

# Standard
import logging

# Third Party
import os
import cv2
import pytesseract  # type: ignore
import numpy as np
import pyautogui
import easyocr  # type: ignore

# Local

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------


class OCR:
    """OCR Functions"""

    def __init__(self, filename: str = "default") -> None:
        self.reader = easyocr.Reader(["en"], False)
        self.tesseract_config = "--psm 7"
        self.filename = f"ocr_results_{filename}"
        self._counter = 0

        os.makedirs(self.filename, exist_ok=True)
        with open(f"{self.filename}/results.csv", "w", encoding="UTF-8") as file:
            file.write("id, tess, easy, calc\n")

    def _preprocess_image(self, image):
        # Convert the image to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for white color with a black outline
        lower_white = np.array([0, 0, 0], dtype=np.uint8)
        upper_white = np.array([180, 50, 255], dtype=np.uint8)

        # Create a mask to extract white text with black outline
        mask = cv2.inRange(hsv, lower_white, upper_white)

        # Bitwise-AND to extract the white text
        result = cv2.bitwise_and(image, image, mask=mask)

        # Convert the result to grayscale
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Use adaptive thresholding to enhance text (binary)
        _, thresholded = cv2.threshold(
            blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        # Invert the image to make text black
        inverted = cv2.bitwise_not(thresholded)

        # Use morphological transformations to remove noise
        kernel = np.ones((3, 3), np.uint8)
        processed_image = cv2.morphologyEx(inverted, cv2.MORPH_CLOSE, kernel)

        return processed_image

    def grab_int(self, region: tuple[int, int, int, int], cash: int):
        """Screenshot and OCR an int from the specified region (left, top, width, height)"""
        # Take a screenshot of the specified region using pyautogui
        screenshot = pyautogui.screenshot(region=region)
        screenshot = np.array(screenshot)  # type: ignore

        # Pre-process the image
        preprocessed_image = self._preprocess_image(screenshot)

        # Perform OCR on the preprocessed image, restricting to digits only
        text_tess = pytesseract.image_to_string(
            preprocessed_image, config=self.tesseract_config
        )
        results_easy = self.reader.readtext(preprocessed_image)
        text_easy = "".join(result[1] for result in results_easy)

        # Extract numbers from the recognized text
        number_str_tess = "".join(filter(str.isdigit, text_tess))
        number_str_easy = "".join(filter(str.isdigit, text_easy))

        with open(f"{self.filename}/results.csv", "a", encoding="UTF-8") as file:
            file.write(f"{self._counter},{number_str_tess},{number_str_easy},{cash}\n")
        cv2.imwrite(
            f"{self.filename}/img_p_{self._counter}.png",
            preprocessed_image,
        )
        cv2.imwrite(f"{self.filename}/img_{self._counter}.png", screenshot)
        logger.info("Processed image %i", self._counter)
        self._counter += 1
        # Convert the extracted string to an integer
        try:
            number = int(number_str_easy)
        except ValueError:
            number = -1

        return number
