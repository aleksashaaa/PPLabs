import datetime

#1
now = datetime.datetime.now()
print(now - datetime.timedelta(days = 5))
print("-----")

#2
print(f"Yesterday: {now - datetime.timedelta(days = 1)}")
print(f"Today: {now}")
print(f"Tomorrow: {now + datetime.timedelta(days = 1)}")
print("-----")

#3
print(f"time without microseconds: {now.replace(microsecond=0)}")
print("-----")

#4
first_date = datetime.date(2024, 2, 1)
second_date = datetime.date(2024, 2, 2)
delta = second_date - first_date
print(delta.total_seconds())