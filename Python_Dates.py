
import datetime
import time


# ------------------------------------------------------------------------------------------------ #
# DATETIME MODULE (GET CURRENT TIME)

# current_time = datetime.datetime.today()
# print('{:%H:%M}'.format(current_time))  # 21:59
# print('{:%A, %B %d, %Y}'.format(current_time))  # Sunday, July 22, 2018
# print(current_time.year)  # 2018


# ------------------------------------------------------------------------------------------------ #
# DATETIME MODULE (GET TODAY'S DATE)

# now = datetime.datetime.today()
# print(now)  # 2018-07-22 22:09:12.435136

# ------------------------------------------------------------------------------------------------ #
# DATETIME MODULE (DATE=dates, TIME=times, DATETIME=dates and times)

# first_launch = datetime.date(2017, 3, 30)
# print(first_launch)
# print(first_launch.year)
# print(first_launch.month)
# print(first_launch.day)

# launch_time = datetime.time(22, 27, 5, 256255)
# print(launch_time)
# print(launch_time.hour)
# print(launch_time.minute)
# print(launch_time.second)
# print(launch_time.microsecond)

# launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
# print(launch_datetime)
# print(launch_datetime.year)
# print(launch_datetime.month)
# print(launch_datetime.day)
# print(launch_datetime.hour)
# print(launch_datetime.minute)
# print(launch_datetime.second)
# print(launch_datetime.microsecond)


# ------------------------------------------------------------------------------------------------ #
# DATETIME MODULE (DATE)

# bnl = datetime.date(1978, 5, 4)
# bnl_message = 'Brett Lampson was born on {:%A, %B %d, %Y}.'
# print(bnl_message.format(bnl))  # Brett Lampson was born on Thursday, May 04, 1978.


# ------------------------------------------------------------------------------------------------ #
# CONVERT A STRING TO A DATETIME OBJECT

# moon_landing = '7-20-1969'
# moon_landing_datetime = datetime.datetime.strptime(moon_landing, '%m-%d-%Y')
# print(moon_landing_datetime)  # 1969-07-20 00:00:00


# ------------------------------------------------------------------------------------------------ #
# TIMEDELTA (FOR CALCULATING BETWEEN DATES) ADD OR SUBTRACT NUMBER OF DAYS FROM A DATE

# y2k = datetime.date(2000, 1, 1)
# days_100 = datetime.timedelta(100)  # 100 days later, -100 days earlier
# print(y2k + days_100)  # 2000-04-10


# ------------------------------------------------------------------------------------------------ #
# MODULE LISTS

# for i in dir(datetime):
#     if not i.startswith('__'):
#         print(i, end=' / ')
# MAXYEAR / MINYEAR / date / datetime / datetime_CAPI / time / timedelta / timezone / tzinfo

#
# for i in dir(datetime.date):
#     if not i.startswith('__'):
#         print(i, end=' / ')
# ctime / day / fromordinal / fromtimestamp / isocalendar / isoformat / isoweekday / max / min
# month / replace / resolution / strftime / timetuple / today / toordinal / weekday / year



