from random import choice


def makeG(n, freeNodes):
    if n == 2:
        n1 = choice(freeNodes)
        freeNodes.remove(n1)
        n2 = choice(freeNodes)
        freeNodes.remove(n2)
        return [(n1, n2)]
    binList = (0,1)
    G1 = makeG(n/2, freeNodes)
    G2 = makeG(n/2, freeNodes)
    n3 = choice(G1)[choice(binList)]
    n4 = choice(G2)[choice(binList)]
    G1.extend(G2)
    G1.append((n3, n4))
    return G1


print makeG(8, range(8))
