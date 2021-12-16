import re, os, csv, requests


#custom imports
from bashOS import *

def chooseType():
    #print file filter types:
    print("FILE TYPES: \n 1] all \n 2] attachments \n 3] external attachments \n 4] emojis \n 5] stickers")
    #prompt for what filter is wanted
    prompt_type = input("What kind of files do you want to download? Enter number: ")
    #error handling
    global regex
        #exec get_link()
        #regex = 'https://media.discordapp.net/attachments/*.*(png|jpg)' #this is usually the filter people want when looking in their cache
        #filters to only attachments/ examples of other filters you can use:
        #general filter: https://*.*(png|jpg|mp4|mov)
        #emojis: https://cdn.discordapp.com/emojis/*.*(png|jpg) 
        #stickers: https://media.discordapp.net/stickers/*.*(png|jpg) 
        #external attachments hosted on different sites: https://images-ext*.*(png|jpg|mp4|mov)

    if prompt_type == '1':
        regex = 'https://*.*(png|jpg|mp4|mov)'
        print("file type urls: " + regex)
    elif prompt_type == '2':
        regex = 'https://media.discordapp.net/attachments/*.*(png|jpg)'
        print("file type urls: " + regex)
    else:
        print("\n")
        os.system('echo -e "\033[5;41;1;37m   Invalid input, restarting filter process...   \033[0m"')
        print("\n")
        #recall function until valid value passed
        chooseType()

chooseType()

print("regex link: " + regex)


print(regex)
def readFile(file):

    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        fileStrings = f.readlines()

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
        os.system('echo -e "\033[5;41;1;37m   Invalid input, please enter y/n   \033[0m"')
        print("\n")
        #recall function until valid value passed
        chooseCsv()

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
        os.system('echo -e "\033[5;41;1;37m   Invalid input, please enter y/n    \033[0m"')
        print("\n")
        #recall function until valid value passed
        chooseDownl()

chooseDownl()
