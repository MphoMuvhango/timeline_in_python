from theflile import GenerateTimeLine
import pandas as pd
data = pd.read_csv(r'events.txt', parse_dates=True, index_col=0)
ax = GenerateTimeLine(data)
plt.show()
