#gets the users from a user
from urllib2 import urlopen
from urllib2 import urlparse
import urllib
from BeautifulSoup import BeautifulSoup
import os
import requests
import sys
from datetime import datetime
start_time = datetime.now()


inFile = sys.argv[1]
#runs = int(inFile)
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

currentDirectory = os.getcwd()+"/"
#print currentDirectory

myPath = currentDirectory+"data/users/"
#myPath = "/home/sal/Desktop/scrape/images/"
twitter = "https://twitter.com/"
url = ""


handle = inFile
url = twitter+handle
request = requests.get(url)

print "\n---------------\nGetting users from: "+handle+"\n---------------\n"
#checks to see if the user exists
if(request.status_code != 200):
    print("Invalid twitter handle")
    sys.exit() 
else:
    print("The handle exists!")
    

handle = handle.lower()
#open the url and reads the html
soup = BeautifulSoup(urlopen(url).read())
#arr = []
#count = 1

#gets all the users from the feed
#for element in soup.findAll('div'):
#    dataScreenName = element.get('data-screen-name')
#    if dataScreenName != None:
#       #print dataScreenName
#       if(dataScreenName.lower() != handle.lower()):
#           arr.append(dataScreenName)
#    count = count +1

#usersFromMain = remove_duplicates(arr)
#usersFromMain = list(set(arr))

arr = []
count = 0
#gets all the users from the html
for element in soup.findAll('a'):
    dataScreenName = element.get('href')
    if dataScreenName != None:
        if dataScreenName.count('/') == 1 and dataScreenName.count('?') < 1:
            temp = dataScreenName.split("/")[1]
            if (temp.lower() != handle.lower() and temp !="" and temp!="tos" and temp!="privacy" and temp!="login" and temp!="about" and temp!="signup"):
                #print temp
                arr.append(temp.lower())
                count = count +1

#usersFromHtml = remove_duplicates(arr)
usersFromHtml = list(set(arr))
handlesFromUser= myPath

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
    print "from "+handle+" : "+i
f.close()

# do your work here
end_time = datetime.now()
print('Done in: {}'.format(end_time - start_time))