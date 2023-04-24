from typing import Dict

import cv2

from Colors import Color


def countCandies(parameters: Dict[str, float or int], img_path: str) -> int:
    """
    Function to count candies of defined color
    :param parameters: Dictionary containing range of color to find
    :param img_path: Path to image to process
    :return: number of candies found in chosen color
    """

    img = cv2.imread(img_path)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    size = img.shape
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsvImg, (parameters["hLow"], parameters["sLow"], parameters["vLow"]),
                         (parameters["hHigh"], parameters["sHigh"], parameters["vHigh"]))
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    candys = 0
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area > size[0] * size[1] * parameters["scale"]:
            candys += 1
    return candys

def detect(img_path: str) -> Dict[str, int]:
    """
    Function to count all candies in all defined colors on given image
    :param img_path: path to image to process
    :return: Dictionary of pairs Color : Number
    """

    countedCandies = {}

    for color in Color:
        countedCandies[color.name] = countCandies(color.value, img_path)

    return countedCandies

