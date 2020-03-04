import BSTIterative
import AVLIterative
import RandomArray


bt = BSTIterative.BST()
at = AVLIterative.AVL()

arraylength = 10000

l = RandomArray.getRandomArray(arraylength)

print("Processing random case")

for i in range(len(l)):
    bt.insertIter(l[i])
    at.insertIter(l[i])

print("BST level traversals: ", bt.traversecount)
print("AVL level traversals: ", at.traversecount)
print("Done")

bt = BSTIterative.BST()
at = AVLIterative.AVL()

print("Processing worst case")

for i in range(arraylength):
    bt.insertIter(i)
    at.insertIter(i)

print("BST level traversals: ", bt.traversecount)
print("AVL level traversals: ", at.traversecount)
print("Done")
