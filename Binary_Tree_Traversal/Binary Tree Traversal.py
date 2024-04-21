# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    nodes = []
    if node.data:
        nodes.append(node.data)
    if node.left:
        nodes.extend(pre_order(node.left))
    if node.right:
        nodes.extend(pre_order(node.right))
    return nodes

# In-order traversal
def in_order(node):
    if node is None:
        return []
    nodes = []
    if node.left:
        nodes.extend(in_order(node.left))
    if node.data:
        nodes.append(node.data)
    if node.right:
        nodes.extend(in_order(node.right))
    return nodes

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    nodes = []
    if node.left:
        nodes.extend(post_order(node.left))
    if node.right:
        nodes.extend(post_order(node.right))
    if node.data:
        nodes.append(node.data)
    return nodes
  
