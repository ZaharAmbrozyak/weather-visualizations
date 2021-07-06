from csv import reader
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
     reader = reader(f)

     header_row = next(reader)

     #0STATION 1NAME 2DATE 3PRCP 4TAVG 5TMAX 6TMIN
     prcp, dates = [], []

     for row in reader:
          current_date = datetime.strptime(row[2], '%Y-%m-%d')
          current_prcp = float(row[3])

          dates.append(current_date)
          prcp.append(current_prcp)

plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(dates, prcp, c='blue')

title = 'Daily prcp - 2018\n Sitka'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
plt.ylabel('prcp', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

# plt.savefig(title, bbox_inches='tight')
plt.show()