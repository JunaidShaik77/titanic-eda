# Titanic Exploratory Data Analysis (EDA) & Dashboard

## 📌 Project Overview
This project performs **exploratory data analysis (EDA)** on the Titanic dataset to uncover patterns related to passenger survival.  
It includes **visual insights**, **feature analysis**, and an optional **interactive dashboard** built with Streamlit.

---

## 📊 Dataset
- Source: Built-in Seaborn Titanic dataset (`sns.load_dataset("titanic")`)  
- Key Features:
  - `survived` — whether passenger survived (0 = No, 1 = Yes)
  - `pclass` — passenger class (1, 2, 3)
  - `sex` — gender
  - `age`, `fare` — numerical features
  - `sibsp`, `parch` — family aboard
  - Others: `embarked`, `who`, `adult_male`, `alone`, etc.

---

## 🛠️ Tools & Libraries
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit (optional for interactive dashboard)

---

## 🔍 Analysis & Visual Insights
- **Overall Survival:** More passengers did not survive than survived.  
- **Gender:** Women had significantly higher survival rates.  
- **Passenger Class:** Higher-class passengers (1st class) survived more often.  
- **Age:** Children and younger adults had higher survival probability.  
- **Fare:** Passengers who paid higher fares tended to survive more.  
- **Family Size:** Small families and solo passengers had varying survival chances.

> Screenshots of charts are saved in `images/` folder.  

---

## 📈 Visualizations
- Countplots: Overall survival, gender, class  
- Boxplots: Fare distribution by survival  
- Violinplots: Age distribution by sex & survival  
- Correlation heatmap: Numeric feature correlations  
- Survival % by class & sex (pivot heatmap)  

---

## 🚀 Interactive Dashboard (Optional)
A **Streamlit dashboard** allows filtering by:
- Gender
- Passenger class
- Age group

Run locally:
```bash
pip install streamlit
streamlit run app.py
