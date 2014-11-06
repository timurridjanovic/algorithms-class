#create generator that will yield the nodes in proper order

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
    
#preorder: A, B, D, E, F, G, C, H, I

def pre_order(G, root):
    generator = _pre_order(G, root, None)
    print_generator(generator)
    
def print_generator(gen):
    for e in gen:
        if type(e) != str:
            print_generator(e)
        else:
            print e
           
    
    
def _pre_order(G, root, parent):
    children = get_children(G, root, parent)
    yield root
    for c in children:
        yield _pre_order(G, c, root)
    
    
    
def get_children(G, root, parent):
    return [child for child in G[root] if child != parent]
    
pre_order(G, 'a')    
    
