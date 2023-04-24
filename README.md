# CandyCounter

# *End of semester project for Introduction to Image Processing*


## General Information
 * The main goal of CandyCounter is to process an image of different coloured candies on white background and return number of candies in each defined colour.
 * Application uses standard image processing techniques to extract contours of colored candies and count them.
 * Counting operation order:
   * Blur image to remove image noise
   * Change colour space from RGB to HSV in order to acces information of colour separeted from brightness and intensity
   * Threshold image using inRange() method, range of thresholding depends on colour
   * Find contours of candies of choosen colour
   * Iterate over detected contours to determine if their size is big enough.

## Usage

### inRangeSearching.py

This file allows you to use trackbars to find adequate parameters of detection for every colour. Use 'a' and 'd' keys to navigate between images. Press 'q' to close windows with preview and save parameters to .json file. Application will show you how many candies are detected on displayed image as program runs.

### Colors.py

It's enum class for storing defined colours. You can simply add more colours if you like. The main detection method iterate over this class to find candies in all defined colours.

### Detect.py

There are defined methods of counting candies depending on provided parameters defining colour and path to image in string format. Method detect use Colors enum class to count all candies and return dictionary of detected candies.

### main.py

Script to run detect method on list of test images. It iterate over all images in defined directory and count candies found on them.