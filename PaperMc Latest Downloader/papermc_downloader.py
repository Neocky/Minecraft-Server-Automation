# Downloads the latest version of PaperMC (https://papermc.io/downloads)
# Author: Neocky (https://github.com/Neocky)

import urllib.request

# change these values to your likings
downloadURL = "https://papermc.io/api/v1/paper/1.16.5/latest/download"
filepath = r"C:\Users\USER\Desktop\papermc.jar"

# Creating request
r = urllib.request.Request(downloadURL)

print(">>>  Download started  <<<")

# send request
data = urllib.request.urlopen(r)

dataLength = int(data.getheader('content-length'))

file = open(filepath, mode='ba')

# read data
byts = data.read(dataLength)

# data to file
file.write(byts)

print (">>>  Download complete <<<")

# close file after succesfull writing
file.close()