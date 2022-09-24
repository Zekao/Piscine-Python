import numpy as np

class ColorFilter():
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (isinstance(array, np.ndarray) and len(array.shape) == 3):
            copy = np.array(array)
            for i in range(3):
                copy[:, :, i] = 1 - copy[:, :, i]
            return copy
        return None

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (isinstance(array, np.ndarray) and len(array.shape) == 3):
            copy = np.array(array)
            for i in range(2):
                copy[:, :, i] = 0
            return copy
        return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """

        if (isinstance(array, np.ndarray) and len(array.shape) == 3):
            copy = np.array(array)
            for i in (0, 2):
                copy[:, :, i] = 0
            return copy
        return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """

        if (isinstance(array, np.ndarray) and len(array.shape) == 3):
            copy = np.array(array)
            for i in (1, 2):
                copy[:, :, i] = 0
            return copy
        return None

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """

        if (isinstance(array, np.ndarray) and len(array.shape) == 3):
            copy = np.array(array)
            values = np.linspace(0, 1, 5)
            for color in values:
                copy[array >= color] = color
            return copy
        return None

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = `mean`/`m`: performs the mean of RBG channels.
        For filter = `weight`/`w`: performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [`m`,`mean`,`w`,`weight`]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (isinstance(array, np.ndarray) and len(array.shape) == 3):
            copy = np.array(array)
            if filter in ['mean', 'm']:
                for row in copy:
                    for pixel in row:
                        pixel[0] = pixel[1] = pixel[2] = pixel.sum() / 3
            elif filter in ['weight', 'w']:
                weight = kwargs['weights']
                for row in copy:
                    for pixel in row:
                        pixel[0] = pixel[1] = pixel[2] = (pixel[:-1] * weight).sum()
            return copy
        return None
