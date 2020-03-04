class node:
    def __init__(self, val, left=None, right=None, height=1):
        self.val = val
        self.left = left
        self.right = right
        self.height = height


class AVL:
    def __init__(self):
        self.root = None
        self.traversecount = 0

    def getBalanceFactor(self, n: node):
        if n:
            return self.getHeight(n.left) - self.getHeight(n.right)
        return 0

    def getHeight(self, n: node):
        if n:
            return n.height
        return 0

    def rightR(self, parent: node, leftchildofparent):
        if parent is None:
            temp = self.root.left
            self.root.left = temp.right
            temp.right = self.root
            self.root = temp
            self.root.right.height -= 2
        elif leftchildofparent:
            temp = parent.left.left
            parent.left.left = temp.right
            temp.right = parent.left
            parent.left = temp
            parent.left.right.height -= 2
        else:
            temp = parent.right.left
            parent.right.left = temp.right
            temp.right = parent.right
            parent.right = temp
            parent.right.right.height -= 2

    def leftR(self, parent: node, leftchildofparent):
        if parent is None:
            temp = self.root.right
            self.root.right = temp.left
            temp.left = self.root
            self.root = temp
            self.root.left.height -= 2
        elif leftchildofparent:
            temp = parent.left.right
            parent.left.right = temp.left
            temp.left = parent.left
            parent.left = temp
            parent.left.left.height -= 2
        else:
            temp = parent.right.right
            parent.right.right = temp.left
            temp.left = parent.right
            parent.right = temp
            parent.right.left.height -= 2

    def leftRightR(self, parent, leftchildofparent):
        if parent is None:
            self.leftR(self.root, True)
            self.root.left.left.height += 1  # here to adjust heights during this inbetween rotation
            self.root.left.height += 1
        elif leftchildofparent:
            self.leftR(parent.left, True)
            parent.left.left.left.height += 1
            parent.left.left.height += 1
        else:
            self.leftR(parent.right, True)
            parent.right.left.left.height += 1
            parent.right.left.height += 1
        self.rightR(parent, leftchildofparent)

    def rightLeftR(self, parent, leftchildofparent):
        if parent is None:
            self.rightR(self.root, False)
            self.root.right.right.height += 1  # here to adjust heights during this inbetween rotation
            self.root.right.height += 1
        elif leftchildofparent:
            self.rightR(parent.left, False)
            parent.left.right.right.height += 1
            parent.left.right.height += 1
        else:
            self.rightR(parent.right, False)
            parent.right.right.right.height += 1
            parent.right.right.height += 1
        self.leftR(parent, leftchildofparent)

    def insertIter(self, val):
        ancestors = []
        if self.root:
            cur = self.root
            prev = self.root
            while cur:
                self.traversecount += 1
                ancestors.append(cur)
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

        i = len(ancestors)-1
        while i >= 0:
            ancestors[i].height = 1 + max(self.getHeight(ancestors[i].left), self.getHeight(ancestors[i].right))
            bf = self.getBalanceFactor(ancestors[i])
            parent = None
            leftchildofparent = False
            if i != 0:
                parent = ancestors[i-1]
                if parent.left == ancestors[i]:
                    leftchildofparent = True

            if bf > 1:
                lcbf = self.getBalanceFactor(ancestors[i].left)
                if lcbf >= 0:
                    self.rightR(parent, leftchildofparent)  # right-right case
                else:
                    self.leftRightR(parent, leftchildofparent)  # left-right case
            elif bf < -1:
                rcbf = self.getBalanceFactor(ancestors[i].right)
                if rcbf <= 0:
                    self.leftR(parent, leftchildofparent)  # right-right case
                else:
                    self.rightLeftR(parent, leftchildofparent)  # right-left case
            i -= 1

    def deleteIter(self, val):
        ancestors = []
        deleted = False
        if self.root:
            cur = self.root
            prev = self.root
            while cur:
                self.traversecount += 1
                ancestors.append(cur)
                if cur.val == val:
                    if cur.left and cur.right:
                        cur.val = self.__findMaxIterHelper(cur.left).val
                        val = cur.val
                        prev = cur
                        cur = cur.left
                        deleted = True
                    elif cur.left:
                        if prev.val < cur.val:
                            prev.right = cur.left
                        else:
                            prev.left = cur.left
                        cur = None
                        deleted = True
                    elif cur.right:
                        if prev.val < cur.val:
                            prev.right = cur.right
                        else:
                            prev.left = cur.right
                        cur = None
                        deleted = True
                    else:
                        if prev.val < cur.val:
                            prev.right = None
                        else:
                            prev.left = None
                        cur = None
                        deleted = True
                elif cur.val < val:
                    prev = cur
                    cur = cur.right
                else:
                    prev = cur
                    cur = cur.left

            if deleted:
                i = len(ancestors) - 2  # final element will be deleted one
                while i >= 0:
                    ancestors[i].height = 1 + max(self.getHeight(ancestors[i].left), self.getHeight(ancestors[i].right))
                    bf = self.getBalanceFactor(ancestors[i])
                    parent = None
                    leftchildofparent = False
                    if i != 0:
                        parent = ancestors[i - 1]
                        if parent.left == ancestors[i]:
                            leftchildofparent = True

                    if bf > 1:
                        lcbf = self.getBalanceFactor(ancestors[i].left)
                        if lcbf >= 0:
                            self.rightR(parent, leftchildofparent)  # right-right case
                        else:
                            self.leftRightR(parent, leftchildofparent)  # left-right case
                    elif bf < -1:
                        rcbf = self.getBalanceFactor(ancestors[i].right)
                        if rcbf <= 0:
                            self.leftR(parent, leftchildofparent)  # right-right case
                        else:
                            self.rightLeftR(parent, leftchildofparent)  # right-left case
                    i -= 1

    def findNextIter(self, val):
        if self.root:
            cur = self.root
            prev = self.root
            max = None
            while cur:
                self.traversecount += 1
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
                self.traversecount += 1
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
            self.traversecount += 1
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
            self.traversecount += 1
            prev = cur
            cur = cur.right
        return prev


# b = AVL()
# b.insertIter(5)
# b.insertIter(12)
# b.insertIter(33)
# b.insertIter(14)
# b.insertIter(6)
# b.insertIter(3)
# b.insertIter(41)
# b.insertIter(30)
# b.insertIter(9)
# b.insertIter(18)
# b.insertIter(52)
# b.insertIter(31)
#
# b.deleteIter(3)
# b.deleteIter(33)
# b.deleteIter(5)
# b.deleteIter(18)
#
# print(b.findMaxIter())
# print(b.findMinIter())
# print(b.findNextIter(14))
# print(b.findPrevIter(14))
