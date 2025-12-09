import time, math
from collections import defaultdict
from itertools import combinations


def get_dist(c1, c2):
    return math.dist(c1, c2)


def process(points, num_connections=0):
    # creates list of tuples for every combinations of 2 points
    combos = combinations(points, 2)
    # distances is list of tuples(distance between two points, point 1, point 2) for every combo in combos
    distances = [(get_dist(a, b), a, b) for a, b in combos]

    distances.sort()  # will sort by the distance ascending

    # Part1
    if num_connections > 0:
        distances = distances[:num_connections]
        # cut distances to be the length of the amount of connections the problem asks for
        # distances is now n shortest elements where n is the num_connections

    point_to_network = {}  # create dicctionary where the keys are points and values are the networks thats associated wit that point
    network_to_points = defaultdict(  # a forest( set of trees)
        set
    )  # another dicctionary whre the network is the key and the values is a set of points
    next_network = 0
    # iterate over every tuple in distances
    # _ is distance, p is point one , q is point two
    for _, p, q in distances:
        # if neither of the points are a key in the ptn dicctionary
        if p not in point_to_network and q not in point_to_network:
            # set the next_network as the values for both points
            point_to_network[p] = next_network
            point_to_network[q] = next_network
            network_to_points[next_network] |= {
                p,
                q,
            }  # join a set of the points to the NtPdictionary at that network
            next_network += 1
        # if both are in the dictionary
        elif p in point_to_network and q in point_to_network:
            # if both points are in the same network, avoid creating a cycle so continue
            if point_to_network[p] == point_to_network[q]:
                continue
            else:  # this is the union/ merging of two components
                # set old_net to the network at the second point
                old_net = point_to_network[q]
                # iterate through each point in the set of points for that pariuclar netowrk
                for point in network_to_points[point_to_network[q]]:
                    # and
                    point_to_network[point] = point_to_network[p]
                network_to_points[point_to_network[p]] |= network_to_points[old_net]
                del network_to_points[old_net]
        elif (
            p in point_to_network
        ):  # only p is in a network, q becomes part of that networ
            point_to_network[q] = point_to_network[p]
            network_to_points[point_to_network[p]].add(q)
        else:  # only q is in a network, add p to that same netwrok
            point_to_network[p] = point_to_network[q]
            network_to_points[point_to_network[q]].add(p)
        # Part 2
        if (
            num_connections == 0
            and len(network_to_points) == 1
            and len(network_to_points[point_to_network[p]]) == len(points)
        ):
            return p[0] * q[0]

    # Part 1
    # sort the lenght of the netowrks in other works the circuits with the most points and then return the 3 biggest multiplied with each other
    biggest_nets = sorted(
        network_to_points.values(), key=lambda x: len(x), reverse=True
    )
    return len(biggest_nets[0]) * len(biggest_nets[1]) * len(biggest_nets[2])


def read_coords(filename):
    return [
        tuple(map(int, line.strip().split(",")))
        for line in open(filename)
        if line.strip()
    ]


# NOT MY SOLUTION, I could not figure out how to do this problem but now i know about Disjoint-set data structure


if __name__ == "__main__":
    start = time.perf_counter()
    coords = read_coords("test_input.txt")
    # part 1
    print(process(coords, 10))
    # part 2
    """
    print(
        process(
            coords,
        )
    )
    """
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
