# author michael leek
import sys
import time
def Knapsack_approximation(sack, weight):
 print("just show that I am running") 
# i probably actually dont need a recursive helper
 
#  def recursive_helper(weight_left,index):
     

def main():


#input format
    # W weight we can take from the bag
    #n items in the bag
    #n lines of the format "ITEM Value Weight"


  print("lets approximate max knapsack!")
  # code for taking in input , use knapsack_input.py to generate a file of the appropriate format
  w = float(input())
  n = int(input())
  items = []
  for _ in range(n):
    i = input().split()
    i[1] = float(i[1])
    i[2] = float(i[2])
    items.append(i)
  print(items)


#start knapsack code
  start_time = time.time()
#  t_val, items_n_sack = Knapsack_approximation(items,w)
  Knapsack_approximation(items,w)
#  end = time.time()
#  print("Results:")
#  print("    Total Value: %0.2f" % t_val)
#  print("    Items:")
#  for i in items_n_sack:
#     print("        ", i[0], i[1], i[2])
#  print("")
#  print("Time taken: %fs" % (end- start_time))
  print("we got to the end!")
if __name__ == "__main__":
    main()
