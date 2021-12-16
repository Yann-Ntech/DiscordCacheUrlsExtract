# Discord Uncacher Linux

Added on to original and added some personal functions

Script to extract urls from files found in discord cache and to download the urls if you want to:

![url](https://user-images.githubusercontent.com/22084147/144713308-1b43ce54-a556-406c-8cac-064d3bada2e7.png)

Should work on linux and MacOS -- it most likely will not work on your computer unless you have a similar filesytem but feel free to edit it as you want. You will see the directory structure in bashOS.py.

If you are on MacOS the bash os.system() commands might differ and not work, so make sure that bashOS.py is compatible with your OS:

Bash in bashOS.py:

![bashsystem](https://user-images.githubusercontent.com/22084147/144713707-d96ef940-fdcf-4288-8527-36f00ef077d9.png)

Bash in extract.py:
![bashsystem](https://user-images.githubusercontent.com/22084147/144716197-6dcf61a8-2b4a-4c3e-9fae-bc5a5b0be972.png)



# How to use
```cd Desktop```

```git clone https://github.com/beans816/DiscordUncacher```

Choose what you want to filter your cache to and edit accordingly in extract.py:

![urlFilter](https://user-images.githubusercontent.com/22084147/144713378-87f6cab5-32e4-4eb4-b14d-c3aa1d47a597.png)



```sudo python3 extract.py```




