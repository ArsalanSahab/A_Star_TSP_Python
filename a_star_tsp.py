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
    
###########################  Shortest Path Algorithm ################################
   
    not_expanded = [] # Not Expanded
    expanded = [] # expanded

   
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add the start node to not_expanded list
    not_expanded.append(start_node)
    
    # Loop until all nodes in not_expanded are expanded
    while len(not_expanded) > 0:

        # Sort The List
        not_expanded.sort()

        # Get the node with the lowest cost
        current_node = not_expanded.pop(0)

        # Add the current node to the expanded list
        expanded.append(current_node)
        
        # Check if we have reached the goal if reached start backtrack , else continue
        if current_node == goal_node:

            # List to Store Shrtest Path
            path = []
            
            # Backtrack back to the start node 
            while current_node != start_node:

                
                path.append("city_"+current_node.name + ': ' + str(current_node.dist_to_start_node))

                current_node = current_node.parent

            path.append("city_"+start_node.name + ': ' + str(start_node.dist_to_start_node))

        

            
            return path[::-1]



        # Get neighbours
        neighbors = graph.get(current_node.name)

        # Loop over neighbours
        for key, value in neighbors.items():

            neighbor = Node(key, current_node)

            # Check if the neighbor is in the expanded list
            if(neighbor in expanded):
                continue

############################ A_Star_Search_Algorithm #######################################

            # Calculate full path cost
            neighbor.dist_to_start_node = current_node.dist_to_start_node + graph.get(current_node.name, neighbor.name)

            neighbor.dist_to_goal_node = heuristics.get(neighbor.name)

            neighbor.total_dist = neighbor.dist_to_start_node + neighbor.dist_to_goal_node

            # Check if this Node Path's f(x) A* Value is > or not           
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
          # City A , City B , Distance Between
    graph.add_connection('0', '1', 4)
    graph.add_connection('0', '7', 8)
    graph.add_connection('1', '2', 8)
    graph.add_connection('1', '7', 11)
    graph.add_connection('2', '3', 7)
    graph.add_connection('2', '8', 2)
    graph.add_connection('2', '5', 4)
    graph.add_connection('3', '4', 9)
    graph.add_connection('3', '5', 14)
    graph.add_connection('4', '5', 10)
    graph.add_connection('5', '6', 2)
    graph.add_connection('6', '7', 1)
    graph.add_connection('6', '8', 6)
    graph.add_connection('7', '8', 7)


    print("Displaying All Nodes")
    print(graph.display_all_nodes())
  




    # Create a dictionary for heuristics : dict{'city_name' : 'distance_to_goal}

    heuristics = {}
    heuristics['0'] = 12
    heuristics['1'] = 8
    heuristics['2'] = 1
    heuristics['3'] = 5
    heuristics['4'] = 13
    heuristics['5'] = 5
    heuristics['6'] = 5
    heuristics['7'] = 3
    heuristics['8'] = 0
  

    
    path = a_star_search(graph, heuristics, '0', '8')
    print("Displaying Shortest Path")
    print(path)
    print()


if __name__ == "__main__": 
    main()