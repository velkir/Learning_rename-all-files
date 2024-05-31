import os
from datetime import date

#Set up path and files variables
path = "files/"
files = os.listdir(path)

#Get current date and format it
current_date = "-"+str(date.today())

#Run loop over files
for file in files:
  if file.endswith(".txt"):
    new_name = file[0:-4]+current_date+".txt"
    os.rename(path+file, path+new_name)
  else:
    print(f"{file} doesn't have .txt extension! It hasn't been changed")
