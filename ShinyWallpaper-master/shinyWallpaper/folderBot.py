"""This file is used to track possible problems that may happen and fix them.
It will also be used to create directorys and files for the first time"""
import os

#Wallpaper directory&txt files
def init():
    try:
        os.mkdir("myWallpapers") #DO NOT RENAME
        with open("photos-urls.txt","a") as z: pass
        with open("dw-links.txt", "a")as p: pass
    except Exception: pass


def quit():
    """Cleans files urls"""
    with open("photos-urls.txt", "w"): pass
    with open("dw-links.txt", "w"): pass