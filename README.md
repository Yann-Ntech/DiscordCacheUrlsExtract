# Discord Uncacher Linux

Added on to original and added some personal functions

Script to extract urls from files found in discord cache and to download the urls if you want to:

![url](https://user-images.githubusercontent.com/22084147/144713308-1b43ce54-a556-406c-8cac-064d3bada2e7.png)

You will see the directory structure in bashOS.py. Check that the directories comply with your file system so you dont get the 'directory does not exist' error.

# Bash that forces some funtionalities that JUST WORK

> libraries like shutil.move, os.rename and os.replace just never seemed to work! This is my solution using os.system.

Bash in bashOS.py:

![bashsystem](https://user-images.githubusercontent.com/22084147/144713707-d96ef940-fdcf-4288-8527-36f00ef077d9.png)

Bash in extract.py:
![bashsystem](https://user-images.githubusercontent.com/22084147/144716197-6dcf61a8-2b4a-4c3e-9fae-bc5a5b0be972.png)



# How to use
```cd Desktop```

```git clone https://github.com/beans816/DiscordUncacher```

```sudo python3 extract.py```




