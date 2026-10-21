import os
##################### Extra Hard Starting Project ######################

import smtplib
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# ----------------------------birthday data to dict---------------------------------------------------------------------
import pandas

from main import my_email

birthday_data=pandas.read_csv("birthdays.csv")
birthday_data_dict=birthday_data.to_dict(orient="records")
print(birthday_data_dict)
# ------------------------------today's date and time-------------------------------------------------------------------
from datetime import *

date_data=datetime.now()
month=float(date_data.month)
print(month)
day=float(date_data.day)
print(day)
# -----------------------------------logic for ending wishes------------------------------------------------------------
for person in birthday_data_dict:
    if person["month"]==month and person["day"]==day:
        print(person)
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            greeting=letter.read()
            letter_wish=greeting.replace("[NAME]",person["name"])
            print(letter_wish)

# ------------------------------------sending Email to person-----------------------------------------------------------


        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=f"{person["email"]}",msg=f"Subject:Birthday Wish\n\n{letter_wish}")
