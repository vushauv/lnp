import pandas
import os

categories = pandas.read_csv("./tables/categories.csv")
relations = pandas.read_csv("./tables/result_selected_relations.csv")
main_table = pandas.read_csv("./tables/main.csv")

for field, values in relations.iterrows():
    if os.path.exists(f"./emails_text/final_emails/{values['participant_id']}.html"):
        continue
    pairs = relations.loc[relations["participant_id"] == values["participant_id"]]
    print(len(pairs))
    targets_data = []
    for pair in pairs.values:
        target_frame = main_table.loc[main_table["id"] == pair[1]].values[0]
        targets_data.append(
            {
                "name": target_frame[3],
                "category": categories.loc[categories["category_id"] == target_frame[2]]["category_name"].values[0] ,
                "address": target_frame[4],
                "index": target_frame[5],
            }
        )
        html_file = open("./emails_text/final.html", "r")
        html = html_file.read()
        html_file.close()


        html_text = ""
        for target in targets_data:
            html_text += f'<li><em>{target["name"]} ({target["category"]}) — {target["address"]} — {target["index"]}</em></li>\n'
            html_text += '<hr style="text-align:left;width:75%;background-color:#4B6A9C; height:1px;">'
        html = html.replace("$list", html_text)
        

        final_html_file = open(f"./emails_text/final_emails/{values['participant_id']}.html", "w")
        final_html_file.write(html)
        final_html_file.close()


        text_file = open("./emails_text/final.txt", "r")
        text = text_file.read()
        text_file.close()


        inner_text = ""
        for target in targets_data:
            inner_text += f'- {target["name"]} ({target["category"]}) — {target["address"]} — {target["index"]}\n'
        text = text.replace("$list", inner_text)

        final_txt_file = open(f"./emails_text/final_texts/{values['participant_id']}.txt", "w")
        final_txt_file.write(text)
        final_txt_file.close()

