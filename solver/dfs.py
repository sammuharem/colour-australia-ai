def dfs(env):
    frontier = [env.get_init_state()]
    explored = set([])
    nodes_explored = 0
    
    while len(frontier):
        node = frontier.pop(-1)
        explored.add(node.get_representation())
        
        if env.is_solved(node.state):
            print(f'Nodes Explored: {nodes_explored}, Nodes on Frontier: {len(frontier)}')
            print(node)
            return node  
        
        nodes_explored += 1
        
        for child in node.get_successors():
            print(child)
            if child.get_representation() not in explored:
                frontier.append(child)
