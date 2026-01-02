from stats import generate_report
import sys

if(len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

generate_report(path)

