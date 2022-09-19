from ImageProcessor import ImageProcessor
import sys
imp = ImageProcessor()
# arr = imp.load('42AI.png')
arr = imp.load(sys.argv[1])
print(imp.display(arr))