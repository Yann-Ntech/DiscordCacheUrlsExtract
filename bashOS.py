#enter your $USER name
usr = 'urmom'

#Directorys
d_fcache = '/home/' + usr + '/Desktop/DiscordUncacher/fakeCache'
d_cache = '/home/' + usr + '/.config/discord/Cache' #discord cache
d_downlCache = '/home/' + usr + '/Desktop/DiscordUncacher/downlCache'
d_UrlsExtract = '/home/' + usr + '/Desktop/DiscordUncacher'
urlsList = []


# moves files from real sicord cache into fake cache to avoid 'cant read IsaDirectoryError'
Cache = "sudo find " + d_cache + " -type f -exec mv -t " + d_fcache + "/ {} \; && sudo chmod 777 -R " + d_fcache


