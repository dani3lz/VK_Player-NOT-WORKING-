# VK Player
[![Icon](https://i.imgur.com/GGSlTqE.png)](https://github.com/dani3lz/VK_Player)

## Libraries

**VK Player** is an application that works on **PyQt5** and **vk_api** library.

- **PyQt5** is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.
PyQt5 may also be embedded in C++ based applications to allow users of those applications to configure or enhance the functionality of those applications.

- **vk_api** is a library that helps you create scripts based on VK.com API.

- Other libraries are also used, such as **mutagen**, **threading**, **json**, **shutil**, **requests** etc., that contribute to the operation of the application.

## Features

**VK Player** at the moment can read your music from your VK page and write information about songs in json file. Also VK Player can download all your music in new folder. The offline function will also be available after this process.

But first of all let's not forget that this application is a music player, therefore VK Player has functions like:
- shuffle
- repeat this
- repeat once. 

In addition, this player contains a volume slider and a song progress slider.
It also has a list of all the songs from your VK profile and also if the song has a cover, then it is illustrated next to the list of songs, otherwise, a default image is illustrated which is taken from the "img" folder.

Example 1 | Example 2
:-------------------------:|:-------------------------:
![Offline Mode](https://i.imgur.com/6ftddBx.png) | ![Online Mode](https://i.imgur.com/2ykmsg4.png)

## Login
Logging on to VK.com is also done in **VK Player**. The user must enter the login, password and VK ID (VK ID must contain only digits). If the user has two factor authentication, then a new window will appear where you will have to enter the code. 
A new image captcha window will also appear if requested by VK.com. And last but not least, if the user enters the wrong data, then he will be informed below the "Login" button.

![Login](https://i.imgur.com/ITV63Hd.png)

**VK Player** by dani3lz (c)
