from NumPyCreator import NumPyCreator

npc = NumPyCreator()
lst = [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]
numpyArray = npc.from_list(lst)
numpyArrayTyped = npc.from_list(lst, int)

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

print(npc.from_list([[],[]]))
print(npc.from_list([[1,2,3],[6,3,4],[8,5,6]]))
print(npc.from_tuple(("a","b","c")))
print(npc.from_iterable(range(5)))
print(npc.from_shape((0, 0)))
print(npc.from_shape((3, 5)))
print(npc.random((3, 5)))
print(npc.identity(4))

print(npc.from_list("toto"))
print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
print(npc.from_tuple(3.2))
print(npc.from_tuple(((1,5,8),(7,5))))
print(npc.from_shape((-1, -1)))
print(npc.identity(-1))