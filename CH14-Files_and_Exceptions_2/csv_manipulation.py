"""

File Name: csv_manipulation.py
Developer: Justin A. Shores
Date Last Modified: Tue Nov 25 16:13:35 PST 2014
Description: Spreadsheet programs such as Microsoft Excel or OpenOffice 
    Calc have an option to export data into CSV files.  In this exercise, 
    you will create a program that will read in a spreadsheet 
    (in CSV format) and manipulate it.  
    Provide the following capabilities:
    - Print the data.
    - Delete a row or column
    - Insert a row or column.
    - Change a value in a cell.
    - Output the data in CSV format.

"""
import csv
import sys


# Editor class designed to manipulate csv files with some interface help
class Editor(object):
    # gets the name fields from user this is data in 1st row
    @staticmethod
    def get_fieldnames(csv_in):
        data = []
        print("\nThe file is empty, please enter name fields")
        while True:
            field_name = input("Enter field name, Enter 'q' to quit: ")
            if field_name != 'q':
                data.append(field_name)
                continue
            else:
                if not data:
                    print("\nCant quit yet, please enter at least one name field")
                    continue
                else:
                    break
        with open(csv_in, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    # gets all the data from file and returns it as a list
    @staticmethod
    def get_data(csv_in):
        data = []
        read_file = open(csv_in, "r")
        reader = csv.reader(read_file)
        for row in reader:
            data.append(row)
        read_file.close()
        return data

    # initializes the editor object
    def __init__(self, csv_in):
        self.csv = csv_in
        data = self.get_data(self.csv)
        if not data[0]:
            self.get_fieldnames(self.csv)

    # inserts an entire row into file
    def insert_row(self):
        data = self.get_data(self.csv)
        with open(self.csv, "a", newline='') as f:
            fieldnames = data[0]
            amender = csv.writer(f)
            if fieldnames == "":
                print("Error: No Data")
            else:
                row_data = []
                for index in range(0, len(fieldnames)):
                    cell_data = input("Enter {}: ".format(fieldnames[index]))
                    row_data.append(cell_data)
                amender.writerow(row_data)

    # deletes an entire row from file
    def delete_row(self):
        data = self.get_data(self.csv)
        valid = False
        while not valid:
            index = input("Enter the number of the row you wish to delete: ")
            try:
                del data[int(index)]
                valid = True
            except IndexError:
                print("Index out of bounds!")
        write_file = open(self.csv, "w")
        writer = csv.writer(write_file)
        for row in data:
            writer.writerow(row)

    # inserts a new column into file
    def insert_column(self):
        data = self.get_data(self.csv)
        column_name = input("Enter the name of the column to insert: ")
        data[0].append(column_name)
        for row in range(1, len(data)):
            data[row].append("")
        write_file = open(self.csv, "w")
        writer = csv.writer(write_file)
        for row in data:
            writer.writerow(row)

    # deletes an entire column from file
    def delete_column(self):
        data = self.get_data(self.csv)
        index = input("Enter the index of the column to remove: ")
        for row in range(0, len(data)):
            try:
                del data[row][int(index)]
            except IndexError:
                continue
        write_file = open(self.csv, "w")
        writer = csv.writer(write_file)
        for row in data:
            writer.writerow(row)

    # gets the location and edits cells of file
    def edit_cell(self):
        data = self.get_data(self.csv)
        row = ""
        col = ""
        valid = False
        while not valid:
            row = input("Enter row index of cell you wish to edit: ")
            col = input("Enter column index: ")
            try:
                correct = input("Cell contains '{}' is this correct? (y or n): ".format(data[int(row)][int(col)]))
                if correct == 'n' or correct == 'N':
                    valid = False
                else:
                    valid = True
            except IndexError:
                print("Index out of bounds!")
        new_cell_data = input("Enter the new data for the cell: ")
        data[int(row)][int(col)] = new_cell_data
        write_file = open(self.csv, "w")
        writer = csv.writer(write_file)
        for row in data:
            writer.writerow(row)

    # prints the data in the file to the screen
    def __str__(self):
        print("\nCurrent data in file {}\n".format(self.csv))
        with open(self.csv, newline='') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    print(" ".join(['%15s' % x for x in row]))
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(self.csv, reader.line_num, e))
        return "\n"


# edits entire row or column based on user selection
def edit_row_or_col(editor, edit_type):
    if edit_type == 3:
        type_str = "insert"
    else:
        type_str = "delete"
    while True:
        option = input("Enter 1 to {} row, Enter 2 to {} column: ".format(type_str, type_str))
        if option == '1':
            if edit_type == 3:
                editor.insert_row()
            else:
                editor.delete_row()
            break
        elif option == '2':
            if edit_type == 3:
                editor.insert_column()
            else:
                editor.delete_column()
            break
        else:
            print("Invalid entry! Please enter a 1 or 2")
            continue


# evaluate user selection
def evaluate_option(selection, editor):
    if selection == 1:
        # print
        print(editor)
    elif selection == 2 or selection == 3:
        # insert or delete
        edit_row_or_col(editor, selection)
        print(editor)
    elif selection == 4:
        # change cell
        editor.edit_cell()
        print(editor)
    else:
        # exit
        sys.exit("Goodbye!")


# get user selection
def get_user_option(editor):
    while True:
        print("1 - Print the data\n2 - Delete row or column"
              "\n3 - Insert row or column\n4 - Change value in a cell"
              "\n5 - Exit")
        user_option = input("Enter a number (1 - 5): ")
        user_int = int(user_option)
        if 1 <= user_int <= 5:
            evaluate_option(user_int, editor)
            break
        else:
            print("\nInvalid Entry! Valid options are between 1 and 5")
            continue


# define the main interface
def main():
    # for the purpose of simplicity there will be no user defined file
    csv_file = "my_file.csv"
    print("\nCSV file manipulator:\nPlease choose one of the following"
          " options.")
    while True:
        editor = Editor(csv_file)
        get_user_option(editor)
        valid_choice = False
        while not valid_choice:
            choice = input("Would you like to continue modifying? (Y or N): ")
            if choice != 'y' and choice != 'Y' and choice != 'n' and choice != 'N':
                valid_choice = False
                print("Invalid entry!")
            else:
                valid_choice = True
        if choice == 'y' or choice == 'Y':
            continue
        else:
            break


# run program
main()