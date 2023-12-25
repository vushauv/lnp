import pandas 
import os
import time


from config import STUDENTS_INITIAL_TABLE_PATH, TEACHERS_INITIAL_TABLE_PATH, MAIN_TABLE_PATH, COPIED_MAIN_TABLES_PATH


if not os.path.exists(STUDENTS_INITIAL_TABLE_PATH):
    raise Exception("Students initial table does not exist")

if not os.path.exists(TEACHERS_INITIAL_TABLE_PATH):
    raise Exception("Teachers initial table does not exist")

students_initial = pandas.read_csv(STUDENTS_INITIAL_TABLE_PATH)
teachers_initial = pandas.read_csv(TEACHERS_INITIAL_TABLE_PATH)


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


if os.path.exists(MAIN_TABLE_PATH):
    # ADDING NEW USERS TO MAIN TABLE
    print("MAIN TABLE ALREADY EXIST. ONLY NEW DATA WILL BE ADDED TO IT")
    if not input("type Y to continue\n") in "Yy":
        raise Exception("CREATING MAIN TABLE WAS STOPPED")
    else:
        timestr = time.strftime("%d-%m-%y_%H:%M:%S") + "__main.csv"
        os.popen(f'cp {MAIN_TABLE_PATH} {COPIED_MAIN_TABLES_PATH + timestr}')
        print(f"MAIN TABLE WAS COPIED AS {COPIED_MAIN_TABLES_PATH + timestr}")
    
    if not input("type Y to continue\n") in "Yy":
        raise Exception("CREATING MAIN TABLE WAS STOPPED")

    main_table = pandas.read_csv(MAIN_TABLE_PATH)
    main_table = main_table.loc[:,col_names]
    main_table["confirmation_was_sent"] = 1 # Прадугледжвае тое, што ўсім было дастаўлена
    print(f"Table length was: {len(main_table)} users")
    
    
    new_users = pandas.DataFrame(columns=col_names)
    for field, value in students_main.iterrows():
        if len(main_table[main_table["email"] == value["email"]]) == 0:
            print(f"New user {value['email']}")
            new_users.loc[len(new_users)] = value

    for field, value in teachers_main.iterrows():
        if len(main_table[main_table["email"] == value["email"]]) == 0:
            print(f"New user {value['email']}")
            new_users.loc[len(new_users)] = value
    
    new_users["confirmation_was_sent"] = 0
    
    main_table = pandas.concat([main_table, new_users], ignore_index=True)
    col_names= ["confirmation_was_sent", "name", "address", "index", "email"]
    main_table = main_table[col_names]
    main_table.index.name = "id"
    print(f"\n{len(new_users)} user(s) will be added")
    if not input("type Y to continue\n") in "Yy":
        raise Exception("CREATING MAIN TABLE WAS STOPPED")
    else:
        main_table.to_csv(MAIN_TABLE_PATH)


    
else:
    # first creation of the main table
    main_table = pandas.concat([students_main, teachers_main], ignore_index=True)
    main_table.index.name = "id"
    main_table["confirmation_was_sent"] = 0
    col_names= ["confirmation_was_sent", "name", "address", "index", "email"]
    main_table = main_table[col_names]
    main_table.to_csv(MAIN_TABLE_PATH)
    
