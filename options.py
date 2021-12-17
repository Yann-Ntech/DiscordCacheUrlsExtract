options = { }

class option:
    def __init__(self, description, fun):
        self.description = description
        self.fun = fun

def newOption(position, description, fun):
    options[position] = option(description,fun)

def userInput():
    Input = input("Option: ")
    return options[Input]

def allDescriptions():
    for k in options:
        print("Description: " + options[k].description)

def getRegex():
    print("Type 'help' to display descriptions.")
    try:
        Input = userInput()
        return Input.fun()
    except KeyError:
        print("Invalid option")
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