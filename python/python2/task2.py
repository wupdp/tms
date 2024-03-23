import sys

def count_chars(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    digit_count = sum(1 for char in string if char.isdigit())
    punctuation_count = sum(1 for char in string if char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    
    print(f"Upper case letters: {upper_count}")
    print(f"Lower case letters: {lower_count}")
    print(f"Digits: {digit_count}")
    print(f"Punctuation: {punctuation_count}")

if __name__ == "__main__":
    string = " ".join(sys.argv[1:])
    count_chars(string)
