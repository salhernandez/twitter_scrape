#gets the users from the text file given
#takes a textfile as input and gets more data through those users
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

print inFile


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

#gets the current directory
currentDirectory = os.getcwd()+"/"
print currentDirectory

myPath = currentDirectory+"data/users/"
twitter = "https://twitter.com/"
url = ""
users = []

#s = open(myPath+"users/titan_n93.txt", "w")

with open(myPath+inFile, "r") as f:
    for line in f:

        #removes the '\n' from the read
        line= line[:-1]
        #print line
        users.append(line)

for user in users:
    handle = user
    print handle
    
    #gets twitter handle
    #handle = raw_input("Enter a twitter handle: ")
    url = twitter+handle
    request = requests.get(url)


    #open the url and reads the html
    soup = BeautifulSoup(urlopen(url).read())

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
    handlesFromUser= myPath
    if not os.path.exists(handlesFromUser):
        os.makedirs(handlesFromUser)

    f = open(handlesFromUser+handle+".txt", "w")
   
    for i in usersFromHtml:
        f.write(i+"\n")
        print i
    f.close()
    print "\n"
# do your work here
end_time = datetime.now()
print('Done in: {}'.format(end_time - start_time))