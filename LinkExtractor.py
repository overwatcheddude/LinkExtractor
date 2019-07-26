#Packages
from bs4 import BeautifulSoup
import re #re stands for Regular Expression

#Read the HTML document that you downloaded. The r is placed before filename to prevent the characters in filename string to be treated as special character.
soup = BeautifulSoup(open(r"C:\Users\Overw\Downloads\Browse Items - Marketplace.tf.html"), "html.parser")

#The text file will be called myLinks.txt
#Write Only (‘w’) : Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
txtFile = open("myLinks.txt", "w")

for link in soup.findAll("a"): #Finds all the <a> tags in the document
    if re.match("https:\/\/marketplace.tf\/items\/tf2\/", str(link.get('href'))): #Gets the link (if the link is not #, empty, none or null)
        txtFile.write(link.get('href') + "\n") #Writes the link into the text file and add a line break

#Closes the file once the execution is complete.
txtFile.close()