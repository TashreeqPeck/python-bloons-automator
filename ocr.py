"""OCR functions for capturing money and health"""
# pylint: disable=E1101

# Standard

# Third Party
import cv2
import pytesseract  # type: ignore
import numpy as np
import pyautogui

# Local


def _preprocess_image(image):
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
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Invert the image to make text white
    inverted = cv2.bitwise_not(thresholded)

    # Use morphological transformations to remove noise
    kernel = np.ones((3, 3), np.uint8)
    processed_image = cv2.morphologyEx(inverted, cv2.MORPH_CLOSE, kernel)

    return processed_image


def grab_int(region: tuple[int, int, int, int]):
    """Screenshot and OCR an int from the specified region (left, top, width, height)"""
    # Take a screenshot of the specified region using pyautogui
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)  # type: ignore

    cv2.imwrite("screenshot.png", screenshot)
    # Pre-process the image
    preprocessed_image = _preprocess_image(screenshot)

    # Save the preprocessed image to a file (optional)
    cv2.imwrite("screenshot_pre.png", preprocessed_image)

    # Perform OCR on the preprocessed image, restricting to digits only
    custom_config = r"--psm 7"
    text = pytesseract.image_to_string(preprocessed_image, config=custom_config)

    # Extract numbers from the recognized text
    number_str = "".join(filter(str.isdigit, text))

    # Convert the extracted string to an integer
    try:
        number = int(number_str)
    except ValueError:
        number = -1

    return number
