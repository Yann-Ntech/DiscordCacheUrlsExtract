import re, os, csv, requests
#
#
#
#
#
#
#
#
#################################################### CHECK THESE ARE CORRECT ####################################################
usr = '/home/YOUR_USERNAME_HERE' #enter in your computers username
d_fcache = usr + '/Desktop/LinuxDiscordUncacher/fakeCache'
d_cache = usr + '/.config/discord/Cache' #discord cache
d_downlCache = usr + '/Desktop/LinuxDiscordUncacher/downlCache'
d_UrlsExtract = usr + '/Desktop/LinuxDiscordUncacher'
##################################################################################################################################
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
##### CLEARS TERMINAL #####
os.system("clear")

#############   REGEX FILTERING   #############

class option_Regex:
    def __init__(self, description, fun):
        self.description = description
        self.fun = fun

def newOption(position, description, fun):
    regex_options[position] = option_Regex(description,fun)

def userInput_regex():
    print("_______________")
    Input_re = input("    Input: ")
    print("===============")
    return regex_options[Input_re]

def allregex_descriptions():
    print("_________")
    os.system('printf "\e[6;33mMAIN MENU\e[0m\n"')
    print("=========\n")
    for k in regex_options:
        print(regex_options[k].description)

def getRegex():
    allregex_descriptions()
    try:
        Input_re = userInput_regex()
        return Input_re.fun()
    except KeyError:
        print('\n')
        os.system('printf "\e[6;33m invalid input \e[0m"')
        print('\n')        
        ##### CLEARS TERMINAL #####
        os.system("sleep 2 && clear")
        allregex_descriptions()
        return getRegex()


newOption("0","0 : Attachments (png/jpg)", lambda : "https://media.discordapp.net/attachments/*.*(png|jpg)")
newOption("1","1 : Attachments (mp4/mov/gif)", lambda : "https://media.discordapp.net/attachments/*.*(png|jpg|mp4|mov|gif)")
newOption("2","2 : All videos and images", lambda : "https://*.*(png|jpg|mp4|mov)")
newOption("3","3 : All gifs", lambda : "https://*.*(gif)")
newOption("4","4 : Emojis", lambda : "https://cdn.discordapp.com/emojis/*.*(png|jpg|gif)")
newOption("5","5 : Stickers", lambda : "https://media.discordapp.net/stickers/*.*(png|jpg|gif) ")
newOption("6","6 : External Attachments", lambda : "https://images-ext*.*(png|jpg|mp4|mov)")
newOption("7","7 : ALL (beta)", lambda : "https://*.*")
newOption("8","8 : Fun! (beta)", lambda : "kewlkidsregex")
newOption("e","e : exit", lambda : exit())
                    
def process_Regex ():
    return getRegex()
    
regex = str(process_Regex())

##### CLEARS TERMINAL #####
os.system("clear")
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
# removes fake cache
RmCache = "sudo find " + d_fcache + " -exec shred {} -uvz \;"
#
#
#
#
#
#
#
#
#############   DOWNLOADING MENU && DICTIONARY   #############

uncache_options = { }

class option_Choose:
    def __init__(self, choice_descriptions, fun_choose):
        self.choice_descriptions = choice_descriptions
        self.fun_choose = fun_choose


def Option_Ch(position, choice_descriptions, fun_choose):
    uncache_options[position] = option_Choose(choice_descriptions,fun_choose)
    return uncache_options[position]

def userInput_choose():
    print("_______________")
    Input_ch = input("    Input: ")
    print("===============")
    return uncache_options[Input_ch]

def allchoice_descriptions():
    print("_______________")
    os.system('printf "\e[6;33mEXTRACTION MENU\e[0m\n"')
    print("===============\n")
    for k in uncache_options:
        print(uncache_options[k].choice_descriptions)

def extract_Error():
    try:
        Input_ch = userInput_choose()
        return Input_ch.fun_choose()
    except KeyError:
        print('\n')
        os.system('printf "\e[6;33m invalid input \e[0m"')
        print('\n')
        ##### CLEARS TERMINAL #####
        os.system("sleep 2 && clear")
        return getChoice()

def readFile(file):

    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        fileStrings = f.readlines()

        for line in fileStrings:
            result = re.search(regex, line)
            if result:
                return(result.group()) # return url

def populate():
    print("Populating arrays and fake cache ... \n")
    print("Depending on how large your cache is, this might take a long time ... \n")
    res = os.system(Cache) # runs cache command to move files from the discord cache into the fake cache
    #populates array
    for file in os.listdir(d_fcache):
        pathFile = os.path.join(d_fcache, file)
        url = readFile(pathFile)
        if url is not None:
            urlsList.append(url)
            print(urlsList)
            return urlsList

def getChoice():
    allchoice_descriptions()
    extract_Error()
        

def writeCsv():
    #populate url array and fake cache
    populate()
    print("Writing Csv ... ")
    with open('urls.csv', 'w') as f:
        writer = csv.writer(f, delimiter="\n")
        writer.writerow(urlsList)
    getChoice()

def writeDownl():
    #populate url array and fake cache
    populate()
    print("Downloading ... ")
    for file in os.listdir(d_fcache):
        pathFile = os.path.join(d_fcache, file)
        url = readFile(pathFile)
        if url is not None:
            r = requests.get(url)
            fileName = url.split('/')[-1] #file is named the same as the original file name
            with open(fileName, 'wb') as f: #saves file
                newfile = f.write(r.content) #writes url into a new file
                res = os.system("sudo mv "+ d_UrlsExtract + '/' + fileName + " " + d_downlCache + '/' + fileName + " && sudo chmod 777 -R " + d_downlCache)
    getChoice()

def Rm_Cache():
    print("Deleting, please have patience ... ")
    os.system(RmCache)
    print("Completed! The files are now unrecoverable (unless you see them in Discord again)")
    getChoice()

Option_Ch("c","c : make Csv file", lambda : writeCsv())
Option_Ch("d","d : download files from cache", lambda : writeDownl())
Option_Ch("r","r : delete fake cache (recommended)", lambda : Rm_Cache())
Option_Ch("e","e : exit", lambda : exit())

                    
def process_Choice ():
    return getChoice()

print(process_Choice())  
