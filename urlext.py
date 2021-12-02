import re, os, csv

#custom imports
from bashOS import *

def readFile(file):

    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        fileStrings = f.readlines()
        regex = 'https://media.discordapp.net/attachments/*.*(png|jpg|mp4|mov)' #this is usually the filter people want when looking in their cache
        #filters to only attachments/ examples of other filters you can use:
        #general filter: https://*.*(png|jpg|mp4|mov)
        #emojis: https://cdn.discordapp.com/emojis/*.*(png|jpg) 
        #stickers: https://media.discordapp.net/stickers/*.*(png|jpg) 
        #external attachments hosted on different sites: https://images-ext*.*(png|jpg|mp4|mov)
        for line in fileStrings:
            result = re.search(regex, line)
            if result:
                return(result.group()) # return url


res = os.system(Cache) # runs cache command to move files from the discord cache into the fake cache

for file in os.listdir(d_fcache):
    pathFile = os.path.join(d_fcache, file)
    url = readFile(pathFile)
    if url is not None:
        urlsList.append(url)

#writes csv file
with open('urls.csv', 'w') as f:
    writer = csv.writer(f, delimiter="\n")
    writer.writerow(urlsList)


#res = os.system(Shred) # runs shred command that safely deletes all the files in the fake cache
