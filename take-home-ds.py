import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# plt.rcParams['figure.figsize'] = [20,5]
df = pd.read_csv('seattle-crime.csv')

#crime type histogram
df['Crime_Type'].hist(bins=10)
plt.show()

#box & whisker plot for all crimes
df['Crime_Type'].plot.box()

#How many unique crimes are there?
df['Crime_Type'].nunique()

#what was the largest number of crimes by type for the year 1996
df[df['Report_Year'] == '1996'].groupby('Crime_Type')['Report_Year_Total'].agg(np.max)

#Crime Types in a Pie Chart
df['Crime_Type'].value_counts().plot(kind='pie')

#making a table of where rows are numbers of a specific crime and columns are years
pd.crosstab(df['Crime_Type'], df['Report_Year'])