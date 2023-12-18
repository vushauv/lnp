import pandas 
import numpy as np

students_initial = pandas.read_csv("./tables/students_initial.csv")
teachers_initial = pandas.read_csv("./tables/teachers_initial.csv")


teachers_name_surname = teachers_initial.axes[1][1]
teachers_address = teachers_initial.axes[1][4]
teachers_index = teachers_initial.axes[1][5]
teachers_email = teachers_initial.axes[1][6]

students_name_surname = students_initial.axes[1][1]
students_address = students_initial.axes[1][4]
students_index = students_initial.axes[1][5]
students_email = students_initial.axes[1][6]



students_main = students_initial.loc[:, [students_name_surname, students_address, students_index, students_email]]
teachers_main = teachers_initial.loc[:, [teachers_name_surname, teachers_address, teachers_index, teachers_email]]
col_names= ["name", "address", "index", "email"]
students_main.columns = col_names
teachers_main.columns = col_names


if len(teachers_main) != len(teachers_main["email"].drop_duplicates()):
    print(teachers_main[teachers_main.duplicated(["email"],keep=False)])
    raise "There are similar columns teachers!"

if len(students_main) != len(students_main["email"].drop_duplicates()):
    print(students_main[students_main.duplicated(["email"],keep=False)])
    raise "There are similar columns students!"

if len(teachers_main) != len(teachers_main.dropna()):
    raise "There are empty strings in teachers!"

if len(students_main) != len(students_main.dropna()):
    raise "There are empty strings in teachers!"




main_table = pandas.concat([students_main, teachers_main], ignore_index=True)
main_table.index.name = "id"
main_table["confirmation_was_sent"] = 0


col_names= [ "confirmation_was_sent", "name", "address", "index", "email"]
main_table = main_table[col_names]




main_table.to_csv("./tables/main.csv")
