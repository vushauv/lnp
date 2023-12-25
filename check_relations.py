import pandas


relations = pandas.read_csv("./tables/relations.csv")


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