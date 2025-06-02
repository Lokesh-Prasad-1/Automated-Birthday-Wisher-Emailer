import pandas
import smtplib
import datetime as dt
import random

my_email = "prasadlokesh8291@gmail.com"
password = "asjt uvjc vsjz keva"

sender_email = "reaperloku8291@gmail.com"

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letters_random = random.choice(letters)

now = dt.datetime.now()
current_date = now.day
current_month = now.month

data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict('index')

for i in data_dict:
    person_name = data_dict[i]['name']
    birth_date = data_dict[i]['day']
    birth_month = data_dict[i]['month']
    person_email = data_dict[i]['email']

    if current_date == birth_date and current_month == birth_month:

        with open(f'letter_templates/{letters_random}', 'r') as letter_data:
            data = letter_data.read()
            name_updated_data = data.replace("[NAME]", f"{person_name}")

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person_email,
                msg=f"Subject:Automated Birthday_Wisher\n\n{name_updated_data}"
            )
    else:
        print('No one have their birthday today')








