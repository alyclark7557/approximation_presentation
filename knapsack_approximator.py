# author Michael Leek
# The approximation solution for the max knapsack problem
# This algorithmn is greedy because it makes the greedy choice of assuming that all items in the knapsack with high value to weight ratios
#   will be in the final solution

# This program runs in nlog(n) time as the sort algorithmn takes log(n) time and then we need to iterate through every item of the sorted list
import sys
import time
def Knapsack_approximation(sack, weight):
 # sort the sack
 # add items to the list until i am out of available weight
 sack.sort(key=lambda x: x[1] / x[2], reverse=True) 
 ret_value = []
 keep_going = True
 index = 0
 weight_remaining = weight
 while (weight_remaining > 0 and index < len(sack)):

     if sack[index][2] <= weight_remaining:
         ret_value.append(sack[index])
         weight_remaining -= sack[index][2]
    
     index = index + 1
 return ret_value
def main():


#input format
    # W weight we can take from the bag
    #n items in the bag
    #n lines of the format "ITEM Value Weight"


  # code for taking in input , use knapsack_input.py to generate a file of the appropriate format
  w = float(input())
  n = int(input())
  items = []
  for _ in range(n):
    i = input().split()
    i[1] = float(i[1])
    i[2] = float(i[2])
    items.append(i)


#start knapsack code
  start_time = time.time()
  items_chosen = Knapsack_approximation(items,w)
  end = time.time()
  total_value = 0
  print("Results:")
  print("    Items:")
  for i in items_chosen:
     total_value += i[1]
     print("        ", i[0], i[1], i[2])
  print("")
  print("Time taken: %fs" % (end- start_time))
  print("    Total Value: %0.2f" % total_value)
if __name__ == "__main__":
    main()
