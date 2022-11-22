# FolderCleanUpScript
Python script to move files from one folder to another. The aim of this project is to help manage downloads folder &amp; segregate various files to their own folders

# Pre-requisites
The source & destination folders must exist. There is a check for this and if not present the script will error out

# How To Run It ?
The script to run is ```main.py``. It takes in 3 parameters
1. source directory
2. destination directory
3. exention/file type to be moved

```py
main.py <source directory> <destination directory> <extension of files>
```

For example below script will move all PDF files from Downloads to PDFContent Folder in F Drive.
```py
main.py C:\Users\pc\Downloads\ F:\PDFContent\ pdf 
```

