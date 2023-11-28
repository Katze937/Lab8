import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Top_rated_movies1.csv')

print(df.head())
print(df.info())
print(df.describe())

sns.histplot(df['popularity'])
plt.show()


plt.savefig('histogram.png')

