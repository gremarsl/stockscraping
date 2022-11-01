import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
'''
Pipeline / Procedure: From data to plot
'''

#Get data - e.g. .csv
file = "D:\\Desktop\\GOOGL\\balanceAnnual.csv"

#Transform data to a panda dataframa
df = pd.read_csv(file, sep=';', decimal=",")

plot_1 = ["TotalRevenue","CostOfRevenue","GrossProfit"] #calc gross margin

x = df["index"]
y1 = df["TotalAssets"]
y2 = df["CurrentRatio"]
y3 = df["TotalLiabilities"]

i1 = "TotalAssets"
i2 = "CurrentRatio"
i3 = "TotalLiabilities"
print(df.columns)

print(y2)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

x_axis = np.arange(len(x))
# Bar Plotting
w = 0.3
if len(x) == len(y1):
    ax1.bar(x_axis +w, y1,width=w, label=i1, color="green")
    ax1.bar(x_axis,y3,width=w,label=i3,color="red")

else:
    print(f"ERROR - Length of x is {len(x)} and length of y is {len(y1)} - must be same")

# Scatter Plotting
if len(x) == len(y2):
    ax2.plot(x, y2, label=i2, color="blue")
    ax2.scatter(x, y2)

else:
    print(f"ERROR - Length of x is {len(x)} and length of y is {len(y2)} - must be same")

# show grid
plt.grid(b=None, which='major', axis='both')
plt.xticks(rotation="vertical")
plt.title(f'GOOGL Data')

plt.xlabel('Year')
plt.ylabel('USD')


ax1.set_ylabel('USD')
ax2.set_ylabel('Ratio')
# plot_full_screen()

ax1.legend(loc='center left', bbox_to_anchor=(0, 0.5))
ax2.legend(loc='center right', bbox_to_anchor=(1, 0.5))
plt.show()
