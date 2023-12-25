import pandas
import json

from config import MAIN_TABLE_PATH, STUDENTS_INITIAL_TABLE_PATH,TEACHERS_INITIAL_TABLE_PATH

main_table = pandas.read_csv(MAIN_TABLE_PATH)
# students_initial = pandas.read_csv(STUDENTS_INITIAL_TABLE_PATH)
# teachers_initial = pandas.read_csv(TEACHERS_INITIAL_TABLE_PATH)



i = 0
for field_participant, value_participant in main_table.iterrows():
    # create links for students
    
    if value_participant["category_id"] in [24,25]:
        print(value_participant["id"], "teacher")
        continue
        print(value_participant)
    links_table = pandas.DataFrame(columns=["participant_id", "target_id"])
    for field_target, value_target in main_table.iterrows():
        if (value_target["category_id"] not in [24, 25] and
            value_target["category_id"] != value_participant["category_id"]):
            links_table.loc[len(links_table.index)] = [value_participant["id"], value_target["id"]]
    if i == 0:
        links_table.to_csv("./tables/relations.csv", mode="a", index=False)
    else:
        links_table.to_csv("./tables/relations.csv", mode="a", index=False, header=False)
    i += 1



json_file = open('./tables/teachers_groups.json', "r")
teachers_groups_dict = json.load(json_file)

for field_participant, value_participant in main_table.iterrows():
    # create relations for teachers
    if value_participant["category_id"] != 24:
        continue
    print(value_participant)
    links_table = pandas.DataFrame(columns=["participant_id", "target_id"])
    for field_target, value_target in main_table.iterrows():
        if (value_target["category_id"] in teachers_groups_dict[str(value_participant["id"])]):
            links_table.loc[len(links_table.index)] = [value_participant["id"], value_target["id"]]
            links_table.loc[len(links_table.index)] = [value_target["id"], value_participant["id"]]

    links_table.to_csv("./tables/relations.csv", mode="a", index=False, header=False)
    

