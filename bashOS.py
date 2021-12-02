#Directorys
d_fcache = '~/Desktop/fakeCache'
d_cache = '~/.config/discord/Cache'
urlsList = []


# moves files from real sicord cache into fake cache to avoid 'cant read IsaDirectoryError'
Cache = "sudo find " + d_cache + " -type f -exec mv -t " + d_fcache + "/ {} \; && sudo chmod 777 -R " + d_fcache

#shreds cache
Shred = "sudo find " + d_fcache + " -type f -exec mv -t /home/be/Desktop/shred/ {} \; && sudo ./killerbean" 
