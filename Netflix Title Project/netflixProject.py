import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

netflixData = pd.read_csv('netflix_titles.csv')

print(netflixData.head(), "\n") 

print(netflixData.info(), "\n")

netflixData['director'] = netflixData['director'].fillna('Unknown')
netflixData['cast'] = netflixData['cast'].fillna('Unknown')
netflixData['date_added'] = netflixData['date_added'].fillna('Unknown')
netflixData['duration'] = netflixData['duration'].fillna('Unknown')
netflixData = netflixData.dropna(subset=['country'])
netflixData = netflixData.dropna(subset=['rating'])

print(netflixData.isnull().sum())

countryList = netflixData['country'].str.split(', ').explode()
countryCount = countryList.value_counts().head(10)
print(countryCount)

plt.figure(figsize=(10, 6))
sns.barplot( x=countryCount.index, y=countryCount.values, palette='viridis')
plt.title('Top 10 Countries by Number of Netflix Titles')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()


