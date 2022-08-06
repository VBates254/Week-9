# Victoria Bates
# CIS245 9.1
import os
import pathlib
import csv

# Create Directory
directory = input("Save to Directory: ")
# filename = input("Save File As: ")
# filename = 'WeekNineCh10.txt' - TEST LINE
# directoryFile = 'W9C10CSV.txt' -TEST LINE
# filepath = os.mkdir - TEST LINE
# parentdir = 'W9C10CSV.txt' - TEST LINE
# path = open(os.path.join("filename.csv")) - TEST LINE
pathlib.Path(directory).mkdir(parents = True, exist_ok = True)
csvFile = open(os.path.isfile(directory))
try:
  os.mkdir(str(csvFile))
except OSError as error:
  print(error)

filename = input("Save File As: ")  
username = input("Enter Full Name: ")
address = input("Enter address: ")
phone = input("Enter phone number: ")

completeFile = os.path.join(directory, filename + ".txt")
# stores without comma separated files
with open(completeFile, 'a') as file_object:
  file_object.write(username + ',')
  file_object.write(address + ',')
  file_object.write(phone)
  file_object.close()
  
# stores as comma sepearted files
with open(completeFile, 'r') as file_object:
 lines = file_object.readlines()
name_string = ''
for line in lines:
  name_string += line.rstrip()

print("You entered the following information: ")
print(lines)