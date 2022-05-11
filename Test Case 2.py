# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sqlite3


class Student:

    def __init__(self, id, fName, lName):
        self.id = id
        self.firstName = fName
        self.lastName = lName


class Enrollment:

    def __init__(self, id, year, studentId):
        self.id = id
        self.year = year
        self.studentId = studentId


def method1():
    conn = sqlite3.connect('test.db')

    cursor = conn.execute("SELECT count(id) FROM students WHERE firstName='John'")

    count = cursor.fetchone()[0]
    print("Total number of rows selected :", count)
    conn.close()

    return count


def method2():
    conn = sqlite3.connect('test.db')

    conn.execute("UPDATE enrollments SET year = 2015 WHERE id >= 20 AND id <= 100")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)

    conn.close()


def init():
    conn = sqlite3.connect('test.db')

    conn.execute(
        'CREATE TABLE students (ID INT PRIMARY KEY NOT NULL,firstName VARCHAR(30) NOT NULL, lastName VARCHAR(30) NOT NULL)')
    conn.execute(
        'CREATE TABLE enrollments( id INTEGER NOT NULL PRIMARY KEY, year INTEGER NOT NULL, studentId INTEGER NOT NULL)')
    conn.execute("INSERT INTO students VALUES (1, 'Paul', 'California' )")
    conn.execute("INSERT INTO students VALUES (2, 'John', 'California' )")
    conn.execute("INSERT INTO enrollments VALUES (1, 2000, 1 )")
    conn.execute("INSERT INTO enrollments VALUES (20, 2000, 2 )")
    conn.commit()

init()
method1()
method2()


