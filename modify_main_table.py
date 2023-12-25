import pandas
from config import MAIN_TABLE_PATH, STUDENTS_INITIAL_TABLE_PATH, TEACHERS_INITIAL_TABLE_PATH


main_table = pandas.read_csv(MAIN_TABLE_PATH)
students_initial = pandas.read_csv(STUDENTS_INITIAL_TABLE_PATH)
teachers_initial = pandas.read_csv(TEACHERS_INITIAL_TABLE_PATH)
categories_table = pandas.read_csv("./tables/categories.csv")

print(main_table)

main_table["category_id"] = 0

for field, value in main_table.iterrows():
    # print(value)
    student = students_initial.loc[students_initial["Ваш адрас электроннай пошты:"] == value["email"]]
    teacher = teachers_initial.loc[teachers_initial["Ваш адрас электроннай пошты:"] == value["email"]]
    
    category = -1
    if len(student) != 0 and len(teacher) == 0:
        category_number = student["Укажыце сваю паралель:"]
        category_name = student["Укажыце свой профіль:"]
        category = category_number + " " + category_name
        category = category.values[0]
        if category == "11 Э/ЭГ":
            category = "11 Э"
        elif category == "10 Э/ЭГ":
            category = "10 ЭГ"
        elif category == "10 Л/ГРАМ":
            category = "10 ГРАМ"
        elif category == "11 Л/ГРАМ":
            category = "11 Л"
        if category_number.values[0] == ">12":
            category = ">12 Выпускнік"
    elif len(teacher) != 0 and len(student) == 0:
        category = teacher["Вы:"]
        category = category.values[0]
    
    try:
        category = categories_table.loc[categories_table["category_name"] == category]["category_id"].values[0]
    except:
        print(value)
        raise Exception("Пізьдзец 1")
    if category == -1:
        raise Exception("Пізьдзец")

    main_table.loc[main_table["id"] == value["id"], ["category_id"]] = int(category)
    if len(main_table) > 242:
        main_table.to_csv("new_main.csv", index= False)
        print(value)
        input()
    # print(value["id"])

col_names= ["id", "confirmation_was_sent", "category_id", "name", "address", "index", "email"]
main_table = main_table[col_names]
# main_table.astype({'id': 'int32'})

main_table.to_csv(MAIN_TABLE_PATH, index= False)