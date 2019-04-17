
# import the necessary packages

import cv2


class SimplePreprocessor():
    """ This class handles image preprocessing by resizing the image, ignoring the aspect ratio.
    ....

    Attributes
    ----------
    width: The target width of our input image after resizing.
    height: The target height of our input image after resizing.
    inter: An optional parameter used to control which interpolation algorithm is used when resizing.
    image: The input image to be preprocessed.

    Methods
    -------
    preprocess()
              resizes the image to specific size while ignoring aspect ratio
    
    """
    
    def __init__(self, width, height, inter = cv2.INTER_AREA):
        """ save the target image width, height and interpolation method to be used when resizing 
        width: int
             width of our input image after resizing
        height: int
              height of our input image after resizing

        """
        self.width = width
        self.height = height
        self. inter = inter 
    
    def preprocess(self, image):
        """ resize the image to a set size 
        Parameters
        ----------
        image: str
             image path

        Return
        ------
        image: 
             resized image
        """
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)
