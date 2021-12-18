import re, os, csv, requests
#custom imports
from bashOS import *
from options import *

def readFile(file):

    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        fileStrings = f.readlines()

        for line in fileStrings:
            result = re.search(regex, line)
            if result:
                return(result.group()) # return url

def populate():
    res = os.system(Cache) # runs cache command to move files from the discord cache into the fake cache
    #populates array
    for file in os.listdir(d_fcache):
        pathFile = os.path.join(d_fcache, file)
        url = readFile(pathFile)
        if url is not None:
           
            urlsList.append(url)
            print(urlsList)
            return urlsList

def chooseCsv():
    prompt_csv = input("Would you like a list of the URLS y/n: ")

    if prompt_csv == 'y':
        #writes csv file
        with open('urls.csv', 'w') as f:
            writer = csv.writer(f, delimiter="\n")
            writer.writerow(urlsList)
    elif prompt_csv == 'n':
        pass
    else:
        print("\n")
        os.system('printf "\e[6;33m Please input y/n \e[0m"')
        print("\n")
        #recall function until valid value passed
        chooseCsv()

def chooseDownl():
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
    elif prompt_downl == 'n':
        pass
    else:
        print("\n")
        os.system('printf "\e[6;33m Please input y/n \e[0m"')
        print("\n")
        #recall function until valid value passed
        chooseDownl()

def cacheDel():
    prompt_del = input("Would you like your cache to be deleted or restored? \n Input 'd' to delete or 'r' to restore: ")
    if prompt_csv == 'd':
        #deletes cache
    elif prompt_csv == 'r':
        #restores cache
    else:
        print("\n")
        os.system('printf "\e[6;33m Please input d/r \e[0m"')
        print("\n")
        #recall function until valid value passed
        chooseDel()

def WOAH_LOOK_AT_THESE():

    populate()
    chooseCsv()
    chooseDownl()
    chooseDel()

WOAH_LOOK_AT_THESE()
