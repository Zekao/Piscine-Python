import numpy as np
from collections.abc import Iterable as iter

class NumPyCreator():
    def __init__(self):
        pass
    
    def from_list(self, lst):
        assert (isinstance(lst, list)), "Parameter should be a list"
        return (np.array(lst))

    def from_tuple(self, tpl):
        assert (isinstance(tpl, tuple)), "Parameter should be a tuple"
        return (np.array(tpl))

    def from_iterable(self, itr):
        assert (isinstance(itr, iter)), "Parameter should be an iterable"
        return (np.array(itr))

    def from_shape(self, shape, value):
        assert (isinstance(shape, tuple)), "First parameter should be a tuple"
        assert (isinstance(value, (int, float))), "Second parameter should be a scalar"
        return (np.full(shape, value))

    def random(self, shape):
        assert (isinstance(shape, tuple)), "Parameter should be a tuple"
        return (np.random.rand(*shape))
        # return (np.random.rand(shape))

# create a main function
def main():
    npc = NumPyCreator()
    tuple1 = ([8, 4, 6], [1, 2, 3])
    print('------------------ from_tuple ------------------')
    print(type(tuple1))
    print('Type (numpy array)')
    print(type(npc.from_tuple(tuple1)))
    print(npc.from_tuple(tuple1))
    print('------------------ from_list ------------------')
    list1 = [8, 4, 6, 1, 2, 3]
    print(type(list1))
    print(list1)
    print('Type (numpy array)')
    print(type(npc.from_list(list1)))
    print(npc.from_list(list1))

    print('------------------ from_iterable ------------------')
    it = ['I', ' ', 'a', 'm', ' ', 'a', ' ', 'c', 'o', 'w']
    it2 = ([8, 4, 6], [1, 2, 3])
    print('test 1')
    print(type(it))
    print(type(npc.from_iterable(it)))
    print(npc.from_iterable(it))
    print('test 2')
    print(type(it2))
    print(type(npc.from_iterable(it2)))
    print(npc.from_iterable(it2))

    print('------------------ from_shape ------------------')
    print(npc.from_shape((0, 0), 2))
    print(npc.from_shape((1, 2), 42))
    print(npc.from_shape((2, 2), 42))
    print(npc.from_shape((2, 2), 42))

    print('------------------ random ------------------')
    print(npc.random((1, 2)))
    print(npc.random((2, 1)))
    print(npc.random((6, 2)))

if __name__ == "__main__":
    main()