import sys
from stats import get_report
from stats import get_num_words

if len(sys.argv) == 1:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
file_path = sys.argv[1]


print('============ BOOKBOT ============')
print('Analyzing book found at books/frankenstein.txt...')
print('----------- Word Count ----------')
num_words = get_num_words(file_path)
print(f'Found {num_words} total words')
print('--------- Character Count -------')
report = get_report(file_path)
for k in report:
    if k['char'].isalpha() == True:
        print(f"{k['char']}: {k['num']}")
print('============= END ===============')