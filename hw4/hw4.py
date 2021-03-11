"""
Description: This is a simple program to create a class precende list.
We used the simple topological sorting algorithm which uses stacks to create the list.
The only change we made is that the original algorithm considers all the nodes in the graph
to order them. In our program we only start with a single node given as input and navigate through
its vertices and their vertices and so on. We learned the topological sorting algorithm from our 
CS-202 Fundamental Structures of Computer Science course at Bilkent. We use adjency list to represent 
the graph. The adjency list is created using Python dictionaries.

Authors:    Umer Shamaan
            Taha Khurram
            Hassan Raza
            Muhammad Ali Khaqan

"""

#creating the adjacency list for part 1
adjList_dict = {}
adjList_dict["ifstream"] = ["istream"]
adjList_dict["istream"] = ["ios"]
adjList_dict["fstream"] = ["iostream"]
adjList_dict["iostream"] = ["istream", "ostream"]
adjList_dict["ostream"] = ["ios"]
adjList_dict["ofstream"] = ["ostream"]
adjList_dict["ios"] = []


#creating the adjacency list for part 2
adjList_dict2 = {}
adjList_dict2["Consultant Manager"] = ["Consultant", "Manager"]
adjList_dict2["Director"] = ["Manager"]
adjList_dict2["Permanent Manager"] = ["Manager", "Permanent Employee"]
adjList_dict2["Consultant"] = ["Temporary Employee"]
adjList_dict2["Manager"] = ["Employee"]
adjList_dict2["Temporary Employee"] = ["Employee"]
adjList_dict2["Permanent Employee"] = ["Employee"]
adjList_dict2["Employee"] = []


#creating the adjacency list for part 3
adjList_dict3 = {}
adjList_dict3["Crazy"] = ["Professors", "Hackers"]
adjList_dict3["Jacque"] = ["Weightlifters", "Shotputters", "Athletes"]
adjList_dict3["Professors"] = ["Eccentrics", "Teachers"]
adjList_dict3["Hackers"] = ["Eccentrics", "Programmers"]
adjList_dict3["Weightlifters"] = ["Athletes", "Endomorpha"]
adjList_dict3["Shotputters"] = ["Athletes", "Endomorpha"]
adjList_dict3["Eccentrics"] = ["Dwarfs"]
adjList_dict3["Teachers"] = ["Dwarfs"]
adjList_dict3["Programmers"] = ["Dwarfs"]
adjList_dict3["Athletes"] = ["Dwarfs"]
adjList_dict3["Endomorpha"] = ["Dwarfs"]
adjList_dict3["Dwarfs"] = ["Everything"]
adjList_dict3["Everything"] = []



#Used to check if all vertices adjacent to the vertex on the top of the stack (node) have been visited or not
def allVisited(node, visited, adjList_dict):
    toCheck = adjList_dict[node]
    temp = len(toCheck)
    for i in range(0,temp):
        if not toCheck[i] in visited:
            return False
    return True


#returns an unvisietd node adjacent to the node given as arguement
def selectUnvisited(node, visited, adjList_dict):
    toCheck = adjList_dict[node]
    temp = len(toCheck)
    for i in range(0, temp):
        if not toCheck[i] in visited:
            return toCheck[i]
    else:
        return 



#the altered version of a basic topological sorting algorithm to create the class precedency list
def topSort(adjList_dict, Node):
    my_stack = []   #the stack
    visited = []    #The list of nodes visited
    PList = []      #The precedence List

    my_stack.append(Node) #pushing in the child node for which the precedence list is being calculated

    while  my_stack:
        if allVisited(my_stack[-1], visited, adjList_dict):  #if all vertices adjacent to node at the top of the stack have been visited
            PList.insert(0, my_stack.pop()) 
        
        else:
            node = selectUnvisited(my_stack[-1], visited, adjList_dict) #select an unvisited node adjacent to the node at the top of stack
            my_stack.append(node)
            visited.append(node)

    return PList




#main starts here

print("Part 1:")
print("Computing the precedency list for ifstream:")
print(topSort(adjList_dict, "ifstream"))
print("Computing the precedency list for fstream:")
print(topSort(adjList_dict, "fstream"))
print("Computing the precedency list for ofstream:")
print(topSort(adjList_dict, "ofstream"))

print("\n--------------------------------------------------\n")

print("Part 2:")
print("Computing the precedency list for Consultant Manager:")
print(topSort(adjList_dict2, "Consultant Manager"))
print("Computing the precedency list for Director:")
print(topSort(adjList_dict2, "Director"))
print("Computing the precedency list for Permanent Manager:")
print(topSort(adjList_dict2, "Permanent Manager"))

print("\n--------------------------------------------------\n")


print("Part 3:")
print("Computing the precedency list for Crazy:")
print(topSort(adjList_dict3, "Crazy"))
print("Computing the precedency list for Jacque:")
print(topSort(adjList_dict3, "Jacque"))

