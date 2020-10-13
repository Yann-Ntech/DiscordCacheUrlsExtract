__name__ = 'Url_to_jpg'
__author__ = 'Yann-NTECH'
__version__ = 0.1
__date__ = '12-10-2020'
__updated__ = '12-10-2020'

"""
Script to extract urls from files found in \Users\$User\Library\Application Support\discord\Cache\
"""

import re, os, csv

def readFile(file):
    '''
    read file, search urls with regex & return it
    :param file: file to read
    :return: Url extracted
    '''
    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        mystring = f.readlines()
        regex = 'https://.*(png|jpg)'
        for line in mystring:
            res = re.search(regex, line)
            if res:
                return(res.group())


DIRECTORY = '.\\files'
urlsList = []

for file in os.listdir(DIRECTORY):
    analyse = os.path.join(DIRECTORY, file)
    url = readFile(analyse)
    if url is not None:
        urlsList.append(readFile(analyse))

with open('urls.csv', 'w') as f:
    writer = csv.writer(f, delimiter="\n")
    writer.writerow(urlsList)
