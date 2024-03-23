import sys

def check_uniqueness(tup):
    if len(tup) == len(set(tup)):
        print("All elements are unique")
    else:
        print("Not all elements are unique")

if __name__ == "__main__":
    tup = tuple(sys.argv[1:])
    check_uniqueness(tup)
