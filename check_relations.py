import pandas
import json


relations = pandas.read_csv("./tables/result_selected_relations.csv")
main_table = pandas.read_csv("./tables/main.csv")

rel_dict = {}
for i in range(255):
    rel_dict[str(i)] = [0,0]

for index, values in relations.iterrows():
    rel_dict[str(values["participant_id"])][0] += 1
    rel_dict[str(values["target_id"])][1] += 1

for participant in rel_dict:
    if rel_dict[str(participant)][0] != rel_dict[str(participant)][1]:
        raise Exception("Problem")


analyze = pandas.DataFrame(columns=["id", "number_of_options"])
for participant in rel_dict:
    analyze.loc[len(analyze.index)] = [participant, rel_dict[str(participant)][0]]

analyze.to_csv("./tables/analyze.csv", index=False)


json_file = open('./tables/teachers_groups.json', "r")
teachers_groups_dict = json.load(json_file)
for index, values in relations.iterrows():
    participant = main_table.loc[main_table["id"] == values["participant_id"]]
    target = main_table.loc[main_table["id"] == values["target_id"]]
    target_category = target["category_id"].values[0]
    participant_category = participant["category_id"].values[0]
    if target_category == participant_category:
        raise Exception("Problem")
    if target_category == 24 and participant_category not in teachers_groups_dict[str(values["target_id"])]:
        print(values)
        input()
    if participant_category == 24 and target_category not in teachers_groups_dict[str(values["participant_id"])]:
        print(values)
        input()


    
