import cv2
import numpy as np
from tqdm import tqdm
import json
from pathlib import Path

DIRECTORY = "data"

parameters = {
    "hLow": 0,
    "hHigh": 179,
    "sLow": 0,
    "sHigh": 255,
    "vLow": 0,
    "vHigh": 255,
    "scale": 0.00001
}

def hueMin(val):
    global parameters
    parameters["hLow"] = val
def hueMax(val):
    global parameters
    parameters["hHigh"] = val
def saturationMin(val):
    global parameters
    parameters["sLow"] = val
def saturationMax(val):
    global parameters
    parameters["sHigh"] = val
def valueMin(val):
    global parameters
    parameters["vLow"] = val
def valueMax(val):
    global parameters
    parameters["vHigh"] = val
def scale(val):
    global parameters
    parameters["scale"] = 1 / val


if __name__ == "__main__":
    directory = DIRECTORY
    img_list = Path(directory).glob('*.jpg')

    images = []
    print("Data reading")
    for img_path in tqdm(sorted(img_list)):
        images.append(cv2.imread(str(img_path)))

    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("hLow", "Trackbars", 0, 179, hueMin)
    cv2.createTrackbar("hHigh", "Trackbars", 179, 179, hueMax)
    cv2.createTrackbar("sLow", "Trackbars", 0, 255, saturationMin)
    cv2.createTrackbar("sHigh", "Trackbars", 255, 255, saturationMax)
    cv2.createTrackbar("vLow", "Trackbars", 0, 255, valueMin)
    cv2.createTrackbar("vHigh", "Trackbars", 255, 255, valueMax)
    cv2.createTrackbar("scale", "Trackbars", 100000, 100000, scale)

    i = 0
    while True:
        img = images[i]
        img = cv2.GaussianBlur(img, (5, 5), 0)
        size = img.shape
        hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsvImg, (parameters["hLow"], parameters["sLow"], parameters["vLow"]), (parameters["hHigh"], parameters["sHigh"], parameters["vHigh"]))
        cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        hsvFont = np.uint8([[[(parameters["hLow"] + parameters["hHigh"]) / 2, (parameters["sLow"] + parameters["sHigh"]) / 2, (parameters["vLow"] + parameters["vHigh"]) / 2]]])
        color = cv2.cvtColor(hsvFont, cv2.COLOR_HSV2BGR)
        color = color.flatten()
        color = (float(color[0]), float(color[1]), float(color[2]))
        skittles = 0
        for cnt in cnts:
            area = cv2.contourArea(cnt)
            if area > size[0] * size[1] * parameters["scale"]:
                skittles += 1
        resized = cv2.resize(thresh, (0, 0), fx=800/size[0], fy=800/size[0])
        resizedColor = cv2.resize(img, (0, 0), fx=800/size[0], fy=800/size[0])
        size = resized.shape
        colored = cv2.cvtColor(resized, cv2.COLOR_GRAY2BGRA)
        cv2.putText(colored, f"img: {i} : {skittles}", (10, size[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 5)
        cv2.imshow("detection", colored)
        cv2.imshow("original", resizedColor)
        key = cv2.waitKey(10)

        if key == ord('a'):
            i -= 1
        if key == ord('d'):
            i += 1
        if i < 0:
            i = 39
        if i > 39:
            i = 0
        if key == ord('q'):
            with open("Result.json", 'w') as ofp:
                json.dump(parameters, ofp, indent=4)
            break
