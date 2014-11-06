

G = {
    'a': ['b', 'c'], 
    'b': ['a', 'd', 'e'], 
    'c': ['a', 'h'], 
    'd': ['b'], 
    'e': ['b', 'f', 'g'], 
    'f': ['e'],
    'g': ['e'],
    'h': ['c', 'i'],
    'i': ['h']}
    
#post-order: D, F, G, E, B, I, H, C, A

def post_order(G, root):
    po = []
    _post_order(G, root, None, po)
    return po
      
    
def _post_order(G, root, parent, po):
    children = get_children(G, root, parent)
    for c in children:
        _post_order(G, c, root, po)
    po.append(root)
    return root
    
    
def get_children(G, root, parent):
    return [child for child in G[root] if child != parent]
    
print post_order(G, 'a')    
    

