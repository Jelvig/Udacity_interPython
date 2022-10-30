"""this was copied from the solution becuase the question it self was not clear,
and was asking to use techniques that we did'nt cover. this was used as a study guide to see
how this code was implemented to get the wanted result"""
#  and files could not be accessed to be observed of how to properly write the code


import csv
import json

import helper

def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]  # creating a dict of code names to the full name of airlines
    return airlines

def read_airports(filename='airports.dat'):
    airports = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]  # creating dict of airport code names to actual names
    return airports

def read_routes(filename='routes.dat'):
    # Note: This could be a collections.defaultdict(list) instead, for elegance.
    routes = {}  # Map from source -> list of dests
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            source, dest = line[2], line[4]  # splicing data of what airport can go to certain destination jfk->SEA
            if source not in routes:
                routes[source] = []  # create dict array for source if it doesnt exist in dict as key
            routes[source].append(dest)  #  append desitnation to values if source is source
    return routes
  
def find_paths(routes, source, dest, max_segments):
    # Run the BFS search
    frontier = {source}
    seen = {source: {(source, )}}
    for steps in range(max_segments):
        next_frontier = set()
        for airport in frontier:
            for target in routes.get(airport, ()):  # add empty parenthesis becuase some flights are only destination
                if target not in seen:
                    next_frontier.add(target)  # adds target to next node to visit if it is not in seen, which is nodes that are visited
                    seen[target] = set()  # setting a dict of target and a set of airports it can visit(currently empty)
                for path in seen[airport]:
                    if len(path) != steps + 1:  #  checking to make sure you are not surpassing number of steps
                        continue
                    seen[target].add(path + (target, ))  # add source path to target
        frontier = next_frontier  # when all nodes are visited on current layer, move on to next layer
    return seen[dest]

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Again, could use a collections.defaultdict(list) here.
    for path in paths:
        segments = len(path) - 1
        if segments not in output:
            output[segments] = []
        output[segments].append(rename_path(path, airports))

    with open(f"{source}->{dest} (max {max_segments}).json", 'w') as f:
        json.dump(output, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
