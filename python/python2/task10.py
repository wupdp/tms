import sys

def common_and_unique(list1, list2):
    common = list(set(list1) & set(list2))
    unique = list(set(list1) ^ set(list2))
    print("Common elements:", common)
    print("Unique elements:", unique)

if __name__ == "__main__":
    list1 = sys.argv[1].split(',')
    list2 = sys.argv[2].split(',')
    common_and_unique(list1, list2)
