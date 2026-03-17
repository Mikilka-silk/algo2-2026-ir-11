class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print_tree(self):
        canvas = [[" "] * 100 for _ in range(40)]
        
        def draw(node, r, c, dir_x, h_step, v_step):
            if not node: return
            
            for i, char in enumerate(str(node.value)):
                canvas[r][c + i] = char
            
            if node.left:
                canvas[r - max(1, v_step // 2)][c + (dir_x * h_step) // 2] = "\\" if dir_x == -1 else "/"
                draw(node.left, r - v_step, c + dir_x * h_step, dir_x, max(2, h_step - 2), max(2, v_step // 2))
                
            if node.right:
                canvas[r + max(1, v_step // 2)][c + (dir_x * h_step) // 2] = "/" if dir_x == -1 else "\\"
                draw(node.right, r + v_step, c + dir_x * h_step, dir_x, max(2, h_step - 2), max(2, v_step // 2))

        root_r = 18
        canvas[root_r][40] = str(self.value)
        
        if self.left:
            canvas[root_r][36:39] = ["-", "-", "-"]
            draw(self.left, root_r, 34, -1, 6, 8)
            
        if self.right:
            canvas[root_r][42:45] = ["-", "-", "-"]
            draw(self.right, root_r, 46, 1, 6, 8)

        for row in canvas:
            line = "".join(row).rstrip()
            if line: print(line)

def build_from_list(arr):
    if not arr or arr[0] in ("N", None):
        return None
    
    root = BinaryTree(int(arr[0]))
    queue = [root]
    
    i = 1
    
    while queue and i < len(arr):
        current = queue.pop(0)
        
        if i < len(arr) and arr[i] not in ("N", None):
            current.left = BinaryTree(int(arr[i]))
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] not in ("N", None):
            current.right = BinaryTree(int(arr[i]))
            queue.append(current.right)
        i += 1

    return root

def main():
    #tree_list = [1, 2, 3, "N", "N", 4, 5]
    tree_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(f"Дані для дерева: {tree_list}\n")
    
    root = build_from_list(tree_list)
    
    if root:
        root.print_tree()
    else:
        print("Дерево порожнє")

if __name__ == "__main__":
    main()
