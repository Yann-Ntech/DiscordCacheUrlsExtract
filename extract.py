import re, os, csv, requests


#custom imports
from bashOS import *

def readFile(file):

    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        fileStrings = f.readlines()
        regex = 'https://media.discordapp.net/attachments/*.*(png|jpg)' #this is usually the filter people want when looking in their cache
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

#populates array
for file in os.listdir(d_fcache):
    pathFile = os.path.join(d_fcache, file)
    url = readFile(pathFile)
    if url is not None:
        urlsList.append(url)

prompt_csv = input("Would you like a list of the URLS y/n: ")

if prompt_csv == 'y':
    #writes csv file
    with open('urls.csv', 'w') as f:
        writer = csv.writer(f, delimiter="\n")
        writer.writerow(urlsList)
else:
    pass

prompt_downl = input("Would you like to download the URLS y/n: ")
if prompt_downl == 'y':
    #downloads images
    for file in os.listdir(d_fcache):
        pathFile = os.path.join(d_fcache, file)
        url = readFile(pathFile)
        if url is not None:
            r = requests.get(url)
            fileName = url.split('/')[-1] #file is named the same as the original file name
            with open(fileName, 'wb') as f: #saves file
                newfile = f.write(r.content) #writes url into a new file
                #Why: files naturally download where the script is
                #Chmod: recursively gives entire file and its contents read, write and execute permisions for current user
                Move = "mv "+ d_UrlsExtract + '/' + fileName + " " + d_downlCache + '/' + fileName + " && sudo chmod 666 -R " + d_downlCache
                res = os.system(Move)
else:
    pass
