class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insertIter(self, val):
        if self.root:
            cur = self.root
            prev = self.root
            while cur:
                if val < cur.val:
                    prev = cur
                    cur = cur.left
                else:
                    prev = cur
                    cur = cur.right
            if val < prev.val:
                prev.left = node(val)
            else:
                prev.right = node(val)
        else:
            self.root = node(val)

    def deleteIter(self, val):
        if self.root:
            cur = self.root
            prev = self.root
            while cur:
                if cur.val == val:
                    if cur.left and cur.right:
                        cur.val = self.__findMaxIterHelper(cur.left).val
                        val = cur.val
                        prev = cur
                        cur = cur.left
                    elif cur.left:
                        if prev.val < cur.val:
                            prev.right = cur.left
                        else:
                            prev.left = cur.left
                        cur = None
                    elif cur.right:
                        if prev.val < cur.val:
                            prev.right = cur.right
                        else:
                            prev.left = cur.right
                        cur = None
                    else:
                        if prev.val < cur.val:
                            prev.right = None
                        else:
                            prev.left = None
                        cur = None
                elif cur.val < val:
                    prev = cur
                    cur = cur.right
                else:
                    prev = cur
                    cur = cur.left

    def findNextIter(self, val):
        if self.root:
            cur = self.root
            prev = self.root
            max = None
            while cur:
                if cur.val > val:
                    max = cur
                    prev = cur
                    cur = cur.left
                else:
                    prev = cur
                    cur = cur.right
            if max and prev.val > max.val:
                return max.val
            elif prev.val > val:
                return prev.val
            else:
                return max.val
        return None

    def findPrevIter(self, val):
        if self.root:
            cur = self.root
            prev = self.root
            min = None
            while cur:
                if cur.val >= val:
                    prev = cur
                    cur = cur.left
                else:
                    min = cur
                    prev = cur
                    cur = cur.right
            if min and prev.val < min.val:
                return min.val
            elif prev.val < val:
                return prev.val
            else:
                return min.val
        return None

    def findMinIter(self):
        if self.root:
            return self.__findMinIterHelper(self.root).val
        return None

    def __findMinIterHelper(self, start):
        cur = start
        prev = start
        while cur:
            prev = cur
            cur = cur.left
        return prev

    def findMaxIter(self):
        if self.root:
            return self.__findMaxIterHelper(self.root).val
        return None

    def __findMaxIterHelper(self, start):
        cur = start
        prev = start
        while cur:
            prev = cur
            cur = cur.right
        return prev


b = BST()
b.insertIter(5)
b.insertIter(12)
b.insertIter(33)
b.insertIter(14)
b.insertIter(6)
b.insertIter(3)
b.insertIter(41)
b.insertIter(30)
b.insertIter(9)
b.insertIter(18)

b.deleteIter(33)
b.deleteIter(5)
b.deleteIter(18)

print(b.findMaxIter())
print(b.findMinIter())
print(b.findNextIter(14))
print(b.findPrevIter(14))
