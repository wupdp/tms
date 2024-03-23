import os
import sys

def find_files(directory, substring):
    found_files = [file for file in os.listdir(directory) if substring in file]
    print(found_files)

if __name__ == "__main__":
    directory = sys.argv[1]
    substring = sys.argv[2]
    find_files(directory, substring)
