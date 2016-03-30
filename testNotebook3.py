#basic tkinter GUI that echoes back what was entered on the Entry field
#now with frames
#now with tabs (notebook)
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os


#imageDirectory = os.getcwd()+"/images/"
imageDirectory = "/home/sal/Desktop/data/images/titan_n93/"
root = Tk()

def echo(*args):
	temp = userInput.get()
	output.set(temp)

	allfiles=os.listdir(imageDirectory)
	imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG"]]
	
	test =[]
	for im in imlist:
		im  = Image.open(imageDirectory+im)
		photo = ImageTk.PhotoImage(im)
		label = Label(redTab,image=photo)
		label.image = photo

		test.append(label)
	
	index = 0
	for row in range(5,12):
		for col in range(0,5):
			test[index].grid(row = row, column = col)
			index+=1


	Tk.update()
	#Tk.update(root)



root.title("TABS BRO!")
mainFrame = ttk.Frame(root)

#sets up the frame
frame = ttk.Frame(mainFrame, borderwidth=5, relief="sunken", width=100, height=200)

#sets up notebook widget on the mainFrame
tabs = ttk.Notebook(mainFrame)

#eacch page on the notebook(tab) is treated as a frame itself
tabWidth = 800
tabHeight = 800
redTab = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)
greenTab = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)
blueTab = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)

#insert image into a frame

allfiles=os.listdir(imageDirectory)
imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG"]]

masterX = 0
masterY = 0
arr = []
'''
for i in range(0,5):
	img1 = ImageTk.PhotoImage(Image.open("UndertowIcon.png"))
	arr.append(Label(redTab, image = img1))
	#arr.append(panel1)
	#arr[i].pack()
	arr[i].place(x=masterX,y=masterY)
	masterX = masterX+50
	masterY = masterY+50
	'''
'''
img1 = ImageTk.PhotoImage(Image.open("UndertowIcon.png"))
panel1 = Label(redTab, image = img1)
#panel1.pack(side = LEFT)


img2 = ImageTk.PhotoImage(Image.open("UndertowIcon.png"))
panel2 = Label(redTab, image = img2)
#panel2.pack(side = LEFT)

img3 = ImageTk.PhotoImage(Image.open("UndertowIcon.png"))
panel3 = Label(redTab, image = img3)
#panel3.pack(side = LEFT)
arr.append(panel1)
arr.append(panel2)
arr.append(panel3)

im=Image.open("UndertowIcon.png")
width, height = im.size
for i in arr:
	i.pack()
'''
#adds the pages to the notebook 'tabs'
tabs.add(redTab, text='Red')
tabs.add(greenTab, text ='Green')
tabs.add(blueTab, text ='Blue')


userInput = StringVar()
output = StringVar()

#make sure for each to insert into 'frame'
#sets up the Entry
userInput_entry = ttk.Entry(frame, width=7, textvariable=userInput)

#label will contain the variable output which will be what was entered on the field
outputLabel = ttk.Label(frame, textvariable=output)

#the button calls on the function 'echo' whcih redefined the variable 'output' to what was
#entered on the field
submitButton = ttk.Button(frame, text="submit", command=echo)
quitButton = ttk.Button(frame, text='Quit', command=quit)

#Labels
promptLabel = ttk.Label(frame, text="Twitter Handle:")
echoLabel = ttk.Label(frame, text="echo: ")

#assign where the frames start in the root
mainFrame.grid(column=0, row=0)

#assign the startpoint and colspan and rowspan
frame.grid(column=0, row=0, columnspan=3, rowspan=3)
tabs.grid(column=100, row=200, columnspan=3, rowspan=3)
#namelbl.grid(column=3, row=0, columnspan=2)

#when the widgets are inserted, they are done so according to their frame!!!
promptLabel.grid(column=0, row=0, sticky= E)
userInput_entry.grid(column=1, row=0, sticky= W)

outputLabel.grid(column=1, row=1, sticky= W)
echoLabel.grid(column=0, row=1, sticky= E)

submitButton.grid(column=0,row=2)
quitButton.grid(column=1, row=2)

#binds the '<Return>' button to the function 'echo'
root.bind('<Return>', echo)

root.mainloop()
