# 📊 Fragile States Index (FSI) – Data Mining & Action Rule Analysis

## 🔍 Overview
This project analyzes the **Fragile States Index (FSI)** using machine learning and action rule mining to identify key socio-economic factors influencing national stability and generate actionable policy insights.

---

## 🎯 Objectives
- Classify countries into fragility categories
- Evaluate impact of external socio-economic features
- Generate actionable rules for improving state stability

---

## 🧠 Methodology

### 📁 Data Sources
- Fragile States Index (2019–2021)
- World Bank datasets:
  - GDP per capita
  - Internet usage
  - Life expectancy
  - Military expenditure

### ⚙️ Data Processing
- Data cleaning & transformation using Python
- Feature integration across datasets
- Discretization for rule mining (Low / Medium / High)

### 🤖 Machine Learning (WEKA)
- J48 Decision Tree  
- Random Forest  
- Bagging  
- PART (Rule-based classifier)

### 🔁 Action Rule Mining
- Tool: **LISP Miner**
- Algorithm: **AC4FT**
- Focus: Transition rules (e.g., Alert → Sustainable)

---

## 📈 Results

| Model | Accuracy |
|------|--------|
| Random Forest | ~96% |
| J48 | ~92% |
| Bagging | ~90% |
| PART | ~91–93% |

👉 External features improved **interpretability**, not predictive accuracy.

---

## ⚡ Key Insights
- GDP, Internet usage, and Life Expectancy strongly reduce fragility
- Military expenditure alone has weak correlation
- Multi-factor improvements lead to stronger stability transitions

---

## 🔁 Sample Action Rules
- GDP: Low → High ⇒ Alert → Very Sustainable  
- Internet + Military ⇒ Warning → Very Sustainable  
- Life Expectancy: Medium → High ⇒ Warning → Sustainable  

---

## 📊 Visual Insights

![Correlation Heatmap](images/Correlation Heatmap.jpeg)
![Scatter Plot](images/scatterplot1.jpeg)

---

## 🛠️ Tech Stack
- Python (Data Processing)
- WEKA (Machine Learning)
- LISP Miner (Action Rule Mining)
- Excel / CSV datasets

---

## 📂 Project Structure
- `data/` → Raw & processed datasets  
- `scripts/` → Data cleaning & feature engineering  
- `weka/` → ML-ready datasets  
- `lisp-miner/` → Rule mining datasets  
- `images/` → Visualizations  
- `report/` → Full project documentation  

---

## 📄 Documentation
Full project report available here:  
📌 `report/Data_Mining_Project_Report.pdf`

---

## 🚀 Key Takeaway
This project demonstrates how data mining can move beyond prediction to **actionable decision-making**, providing real-world policy insights.
