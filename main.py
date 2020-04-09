"""

Steps :


Create Graph Class
Create Node Class
Implement A* Search
Implement Heuristics



"""

#########################################  NODE CLASS ##############################################

class Node:

    # constructor
    def __init__(self, name:str, parent:str):

        self.name = name
        self.parent = parent

        self.dist_start_node = 0 # Distance to start node
        self.dist_goal_node = 0 # Distance to goal node
        self.total_cost = 0 # Total cost


    # Built in Object Comparision Function (__eq__)
    # Check if two nodes are identical
    def __eq__(self, node_to_compare):

        return self.name == node_to_compare.name

    # Built in Object Sorting (__lt__)
    # Sort Nodes Based on Total Cost
    def __lt__(self, node_to_compare):

         return self.f < node_to_compare.f

    # Built in Object toString Java like function
    # Print Node
    def __repr__(self):

        return ('({total_cost})'.format(self.total_cost))

'''
class Node:



    # Contructor
    def __init__(slef, name, parent):

        self.name = name
        self.parent = parent
        self.dist_start_node = 0 # represents : f(g)
        self.dist_goal_node = 0 # represents : f(h)
        self.total_cost = 0     # represents : f(x)


    # Built in Object Comparision Function (__eq__)
    # Check if two nodes are identical

    def __eq__(self, node_to_compare):

        return (self.name == node_to_compare.name)


    # Built in Object Sorting (__lt__)
    # Sort Nodes Based on Total Cost

    def __lt__(self, node_to_compare):

        return (self.total_cost < node_to_compare.total_cost)

    # Built in Object toString Java like function
    # Print Node
    def __repr__(self):

        return ("{total_cost}".format(self.total_cost)) '''

    



####################################### GRAPH CLASS #######################################


class Graph:

    # constructor
    def __init__(self, input_dict=None):

        self.input_dict = input_dict or {}

        for element in list(self.input_dict.keys()):

            for (city, dist) in self.input_dict[element].items():

                self.input_dict.setdefault(city, {})[element] = dist



    # Add conection / edge between nodes/verices
    def add_connection(self, node_a, node_b, distance=1):

        self.input_dict.setdefault(node_a, {})[node_b] = distance

        self.input_dict.setdefault(node_b, {})[node_a] = distance




    # get neighbours of the current node/vertex
    def get_neighbours(self, node_a, node_b=None):

        connections = self.input_dict.setdefault(node_a, {})

        if node_b is None:

            return connections

        else:

            return connections.get_neighbours(node_b)


    # Return a list of nodes in the graph
    def display_all_nodes(self):

        citys = set([city for city in self.input_dict.keys()])

        dists = set([dist_1 for dist_2 in self.input_dict.values() for dist_1, dist_x in dist_2.items()])

        nodes = citys.union(dists)

        return list(nodes)
















'''
class Graph:

    #Constructor
    def __int__(self, input_dict=None):

        self.input_dict = input_dict or {}


        for element in list(self.input_dict.keys()):

            for (city, distance) in self.input_dict[element].items():

                self.input_dict.setdefault(city, {})[element] = distance
    


    # Add conection / edge between nodes/verices
    def add_connection(self, node_a, node_b, distance=1):

        self.input_dict.setdefault(node_b, {})[node_a] = distance           


    # get neighbours of the current node/vertex
    def get_neighbours(self, node_a, node_b=None):

        connections = self.input_dict.setdefault(node_a, {})

        if node_b is None :

            return connections

        else :

            return connections.get_neighbours(node_b)


    def display_all_nodes(self):

        citys = set([city for city in self.input_dict.keys()])
        distances = set([distance_1 for distance in self.input_dict.values() for distance_1, edge in distance.items()])

        nodes = citys.union(distances)

        return list(nodes) '''


################################################ A STAR SEARCH ##########################################################

def a_star_search(graph, heuristics, start, end):
    
    # Create lists for not_expanded nodes and expanded nodes
    not_expanded = []
    expanded = []

    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add the start node
    not_expanded.append(start_node)
    
    # Loop until the not_expanded list is empty
    while len(not_expanded) > 0:

        # Sort the not_expanded list to get the node with the lowest cost first
        not_expanded.sort()

        # Get the node with the lowest cost
        current_node = not_expanded.pop(0)

        # Add the current node to the expanded list
        expanded.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:

            path = []

            while current_node != start_node:

                path.append(current_node.name + ': ' + str(current_node.dist_start_node))

                current_node = current_node.parent

            path.append(start_node.name + ': ' + str(start_node.dist_start_node))

            # Return reversed path
            return path[::-1]

        # Get neighbours
        neighbours = graph.get_neighbours(current_node.name)

        # Loop neighbours
        for key, value in neighbours.items():

            # Create a neighbour node
            neighbour = Node(key, current_node)

            # Check if the neighbour is in the expanded list
            if(neighbour in expanded):
                continue

            # Calculate full path cost
            neighbour.dist_start_node = current_node.dist_start_node + graph.get_neighbours(current_node.name, neighbour.name)
            neighbour.dist_goal_node = heuristics.get_neighbours(neighbour.name)
            neighbour.total_cost = neighbour.dist_start_node + neighbour.dist_goal_node

            # Check if neighbour is in not_expanded list and if it has a lower f value
            for node in not_expanded:

                if (neighbour == node and neighbour.total_cost > node.total_cost):

                    continue

            # Everything is green, add neighbour to not_expanded list
            not_expanded.append(neighbour)

    # Return None, no path is found
    return None


'''

# A* Search Algorithm

def a_star_search(graph, heuristic, start, end):

    not_expanded = [] # close
    not_not_expanded = [] # not_expanded

    start_node = Node(start, None)
    goal_node = Node(end, None)




    while (len(not_not_expanded) > 0) :


        not_not_expanded.sort()



        current_node = not_not_expanded.pop(0)


        not_expanded.append(current_node)



        if current_node == goal_node:

            path = []


            while current_node != start_node:

                path.append(current_node.name + ': ' + str(current_node.dist_start_node))

                current_node = current_node.parent

            path.append(start_node.name + ': ' + str(start_node.dist_start_node))

        return (path[::-1])



        neighbours = graph.get_neighbours(current_node.name)

        for key, value in neighbours.items():

            neighbour = Node(key, current_node)

            if (neighbour in not_expanded) :
                
                continue


            neighbour.dist_start_node = current_node.dist_start_node + graph.get_neighbours(current_node.name, neighbour.name)
            neighbour.dist_goal_node = heuristics.get_neighbours(neighbour.name)
            neighbour.total_cost = neighbour.dist_start_node + neighbour.dist_goal_node


            for temp_node in not_not_expanded:
                if (neighbour == temp_node and neighbour.dist_goal_node > temop_node.dist_goal_node):

                    continue


            not_not_expanded.append(neighbour)


        return None '''



# The main entry point for this module
def main():

    # Create a graph
    graph = Graph()

    # Create graph connections (Actual distance)
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

   

    # Create heuristics (straight-line distance, air-travel distance)
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

    # Run the search algorithm
    path = a_star_search(graph, heuristics, 'Frankfurt', 'Ulm')
    print(path)
    print()

# Tell python to run main method
if __name__ == "__main__":
     main()

