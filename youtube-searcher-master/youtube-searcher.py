#!/usr/bin/python3

import bs4 as bs
import urllib.request
import re
import os

def webRequest(url):
    """Creates a request based in the url"""
    headers = {"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
    req = urllib.request.Request(url, headers=headers) #Creating a request
    raw_sauce = urllib.request.urlopen(req) #Opening url with created request
    sauce = raw_sauce.read() #Source code
    soup = bs.BeautifulSoup(sauce, features="lxml") #Creating BS4 object

    return soup

def youtubeSearch():
    """Use user input for retrieving desired background"""
    query = input("Insert query: ") #this is a trivial input method, consider changing it ;)
    query_keywords = query.split(" ")
    print("+".join(query_keywords))

    url = 'https://www.youtube.com/results?search_query=' + "+".join(query_keywords)
    return url

def writeToFile(url_list):
	with open("found_urls.txt", "w") as f:
		for url in url_list:
			f.write("www.youtube.com{url}\n".format(url=url))

def parse():
	url_list = []
	url = youtubeSearch()
	source = webRequest(url)
	pattern = r'/watch'
	
	for link in source.find_all('a'):
		link = link.get('href')
		if re.match(pattern, link):
			url_list.append(link)

	return url_list
 
if __name__ == "__main__":
	url_list = parse()
	writeToFile(url_list)
