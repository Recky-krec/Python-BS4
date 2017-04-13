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

def writeToFile(url_list, title_list):
	counter = 0

	with open("found_urls.txt", "w") as f:
		for title in title_list:
			title = str(title)
			counter += 1 
			
			title = title.replace("['title=\"","")

			title = title.replace("</a>']","")

			title = re.sub(r"\">.*","",title)

			title = re.sub(r"\\x.*\s","",title)

			f.write(str(counter) + ". - " + title + "\n\n")

		counter = 0		

		for url in url_list:
			f.write("{num}. - www.youtube.com{url}\n".format(num=counter,url=url))
			counter +=1 


def parseForUrls():
	url_list = []
	title_list = []
	
	url = youtubeSearch()
	source = webRequest(url)
	
	pattern = r'/watch'
	pattern2 = r"title=\"[^http|Carregar|Load|Pesquisar|Search|Ordenar|Order].*</a>"
	
	for link in source.find_all('a'):
		
		#Appending video title to a list
		title = re.findall(pattern2, str(link))
		if title:
			title_list.append(title)

		#Appending video urls to a list
		link = link.get('href')
		if re.match(pattern, link):
			url_list.append(link)

	#Filtering repeated URLS in the list
	seen_items = set()
	fieltered_urls = []
	first_time = True
	counter = 0
	
	for item in url_list:
		if item not in seen_items:

			if first_time:
				first_time = False
				fieltered_urls.append(item)
				seen_items.add(item)
				counter += 1

			elif item[-10:] == fieltered_urls[counter-1][-10:]:
				pass
			
			else:
				fieltered_urls.append(item)
				seen_items.add(item)
				counter += 1	

	url_list = fieltered_urls
	return url_list, title_list
 

if __name__ == "__main__":
	url_list, title_list = parseForUrls()
	writeToFile(url_list, title_list)