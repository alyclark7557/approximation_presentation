import random
import os

def create_input_file(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    w = str(round(random.random() * n * 2, 1))
    num = str(n)
    os.remove("knapsack_in.txt")
    f = open("knapsack_in.txt", "a")
    f.write(w + "\n")
    f.write(num + "\n")
    for _ in range(n):
        item_name = ""
        for i in range(5):
            item_name += letters[int(random.random() * 26)]
        item_value = str(round(random.random() * n * 10, 1))
        item_weight = str(round(random.random() * n, 1))
        f.write(item_name + " " + item_value + " " + item_weight + "\n")
    f.close()

def not_main():
    n = int(input())
    create_input_file(n)

if __name__ == "__main__":
    not_main()
