# Python 2.7.1
#
# Author:       Nikki Yoke
#
# Edited by:    Dylan D. (modified code and created function)  
#
# Purpose:      The Tech Academy, Drill 3
#               Create a program that finds the current
#               time in multiple timezones to determine if
#               a branch of a store is currently open.

#
#
#
#

from datetime import datetime, time
import pytz                                                                     #import Python timezones module
from pytz import timezone

#just finds times, for reference
localFormat = "%m/%d/%Y %H:%M"                                                  #format the way the time/date will be displayed

utcmoment_unaware = datetime.utcnow()                                           #use current time, then replace w/ other variable
utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)                          #use local time to find other timezone's current time

timezones = ['America/Los_Angeles', 'America/New_York', 'Europe/London']
for tz in timezones:
    localDatetime = utcmoment.astimezone(pytz.timezone(tz))
    print localDatetime.strftime(localFormat)
#########################################################################################################################################

def checkOpenClose(branchName, tz):
    branchTZ = timezone(tz)
    now = datetime.now(branchTZ)
    branchTime = now.time()
    if branchTime >=time(9,00) and branchTime <=time(21,00):      #looks at time, prints local time and if open/closed
        print branchTime.strftime(branchName + ': %H:%M, Open')
    else:
        print branchTime.strftime(branchName + ': %H:%M, Closed')

checkOpenClose("London", "Europe/London")
checkOpenClose("New York", "America/New_York")





        


