import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageProcessor():

    def __init__(self):
        pass

    def load(self, path):
        try:
            with open(path, 'r') as f:
                img = mpimg.imread(path)
                print("Loading image of dimensions {} x {}".format(img.shape[0], img.shape[1]))
                return img
        except Exception as e:
            print('Error: unable to open file ' + path + '\n' + str(e))

    def display(self, img):
        try:
            imgplot = plt.imshow(img)
        except:
            print('Error: unable to display image')
            return None
        plt.show()