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
    
#in order: D, B, F, E, G, A, I, H, C

def in_order(G, root):
    generator = _in_order(G, root, None)
    print_generator(generator)
    
def print_generator(gen):
    for e in gen:
        if type(e) != str:
            print_generator(e)
        else:
            print e
               
    
def _in_order(G, root, parent):
    left = get_left_child(G, root, parent)
    right = get_right_child(G, root, parent, left)
    if left:
        yield _in_order(G, left, root)
    yield root
    if right:
        yield _in_order(G, right, root)
    
     
def get_left_child(G, root, parent):
    children = [child for child in G[root] if child != parent]
    if not children:
        return None
    return min(children)

def get_right_child(G, root, parent, left):
    children =  [child for child in G[root] if child != parent and child != left]
    if not children:
        return None
    return max(children)  
    
in_order(G, 'a') 
