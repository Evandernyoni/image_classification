# import necesssary packages 
import numpy as np 
import cv2
import os 


class SimpleDatasetLoader():
    """ For loading and preprocessing data 
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
        """ store/save the image preprocessors 

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
        """loads the image and exracts the class label.

        Parameters
        ----------
        data: list
            list of image paths  
        labels: list
              list of image labels
        imagePaths: list
                   specifies the file paths to the images in the dataset
        Return
        ------
        a tuple of the data and labels
        
        """ 
        data = []
        labels = []

        # loop ove the input images
        for (i, imagePaths) in enumerate(imagePaths):
            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]

            # verify that the preprocessor != None
            if self.preprocessors is not None:
                # loop over the preprocessors and apply each to the image
                for pros in self.preprocessors:
                    image = pros.preprocess(image)
                
            # update the data list and labels list
            data.append(image)
            labels.append(label)
        
            # show an update every 'verbose' images
            if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                print("[INFO] processed {}/{}".format(i+1, len(imagePaths)))
    
        # return a tuple of the data and labels
        return (np.array(data), np.array(labels))




