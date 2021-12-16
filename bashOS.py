import getpass

usr = '/home/' + getpass.getuser()

#Directorys
d_fcache = usr + '/Desktop/DiscordUncacher/fakeCache'
d_cache = usr + '/.config/discord/Cache' #discord cache
d_downlCache = usr + '/Desktop/DiscordUncacher/downlCache'
d_UrlsExtract = usr + '/Desktop/DiscordUncahcer'
urlsList = []


# moves files from real dicord cache into fake cache to avoid 'cant read IsaDirectoryError'
Cache = "sudo find " + d_cache + " -type f -exec mv -t " + d_fcache + "/ {} \; && sudo chmod 777 -R " + d_fcache


