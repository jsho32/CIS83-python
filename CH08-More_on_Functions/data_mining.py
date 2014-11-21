"""

File Name: data_mining.py
Developer: Justin A. Shores
Date Last Modified: Fri Oct 24 16:45:01 PDT 2014
Description: In this project, we want to do some preliminary data mining to the prices of some
company’s stock. So that we can speak in specifics, let’s look at Google. Your program
will calculate the monthly average prices of Google stock from 2004 to 2008 and tell
us the six best and six worst months for Google.

"""
import operator

# predefined function to get data from file
def get_data_list(file_name):
    data_file = open(file_name,"r")
    # start with an empty list
    data_list = [ ]
    for line_str in data_file:
        # strip end-of-line, split on commas, and append items
        data_list.append(line_str.strip().split(','))
    return data_list

# get the monthly averages
def get_monthly_averages(data_list):
    monthly_averages_list = []
    numerator, denominator, month_average = 0, 0, 0
    new_data_list = data_list[1:]
    date = new_data_list[0][0][:-3]
    for info_list in new_data_list:
        if info_list[0][:-3] == date:
            numerator += float(info_list[-2]) * float(info_list[-1])
            denominator += float(info_list[-2])
        else:
            month_average = (numerator/denominator)
            average_tuple = (date, month_average)
            monthly_averages_list.append(average_tuple)
            numerator = float(info_list[-2]) * float(info_list[-1])
            denominator = float(info_list[-2])
            date = info_list[0][:-3]
    return monthly_averages_list

# print the 6 best and 6 worst months
def print_info(monthly_averages_list):
    sorted_averages = sorted(monthly_averages_list, 
            key = operator.itemgetter(1), reverse = True)
    reverse_sorted_averages = sorted(monthly_averages_list, 
            key = operator.itemgetter(1), reverse = False)
    six_best = sorted_averages[:6]
    six_worst = reverse_sorted_averages[:6]
    best_str = "\nSix best months:"
    worst_str = "Six worst months:\n"
    for x in range(-1, 6):
        if x == -1:
            print("{0:22} {1:22}".format(best_str, worst_str))
        else:
            print("{0:9} {1:11} {2:10} {3:10}".format(six_best[x][0],
                 "{0:.2f}".format(six_best[x][1]), six_worst[x][0], 
                 "{0:.2f}".format(six_worst[x][1])))

# run program to find 6 best and worst in data from file
data_list = get_data_list("table.csv")
monthly_averages = get_monthly_averages(data_list)
print("\nGoogle's six best and six worst average stock prices\n" \
        "from the table:")
print_info(monthly_averages)
