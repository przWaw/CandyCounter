# CandyCounter

## End of semester project for Introduction to Image Processing

### General Information
* Main purpose of CandyCounter is counting colored candies on provided image with white background.
* Application uses standard image processing methods to separate candies into colors and count theme
* Chain of operations
  * Blur image to reduce noise
  * Shift to HSV color space from RGB to separate information about color from brightness and intensity
  * Threshold image using range specified for chosen color
  * Find contours of candies in separated color
  * check size of contour relative to size of image

### Used technologies

* Python 3.10
* OpenCv
* NumPy
* tqdm

## Usage

### InRangeSearching.py

Program to find range of each color in HSV color space. To navigate through images use "a" and "d" keys. Use trackbars to change range of detection threshold. Press "q" to end work and save parameters into .json file.

### Colors.py

Enum class storing values for detection of all defined colors.

### Detect.py

File containing method to count candies of all defined colors from image provided as path to image. Returns dictionary of number of candies in each color.

### TestGroup.py

File to test detection on test images. Iterate over all images in given directory and prints results.
