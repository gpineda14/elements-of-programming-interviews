def tree_traversal(root):
    if root:
        print('Preorder: %d' % root.data)
        tree_traversal(root.left)

        print('Inorder: %d' % root.data)
        tree_traversal(root.right)

        print('Postorder: %d' % root.data)
