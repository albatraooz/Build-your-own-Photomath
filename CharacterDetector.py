from typing import Iterable, List, Tuple

import cv2 as cv
import numpy as np

def detect_characters_in_image(image: np.ndarray) -> Iterable[List[np.ndarray], Iterable[Tuple[Tuple[int, int], Tuple[int, int]]]]:
    """Receives an image in a form of a numpy array and for each detected
    character returns its coordinates, and a cropped image (cropped up to its bounding box)

    Parameters
    ----------
    image : np.ndarray
        an image that contains mathematical expression

    Returns
    -------
    Iterable: Iterable[List[np.ndarray], Iterable[Tuple[Tuple[int, int], Tuple[int, int]]]]
        a list of cropped images
        a list of coordinates for every cropped image where every tuple contains the starting and the ending coordinates
        of rectangle
    """

    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(image_gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)

    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])

    cropped_images = []
    coordinates = []

    for i in range(0, len(contours)):
        starting_point = (int(boundRect[i][0]), int(boundRect[i][1]))
        ending_point = (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3]))

        coordinates.append((starting_point, ending_point))

        image_of_one_sign = image[int(boundRect[i][1]) : int(boundRect[i][1]+boundRect[i][3]),
            int(boundRect[i][0]) : int(boundRect[i][0]+boundRect[i][2])]

        cropped_images.append(image_of_one_sign)

    # slicing due to omiting outer frame
    return coordinates[1:], cropped_images[1:]
