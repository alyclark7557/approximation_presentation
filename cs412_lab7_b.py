"""
    name:  Jonny Lynch
    
"""

import time

def Knapsack(items, weight):
    optimal_knapsack = []
    items = sorted(items, key=lambda item: item[1] / item[2], reverse=True)
    for item in items:
        remaining_w = weight - item[2]
        if remaining_w > 0:
            optimal_knapsack.append(item)
            weight -= item[2]
        else:
            item[1] = round((weight/item[2]) * item[1], 1)
            item[2] = round((weight/item[2]) * item[2], 1)
            optimal_knapsack.append(item)
            break
    return optimal_knapsack

def main():
    weight = float(input())
    n = int(input())
    #items = [input().split(" ") for _ in range(n)] I don't know why this doesn't work but it always keeps the return carrage
    items = []
    for i in range(n):
        item = input().split(" ")
        item[2].replace('\r', '')
        item[1] = float(item[1])
        item[2] = float(item[2])
        items.append(item)
    start = time.time()
    optimal_items = Knapsack(items, weight)
    end = time.time()
    '''
    for item in optimal_items:
        if item != optimal_items[-1]:
            print("%s(%0.2f, %0.2f) " % (item[0], item[1], item[2]), end="")
        else:
            print("%s(%0.2f, %0.2f)" % (item[0], item[1], item[2]), end="")
    print()
    sum = 0
    for item in optimal_items:
        sum += item[1]
    print("%0.1f" % sum)
    '''

    print("Results:")
    sum = 0
    for item in optimal_items:
        sum += item[1]
    print("    Total Value: %0.2f" % sum)
    print("    Items:")
    for i in optimal_items:
        print("        ", i[0], i[1], i[2])
    print("")
    print("Time Taken: %fs" % (end - start))

if __name__ == "__main__":
    main()