# import necesssary packages 
import numpy as np 
import cv2
import os 


class SimpleDatasetLoader():
    """ 
    
    
    Attributes
    ----------
    preprocessors:
    imagePaths: list specifying the file paths to the images in our dataset

    Methods
    --------
    load()
         loads the image and exracts the class label.
    """

    def __init__(self, preprocessors=None):
        """ store the image preprocessor 
        Parametrs
        ---------
        preprocessors: list
                     file paths to the images in our dataset
        
                      
        """
        self.preprocessors = preprocessors
        # if the preprocessors are None, initialize them as an empty list
        if self.preprocessors is None:
            self.preprocessors = []
    
    def load(self, imagePaths, verbose=-1):
        """initialize the list of features and labels
        Parameters
        ----------
        data: list
            list of image paths  
        labels: list
              list of image labels
        imagePaths: list
                   specifies the file paths to the images in the dataset
              
        """ 
        data = []
        labels = []

        # loop ove the input images
        for (i, imagePaths) in enumerate(imagePaths):
            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]

