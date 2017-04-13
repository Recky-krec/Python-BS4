import bs4 as bs
import urllib.request
import re
import os
import folderBot
from constants import *
from ordinaryFunctions import *

folderBot.init()

def userPreferences():
    """Use user input for retrieving desired background"""
    backgroundTheme = input("Inser favorite background theme: ")
    url = 'https://www.pexels.com/search/' + str(backgroundTheme)
    #todo: maybe write preferences in a file
    return url

url = userPreferences()

def webRequest(url):
    """Creates a request based in the url"""
    req = urllib.request.Request(url, headers=headers) #Creating a request
    raw_sauce = urllib.request.urlopen(req) #Opening url with created request
    sauce = raw_sauce.read() #Source code
    soup = bs.BeautifulSoup(sauce, features="lxml") #Creating BS4 object

    return soup

soup = webRequest(url)

#Finding all images in url affected by userPreferences
def imageScraping():
    for url in soup.find_all("a"):
        imageWebPath = url.get("href")

        if typeNone(imageWebPath): pass

        else:
            if re.match(pattern, imageWebPath):
            #Fieltering undesired links, and writting desired ones(wallpapers) in a file
                with open("photos-urls.txt", "a") as f:
                    f.write(wallpaperSite + imageWebPath + "\n")


def finalURL(downloadCount):
    with open("photos-urls.txt","r") as k:
        for x in range(downloadCount):

            downloadUrls = k.readline()
            soup = webRequest(downloadUrls)

            for actualURL in soup.find_all("a"):
                imageWebPath = actualURL.get("href")

                if typeNone(imageWebPath):
                    pass

                else:
                    if re.match(pattern2, imageWebPath):
                        # Fieltering undesired links, and writting desired ones(wallpapers) in a file
                        with open("dw-links.txt", "a") as f:
                            f.write(imageWebPath + "\n")


def imageDownloader(downloadCount):
    """"""
    with open("dw-links.txt","r") as m:
        for x in range(downloadCount):
            downloadUrls = m.readline()

            file_name = nameGenerator()
            file_name = "".join(file_name)

            #Write file-name to a file
            with open("file-name.txt", "a") as n:
                n.write(wallpapersPath+"/"+file_name+"\n")
            print(file_name)
            os.system("wget -O {} {}".format(file_name, downloadUrls))
            os.system("mv wallpaper* myWallpapers/")

def ubuntuBackground():
    with open("file-name.txt", "r") as k:
        change_background = str(input("Change background? (y/n)"))
        if change_background == "y":
            file_name = k.readline()

            os.system("gsettings set org.gnome.desktop.background picture-uri file:{}".format(file_name))
        elif change_background == "n":
            quit()
        
        else:
            ubuntuBackground()
if __name__ == "__main__":
    imageScraping()
    dwQuantity = int(downloadCount())
    finalURL(dwQuantity)
    linkUniq()
    imageDownloader(dwQuantity)
    ubuntuBackground()
    folderBot.quit()
