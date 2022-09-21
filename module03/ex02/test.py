import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print (arr2)
print(spb.crop(arr1, (3,1),(1,0)))

print(spb.thin(arr2,3,0))
#Output :
# array([[ 5] 
# [10]
# [15]])

