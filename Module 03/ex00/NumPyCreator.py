from typing import Iterable
import numpy


class NumPyCreator():
    def from_list(self, lst, dtype=None):
        """
            takes a list or nested lists and returns its corresponding Numpy array
        """
        if (not isinstance(lst, list)):
            return None
        it = iter(lst)
        the_len = len(next(it))
        if not all(len(el) == the_len for el in it):
            return None
        return numpy.array(lst, dtype=dtype)

    def from_tuple(self, tpl, dtype=None):
        """
            takes a tuple or nested tuples and returns its corresponding Numpy array
        """
        if (not isinstance(tpl, tuple)):
            return None
        return numpy.array(tpl, dtype=dtype)

    def from_iterable(self, itr, dtype=None):
        """
            takes a iterable and returns its corresponding Numpy array
        """
        if (not isinstance(itr, Iterable)):
            return None
        return numpy.fromiter(itr, dtype=dtype)

    def from_shape(self, shape, value=0, dtype=None):
        """
            returns an array filled with the same value.
            The first argument is a tuple which specifies the shape of the array, and the second
            argument specifies the value of the element
        """
        return numpy.full(shape, value, dtype)

    def random(self, shape, dtype=None):
        """
            returns an array filled with random values. It takes as an
            argument a tuple which specifies the shape of the array.
        """
        return numpy.random.randn(10, 10).astype(dtype)

    def identity(self, n, dtype=None):
        """
            returns an array representing the identity matrix of size n.
        """
        return numpy.identity(n, dtype)


npc = NumPyCreator()
lst = [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]
numpyArray = npc.from_list(lst)
numpyArrayTyped = npc.from_list(lst, int)

print(numpyArray, numpyArray.dtype)
print(numpyArrayTyped, numpyArrayTyped.dtype)

tpl = ((1., 0., 0.), (0., 1., 0.), (0., 0., 1.))
numpyArray = npc.from_tuple(tpl)
numpyArrayTyped = npc.from_tuple(tpl, int)

print(numpyArray, numpyArray.dtype)
print(numpyArrayTyped, numpyArrayTyped.dtype)

numpyArray = npc.from_iterable((x*x for x in range(5)))
numpyArrayTyped = npc.from_iterable((x*x for x in range(5)), int)

print(numpyArray, numpyArray.dtype)
print(numpyArrayTyped, numpyArrayTyped.dtype)

numpyArray = npc.from_shape((5, 5), 5)
numpyArrayTyped = npc.from_shape((5, 5), 5, float)

print(numpyArray, numpyArray.dtype)
print(numpyArrayTyped, numpyArrayTyped.dtype)

numpyArray = npc.random((5, 5))
numpyArrayTyped = npc.random((5, 5), int)

print(numpyArray, numpyArray.dtype)
print(numpyArrayTyped, numpyArrayTyped.dtype)

numpyArray = npc.identity(5)
numpyArrayTyped = npc.identity(5, int)

print(numpyArray, numpyArray.dtype)
print(numpyArrayTyped, numpyArrayTyped.dtype)


print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
# Output : array([[1, 2, 3],[6, 3, 4]])
print(npc.from_list([[1, 2, 3], [6, 4]]))
# Output :None
print(npc.from_list([[1, 2, 3], ["a", "b", "c"], [6, 4, 7]]))
# Output :array([[’1’,’2’,’3’],[’a’,’b’,’c’],[’6’,’4’,’7’], dtype=’<U21’])
print(npc.from_list(((1, 2), (3, 4))))
# Output :None
print(npc.from_tuple(("a", "b", "c")))
# Output :array([’a’, ’b’, ’c’])
print(npc.from_tuple(["a", "b", "c"]))
# Output :None
print(npc.from_iterable(range(5)))
# Output :array([0, 1, 2, 3, 4])
shape = (3, 5)
print(npc.from_shape(shape))
# Output :array([[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]])
print(npc.random(shape))
# Output :
# array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
# [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
# [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
print(npc.identity(4))
# Output :
# array([[1., 0., 0., 0.],
# [0., 1., 0., 0.],
# [0., 0., 1., 0.],
# [0., 0., 0., 1.]])
