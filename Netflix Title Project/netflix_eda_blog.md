# 🎬 Analyzing Netflix’s Global Content: Which Countries Produce the Most Titles?

## ✨ Introduction

Netflix is a powerhouse in streaming, boasting thousands of movies and TV shows from around the world. But which countries are producing the most content on Netflix? In this project, I explored Netflix’s global catalog to uncover the top countries contributing titles to the platform.

## 🔍 Objective

The goal was simple:
- Clean and preprocess Netflix’s dataset.
- Analyze the number of titles produced by country.
- Visualize the top countries by title count.
- Practice key data analysis and visualization skills using Python.

## 🗂 Dataset Overview

I worked with the publicly available `netflix_titles.csv` dataset, which contains:
- `title`
- `country`
- `director`
- `cast`
- `date_added`
- `duration`
- `rating`
- and more...

## 🧹 Step 1: Data Cleaning

The dataset had some missing values, especially for `director`, `cast`, `date_added`, `duration`, `country`, and `rating`. I cleaned the data by:
- Filling missing director and cast values with `'Unknown'`.
- Dropping entries with missing country or rating fields (essential for analysis).

```python
netflixData['director'] = netflixData['director'].fillna('Unknown')
netflixData['cast'] = netflixData['cast'].fillna('Unknown')
netflixData = netflixData.dropna(subset=['country', 'rating'])
```

## 🔍 Step 2: Handling Multiple Countries

Many titles are co-productions across multiple countries, listed as comma-separated values in the country column. To get accurate counts, I:

Split the country column by commas.

Used the .explode() function to create one row per country per title.
```
countryList = netflixData['country'].str.split(', ').explode()
```

## 📊 Step 3: Analysis & Visualization
I counted the number of titles per country and identified the Top 10: 
```
countryCount = countryList.value_counts().head(10)
```

Then I plotted a bar chart using Seaborn for a clear visual:
```
sns.barplot(x=countryCount.index, y=countryCount.values, palette='viridis')
```

## 📉 Insights
#### 🏆 Top 10 Countries:

1. United States   
2. India 
3. United Kingdom 
4. Canada 
5. France 
6. Japan
7. Spain
8. South Korea
9. Germany 
10. Mexico

- **The United States leads by a large margin, followed by India, the United Kingdom, and Canada.**
- **The results reflect both the size of production industries and Netflix’s international licensing deals.**
- **Co-productions make it important to carefully handle multi-country data.**

## 🧰 Tools Used
- **Python**
- **pandas, seaborn, matplotlib**
- **Visual Studio Code**

## 📎 How to Run
1. Download the dataset and script.
2. Make sure both are in the same folder.
3. Install dependencies:
```
pip install pandas matplotlib seaborn
```
4. Run the script:
```
python netflixProject.py
```

## 🎯 Conclusion
This simple yet insightful analysis highlights the global nature of Netflix’s content library. It also reinforces important data cleaning techniques for messy real-world data — especially handling multi-valued fields.

