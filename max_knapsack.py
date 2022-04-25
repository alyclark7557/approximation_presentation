import sys
import time

def Knapsack(items, weight):

    def Knapsackinator(w_remaining, i_index):
        if w_remaining == 0 or i_index >= len(items):
            return [0, []]
        elif w_remaining < 0:
            return [-sys.maxsize, []]
        with_item = Knapsackinator(w_remaining-items[i_index][2], i_index+1)
        without_item = Knapsackinator(w_remaining, i_index+1)
        with_item[0] += items[i_index][1]
        with_item[1].append(items[i_index])
        if with_item[0] >= without_item[0] and w_remaining-items[i_index][2] >= 0:
            return with_item
        else:
            return without_item
    return Knapsackinator(weight, 0)

def main():
    w = float(input())
    n = int(input())
    items = []
    for _ in range(n):
        i = input().split()
        i[1] = float(i[1])
        i[2] = float(i[2])
        items.append(i)
    print(items)
    start = time.time()
    t_val, items_n_sack = Knapsack(items, w)
    end = time.time()
    print("Results:")
    print("    Total Value: %0.2f" % t_val)
    print("    Items:")
    for i in items_n_sack:
        print("        ", i[0], i[1], i[2])
    print("")
    print("Time Taken: %fs" % (end - start))

if __name__ == "__main__":
    main()