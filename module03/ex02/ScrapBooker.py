import numpy as np

class ScrapBooker():
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """

        # assert (isinstance(array, np.ndarray)), "Parameter should be a numpy.ndarray"
        # assert (isinstance(dim, tuple)) and len(dim) == 2 and all(isinstance(x, int) for x in dim), "dim should be a tuple of 2 integers"
        # assert (isinstance(position, tuple)) and len(position) == 2 and all(isinstance(x, int) for x in position), "Parameter should be a tuple of 2 integers"

        if not isinstance(array, np.ndarray):
            return None
        elif not isinstance(dim, tuple) or len(dim) != 2 or not all(isinstance(x, int) for x in dim):
            return None
        elif not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(x, int) for x in position):
            return None
        

        if (position[0] + dim[0] > array.shape[0] or position[1] + dim[1] > array.shape[1]):
            return None
        new_arr = array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
        return new_arr

            
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """


        if not isinstance(array, np.ndarray):
            return None
        elif not isinstance(n, int) or n < 0:
            return None
        elif not isinstance(axis, int) or axis < 0:
            return None

        if (axis == 0 and n >= array.shape[0]):
            return None
        elif (axis == 1 and n >= array.shape[1]):
            return None
        if (axis == 0):
            new_arr = np.delete(array, np.s_[n-1::n], axis=1)
        elif (axis == 1):
            new_arr = np.delete(array, np.s_[n-1::n], axis=0)
        return new_arr            


    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        elif not isinstance(n, int) or n < 0:
            return None
        elif not isinstance(axis, int) or axis != 0 and axis != 1:
            return None

        new_arr = np.concatenate([array for i in range(n)], axis=axis)
        return new_arr
        # ... your code ...
    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dim, tuple) or len(dim) != 2 or not all(isinstance(x, (int, float)) for x in dim):
            return None

        new_arr = np.tile(array, dim)
        return new_arr