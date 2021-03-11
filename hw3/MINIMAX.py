#MINIMAX - PART A
""" 
Group Members: Taha Khurram, Umer Shamaan, Hassan Raza, Muhammad Ali Khaqan

Project Description: First part of HW3, Code for MINIMAXING
INPUT: 9 Integer Values - A,B,C,D,E,F,G,H,I
"""

from io import StringIO

def minimax(myStr):
    #split the string into an array of integers
    data = myStr.split()
    A = data[0]
    B = data[1]
    C = data[2]
    #L

    D = data[3]
    E = data[4]
    F = data[5]
    #M

    G = data[6]
    H = data[7]
    I = data[8]
    #R

    temp1 = min(A , B)
    minL = min(temp1 , C)   #min of L calculated

    temp2 = min(D, E)
    minM = min(temp2, F)    # min of M calculated

    temp3 = min(G, H)
    minR = min(temp3, I)    # min of R calculated

    temp4 = max(minL, minM)
    maxVal = max(temp4, minR)   #max value has been calculated

    if(maxVal == minR):
        print("R")
    elif(maxVal == minL):
        print("L")
    elif(maxVal == minM):
        print("M")
    else:
        print("Error")
    #print("The max value: ", maxVal, " The min values: ", minL, " ", minM, " ", minR)


if __name__ == "__main__":
    # taking given data for part1
    print("Part 1")
    minmax1 = "5 3 1 2 5 4 1 3 3"
    minimax(minmax1)
    #taking data from user
    print("Part 2")
    minmax2 = input("Enter your values: ")
    minimax(minmax2)