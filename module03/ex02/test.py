import numpy as np
from ScrapBooker import ScrapBooker


### # 03.02.00


spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))

# Output:

# array([[ 5],
#       [10],
#       [15]])




### # 03.02.01

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2,3,0))

# Output :

# array([['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')




### # 03.02.02

arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
print(spb.thin(arr3,3,1))

# Output : 

# array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
#       ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
#       ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
#       ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
#       ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']], dtype='<U1')




### # 03.02.03

arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(spb.juxtapose(arr4, 2, 0))

# Output :

# array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9],
#       [1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(spb.mosaic(arr4, (2, 2)))
# Output :
# array([[1 2 3 1 2 3]
#  [4 5 6 4 5 6]
#  [7 8 9 7 8 9]
#  [1 2 3 1 2 3]
#  [4 5 6 4 5 6]
#  [7 8 9 7 8 9]])