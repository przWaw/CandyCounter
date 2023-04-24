import cv2
from typing import Dict
from Colors import Colors


def countCandies(parameters: Dict[str, float or int], img_path: str) -> int:
    """
    Function to count candies visible on given image.

    Parameters
    ----------
    parameters : Dict
       Dictionary of parameters describing colour of candies to detect
    img_path : str
       Path to processed image.

    Returns
    -------
    int
       Number of candies in choosen colour.
       """

    img = cv2.imread(img_path)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    size = img.shape
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsvImg, (parameters["hLow"], parameters["sLow"], parameters["vLow"]),
                         (parameters["hHigh"], parameters["sHigh"], parameters["vHigh"]))
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    candies = 0
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area > size[0] * size[1] * parameters["scale"]:
            candies += 1
    return candies

def detect(img_path: str) -> Dict[str, int]:
    """Function to detect candies in all defined colours

    Parameters
    ----------
    img_path : str
        Path to processed image.

    Returns
    -------
    Dict[str, int]
        Dictionary with quantity of each defined colour.
    """

    candyNumber = {}

    for color in Colors:
        candyNumber[color.name] = countCandies(color.value, img_path)

    return candyNumber