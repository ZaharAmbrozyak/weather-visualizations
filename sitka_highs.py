import csv
from datetime import date, datetime
import matplotlib.pyplot as plt


filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
     reader = csv.reader(f)

     header_row = next(reader)

     #1NAME 2DATE 3PRCP 4TAVG 5TMAX 6TMIN
     
     # Отримати дати та високі температури з цього файлу.
     dates, highs = [], []
     for row in reader:
          current_date = datetime.strptime(row[2], '%Y-%m-%d')
          high = int(row[5])

          dates.append(current_date)
          highs.append(high)

# Створити графік високих температур.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Відформатувати графік.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temepratur (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
