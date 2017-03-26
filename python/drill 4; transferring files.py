# Python 2.7.1
#
# Author:   Nikki Yoke
#
# Purpose:  The Tech Academy, Drill 4:
#           Create a script that will transfer files
#           from one directory to another



import os, shutil




FolderA = ('C:\Users\Jacqueline\Desktop\A')         #define paths as variables
FolderB = ('C:\Users\Jacqueline\Desktop\B')
print os.listdir(FolderA)                           #print txt files in A




for filename in os.listdir(FolderA):                #if file in A has txt
    if filename.endswith('.txt'):                   #    extension, moves to B
        pathname = os.path.join(FolderA, filename)
        if os.path.isfile(pathname):
            shutil.move(pathname, FolderB)

print os.listdir(FolderA)                           #checks to see contents of A
print os.listdir(FolderB)                           #confirms move to B of txt




