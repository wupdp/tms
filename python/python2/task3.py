import sys

def common_elements(list1, list2):
    common = [elem for elem in list1 if elem in list2]
    print(common)

if __name__ == "__main__":
    list1 = sys.argv[1].split(',')
    list2 = sys.argv[2].split(',')
    common_elements(list1, list2)
