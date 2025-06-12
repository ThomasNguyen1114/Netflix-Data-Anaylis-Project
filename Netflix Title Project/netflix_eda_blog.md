## 🎬 Netflix Movies Around the World: What the Data Says  
*By Thomas Nguyen*

---

### 📊 Introduction

Netflix is home to thousands of movies from around the globe, but have you ever wondered which countries produce the most content on the platform? In this exploratory data analysis (EDA), I dug into a public dataset of Netflix titles to find out. I cleaned up the data, and visualized an interesting trends by looking at the countries.

---

### 🗓 Loading and Cleaning the Data

I used the `netflix_titles.csv` dataset available on Kaggle. It contains information about movies and TV shows on Netflix, including title, type, director, country, release year, and maturity rating.

Many rows had multiple countries listed (e.g., "United States, Canada"). To accurately count movie production by country, I split them.

### 🌍 Which Countries Make the Most Netflix Movies?

After cleaning the data, I counted how many times each country appeared:

Then I visualized it using Seaborn:

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

Unsurprisingly, the U.S. leads by a wide margin, but it's interesting to see India and the U.K. following close behind.

### 📁 Tools Used

- Python 🐍  
- pandas  
- seaborn & matplotlib  
- Jupyter Notebook
