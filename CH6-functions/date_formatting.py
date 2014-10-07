"""

File Name: date_formatting.py
Developer: Justin A. Shores
Date Last Modified: Mon Oct  6 20:42:56 PDT 2014
Description: Write a function that takes as input a string that stores date
and time (24-hour clock) in the following format:
“MM/DD/YYYY HR:MIN:SEC” and prints the following:
- DD/MM/YYYY
- HR:MIN:SEC
- MM/YYYY
- Whether the time is a.m. or p.m.
Validation of the input in the function is necessary. For example, if the 
user gives an input of “122/04/1990 13:12:12”, the given string is invalid,
as there can be only 12 months in a year. Think of all possible erroneous 
inputs and write code to handle them. The function doesn’t return anything.

"""

# define unnecessarily long date formatter
def date_format(date_time):
    date_time = date_time.strip()
    split = date_time.split() 
    if len(split) != 2:
        print("Invalid entry")
        return
    
    date = split[0]
    time = split[1]
    month = date[:date.index("/")]    
    if int(month) < 0 or int(month) > 12:
        print("Invalid value for month!")
        return
    
    date = date[date.index("/")+1:]
    day = date[:date.index("/")]
    if int(day) < 0 or int(day) > 31:
        print("Invalid value for day!")
        return
    
    date = date[date.index("/")+1:]
    year = date    
    if len(year) != 4:
        print("Invalid value for year!")
        return
    
    hour = time[:time.index(":")]
    if int(hour) < 0 or int(hour) > 23:
        print("Invalid value for hour!")
        return

    time = time[time.index(":")+1:]
    minute = time[:time.index(":")]
    if int(minute) < 0 or int(minute) > 59:
        print("Invalid entry for min")
        return

    time = time[time.index(":")+1:]
    seconds = time
    if int(seconds) < 0 or int(seconds) > 59:
        print("Invalid entry for seconds")
        return

    print("{}/{}/{}".format(day,month,year))
    print("{}:{}:{}".format(hour, minute, seconds))
    print("{}/{}".format(month, year))
    if int(hour) < 12 and int(hour) >= 0:
        print("It is AM")
    else:
        print("It is PM")


# test program
usr_date = input("Enter date and time (format: MM/DD/YYYY hh:mm:ss): ")
date_format(usr_date)
