import sys

def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median_value = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median_value = numbers[n//2]
    return median_value

if __name__ == "__main__":
    numbers = list(map(int, sys.argv[1:]))
    print(median(numbers))
