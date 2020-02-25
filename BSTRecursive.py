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

    def deleteRec(self, val):
        if self.root:
            self.__deleteRecHelper(val, self.root)

    def __deleteRecHelper(self, val, cur):
        if cur.left and cur.left.val == val:
            if cur.left.left and cur.left.right:
                cur.left.val = self.__findMaxRecHelper(cur.left.left).val
                self.__deleteRecHelper(cur.left.val, cur.left)
            elif cur.left.left:
                cur.left = cur.left.left
            elif cur.left.right:
                cur.left = cur.left.right
            else:
                cur.left = None
        elif cur.right and cur.right.val == val:
            if cur.right.left and cur.right.right:
                cur.right.val = self.__findMaxRecHelper(cur.right.left).val
                self.__deleteRecHelper(cur.right.val, cur.right)
            elif cur.right.left:
                cur.right = cur.right.left
            elif cur.right.right:
                cur.right = cur.right.right
            else:
                cur.right = None
        elif cur == self.root and self.root.val == val:
            if self.root.left and self.root.right:
                self.root.val = self.__findMaxRecHelper(self.root.left).val
                self.__deleteRecHelper(self.root.val, cur)
            elif self.root.left:
                self.root = self.root.left
            elif self.root.right:
                self.root = self.root.right
            else:
                self.root = None
        elif cur.left and val <= cur.val:
            self.__deleteRecHelper(val, cur.left)
        elif cur.right and val > cur.val:
            self.__deleteRecHelper(val, cur.right)

    def findNextRec(self, val):
        return self.__findNextRecHelper(val, self.root).val

    def __findNextRecHelper(self, val, cur):
        if cur is None:
            return None
        if cur.val <= val:
            return self.__findNextRecHelper(val, cur.right)
        child = self.__findNextRecHelper(val, cur.left)
        if child and child.val < cur.val:
            return child
        return cur

    def findPrevRec(self, val):
        return self.__findPrevRecHelper(val, self.root).val

    def __findPrevRecHelper(self, val, cur):
        if cur is None:
            return None
        if cur.val >= val:
            return self.__findPrevRecHelper(val, cur.left)
        child = self.__findPrevRecHelper(val, cur.right)
        if child and child.val > cur.val:
            return child
        return cur

    def findMinRec(self):
        if self.root:
            return self.__findMinRecHelper(self.root).val
        return None

    def __findMinRecHelper(self, cur):
        if cur.left:
            return self.__findMinRecHelper(cur.left)
        return cur

    def findMaxRec(self):
        if self.root:
            return self.__findMaxRecHelper(self.root).val
        return None

    def __findMaxRecHelper(self, cur):
        if cur.right:
            return self.__findMaxRecHelper(cur.right)
        return cur


b = BST()
b.insertRec(5)
b.insertRec(12)
b.insertRec(33)
b.insertRec(14)
b.insertRec(6)
b.insertRec(3)
b.insertRec(41)
b.insertRec(30)
b.insertRec(9)
b.insertRec(18)

b.deleteRec(33)
b.deleteRec(5)
b.deleteRec(18)

print(b.findMaxRec())
print(b.findMinRec())
print(b.findNextRec(14))
print(b.findPrevRec(14))
