import csv
import random

def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter= '\t')
    G = {}
    movies = {}
    actors = {}

    for (actor,movie_name,date) in tsv:

        movie = str(movie_name)+", "+str(date)

        actors[actor] = 1
        movies[movie] = 1


        make_link(G, actor, movie)

    return (G, actors, movies)



def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return



def partition(L, i):

    smaller = {}
    equal = {}
    bigger = {}
    v = random.choice(L.keys())
    for val in L.keys():
        if L[val] < L[v]:
            smaller[val] = L[val]
        elif L[val] > L[v]:
            bigger[val] = L[val]
        elif L[val] == L[v]:
            equal[val] = L[val]

    if len(smaller) >= i:
        return partition(smaller, i)

    if len(smaller)+len(equal) == i:
        return v
    else:
        return partition(bigger, i - len(smaller) - len(equal))
        
        

def main():
    (G, actors, movies) = read_graph("imdb-4.tsv")

    centralities = {}

    for actor in actors.keys():
        centralities[actor] = centrality(G, actor)


    actor_index = partition(centralities, 20)

    print actor_index
    print centralities[actor_index]



if __name__ == '__main__':
    main()
    

