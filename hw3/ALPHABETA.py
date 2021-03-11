#ALPHABETA - PART B
""" 
Group Members: Taha Khurram, Umer Shamaan, Hassan Raza, Muhammad Ali Khaqan

Project Description: First part of HW3, Code for ALPHABETA PRUNING
INPUT: 9 Integer Values - A,B,C,D,E,F,G,H,I
"""
#Initial values for Aplha and Beta
MAX = float('inf')  #Positive infinity
MIN = float('-inf') #negative infinity

def listOfPrunedChildren(i, data):
    i = i + 1
    values = ""
    if i >= 0 and i <= 2:
        #L
        #print("The value is pruned from the L subtree")
        for j in range(i,3):
            if(j == 0):
                values += "A "
            elif(j == 1):
                values += "B "
            elif(j == 2):
                values += "C "
            else:
                print("Error")

    elif i >= 3 and i <= 5:
        #M
        #print("The value is pruned from the M subtree")
        for j in range(i, 6):
            if(j == 3):
                values += "D "
            elif(j == 4):
                values += "E "
            elif(j == 5):
                values += "F "
            else:
                print("Error")

    else:
        #R
        #print("The value is pruned from the R subtree")
        for j in range(i, 9):
            if(j == 6):
                values += "G "
            elif(j == 7):
                values += "H "
            elif(j == 8):
                values += "I "
            else:
                print("Error")
    
    print("Values pruned: ", values)


def minimax(depth, nIndex, MinOrMax, data, alpha, beta):
    #leaf node
    if depth == 2:
        return data[nIndex]

    if MinOrMax == 1:
        best = MIN
        temp = 0
        # Recursion for left, middle, and right children
        for i in range(0, 3):
            val = minimax(depth + 1, nIndex * 3 + i, 0, data, alpha, beta) #False is for minimum
            best = max(best, val)
            
            if(best > alpha):
                temp = i    #if best is in right temp = 2, if best is in middle temp = 1, if best is left temp = 0
                            #0(left node) , 1(Middle node) , 2(Right node)
            
            alpha = max(alpha, best)

            #Pruning
            if alpha >= beta:
                #print("Pruned at depth: ", depth)
                #print("Value of alpha: ", alpha, " The value of beta: ", beta)
                listOfPrunedChildren(nIndex * 3 + i, data)
                break
        
        if(temp == 0):
            print("L")
        elif(temp == 1):
            print("M")
        elif(temp == 2):
            print("R")
        else:
            print("Error")
        return best

    else:
        best = MAX

        # Recur for left, middle and right children
        for i in range(0, 3):
            val = minimax(depth + 1, nIndex * 3 + i, 1, data, alpha, beta)  #true is for max
            best = min(best, val)
            beta = min(beta, best)

            #Pruning
            if alpha >= beta:
                #print("Pruned at depth: ", depth)
                #print("Value of alpha: ", alpha, " The value of beta: ", beta)
                listOfPrunedChildren(nIndex * 3 + i, data)
                break

        return best

#Main
if __name__ == "__main__":
    print("Part 1")
    data = [5, 3, 1, 2, 5, 4, 1, 3, 3]
    minimax(0, 0, 1, data, MIN, MAX)

    print()
    
    print("Part 2")
    data = [5, 2, 2, 5, 1, 3, 2, 4, 2]
    minimax(0, 0, 1, data, MIN, MAX)

    print()

    print("Part 3")
    data = [1, 3, 4, 1, 4, 1, 3, 5, 3]
    minimax(0, 0, 1, data, MIN, MAX)

    print()

    print("Part 4")
    myStr = input("Enter your values: ")
    data = myStr.split()
    data = list(map(int, data))
    minimax(0, 0, 1, data, MIN, MAX)
