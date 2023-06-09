# Augmented Reality script with ArUco markers

This script detects ArUco markers and creates different figures depending on marker id. 
It includes a Calibration class with two methods, the first one uses a chessboard to calibrate and get camera's distorsion value and its matrix, the second one takes photos of the chessboard on different transformations. If calibration folder is empty, automaticaly starts the capture.

It is a generalized version so it should work with any camera resolution.

TODO:
- Export camera matrix and distortion value on a file.
- A validation for such file, if it doesn't exist, must run Calibration methods.
- A dictionary, array or something that connects the marker id with a figure
- A graphication function
- Image augmentation

Used python and packages versions:
- python 3.9.12
- opencv-python 4.6.0.66
- opencv-contrib-python 4.6..0.72
- numpy 1.21.5
- glob2 0.7