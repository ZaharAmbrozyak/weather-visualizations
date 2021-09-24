from csv import reader
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
     reader = reader(f)
     
     header_row = next(reader)

     #0STATION 1NAME 2DATE 3PRCP 4TMAX 5TMIN 6TOBS
     dates, prcp = [], []

     for row in reader:
          current_date = datetime.strptime(row[2], '%Y-%m-%d')
          current_prcp = float(row[3])

          dates.append(current_date)
          prcp.append(current_prcp)

plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(dates, prcp, c='blue')

title = 'Daily prcp - 2018\n Death Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
plt.ylabel('prcp', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
fig.autofmt_xdate()

# plt.savefig(title,bbox_inches='tight')
plt.show()