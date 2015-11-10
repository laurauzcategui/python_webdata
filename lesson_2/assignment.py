import re

files = ''

def process_file(filename):
    with open(filename, 'rb') as f:
        print sum([int(elem) for line in f if re.search('[0-9]+', line) is not None for elem in re.findall('[0-9]+', line)])

files = 'regex_sum_198539.txt'
process_file(files)
