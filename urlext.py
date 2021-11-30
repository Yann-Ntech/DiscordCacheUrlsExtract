import re, os, csv

def readFile(file):

    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        fileStrings = f.readlines()
        regex = 'https://.*(png|jpg|mp4)'
        for line in fileStrings:
            result = re.search(regex, line)
            if result:
                return(result.group()) # return url


d_fcache = '/home/be/Desktop/fakeCache'
d_cache = '/home/be/.config/discord/Cache'

urlsList = []

# 1.move files from real sicord cache into fake cache to avoid 'cant read IsaDirectoryError'
#find /home/be/.config/discord/Cache -type f
commandCache = "sudo find " + d_cache + " -type f -exec mv -t " + d_fcache + "/ {} \; && sudo chmod 777 -R " + d_fcache #command to be executed bash
res = os.system(commandCache) # runs above command

for file in os.listdir(d_fcache):
    pathFile = os.path.join(d_fcache, file)
    url = readFile(pathFile)
    if url is not None:
        urlsList.append(url)

#writes csv file
with open('urls.csv', 'w') as f:
    writer = csv.writer(f, delimiter="\n")
    writer.writerow(urlsList)

#moves contents of fakeCache into shredder and shreds using killerbean
#wont work unless you have set killerbean to shred the diectory /shred otherwise you might mistakenly destroy your /boot file o-o
#uncomment to use but at your own risk
#commandShred = "sudo find " + d_fcache + " -type f -exec mv -t /home/be/Desktop/shred/ {} \; && sudo ./killerbean" #shreds cache
#res = os.system(commandShred) # runs above command
