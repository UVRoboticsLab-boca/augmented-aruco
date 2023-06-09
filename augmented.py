import cv2
import numpy as np
from Calibration import Calibration
from cv2 import aruco

def draw_prism(frame):
    pass

marker_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50) # load ArUco dictionary
param_markers = aruco.DetectorParameters() # parameters for aruco marker detection

cap = cv2.VideoCapture(1) # default camera = 0
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

matrix, dist = Calibration.calibrate((width, height), (9, 6))

print(matrix)
print(dist)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, reject = aruco.detectMarkers(gray, marker_dict, parameters=param_markers)#, cameraMatrix=matrix, distCoeff=dist)
    if corners:
        for i in range(len(ids)):
            rvec, tvec, marker_points = aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix, dist)

            (rvec - tvec).any()

            aruco.drawDetectedMarkers(frame, corners)

            cv2.drawFrameAxes(frame, matrix, dist, rvec, tvec, 0.01)

            augmented_frame = draw_prism(frame)


            # requires more work
    cv2.imshow('aruco detector', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()