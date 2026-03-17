class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.__value = value
        self.__left = left
        self.__right = right
        self.__parent = parent

    def get_value(self):
        return self.__value

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_parent(self):
        return self.__parent

    def set_left(self, node):
        self.__left = node
        if node is not None:
            node.set_parent(self)

    def set_right(self, node):
        self.__right = node
        if node is not None:
            node.set_parent(self)

    def set_parent(self, node):
        self.__parent = node

    def find_successor(self) -> 'BinaryTree':    
        if self.get_right() is not None:
            current = self.get_right()
            while current.get_left() is not None:
                current = current.get_left()
            return current

        current = self
        while current.get_parent() is not None and current.get_parent().get_right() == current:
            current = current.get_parent()

        return current.get_parent()
