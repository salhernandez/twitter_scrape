#stored the user names in a file in a folder based on the user from which it was obtained from
from urllib2 import urlopen
import urllib
from BeautifulSoup import BeautifulSoup
import os
import requests
import sys
from datetime import datetime
start_time = datetime.now()

#inFile = sys.argv[1]
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
print currentDirectory

imgPath = currentDirectory+"data/images/"
myPath = currentDirectory+"data/users/"
#myPath = "/home/sal/Desktop/scrape/images/"
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
    print i
f.close()

#downloads images from the anchor userr
print("\n---------------\nDownloading stuff from: "+handle+"\n---------------\n")
os.system("python imgUser.py "+handle)#gets all images from user

#1st level
#os.system("python threadTest.py "+handle+".txt")

#2nd level
for x in usersFromHtml:
    print("\n---------------\n"+handle+" -> "+x+"\n---------------")
    os.system("python getUsers.py "+x)#generates more users based on current user
    #os.system("python threadTest.py "+x+".txt")
    #print("\n---------------\nDownloading stuff from: "+x+"\n---------------\n")
    os.system("python imgUser.py "+x)#gets all images from user
    
    #was created with getUsers.txt
    file = myPath+x+".txt"

   #3rd level
   #fix so that it dumps the names into an array,
    with open(file, "r") as f:
        for line in f:
            line= line[:-1]
            print("\n---------------\n"+handle+" -> "+x+" -> "+line+"\n---------------")
            #print("\n---------------\nSource: "+x+"\n---------------")
            #print("\n---------------\nSecond Level\n-------------\n")
            os.system("python getUsers.py "+line)#gets more users based on the users...for imageScrape.py
            #os.system("python threadTest.py "+handle+".txt")
            #print("\n---------------\nDownloading stuff from: "+line+"\n---------------\n")
            os.system("python imgUser.py "+line)#gets all images from user
    #os.system("python imageScape.py "+myPath+x+".txt")
# do your work here
end_time = datetime.now()
print('All Done in: {}'.format(end_time - start_time))