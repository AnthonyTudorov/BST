def sort(inlst):
    class node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class BST:
        def __init__(self):
            self.root = None

        def insertRec(self, val):
            if self.root:
                self.__insertRecHelper(val, self.root)
            else:
                self.root = node(val)

        def __insertRecHelper(self, val, cur):
            if val < cur.val:
                if cur.left:
                    self.__insertRecHelper(val, cur.left)
                else:
                    cur.left = node(val)
            else:
                if cur.right:
                    self.__insertRecHelper(val, cur.right)
                else:
                    cur.right = node(val)

        def inOrderTraversal(self, lst):
            self.__inOrderTraversalHelper(lst, self.root)

        def __inOrderTraversalHelper(self, lst, cur):
            if cur:
                self.__inOrderTraversalHelper(lst, cur.left)
                lst.append(cur.val)
                self.__inOrderTraversalHelper(lst, cur.right)

    b = BST()
    for i in inlst:
        b.insertRec(i)
    relst = []
    b.inOrderTraversal(relst)
    return relst


l = [5, 12, 6, 29, 43, 32, 7, 8, 1, 19]
l = sort(l)
print(l)