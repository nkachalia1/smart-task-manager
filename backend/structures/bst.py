class TreeNode:
    def __init__(self, priority, task):
        self.priority = priority
        self.tasks = [task]
        self.left = None
        self.right = None

class PriorityBST:
    def insert(self, root, priority, task):
        if not root:
            return TreeNode(priority, task)
        if priority < root.priority:
            root.left = self.insert(root.left, priority, task)
        elif priority > root.priority:
            root.right = self.insert(root.right, priority, task)
        else:
            root.tasks.append(task)
        return root
