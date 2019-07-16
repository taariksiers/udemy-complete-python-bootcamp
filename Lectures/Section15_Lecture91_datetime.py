import datetime
print(f'datetime\n=================\n')

t = datetime.time(5, 25, 10)
print(f't = datetime.time(5, 25, 10) | {t} type {type(t)} | t.minute {t.minute} | t.hour {t.hour} | t.tzname {t.tzname} | datetime.time.min {datetime.time.min} | datetime.time.resolution {datetime.time.resolution}\n')

today = datetime.date.today()
print(f'today {today} | today.timetuple() {today.timetuple()}\n')

print(f'today.year {today.year} | today.month {today.month}\n')

print(f'min {datetime.date.min} - max {datetime.date.max} | {datetime.date.resolution}')

d1 = datetime.date(2015,3,11)
print(f'd1 = datetime.date(2015,3,11) | {d1}')

d2 = d1.replace(year=1990)
print(f'd2 = d1.replace(year=1990) | {d2}')

print(f'd1 - d2 {d1 - d2}')
