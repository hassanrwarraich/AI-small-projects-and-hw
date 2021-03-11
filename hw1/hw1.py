class Node:
    """
    This is a definition of the class to be used

    Properties:
    state:  A tupple containing the data for the number of Missionaries on West and East banks
            along with the number of cannibals on each side as well as the location of the boat
            i.e. 0 for west bank and 1 for east bank. 
            The syntax: (Missionary_west, Cannibal_west, Missionary_east, Cannibal_east, boat location) 
    parent: The parent node of the current node
    """

    def __init__(self, state):
        self.state = state
        self.__parent = None

    def set_parent(self, parent):
        self.__parent = parent

    def get_parent(self):
        return self.__parent


def checkConstraint(node, visited, M, C):
    """
    This function scans the given node to check if the node is legal (eg if the missionaries are greate or equal to the cannibals)

    Parameters:
    node      : the node to be checked
    to_travel : 
    visited   : list that have already been visited (in order to prevent looping)
    M         : total number of missionaries
    C         : total number of cannibals

    Returns:
    whether the node meets the given requirements
    """
    if(node[4] == 0):

        if node in visited:
            return False

        # elif node in to_travel:
        #     return False

        # if more than 0 missionary in west and less M than C in west
        elif (node[0] != 0 and node[0] < node[1]):
            return False

        # if more than one M at east and less M at east than C at east
        elif (((M-node[0]) != 0) and ((M-node[0]) < (C-node[1]))):
            return False

        # if no M at west and no C at west
        elif (node[0] < 0 or node[1] < 0):
            return False

        else:
            return True

    else:

        if node in visited:
            return False

        elif (node[2] > M or node[3] > C):
            return False

        # if more than one missionary at west and less misionary at wes than on east
        elif (((M-node[2]) != 0) and ((M-node[2]) < (C-node[3]))):
            return False

        # if more than one missionary on the east and less missionary than cannibal at east
        elif ((node[2] != 0) and (node[2] < node[3])):
            return False

        else:
            return True


# moves the boat
def moveBoat(current_state):
    """
    This functions calculates all the possible movements of the boat from one side to the other and the number
    of cannibals/missionaries it may carry on each trip

    Parameters:
    current_state:      Takes the current state i.e. the number of missionaries and cannibals on each side along
                        with the location of the boat

    Returns:
    possible_states:    All possible end states after the boat has made its movements,
                        it returns a list of tupples.
    """
    possible_states = []

    if current_state.state[4] == 0:  # if boat is on the west
        for i in range(BOAT_CAPACITY + 1):
            if i <= current_state.state[0]:
                for j in range(BOAT_CAPACITY + 1):
                    if j <= current_state.state[1]:
                        if i + j > 0:  # there should be atleast one person on the boat to manuever the boat
                            # the number of ppl on the boat should be less than or equal to all the peaople on this side of the bank
                            if i + j <= current_state.state[0] + current_state.state[1]:
                                if i + j <= BOAT_CAPACITY:  # the boat can only hold a limited amount of ppl
                                    if i > 0:  # if there is atleast one missionary on the boat then the number of cannibals should be less on the boat
                                        if j <= i:
                                            new_node = Node(
                                                (current_state.state[0] - i, current_state.state[1] - j, current_state.state[2] + i, current_state.state[3] + j, 1))
                                            possible_states.append(new_node)
                                    else:  # if no missionaries then the boat can only have cannibals
                                        new_node = Node(
                                            (current_state.state[0] - i, current_state.state[1] - j, current_state.state[2] + i, current_state.state[3] + j, 1))
                                        possible_states.append(new_node)

    else:  # if boat is on the east, same logic as for west
        for i in range(BOAT_CAPACITY + 1):
            if i <= current_state.state[2]:
                for j in range(BOAT_CAPACITY + 1):
                    if j <= current_state.state[3]:
                        if i + j > 0:
                            if i + j <= current_state.state[2] + current_state.state[3]:
                                if i + j <= BOAT_CAPACITY:
                                    if i > 0:
                                        if j <= i:
                                            new_node = Node(
                                                (current_state.state[0] + i, current_state.state[1] + j, current_state.state[2] - i, current_state.state[3] - j, 0))
                                            possible_states.append(new_node)
                                    else:
                                        new_node = Node(
                                            (current_state.state[0] + i, current_state.state[1] + j, current_state.state[2] - i, current_state.state[3] - j, 0))
                                        possible_states.append(new_node)
    return possible_states


# simulating
def main(initial_state):
    """
    The main 'method', it is provided with the root node and then traverses the tree using DFS from the right most node
    and if the solution is found it return the solution node which can be traced back to the root node through its parenting
    nodes. If the leaf node is reached and it is not the solution then the siblings nodes will be picked up and searched for
    further children nodes to find the solution node. There will be no repetition of states.

    Parameters:
    initial_state:  This is the initial number of missionaries and cannibals on the west coast

    Returns:
    found:          True or False; to show that the solution has been found or not
    next_state:     The solution node, this will be used to trace back the solution's path
    """
    total_M = initial_state.state[0]  # total number of missionaries
    total_C = initial_state.state[1]  # total number of cannibals

    # Setting the current state to be the initial state as the code just started
    current_state = initial_state

    found = False  # the solution is yet to be found

    possible_states = []
    visited_states = []
    to_travel = []

    while not found:
        # determine the next possible states according to boat constraints
        possible_states = moveBoat(current_state)
        legal_states = []

        # determining which states are legal
        for i in range(len(possible_states)):
            if (checkConstraint(possible_states[i].state, visited_states, total_M, total_C)):
                # we have filtered out states to make it so that the missionaries >= cannibals on each side
                legal_states.append(possible_states[i])
                # or we only have cannibals at one side

        if legal_states != []:  # if legal states present
            # dept first search, poping out the right most child node in the tree
            next_state = legal_states.pop()
            # adding the current state to the list of visited to avoid
            visited_states.append(current_state.state)
            # cycling in our tree
            # leaving the nodes not visited in this array to be taken out later on
            to_travel += legal_states
            # if we reach legal states = [], then will pop out the last to travel state
            # defining the children and parent relationship
            next_state.set_parent(current_state)

            for i in legal_states:
                i.set_parent(current_state)
                # defining the other legal states of the current node as its children aswell
                to_travel.append(i)

            # have successfully transferred all missionaries and cannibals to the opposite coast
            if(next_state.state == (0, 0, total_M, total_C, 1)):
                print("Solution Found")
                found = True  # set true inorder to exit the loop
                # returning the final state inorder to trace it back to its parents
                return (next_state, found)

            else:
                current_state = next_state

        else:  # legal states not present
            if(to_travel != []):
                to_travel.pop()
                # getting the sibling node into the next_state instead of the right-most
                next_state = to_travel.pop()
                # child node
                # adding the current node into the visited nodes list to avoid
                visited_states.append(current_state.state)
                # repetition
                current_state = next_state  # setting the new current node

            else:
                print("solution not found")
                found = False
                # the solution was not found so we return false and no solution node
                return (None, found)


def getPath(curr_node, end_node):
    """
    Returns the array of the sequetial states that lead to the answer. The path starts from the root to the solution state

    Parameters:
    curr_node:  the final (answer) state 
    end_node: the root node from which the path should be formed

    Returns:
    path:          the array of the states that show the states in sequence leading up to the solution
    """
    found = False
    path = [curr_node.state]

    while not found:
        parent = curr_node.get_parent()
        if parent != end_node:
            path.append(parent.state)
            curr_node = parent
        elif parent == end_node:
            path.append(parent.state)
            return path


# returns the concatenated string of a given character of given length
def getString(c, num):
    if num == 0:
        return ""
    s = c
    for i in range(num - 1):
        s = s + " " + c
    return s


# print the array of paths in a suqenece that makes it easy to read and understand
def printPath(path):
    """
    print the array of paths in a suqenece that makes it easy to read and understand

    Parameters:
    path: the array of states to be printed
    """
    cwString = getString('c', path[0][1])
    mwString = getString('m', path[0][0])
    print(cwString+"\n"+mwString)

    for i in range(1, len(path)):
        cwString = ceString = mwString = meString = ""
        print("-----------------------------------------")
        prevState = path[i - 1]
        currState = path[i]

        if currState[4] == 0:  # if boat returning to west side
            cDif = abs(currState[1] - prevState[1])
            pDif = abs(currState[0] - prevState[0])
            print("Return " + str(cDif) + " cannibals and " +
                  str(pDif) + " missionaries")

        else:  # boat going to east side
            cDif = abs(currState[3] - prevState[3])
            pDif = abs(currState[2] - prevState[2])
            print("Send " + str(cDif) + " cannibals and " +
                  str(pDif) + " missionaries")

        cwString = getString('c', currState[1])
        ceString = getString('c', currState[3])
        print(cwString + "\t\t" + ceString)
        mwString = getString('m', currState[0])
        meString = getString('m', currState[2])
        print(mwString + "\t\t" + meString)

################################################################################
# Program begins here


# PART 1
print("Part1\nBoat Capacity: 3\nNumber of Missionaries: 5\nNumber of Cannibals: 5\n=============================================\n")
BOAT_CAPACITY = 3
# the boat capacity
# the initial state with the number of missionaries and cannibals on the west coast
initial_state = Node((5, 5, 0, 0, 0))
# calling the main method to find any solution
(node, found) = main(initial_state)

if found:
    path = getPath(node, initial_state)
    path = path[::-1]
    printPath(path)  # if the solution is found output the path taken

else:
    print("Solution Not Possible!")  # solution not possible

print("=========================================================================\n")
##################################################################################################
# PART 2
print("Part1\nBoat Capacity: 4\nNumber of Missionaries: 6\nNumber of Cannibals: 6\n=============================================\n")
BOAT_CAPACITY = 5
# the boat capacity
# the initial state with the number of missionaries and cannibals on the west coast
initial_state = Node((6, 6, 0, 0, 0))
# calling the main method to find any solution
(node, found) = main(initial_state)

if found:
    path = getPath(node, initial_state)
    path = path[::-1]
    printPath(path)  # if the solution is found output the path taken

else:
    print("Solution Not Possible!")  # solution not possible
