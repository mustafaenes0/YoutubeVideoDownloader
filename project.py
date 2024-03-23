# Importing Required Modules
import pytube

#Give the url of the YouTube video you want to download
url=input("what's the url what you want youtube video : ")

#Assign the location of the project file to the variable
path=""

pytube.YouTube(url).streams.get_highest_resolution().download(path)
#Finish Message
print("Download is completed")
