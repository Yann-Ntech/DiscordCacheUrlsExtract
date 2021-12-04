#enter your $USER name
usr = '/home/urmom'

#Directorys
d_fcache = usr + '/Desktop/UrlsExtract/fakeCache'
d_cache = usr + '/.config/discord/Cache' #discord cache
d_downlCache = usr + '/Desktop/UrlsExtract/downlCache'
d_UrlsExtract = usr + '/Desktop/UrlsExtract'
urlsList = []


# moves files from real dicord cache into fake cache to avoid 'cant read IsaDirectoryError'
Cache = "sudo find " + d_cache + " -type f -exec mv -t " + d_fcache + "/ {} \; && sudo chmod 777 -R " + d_fcache


