#coding:utf-8
"""
Manage with date
"""
import datetime


print("Today date is :", datetime.date.today())
print("Today date time is :", datetime.datetime.now())

d1 = datetime.date(2018, 12, 28)
d2 = datetime.date(2018, 12, 27)
print("Date 1 :", d1, "et date 2 :", d2)
print("d1 est anterieur a d2 :", d1 < d2)
print("d1 est posterieur a d2 :", d1 > d2)
print("Get year :", d1.year, ", get month : ", d1.month, ", get day :", d1.day)

t1 = datetime.time(13, 58, 20)
print("Get hour :", t1.hour, ", get minute : ", t1.minute, ", get seconds :", t1.second)