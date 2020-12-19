# program to manage student details
#import pdb;pdb.set_trace()
import pandas
import csv
import time
import sys
# class for holding variables


class Student:
    def __init__(self, id, name, age, course, ecr):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.ecr = ecr


def createdb():
    df = pandas.DataFrame([['', '', '', '', '', '']], columns=[
                          'id', 'name', 'age', 'course', 'ecr', 'contact'])
    df.to_csv('studentdata.csv', index=False)
    print('Table successfully created')


# functions to show main menu
def main_menu():

    selection = '1'
    while selection != 'exit':

        print('\n***Welcome to Student D B M S***\n***Please select an option below***\n')
        selection = input(
            ' |1.| VIEW STUDENT DETAILS: \n |2.| ADD A NEW STUDENT DETAIL: \n |3.| EDIT A STUDENT DETAIL:\n |4.| View All student details:\nOR TYPE EXIT  ')
        if selection == '1' or selection == '2' or selection == '3' or selection == '4' or selection == 'exit':
            if selection == '4':
                viewall()
            elif selection == '1':
                viewstudent()
            elif selection == '2':
                create_new_student()
            elif selection == '3':
                editstudent()
            else:
                break

        else:
            print('\nOops..Invalid Selection:')
            time.sleep(1)


# function to clear a new student
def create_new_student():
    print('Enter student details:')
    student = Student(None, None, None, None, None)
    student.name = input('Name: ')
    student.age = input('Age: ')
    student.course = input('Course/Class: ')
    student.ecr = input('Extra Curricular Activity: ')
    student.con = input('Contact number: ')
    id = 'del'+'al'+str(student.con[0:3])
    newdf = pandas.DataFrame([[id, student.name, student.age, student.course, student.ecr, student.con]], columns=[
                             'id', 'name', 'age', 'course', 'ecr', 'contact'])
    df = pandas.read_csv('studentdata.csv')
    df = df.append(newdf, ignore_index=True)
    df.to_csv('studentdata.csv', index=False)
    print("\nDetails created successfulyy with student ID: ", id)
    print(' *Imp.  Please note the new Student ID created  ^^^ *')
    time.sleep(1)


def viewstudent():

    id = input('Enter student ID:')
    df = pandas.read_csv('studentdata.csv')  # to load dataframe
    requirement = df['id'] == id               # to filter out a row (1 of 2)
    # requirement has boolean values which we can not use we need to assign these values to a variable through .loc attribute (its a syntax, no question) (2 of 2)
    new = df.loc[requirement]

    if True in requirement.values:
        print('Student Details are:\n')
        print(new)
        time.sleep(1)
    else:
        print('Oops..No student with this ID:')
        time.sleep(1)

    return new


def editstudent():
    new = viewstudent()
    if new.empty == False:
        print('\nWhich field you want to edit:')
        req = input(
            '|1.|Name, \n|2.|Age, \n|3.|Course, \n|4.|Extra_Curricular, \n|5.|Contact ')
        if req == '1' or req == '2' or req == '3' or req == '4' or req == '5':
            if req == '1':
                req = 'name'
                newvalue = input('Enter new Name: ')
            elif req == '2':
                req = 'age'
                newvalue = input('Enter new Age: ')
            elif req == '3':
                req = 'course'
                newvalue = input('Enter new Course: ')
            elif req == '4':
                req = 'ecr'
                newvalue = input('Enter new Extra_Curricular: ')
            else:
                req = 'contact'
                newvalue = input('Enter new Contact: ')

            df = pandas.read_csv('studentdata.csv')
            getindex = new.index    # to get the index number of the series
            # to get only the row number from series
            getrownum = list(getindex)
            fetchrownum = getrownum[0]            # to fetch the list value
            # to set the new value in file
            valuesetter = df.loc[fetchrownum, req] = newvalue
            df.to_csv('studentdata.csv', index=False)
            print('\nSuccessfully Updated')
            time.sleep(1)

        else:
            print("\nOops Invalid Selection")

    else:
        print('Please check the ID')


def viewall():
    df = pandas.read_csv('studentdata.csv')
    print(df)
    time.sleep(1)

# Credential checker


def logincheck():
    while True:
        try:
            print('Press Ctrl/Cmd + C any time to exit.\nSelect a user:\n')
            login = input('Press *A* for admin and *U* for user\n')
            if login.lower() == 'a':
                password = input("Enter Password:\n")
                if password == 'admin':
                    print('Welcome Admin:')
                    print(
                        'From here you can access Student Database and create a new database table')
                    print('Type *create* to create new Database Table')
                    print('Type *access* to Acess old database')
                    selection = input()
                    if selection.lower() == 'create':
                        selectio2 = input(
                            "\t*Warning*\n Old data will be deleted: Do you still want to continue: (y/n)\n")
                        if selectio2.lower() == 'y':
                            createdb()
                            time.sleep(1)
                            main_menu()
                        else:
                            # print("Exiting:")
                            time.sleep(1)
                    elif selection == 'access':
                        try:
                            df = pandas.read_csv('studentdata.csv')
                            main_menu()
                        except FileNotFoundError:
                            print(
                                'Oops..No database exists Please run the *create* command')

                    else:
                        print('\nOops.. Invalid Command')
                        # logincheck()
                        continue
                else:
                    print("Login failed")
                    # logincheck()
                    continue

            elif login.lower() == 'u':
                try:
                    df = pandas.read_csv('studentdata.csv')
                    for remaining in range(3, 0, -1):
                        sys.stdout.write("\r")
                        sys.stdout.write(
                            'Loading DBMS '"{:2d} seconds remaining.".format(remaining))
                        sys.stdout.flush()
                        time.sleep(1)
                    main_menu()
                except FileNotFoundError:
                    print('\nNo database exists Please contact Admin')

            else:
                print('\n Oops.. Invalid selection')
                # logincheck()
                continue
        except KeyboardInterrupt as e:
            exit_prompt = input('\nKeyboardInterrupt received, exit? (y/n):\n')
            # print(exit_prompt)
            if exit_prompt.lower() == 'y':
                break


logincheck()
