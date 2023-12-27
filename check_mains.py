import pandas

main_original = pandas.read_csv("./tables/copied_tables/main.csv")
main_last = pandas.read_csv("./tables/main.csv")


for field, values in main_original.iterrows():
    new = main_last.loc[main_last["id"] == values["id"]]
    if len(new) == 0:
        print(f"there is no {values}")
        input()
        continue
    new = new.values[0]
    old = values.values


    new_name = new[3]
    new_name = new_name.replace(" ", "")
    new_name = new_name.replace("&nbsp;","")

    old_name = old[2]
    old_name = old_name.replace(" ", "")

    if old_name != new_name:
        print(new_name)
        print(old_name)
        print()
        input()

    new_name = new[4]
    new_name = new_name.replace(" ", "")
    new_name = new_name.replace("&nbsp;","")

    old_name = old[3]
    old_name = old_name.replace(" ", "")

    if old_name != new_name:
        print(new_name)
        print(old_name)
        print()
        input()
