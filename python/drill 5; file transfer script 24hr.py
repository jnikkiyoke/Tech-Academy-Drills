# Python 2.7.12
#
# Author:   Nikki Yoke
#
# Purpose:  The Tech Academy, Drill 5: write a script that
#           will transfer files modified within the last
#           24hrs to a specified destination directory.



import os,time
import datetime
import shutil

import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
created = 'C:\Users\Jacqueline\Desktop\created'
dest = 'C:\Users\Jacqueline\Desktop\dest'

def file_trans():
    for root, dirs,files in os.walk(created):  
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)    
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
                shutil.move(path, dest)
                # this is actual move

print file_trans()


