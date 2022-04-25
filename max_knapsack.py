import sys

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
        if with_item[0] >= without_item[0]:
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
    print("Results: ", Knapsack(items, w))

if __name__ == "__main__":
    main()