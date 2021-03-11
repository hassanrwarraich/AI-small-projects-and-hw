# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:28:35 2020

@authors: 
Hassan Raza Warraich
Umer Shamaan
Taha Khurram
Muhammed Ali Khaqan


This porgram generates 12 E-15 puzzles and solves them. A* search method is used to find 
the most optimal path to the goal state.

H1 heuristic has been used to approximate the number of steps required to reach the goal state.
This heuristic calculates by counting the number of tiles in the puzzle that are out of place. 
This way it gives a very rough estimate of the number of further moves required to solve the puzle
        
"""
import numpy as np
import time
import random

from numpy import array
from random import sample


    
class Node():
    def __init__(self, state, num_shifted=0, g_cost=0, h_cost=0, parent=None, move=None):
        # current state of the node
        self.state = state

        #the tile number that had to be moved to get to the current state
        self.num_shifted = num_shifted 

        #the number of moves made to reach the state
        self.g_cost = g_cost 

        # The heuristic cost
        self.h_cost = h_cost

        #the parent node
        self.parent = parent

        #the direction the tile was moved to reach this state
        self.move = move
        
        #children nodes
        self.up = None 
        self.right = None
        self.down = None
        self.left = None

 
    #play a turn by moving the tile to the given direction to get a new state
    def play_turn(self, direction):

        #searching for the index of the empty tile (with value 0)
        zero_index = (0, 0) 
        for i in range(4):
            for j in range(4):
                if self.state[i][j] == 0:
                    zero_index = (i, j)
                    break
        

        if direction == 'right':
            if zero_index[1] == 0: 
                return False
            else:
                left_num = self.state[zero_index[0]][zero_index[1] - 1]
                new_state = self.state.copy()
                new_state[zero_index[0]][zero_index[1]] = left_num
                new_state[zero_index[0]][zero_index[1] - 1] = 0
                return new_state,left_num

        elif direction == 'left':
            if zero_index[1] == 3:
                return False
            else:
                right_num = self.state[zero_index[0]][zero_index[1] + 1]
                new_state = self.state.copy()
                new_state[zero_index[0]][zero_index[1]] = right_num
                new_state[zero_index[0]][zero_index[1] + 1] = 0
                return new_state,right_num

        elif direction == 'down':
            if zero_index[0] == 0:
                return False
            else:
                upper_num = self.state[zero_index[0] - 1][zero_index[1]]
                new_state = self.state.copy()
                new_state[zero_index[0]][zero_index[1]] = upper_num
                new_state[zero_index[0]-1][zero_index[1]] = 0
                return new_state,upper_num 

        else:
            if zero_index[0] == 3:
                return False
            else:
                lower_num = self.state[zero_index[0] + 1][zero_index[1]]
                new_state = self.state.copy()
                new_state[zero_index[0]][zero_index[1]] = lower_num
                new_state[zero_index[0] + 1][zero_index[1]] = 0
                return new_state,lower_num



    # Get number of misplaced tiles (heuristic)
    def get_heuristic(self, new_state, goal_state):
        h = 0

        for i in range(4):
            for j in range(4):
                if new_state[i][j] != goal_state[i][j]:
                    h+=1

        return h


    def print_path(self):
        movement = [self.move]      #setting self as the first movement
        state_trace = [self.state]  #starting trace with self as the staring node
        
        step_stack = [self.num_shifted] #the number that has been shifted
        depth_path = [self.g_cost]          #our g path that has been taken so far/ or the depth
        hr_cost = [self.h_cost]         #heuristic value taken so far
        
        # add node information as tracing back up the tree
        while self.parent:
            #setting self as the parent
            self = self.parent

            #adding self to the trace
            movement.append(self.move)
            state_trace.append(self.state)  

            step_stack.append(self.num_shifted)
            depth_path.append(self.g_cost)
            hr_cost.append(self.h_cost)

        steps = 0

        # Initial state
        value = movement.pop()

        temp1 = step_stack.pop()
        number = str(temp1)

        temp2 = depth_path.pop()
        depth = str(temp2)

        temp3 = hr_cost.pop()
        h_cost = str(temp3)

        total_steps = 0
        while (state_trace):

            print('\n', 'Step: {}'.format(steps))
            print(state_trace.pop())

            if (steps > 0):
                temp = step_stack.pop()
                number = str(temp)

                value = movement.pop()

                depth = depth_path.pop()
                h_cost = hr_cost.pop()
                
                total_cost = depth + h_cost
                total_steps = total_steps + depth

                if (value == 'up'):
                    print('moving {} {}'.format(number, 'up'))

                if (value == 'down'):
                    print('moving {} {}'.format(number, 'down'))

                if  (value == 'left'):
                    print('moving {} {}'.format(number, 'left'))

                if (value == 'right'):
                    print('moving {} {}'.format(number, 'right'))
                
                temp1 = str(depth)
                temp2 = str(h_cost)
                temp3 = str(total_cost)
                temp4 = str(total_steps)

                print('g = {}, h = {}, f = g + h ={}'.format(temp1,
                                                             temp2, temp3))
                print('total no of steps take: {}'.format(temp4))
            else:
                print('The Initial State')

            
            steps += 1




    #searches for the most optimum path from a start goal to the goal node
    def a_star_search(self,goal_state):

        queue = [(self,0)]  #[0]: node instance  [1]: estimate distance to goal f(x)
        visited = []  #to keep tabs on the already visited nodes
        
        queue_max_length = 1
        
        while queue:
            # sort the nodes according to the estimated cost to the node
            queue = sorted(queue, key=lambda x: x[1]) 

            # update maximum length of the queue
            if len(queue) > queue_max_length:
                queue_max_length = len(queue)

            #get the node which has the lowest cost
            current_node = queue.pop(0)[0]
            
            current_g = current_node.g_cost

            #add the current node to visited
            visited.append(tuple(current_node.state.reshape(1,16)[0]))

            
            #if the goal node is reached simply print the steps
            if np.array_equal(current_node.state, goal_state):
                current_node.print_path()
                return queue_max_length
                
            else:
                #moving up
                if current_node.play_turn('up'):
                    new_state, lower_num = current_node.play_turn('up')

                    #if state not already visited
                    if tuple(new_state.reshape(1,16)[0]) not in visited:
                        g_val = current_g + 1

                        # calculating heuristic cost to goal node
                        h_cost = self.get_heuristic(
                            new_state,
                            goal_state
                        )

                        #creating the new child node after the move
                        total_cost = g_val + h_cost
                        current_node.up = Node(
                            state = new_state,
                            parent = current_node,
                            move = 'up',
                            num_shifted = lower_num,
                            g_cost = g_val,
                            h_cost = h_cost
                        )
                        queue.append((current_node.up, total_cost))


                # moving right
                if current_node.play_turn('right'):
                    new_state, left_num = current_node.play_turn('right')

                    #if state not already visited
                    if tuple(new_state.reshape(1,16)[0]) not in visited:
                        g_val = current_g + 1

                        # calculating heuristic cost to goal node
                        h_cost = self.get_heuristic(
                            new_state,
                            goal_state
                        )

                        #creating the new child node after the move
                        total_cost = g_val + h_cost
                        current_node.right = Node(
                            state = new_state,
                            parent = current_node,
                            move = 'right',
                            num_shifted = left_num,
                            g_cost = g_val,
                            h_cost = h_cost
                        )
                        queue.append((current_node.right, total_cost)) 

                #moving down
                if current_node.play_turn('down'):
                    new_state, upper_num = current_node.play_turn('down')

                    #if state not already visited
                    if tuple(new_state.reshape(1,16)[0]) not in visited:
                        g_val = current_g + 1

                        # calculating heuristic cost to goal node
                        h_cost = self.get_heuristic(
                            new_state,
                            goal_state
                        )

                        #creating the new child node after the move
                        total_cost = g_val + h_cost
                        current_node.down = Node(
                            state = new_state,
                            parent = current_node,
                            move= 'down',
                            num_shifted = upper_num,
                            g_cost = g_val,
                            h_cost = h_cost
                        )
                        queue.append((current_node.down, total_cost))

                #moving left
                if current_node.play_turn('left'):
                    new_state, right_num = current_node.play_turn('left')

                    #if state not already visited
                    if tuple(new_state.reshape(1,16)[0]) not in visited:
                        g_val = current_g + 1

                        # calculating heuristic cost to goal node
                        h_cost = self.get_heuristic(
                            new_state,
                            goal_state
                        )

                        #creating the new child node after the move
                        total_cost = g_val + h_cost
                        current_node.left = Node(
                            state = new_state,
                            parent = current_node,
                            move = 'left',
                            num_shifted = right_num,
                            g_cost = g_val,
                            h_cost = h_cost
                        )
                        queue.append((current_node.left, total_cost))



class Puzzle():
    def __init__(self):
        self.puzzles = []

    
    #shuffles 12 puzzles and returns them
    def gen_puzzles(self):
        while len(self.puzzles) < 12:
            arr = np.array([1,2,3,4,2,3,4,5,3,4,5,5,4,5,5,0])
            for i in range (0,10):
                hello = 0
                result = np.where(arr == 0)
                while hello == 0:
                    list1 = [-4,-1,1,4]
                    hello = random.choice(list1)
                    
                    if((hello+result[0][0])>15 or(hello+result[0][0])<0 or((result[0][0]+1)%4 == 0 and hello == 1)or((result[0][0])%4 == 0 and hello == -1)):
                        hello = 0
                
                temp = arr[result[0][0]]
                arr[result[0][0]] = arr[result[0][0]+hello]
                arr[result[0][0]+hello] = temp 
            
            self.puzzles.append(np.array(arr).reshape(4,4))
        return self.puzzles



    
goal_state = np.array([1,2,3,4,2,3,4,5,3,4,5,5,4,5,5,0]).reshape(4,4)
puzzle_gen = Puzzle()
puzzles = puzzle_gen.gen_puzzles()
count = 1
for puzzle in puzzles:
    print("puzzle number: ", count)
    count = count +1
    print(puzzle)


#initial_state_one = np.array([1,2,3,4,2,3,4,5,0,4,5,5,3,4,5,5]).reshape(4,4)
i = 0
for i in range (0,12):
    print('Trace of initial state :', i+1)
    root_node = Node(state=puzzles[i],num_shifted=0 ,g_cost=0,h_cost=0)
    print(root_node.a_star_search(goal_state))
