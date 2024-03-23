import sys

def common_characters(str1, str2):
    common = set(str1) & set(str2)
    print(common)

if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    common_characters(str1, str2)
