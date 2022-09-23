from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load('42AI.png')
    cf = ColorFilter()
    # arr = cf.invert(arr)
    imp.display(cf.invert(arr))
    imp.display(cf.to_blue(arr))
    imp.display(cf.to_green(arr))
    imp.display(cf.to_red(arr))
    imp.display(cf.to_celluloid(arr))
    imp.display(cf.to_grayscale(arr, 'mean'))
    # arr = cf.to_grayscale(arr, 'weight', weights=[1, 1, 1])
    # imp.display(arr)