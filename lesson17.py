# dates
from datetime import date, timedelta, datetime

today = date.today()
print(today)

formatted_date = today.strftime("%a, %d-%b-%Y")
print(formatted_date)

after_34_days = today + timedelta(days=34)
print(after_34_days)

dob = "2003-01-28"
# convert to date object
date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
age = today.year - date_of_birth.year
print("I am ",age, "years old")

age_in_days = datetime.today()- date_of_birth
print(age_in_days.days)