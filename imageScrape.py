#gets the users from the text file given
#SCRAPE IMAGES FROM THE USERS GIVEN
#checks if the textfile has any contents
#Done
from urllib2 import urlopen
from urllib2 import urlparse
import urllib
from BeautifulSoup import BeautifulSoup
import os
import requests
import sys

inFile = sys.argv[1]
inFile = inFile.lower()
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

currentDirectory = os.getcwd()+"/"
print currentDirectory

imgPath = currentDirectory+"data/images/"
myPath = currentDirectory+"data/users/"
twitter = "https://twitter.com/"
url = ""
users = []

file = myPath+inFile
#s = open(myPath+"users/titan_n93.txt", "w")

#if the file has size 0, it has nothing in it
statinfo = os.stat(file)
if statinfo.st_size == 0:
    print("The file has nothing in it!")
    sys.exit()
with open(file, "r") as f:
    for line in f:

        #removes the '\n' from the read
        line= line[:-1]
        #print line
        users.append(line)

for user in users:
    handle = user
    handle = handle.lower()
    print handle
    
    #gets twitter handle
    #handle = raw_input("Enter a twitter handle: ")
    url = twitter+handle
    request = requests.get(url)


    #open the url and reads the html
    soup = BeautifulSoup(urlopen(url).read())
    arr = []
   
    #stores the image links into an array
    #based on the img tag and src element
    for element in soup.findAll('img'):
        source = element.get('src')
        if source != None:
            arr.append(source)

    #gets the unique links from the array
    #uniqueLinks = remove_duplicates(arr)
    uniqueLinks = list(set(arr))
    
    count = 1
    temp = ""

    newFolder = imgPath+handle
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)

    #downloads the images from the list
    for i in uniqueLinks:
        #gets the last element from the link which is the name of the image itself
        temp = i.split("/")[-1:]
        #joins the path to the folder to the name of the image
        #fullfilename = os.path.join(myPath, temp[0])
        fullfilename = imgPath+handle+"/"+temp[0]
        #downloads the image to the folder and names it the same as from where it was retrived from
        print("Downloading: "+i)
        urllib.urlretrieve(i, fullfilename)

        count = count +1
    print "\n"
print("done")