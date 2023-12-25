import pandas
import json 


from config import TEACHERS_INITIAL_TABLE_PATH, MAIN_TABLE_PATH


teachers_initial = pandas.read_csv(TEACHERS_INITIAL_TABLE_PATH)
categories_table = pandas.read_csv("./tables/categories.csv")
main_table = pandas.read_csv(MAIN_TABLE_PATH)


teachers_categories_dict = {}
for field, value in teachers_initial.iterrows():
    working_groups = value["Калі ласка, адзначце класы, у якіх вы выкладаеце:"]
    if working_groups == "Творчы саюз/Супрацоўнік/Іншае":
        continue
    working_groups = working_groups.split(", ")
    print(working_groups)

    # find id for a teacher
    id = main_table.loc[main_table["email"] == value["Ваш адрас электроннай пошты:"]]["id"].values[0]
    print(id)
    for i in  range(len(working_groups)):
        if working_groups[i] == "Творчы саюз/Супрацоўнік/Іншае":
            working_groups.remove(working_groups[i])
            continue
        working_groups[i] = categories_table.loc[categories_table["category_name"] == working_groups[i]].values[0][0]
    teachers_categories_dict[str(id)] = working_groups

with open("./tables/teachers_groups.json", "w") as outfile: 
    json.dump(teachers_categories_dict, outfile, indent = 4)
    
