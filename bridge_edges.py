# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       

def make_link(G, node1, node2, r_or_g):
    # modified make_link to apply
    # a color to the edge instead of just 1
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = r_or_g
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = r_or_g
    return G


def create_rooted_spanning_tree(G, root):
    # use DFS from the root to add edges and nodes
    # to the tree.  The first time we see a node
    # the edge is green, but after that its red
    open_list = [root]
    S = {}
    while open_list:
        node = open_list.pop(0)
        neighbors = G[node]
        for n in neighbors:
            if n not in S:
                # we haven't seen this node, so
                # need to use a green edge to connect
                # it
                make_link(S, node, n, 'green')
                open_list.append(n)
            else:
                # we have seen this node,
                # but, first make sure that 
                # don't already have the edge
                # in S
                if node not in S[n]:
                    make_link(S, node, n, 'red')
    return S

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")

    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

test_create_rooted_spanning_tree()
###########

def _post_order(S, root, parent, val, po):
    left = get_left_child(S, root, parent)
    right = get_right_child(S, root, parent, left)
    if left:
        val = _post_order(S, left, root, val, po)   
    if right:
        val = _post_order(S, right, root, val, po)      
    po[root] = val
    return val + 1


def get_left_child(S, node, parent):
    children = [n for n, e in S[node].items() if not n == parent and e == 'green']
    if not children:
        return None
    return min(children)

def get_right_child(S, node, parent, left):
    children = [n for n, e in S[node].items() if not n == parent and not n == left and e == 'green']
    if not children:
        return None
    return max(children)

def post_order(S, root):
    po = {}
    _post_order(S, root, None, 1, po)
    return po

        
        
    

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

test_post_order()
##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    nd = {}
    _number_of_descendants(S, root, nd, None)
    return nd

def _number_of_descendants(S, root, nd, parent):
    children = get_children(S, root, parent)
    num = 1
    for c in children:
        num += _number_of_descendants(S, c, nd, root)
    nd[root] = num
    return num
   
    
def get_children(S, root, parent):
    return [n for n, e in S[root].items() if not n == parent and e == 'green']

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}
    
test_number_of_descendants()
###############


def _general_post_order(S, root, parent, po, gpo, comp):
    green, red = get_children_all(S, root, parent)
    val = po[root]
    for c in green:
        # recursively find the low/high post order value of the children
        test = _general_post_order(S, c, root, po, gpo, comp)
        # and save the low/highest one
        if comp(val, test):
            val = test
    for c in red:
        test = po[c]
        # and also look at the direct children
        # from following red edges
        # and save the low/highest one if needed
        if comp(val, test):
            val = test
    gpo[root] = val
    return val
    
def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    lpo = {}
    _general_post_order(S, root, None, po, lpo, lambda x, y: x>y)
    return lpo

def get_children_all(S, root, parent):
    """returns the children from following
    green edges and the children from following
    red edges"""
    green = []
    red = []
    for n, e in S[root].items():
        if n == parent:
            continue
        if e == 'green':
            green.append(n)
        if e == 'red':
            red.append(n)
    return green, red

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}

test_lowest_post_order()
################

def highest_post_order(S, root, po):
    hpo = {}
    _general_post_order(S, root, None, po, hpo, lambda x, y: x<y)
    return hpo

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}

test_highest_post_order()    
#################

def bridge_edges(G, root):
    rooted_spanning_tree = create_rooted_spanning_tree(G, root)
    po = post_order(rooted_spanning_tree, root)
    nod = number_of_descendants(rooted_spanning_tree, root)
    lpo = lowest_post_order(rooted_spanning_tree, root, po)
    hpo = highest_post_order(rooted_spanning_tree, root, po)
    
    bridges = []
    open_list = [(root, None)]
    
    while open_list:
        node, parent = open_list.pop()
        for n in get_children(rooted_spanning_tree, node, parent):
            open_list.append((n, node))
            if hpo[n] <= po[n] and lpo[n] > po[n] - nod[n]:
                bridges.append((node, n))
    return bridges
            
    
    
            

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    print bridges
    assert bridges == [('d', 'e')]
    
test_bridge_edges()

