def tree_by_levels(node):
    if node is None:
        return []
    nodes = [node.value]
    points = [node]
    while len(points)!= 0:
        new_points = []
        for i in points:
            if i.left is not None:
                nodes.append(i.left.value) 
                new_points.append(i.left)
            if i.right is not None:
                nodes.append(i.right.value) 
                new_points.append(i.right)
            points = new_points
    return nodes
