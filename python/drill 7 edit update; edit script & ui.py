# Python 3.5.2
#
# Author:   Nikki Yoke
# Edited:   Daniel
#
# Purpose:  The Tech Academy, Drill #6: Create a UI to increase
#           functionality of script written in Drill #5 that:
#               1. allows user to browse and choose specific folder to contain
#                   files to be checked daily
#               2. allows user to browse and choose specific folder to receive
#                   copied files
#               3. allows user to manually initiate "file check" process
#                   performed by the script


##################################################################################
#                   EDITS MADE BY DANIEL IN ORDER OF OCCURANCE:                  #
#--------------------------------------------------------------------------------#
#   1. got rid of global variables. global variables = evil                      # 
#   2. got rid of open_dir function; tried to do too much at once; replaced      #
#       with get_src and get_dst functions to split process into two functions   #
#   3. inserted my transfer script into this program instead of calling it from  #
#       another file                                                             #
#   4. defined get_src and get_dst as StringVar() (done separately because they  #
#       are two separate entry widgets                                           #
#   5. streamlined sqlite table to make life easier                              #
#   6. inserted my create sqlite table into this program & added in functions    #
#       to allow "file check" date display in UI                                 #
#   7. added in "main" at the end                                                #
#--------------------------------------------------------------------------------#
# Daniel suggests I keep all my code in one file until I completely understand   #
# how to set up my code within classes for exterior module usage.                #
#                                                                                #
# Note to self: work on this!!                                                   #
##################################################################################






from tkinter import *
from tkinter import ttk
import os
import shutil 
import datetime as dt
from tkinter import filedialog
import time

import sqlite3 #SQL
conn = sqlite3.connect('file_check.db') #SQL
c = conn.cursor()

root = Tk()
root.title = ("File Transfer")
root.geometry('500x120+250+100')

################################################################################
#           Function for selecting directories and initiating script           #
################################################################################

#GOT RID OF GLOBAL VARIABLES AND OPEN_DIR FUNCTION; TOO MUCH AT ONCE

#makes browse buttons function(allow selection of directory, print its path)
def get_src():
                                            #Get selected path & fill entry field
    srcPath = filedialog.askdirectory()     #.askdirectory allows input of loc.
    var_src.set(srcPath)

def get_dst():
                                            #Get selected path & fill entry field
    dstPath = filedialog.askdirectory()
    var_dst.set(dstPath)


def file_trans():
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
                                            #grabs user's indicated file dir.
    srcPath = var_src.get()
    dstPath = var_dst.get()
    for _file in os.listdir(srcPath):  
        if _file.endswith('.txt'):
            src = os.path.join(srcPath, _file)
            dst = os.path.join(dstPath, _file)
            st = os.stat(src)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                print("( {} ) moved to: {}".format(_file,dstPath))#just for shell
                shutil.move(src, dstPath)
            ###commit transfer to sqlite table###
            """**************************************************************"""
##            unix = time.time()              #redefine to avoid 'undefined' error                      #UPDATE statement commented out;
##            conn.execute("UPDATE FileCheck SET(unix = (?)",(unix,))                                   #do I need an INSERT here instead?
            """**************************************************************"""
##            conn.commit()
##    conn.close()

################################################################################
#                           Create sqlite table &                              #
#                    define functions for actual file check                    #
################################################################################

def create_table():
    conn = sqlite3.connect("file_check.db")             #defines connection
    with conn:                                          #what to do with conn
        c = conn.cursor()
        unix = time.time()
        datestamp = str(dt.datetime.fromtimestamp(unix).strftime('%d/%m/%Y'))
        c.execute("CREATE TABLE IF NOT EXISTS FileCheck(unix REAL, datestamp TEXT)")

        conn.commit()                                   #commits
    conn.close()
    first_run()                                                                             #first_run() function is called here
    
"""*********************All new, per Daniel's suggestion*********************"""

def first_run():
    conn = sqlite3.connect("file_check.db")             #defines connection
    with conn:                                          #what to do with conn
        c = conn.cursor()
        c, count = count_records(c)                     #counts records in table
        unix = time.time()
        datestamp = str(dt.datetime.fromtimestamp(unix).strftime('%d/%m/%Y'))
        if count < 1:                                   #if 1+ records: check
                              #--when, then insert new
            c.execute("""INSERT INTO FileCheck (unix, datestamp) VALUES (?,?)""",                        #INSERT statement called here; needed earlier?
                      (unix,datestamp,))                #comma needed for tuple
            conn.commit()
    conn.close()
    show_date()

def show_date():
    conn = sqlite3.connect("file_check.db")             #defines connection
    with conn:                                          #what to do with conn
        c = conn.cursor()
        c.execute("""SELECT unix FROM FileCheck""")
        data = c.fetchone()[0]                          #fetch data index 0
        lastDate = float(data)                          #defines as float
        readDate = dt.datetime.fromtimestamp(lastDate).strftime("%m/%d/%Y")
        var_date.set(readDate)                          #sets var format (above)
        conn.commit()
    conn.close()

def count_records(c):
    count = ""
    c.execute("""SELECT COUNT(*) FROM FileCheck""")     #queries number of rows
    count = c.fetchone()[0]                             #fetch data index 0
    return c, count
        
"""**************************************************************************"""


                
################################################################################
#                                   GUI coolness                               #
################################################################################

mf = Frame(root)
mf.pack()

f1 = Frame(mf, width = 600, height = 250)
f1.pack(fill = X)
f2 = Frame(mf, width = 600, height = 250)
f2.pack()
f3 = Frame(mf, width = 600, height = 250)
f3.pack()

#define for each entry widget
var_src = StringVar()
var_dst = StringVar()
"""***************"""
var_date = StringVar()
"""***************"""

#select origin folder
ttk.Label(f1, text = "Select Folder: ").grid(row = 0, column = 0, sticky = 'w')
txt_src = Entry(f1, width = 40, textvariable = var_src)
txt_src.grid(row =0, column =1, padx =2, pady =2, sticky ='we', columnspan = 20)
#browse button

#Add correct function for button callback.
Button1 = ttk.Button(f1, text = "Browse", command = get_src)
Button1.grid(row = 0, column = 22, sticky = 'e', padx = 8, pady = 4)

#select destination folder

#Add correct function for button callback.
ttk.Label(f2, text = "Select Folder: ").grid(row = 1, column = 0, sticky = 'w')
txt_dst = Entry(f2, width = 40, textvariable = var_dst)
txt_dst.grid(row =1, column =1, padx =2, pady =2, sticky ='we', columnspan = 20)
#browse button
Button2 = ttk.Button(f2, text = "Browse", command = get_dst)
Button2.grid(row = 1, column = 22, sticky = 'e', padx = 8, pady = 4)

#execute file transfer button
Button3 = ttk.Button(f3, text= "Transfer Files", width =14, command= file_trans)
Button3.grid(row = 2, column = 22, sticky = 'e', padx = 10, pady = 10)

"""********************************************************************"""
#label for date check
lbl_dt = ttk.Label(f3, text = "Last check:")
lbl_dt.grid(row = 2, column = 0, sticky = "w", padx = 8, pady = 4)

#actual date check format
lbl_date = ttk.Label(f3, textvariable = var_date)
lbl_date.grid(row = 2, column = 1, sticky = "w", padx = 8, pady = 4)

create_table()
"""********************************************************************"""


if __name__ == "__main__":
    dir_path = Label(root)
    dir_path.pack()
    first_run()
    root.mainloop()











