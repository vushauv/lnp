import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas
import time

from config import SENDER_EMAIL, PASSWORD








def send_confirmation(sender_email, receiver_data,  password):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Пацвярджэнне Ўдзелу"
    message["From"] = "ЛНП"
    message["To"] = receiver_data["email"]

    f = open("./emails_text/confirmation.txt", "r")
    text = f.read()
    text = text.replace("$name", receiver_data["name"])
    text = text.replace("$address", receiver_data["address"])
    text = text.replace("$index", receiver_data["index"])
    f.close()

    f = open("./emails_text/confirmation.html", "r")
    html = f.read()
    html = html.replace("$name", receiver_data["name"])
    html = html.replace("$address", receiver_data["address"])
    html = html.replace("$index", receiver_data["index"])
    f.close()

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    context = ssl.create_default_context()


    f = open(f"./emails_text/confirmation_emails/{receiver_data['id']}.html", "w")
    f.write(html)
    f.close()


    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_data["email"], message.as_string())
        print(f"Email was sent to {receiver_data['email']}")


main_table = pandas.read_csv("./tables/main.csv")
i = 0
for field, value in main_table.iterrows():
    receiver_data = {
        "email": value["email"],
        "address": value["address"],
        "name": value["name"],
        "index": value["index"],
        "id": value["id"],
    }
    
    if(value["confirmation_was_sent"] == 0):
        try:
            send_confirmation(SENDER_EMAIL, receiver_data, PASSWORD)
            table = pandas.read_csv("./tables/main.csv")
            table.loc[table["id"] == value["id"], "confirmation_was_sent"] = 1
            table.to_csv("./tables/main.csv", index=False)
            time.sleep(0.5)
            i += 1
        except:
            print(f"{i} Email was not sent to {receiver_data['email']}")
            input()
    if i == 20:
        break
    



            
# send_confirmation(SENDER_EMAIL, receiver_data, PASSWORD)