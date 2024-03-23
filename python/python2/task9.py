import sys

def replace_vowels(string):
    vowels = 'aeiouAEIOU'
    new_string = ''.join(['-' if char in vowels else char for char in string])
    print(new_string)

if __name__ == "__main__":
    string = sys.argv[1]
    replace_vowels(string)
