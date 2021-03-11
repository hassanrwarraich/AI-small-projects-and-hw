"""
Description: This program creates a simple k-d tree (with k value 2) from the data given in figure 19.2 of the Winston Text Book
             The fomred 2-d tree is similar to the one in figure 19.7 of the same book. To determine the color of the block, the 
             program simply traveres the tree accordingly until it reaches a leaf node. That way it searches for the closest neighbour
             to find the color.
Authors:    Hassan Raza
            Umer Shamaan
            Taha Khurram
            Muhammad Ali Khaqan

"""


class node:
  def __init__(self, data ,  color_left=None, color_right=None ):
    self.data = data
    self.right = None
    self.left = None
    self.color_left = color_left
    self.color_right = color_right


  def insert(self, root, key, k,i,j): 
    if (k==0):
      k = 1
    else:
      k = 0 
      
    if root is None: 
      if (i!=None):
        return node(key,i,j)
      return node(key) 
    elif root.data[k] < key[k]: 
      root.right = root.insert(root.right, key,k,i,j) 
    else: 
      root.left = root.insert(root.left, key,k,i,j) 
    return root 

  def search(self, root, key, k): 
    if (k==0):
      k = 1
    else:
      k = 0 
    
    if root.data[k] < key[k]:
      if root.right is None: 
        return root
      root = root.search(root.right, key,k) 
    else:
      if root.left is None: 
        return root 
      root = root.search(root.left, key,k) 
    return root 


if __name__ == "__main__":
  # inserting all the nodes in the tree
  n = node([3,3.5])
  k = 0 
  n.insert(n,[3.5,4],k,None,None)
  n.insert(n,[3,2],k,None,None)
  n.insert(n,[4,5.5],k,"purple","yellow")
  n.insert(n,[2,5.5],k,"orange","red")
  n.insert(n,[4,1.5],k,"green","blue")
  n.insert(n,[2,1.5],k,"violet","red")
   
  #In the testing below, search method looks into the tree and moves 
  #accordingly giving us the result
  #testing for first point
  x=1
  y=4
  print("1st input: U(" + str(x) + ", " + str(y) + ")")
  result = n.search(n,[x,y],k)
  if (result.data[1]>y):
    print("The color is " + result.color_left)
  else:
    print("The color is " + result.color_right)
  
  #testing for second point
  x=1
  y=1
  print("\n2nd input: U(" + str(x) + ", " + str(y) + ")")
  result = n.search(n,[x,y],k)
  if (result.data[1]>y):
    print("The color is " + result.color_left)
  else:
    print("The color is " + result.color_right)

  #testing for third point
  x=6
  y=6
  print("\n3rd input: U(" + str(x) + ", " + str(y) + ")")
  result = n.search(n,[x,y],k)
  if (result.data[1]>y):
    print("The color is " + result.color_left)
  else:
    print("The color is " + result.color_right)

  #testing for fourth point
  x=6
  y=1
  print("\n4th input: U(" + str(x) + ", " + str(y) + ")")
  result = n.search(n,[x,y],k)
  if (result.data[1]>y):
    print("The color is " + result.color_left)
  else:
    print("The color is " + result.color_right)


  #testing for last point by taking input from user
  print("\nUser defined input:")
  x=int(input("Please enter width:\n"))
  y=int(input("Please enter height:\n"))
  result = n.search(n,[x,y],k)
  if (result.data[1]>y):
    print("The color is " + result.color_left)
  else:
    print("The color is " + result.color_right)    

  

  

