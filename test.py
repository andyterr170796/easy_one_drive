import os
os.chdir(r'your_directory') # where the dependencies will be stored
!git clone https://github.com/andyterr170796/easy_one_drive.git

# Just one time (in local, in colab or similars you should put this always), then only proceed from line 10
import sys
sys.path.insert(0,os.path.join(os.getcwd(),'easy_one_drive'))
# Ready to go!

from easy_one_drive import easy_one_drive

# Set the class to object "s"
s = easy_one_drive('correo', 'password', driver_path='')

# First you must logging in
s.logging_in()

# Some examples here:
## First for downloading files with patterns, you only must set URL where files are located, then the pattern (string, not list), and optionally the waiting time
s.download_file('url','_d') # Here all files that contains string '_d' in their names will be downloaded with default waiting time
s.download_file('url','informe',30) # Here all files that contains string 'informe' in their names will be downloaded with only 30 seconds of waiting to download
s.download_file('url','.xlsx') # Here all files with extension '.xlsx' will be downloaded with default waiting time

### NOTE: CAN'T use REGEX, so a suggestion is first create a list with files you want to download like in the next lines:

## Now let's download only 2 files, you only must set URL where files are located, then the files to download (in list, with their extensions), and optionally the waiting time
s.download_file('url',['archivo1.xlsx','archivo2.xlsx']) # Like before, optionally you can change waiting time after set the list

## For download an entire folder (more robust if you want all files)
s.download_folder('url',"folder_name") # Here given the url, will download the folder with the name specified, and you can change waiting time

## In case of uploading you must specify the complete route of the file to upload like this:
archivo = r"C:\Users\IDEAPAD530S\data_todo.dta"
s.upload_file('url',archivo,50) # Finally, specify the url where file will be upload, as before optionally you can change waiting time

## When you finish everything, log out! (security reasons only)
s.logging_out()

### NOTE: you can make any actions as you want between loggin_in and logging_out!
