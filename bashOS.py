#enter your $USER name
usr = 'urmom'

#Directorys
d_fcache = '/home/' + usr + '/Desktop/UrlsExtract/fakeCache'
d_cache = '/home/' + usr + '/.config/discord/Cache' #discord cache
d_downlCache = '/home/' + usr + '/Desktop/UrlsExtract/downlCache'
d_UrlsExtract = '/home/' + usr + '/Desktop/UrlsExtract'
urlsList = []


# moves files from real sicord cache into fake cache to avoid 'cant read IsaDirectoryError'
Cache = "sudo find " + d_cache + " -type f -exec mv -t " + d_fcache + "/ {} \; && sudo chmod 777 -R " + d_fcache

#shreds cache
Shred = "sudo find " + d_fcache + " -type f -exec mv -t /home/be/Desktop/shred/ {} \; && sudo ./killerbean" 

