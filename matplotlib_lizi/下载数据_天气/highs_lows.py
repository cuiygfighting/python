import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)


    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            high=int(row[1])
            low=int(row[3])
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
        except ValueError:
            print(current_date,'missing_date')
        else:
            lows.append(low)
            highs.append(high)
            dates.append(current_date)

    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    plt.title('Daily TemperatureJuly 2014',fontsize=24)
    plt.xlabel("",fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('T(F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()
