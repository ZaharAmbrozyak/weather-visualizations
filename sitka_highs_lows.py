import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
     reader = csv.reader(f)

     header_row = next(reader)

     #1NAME 2DATE 3PRCP 4TAVG 5TMAX 6TMIN
     
     # Отримати дати та високі температури з цього файлу.
     dates, highs, lows = [], [], []
     for row in reader:
          current_date = datetime.strptime(row[2], '%Y-%m-%d')
          high = int(row[5])
          low = int(row[6])

          dates.append(current_date)
          highs.append(high)
          lows.append(low)

# Створити графік високих температур.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Відформатувати графік.
title = "Daily high and low temperatures - 2018"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temeprature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig(f"{title}.png", bbox_inches='tight')
plt.show()
