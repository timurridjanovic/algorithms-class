

def open_file(file):
    with open(file) as f:
        output = [line.replace('\n', '').replace('"', '').split('\t') for line in f]
    G = {}
    superheroes = {}
    comics = {}

    for (node1, node2) in output:
        superheroes[node1] = 1
        comics[node2] = 1
        make_link(G, node1, node2)

    return (superheroes, comics, G)
        
def strength_connections(G, superheroes):
    strength = {}
    for superhero in superheroes.keys():
        for comic in G[superhero]:
            for neighbor in G[comic]:
                if superhero != neighbor:
                    if strength.get(' - '.join(sorted((superhero, neighbor)))):
                        strength[' - '.join(sorted((superhero, neighbor)))] += 1
                    else:
                        strength[' - '.join(sorted((superhero, neighbor)))] = 1
    return strength
                            



def make_link(G, node1, node2):
    if not G.get(node1):
        G[node1] = []
    G[node1].append(node2)
    if not G.get(node2):
        G[node2] = []
    G[node2].append(node1)

def main():
    (superheroes, comics, G) = open_file('marvelgraph.txt')
    strength = strength_connections(G, superheroes)
    print 'HUMAN TORCH/JOHNNY S - THING/BENJAMIN J. GR: ', strength['HUMAN TORCH/JOHNNY S - THING/BENJAMIN J. GR']
    print 'INVISIBLE WOMAN/SUE - MR. FANTASTIC/REED R: ', strength['INVISIBLE WOMAN/SUE  - MR. FANTASTIC/REED R']    
    print 'SPIDER-MAN/PETER PARKER - WATSON-PARKER, MARY: ', strength['SPIDER-MAN/PETER PAR - WATSON-PARKER, MARY ']
    print 'CAPTAIN AMERICA - IRON MAN/TONY STARK: ', strength['CAPTAIN AMERICA - IRON MAN/TONY STARK ']


main()       
