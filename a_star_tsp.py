#################################################  NODE CLASS #######################################

class Node:

    # CONSTRUCTOR
    def __init__(self, name:str, parent:str):

        self.name = name
        self.parent = parent
        self.dist_to_start_node = 0 # Distance to start node
        self.dist_to_goal_node = 0 # Distance to goal node
        self.total_dist = 0 # Total cost

    # Built in Object Comparision Function (__eq__)
    # Check if two nodes are identical
    def __eq__(self, node_to_compare):

        return self.name == node_to_compare.name

    # Built in Object Sorting (__lt__)
    # Sort Nodes Based on Total Cost
    def __lt__(self, node_to_compare):

         return self.total_dist < node_to_compare.total_dist

    # Built in Object toString Java like function
    # Print Node
    def __repr__(self):

        return ('({position},{total_dist})'.format(self.position, self.total_dist))




################################################## GRAPH CLASS #############################################


class Graph:

    # CONSTRUCTOR
    def __init__(self, input_dict=None):

        self.input_dict = input_dict or {}

        for city_1 in list(self.input_dict.keys()):

            for (city_2, dist) in self.input_dict[city_1].items():

                self.input_dict.setdefault(city_2, {})[cit_1] = dist
       


    # Add conection / edge between nodes/verices
    def add_connection(self, node_a, node_b, distance=1):

        self.input_dict.setdefault(node_a, {})[node_b] = distance
        
        self.input_dict.setdefault(node_b, {})[node_a] = distance

    # get neighbours of the current node/vertex
    def get(self, node_a, node_b=None):

        connections = self.input_dict.setdefault(node_a, {})

        if node_b is None:

            return connections

        else:

            return connections.get(node_b)

    # Get all nodes in the graph
    def display_all_nodes(self):

        citys = set([city for city in self.input_dict.keys()])

        city_distances = set([distances for dist in self.input_dict.values() for distances, dist_2 in dist.items()])

        display_all_nodes = citys.union(city_distances)

        return list(display_all_nodes)



##############################################  A STAR SEARCH ##################################################



def a_star_search(graph, heuristics, start, end):
    
   
    not_expanded = [] # Not Expanded
    expanded = [] # expanded

   
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add the start node to not_expanded list
    not_expanded.append(start_node)
    
    # Loop until all nodes in not_expanded are expanded
    while len(not_expanded) > 0:

        # Sort List get lowest cost first
        not_expanded.sort()

        # Get the node with the lowest cost
        current_node = not_expanded.pop(0)

        # Add the current node to the expanded list
        expanded.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:

            path = []

            while current_node != start_node:

                path.append(current_node.name + ': ' + str(current_node.dist_to_start_node))

                current_node = current_node.parent

            path.append(start_node.name + ': ' + str(start_node.dist_to_start_node))

            
            return path[::-1]

        # Get neighbours
        neighbors = graph.get(current_node.name)

        # Loop over neighbours
        for key, value in neighbors.items():

            neighbor = Node(key, current_node)

            # Check if the neighbor is in the expanded list
            if(neighbor in expanded):
                continue

            # Calculate full path cost
            neighbor.dist_to_start_node = current_node.dist_to_start_node + graph.get(current_node.name, neighbor.name)

            neighbor.dist_to_goal_node = heuristics.get(neighbor.name)

            neighbor.total_dist = neighbor.dist_to_start_node + neighbor.dist_to_goal_node

           
            for node in not_expanded:

                if (neighbor == node and neighbor.total_dist > node.total_dist):

                    continue

          
            not_expanded.append(neighbor)

    
    return None



################################################# MAIN  ##############################################################


def main():

    # Create graph instance
    graph = Graph()

    # add edges/connections between nodes/cities

    graph.add_connection('Frankfurt', 'Wurzburg', 111)
    graph.add_connection('Frankfurt', 'Mannheim', 85)
    graph.add_connection('Wurzburg', 'Nurnberg', 104)
    graph.add_connection('Wurzburg', 'Stuttgart', 140)
    graph.add_connection('Wurzburg', 'Ulm', 183)
    graph.add_connection('Mannheim', 'Nurnberg', 230)
    graph.add_connection('Mannheim', 'Karlsruhe', 67)
    graph.add_connection('Karlsruhe', 'Basel', 191)
    graph.add_connection('Karlsruhe', 'Stuttgart', 64)
    graph.add_connection('Nurnberg', 'Ulm', 171)
    graph.add_connection('Nurnberg', 'Munchen', 170)
    graph.add_connection('Nurnberg', 'Passau', 220)
    graph.add_connection('Stuttgart', 'Ulm', 107)
    graph.add_connection('Basel', 'Bern', 91)
    graph.add_connection('Basel', 'Zurich', 85)
    graph.add_connection('Bern', 'Zurich', 120)
    graph.add_connection('Zurich', 'Memmingen', 184)
    graph.add_connection('Memmingen', 'Ulm', 55)
    graph.add_connection('Memmingen', 'Munchen', 115)
    graph.add_connection('Munchen', 'Ulm', 123)
    graph.add_connection('Munchen', 'Passau', 189)
    graph.add_connection('Munchen', 'Rosenheim', 59)
    graph.add_connection('Rosenheim', 'Salzburg', 81)
    graph.add_connection('Passau', 'Linz', 102)
    graph.add_connection('Salzburg', 'Linz', 126)



    # Create a dictionary for heuristics : dict{'city_name' : 'distance_to_goal}

    heuristics = {}
    heuristics['Basel'] = 204
    heuristics['Bern'] = 247
    heuristics['Frankfurt'] = 215
    heuristics['Karlsruhe'] = 137
    heuristics['Linz'] = 318
    heuristics['Mannheim'] = 164
    heuristics['Munchen'] = 120
    heuristics['Memmingen'] = 47
    heuristics['Nurnberg'] = 132
    heuristics['Passau'] = 257
    heuristics['Rosenheim'] = 168
    heuristics['Stuttgart'] = 75
    heuristics['Salzburg'] = 236
    heuristics['Wurzburg'] = 153
    heuristics['Zurich'] = 157
    heuristics['Ulm'] = 0

    
    path = a_star_search(graph, heuristics, 'Frankfurt', 'Ulm')
    print(path)
    print()


if __name__ == "__main__": 
    main()