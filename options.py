import re, os, csv, requests
import getpass
#
#
#
#
#
#
#
#
usr = '/home/' + getpass.getuser()

#Directorys
d_fcache = usr + '/Desktop/DiscordUncacher/fakeCache'
d_cache = usr + '/.config/discord/Cache' #discord cache
d_downlCache = usr + '/Desktop/DiscordUncacher/downlCache'
d_UrlsExtract = usr + '/Desktop/DiscordUncahcer'

urlsList = []
regex_options = { }
#
#
#
#
#
#
#
#

#############REGEX FILTERING#############

class option:
    def __init__(self, description, fun):
        self.description = description
        self.fun = fun

def newOption(position, description, fun):
    regex_options[position] = option(description,fun)

def userInput():
    Input = input("Option: ")
    return regex_options[Input]

def allDescriptions():
    for k in regex_options:
        print("Description: " + regex_options[k].description)

def getRegex():
    print("Type 'help' to display descriptions.")
    try:
        Input = userInput()
        return Input.fun()
    except KeyError:
        print("\e[6;33m Please input y/n \e[0m")
        allDescriptions()
        return getRegex()

        
def handleHelp ():
    allDescriptions()
    return getRegex()

newOption("0"," 0 : Attachments", lambda : "https://media.discordapp.net/attachments/*.*(png|jpg)")
newOption("1"," 1 : General", lambda : "https://*.*(png|jpg|mp4|mov)")
newOption("2"," 2 : Emojis", lambda : "https://cdn.discordapp.com/emojis/*.*(png|jpg)")
newOption("3"," 3 : Stickers", lambda : "https://media.discordapp.net/stickers/*.*(png|jpg) ")
newOption("4"," 4 : External Attachments", lambda : "https://images-ext*.*(png|jpg|mp4|mov)")
newOption("5"," 5 : Fun!", lambda : "kewlkidsregex")
newOption("help","Help", lambda : handleHelp())
                    
def process ():
    return getRegex()
    
#print(process())  
regex = str(process())
print("store: " + regex)
print(type(regex))

#
#
#
#
#
#
#
#

#############   BASH SCRIPT COMMANDS   #############

# moves files from real dicord cache into fake cache to avoid 'cant read IsaDirectoryError'
Cache = "sudo find " + d_cache + " -type f -exec mv -t " + d_fcache + "/ {} \; && sudo chmod 777 -R " + d_fcache
#Why: files naturally download where the script is
#Chmod: recursively gives entire file and its contents read, write and execute permisions for current user
Move = "mv "+ d_UrlsExtract + '/' + fileName + " " + d_downlCache + '/' + fileName + " && sudo chmod 666 -R " + d_downlCache
RmCache = ""
MoveFake= ""

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

                    res = os.system(Move)
    elif prompt_downl == 'n':
        pass
    else:
        print("\n")
        os.system('printf "\e[6;33m Please input y/n \e[0m"')
        print("\n")
        #recall function until valid value passed
        chooseDownl()

def chooseDel():
    prompt_del = input("Would you like your cache to be deleted or restored? \n Input 'd' to delete or 'r' to restore: ")
    if prompt_del == 'd':
        #deletes cache
        pass
    elif prompt_del == 'r':
        #restores cache
        pass
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
