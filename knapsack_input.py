import random
import os
import sys

def create_input_file(n, fn):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    w = str(round(random.random() * n * 2, 1))
    #w = str(sys.maxsize)
    num = str(n)
    try:
        os.remove(fn)
    except:
        print("No file to remove")
    f = open(fn, "a")
    f.write(w + "\n")
    f.write(num + "\n")
    for _ in range(n):
        item_name = ""
        for _ in range(5):
            item_name += letters[int(random.random() * 26)]
        item_value = str(round(random.random() * n * 10, 1))
        item_weight = str(round(random.random() * n, 1))
        f.write(item_name + " " + item_value + " " + item_weight + "\n")
    f.close()

def not_main():
    fn = sys.argv[1]
    n = int(sys.argv[2])
    create_input_file(n, fn)

if __name__ == "__main__":
    not_main()