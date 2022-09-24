from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load('elon_canaGAN.png')
    cf = ColorFilter()
    imp.display(cf.invert(arr))
    imp.display(cf.to_blue(arr))
    imp.display(cf.to_green(arr))
    imp.display(cf.to_red(arr))
    imp.display(cf.to_celluloid(arr))
    imp.display(cf.to_grayscale(arr, 'mean'))
    imp.display(cf.to_grayscale(arr, 'weight', weights=[0.2, 0.3, 0.5]))