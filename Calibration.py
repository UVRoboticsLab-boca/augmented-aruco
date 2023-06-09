import numpy as np
import cv2
import glob


class Calibration():
    
    def generate_images():
        cap = cv2.VideoCapture(1) # default camera is 0
        num = 0

        while cap.isOpened():

            success, img = cap.read()

            k = cv2.waitKey(5)

            if k == 27:
                break
            elif k == ord('s'):
                cv2.imwrite('calibration/img' + str(num) + '.png', img)
                print("image saved!")
                num += 1

            cv2.imshow("chessboard", img)

        cap.release()

        cv2.destroyAllWindows()

        return glob.glob('calibration/*.png')
    
    def calibrate(frame_size, chessboard_size):
        criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        object_points = np.zeros(
            (chessboard_size[0] * chessboard_size[1], 3), np.float32)
        object_points[:, :2] = np.mgrid[0:chessboard_size[0],
                                        0:chessboard_size[1]].T.reshape(-1, 2)

        points_3d = []
        points_2d = []

        images = glob.glob('calibration/*.png')

        if not images:
            images = Calibration.generate_images()

        for image in images:
            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            ret, corners = cv2.findChessboardCorners(
                gray, chessboard_size, None)

            if ret == True:
                points_3d.append(object_points)
                corners2 = cv2.cornerSubPix(
                    gray, corners, (11, 11), (-1, -1), criteria)
                points_2d.append(corners)

                cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)

        ret, camera_matrix, dist, rvecs, tvecs = cv2.calibrateCamera(points_3d, points_2d, frame_size, None, None)
        return camera_matrix, dist