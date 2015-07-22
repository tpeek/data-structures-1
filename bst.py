class Node(object):
        def __init__(self, val, parent=None, left=None, right=None):
            self.val = val
            self.parent = parent
            self.left = left
            self.right = right

        def __repr__(self):
            return ("Node({self.val}, parent={self.parent},"\
                    "left={self.left}, right={self.right})".format(self=self))


class BST(object):
    def __init__(self, val=None):
        self.size = 0
        self.balence = 0
        if val is not None:
            self.root = Node(val)
            self.size += 1
        else:
            self.root = None

    def insert(self, val):
        """Insert val into BST if not present. Always returns None."""
        if self.root is None:
            self.root = Node(val)
        else:
            new_parent = self._find(val)
            if new_parent.val > val:
                new_parent.left = Node(val, new_parent)
            elif new_parent.val < val:
                new_parent.right = Node(val, new_parent)
            else:
                pass

    def contains(self, val):
        """Return True if val in BST. Else, return False."""
        pass

    def size(self):
        """Return int size of tree. Will return 0 if tree is empty."""
        pass

    def depth(self):
        """Return the int number of levels in the tree.
        Return 0 if tree is empty."""
        pass

    def balance(self):
        """Return the difference between the number of nodes on the left with
        respect to the right side.
        --Negative if more on right
        --Positive if more on left
        --Zero if tree is perfectly balanced"""
        pass

    def _find(self, val):
        """Return a tuple containing (node, side) with target val if it exists,
        otherwise return the would be parent and 1 if it is on the left, -1 if
        it is on the right, 0 if it is the root."""

        def _look(node):
            if node.val > val:
                if node.left is not None:
                    self._find(node.left)
            elif node.val < val:
                if node.right is not None:
                    self._find(node.right)
            return node

        if self.root is not None:
            return _look(self.root)
        else:
            return None


def test_helper():
    A = Node(5)
    B = Node(4, parent=A)
    C = Node(6, parent=A)
    D = Node(3, parent=B)
    E = Node(2, parent=B)
    F = Node(7, parent=C)

    # Backrefs
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F

    return [A, B, C, D, E, F]
