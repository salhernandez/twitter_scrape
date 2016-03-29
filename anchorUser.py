#stored the user names in a file in a folder based on the user from which it was obtained from
from urllib2 import urlopen
from urllib2 import urlparse
import urllib
from BeautifulSoup import BeautifulSoup
import os
import requests

#no longer needed
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


myPath = "/home/sal/Desktop/scrape/images/"
twitter = "https://twitter.com/"
url = ""

while(1):
	#gets twitter handle
	handle = raw_input("Enter a twitter handle: ")
	url = twitter+handle
	request = requests.get(url)

	#checks to see if the user exists
	if(request.status_code != 200):
		print("Invalid twitter handle, please try again") 
	else:
		print("The handle exists!")
		break

#open the url and reads the html
soup = BeautifulSoup(urlopen(url).read())
arr = []
count = 1

#gets all the users from the feed
for element in soup.findAll('div'):
    dataScreenName = element.get('data-screen-name')
    if dataScreenName != None:
    	#print dataScreenName
    	if(dataScreenName.lower() != handle.lower()):
    		arr.append(dataScreenName)
    count = count +1

#usersFromMain = remove_duplicates(arr)
usersFromMain = list(set(arr))

arr = []
count = 0
#gets all the users from the html
for element in soup.findAll('a'):
    dataScreenName = element.get('href')
    if dataScreenName != None:
    	if dataScreenName.count('/') == 1 :
    		temp = dataScreenName.split("/")[1]
    		if (temp.lower() != handle.lower() and temp !="" and temp!="tos" and temp!="privacy" and temp!="login" and temp!="about"):
    			#print temp
    			arr.append(temp)
    			count = count +1

#usersFromHtml = remove_duplicates(arr)
usersFromHtml = list(set(arr))
handlesFromUser= myPath+"/users/"
if not os.path.exists(handlesFromUser):
    os.makedirs(handlesFromUser)
f = open(handlesFromUser+handle+".txt", "w")
#users taken from the main feed
#for i in usersFromMain:
	#print i
#print("\nFrom html\n")
#users taken from main feed and any user mentioned within
for i in usersFromHtml:
    f.write(i+"\n")
    print i
f.close()
print("done")