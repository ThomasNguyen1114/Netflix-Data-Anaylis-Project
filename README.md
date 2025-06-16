# 🎬 Netflix Titles Analysis Project

This project analyzes Netflix's global content catalog using Python. It focuses on identifying which countries produce the most titles on the platform, while practicing fundamental data analysis and visualization techniques.

---

## 📌 Project Features

- **Data Cleaning:** Handled missing values for key columns (`director`, `cast`, `date_added`, `duration`, `country`, `rating`).
- **Exploding Country Field:** Used `.explode()` to break out multiple countries listed per title for accurate counting.
- **Top Countries Analysis:** Counted and visualized the top 10 countries producing Netflix content.
- **Data Visualization:** Created a bar plot using Seaborn and Matplotlib.

---

## 🛠 Technologies Used

- Python (with libraries: pandas, seaborn, matplotlib)
- Visual Studio Code (for development)

---

## ▶️ How to Run the Project

1. Clone the repository or download the script file.
2. Make sure the dataset file `netflix_titles.csv` is in the same directory as the script.
3. Install required libraries:
   ```
   pip install pandas matplotlib seaborn
   ```
4. Run the script in your IDE or terminal:
   ```
   python netflixProject.py
   ```

---

## 📬 Author

**Thomas Nguyen**
