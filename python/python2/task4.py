import sys

def sort_descending(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    print(sorted_numbers)

if __name__ == "__main__":
    numbers = list(map(int, sys.argv[1:]))
    sort_descending(numbers)
