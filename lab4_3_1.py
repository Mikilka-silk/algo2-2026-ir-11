class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1

class RBPriorityQueue:
    def __init__(self):
        self.nil = Node(None, 0)
        self.nil.color = 0
        self.root = self.nil

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _insert_fix(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1 
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def _delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right 
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self._right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self._left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def _get_max(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _del_node_helper(self, node, key_node):
        z = self.nil
        while node != self.nil:
            if node == key_node:
                z = node
                break
            if key_node.priority >= node.priority:
                node = node.left
            else:
                node = node.right

        if z == self.nil:
            return

        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._get_max(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 0:
            self._delete_fix(x)

    def insert(self, value, priority):
        node = Node(value, priority)
        node.parent = None
        node.left = self.nil
        node.right = self.nil
        node.color = 1

        y = None
        x = self.root

        while x != self.nil:
            y = x
            if node.priority >= x.priority:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.priority >= y.priority:
            y.left = node
        else:
            y.right = node
        
        if node.parent == None:
            node.color = 0
            return
        
        if node.parent.parent == None:
            return
        
        self._insert_fix(node)

    def peek(self):
        if self.root == self.nil:
            return None
        max_node = self._get_max(self.root)
        return (max_node.value, max_node.priority)

    def extract_max(self):
        if self.root == self.nil:
            return None
        max_node = self._get_max(self.root)
        
        val, prio = max_node.value, max_node.priority
        self._del_node_helper(self.root, max_node)
        return (val, prio)
