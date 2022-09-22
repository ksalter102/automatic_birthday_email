import smtplib
from datetime import datetime
import random
import pandas

# TODO Add code to 'Pythonanywhere' to constantly run code,
#  create a bash console, run python3 main.py,
#  follow support URL to config email.
#  Create scheduled task for the code to run at a scheduled time.

MY_EMAIL = "fakeemail@gmail.com" # TODO Change to email
PASSWORD = "qwerty" # TODO Change to password

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv") #TODO Change CSV for pers use

birthday_dict = {(data_row["month"], data_row["day"]):
                 data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    file_path = f"letter_{random.randint(1,3)}.txt"
    birthday_person = birthday_dict[today_tuple]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        message = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encrypts email
        connection.login(user=MY_EMAIL,
                         password=PASSWORD)
        connection.sendmail(

            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{message}"
        )