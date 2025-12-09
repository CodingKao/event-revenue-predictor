# 🍽️ Catering Event Revenue Prediction (Regression Analysis)

### 📊 Data Science + Financial Analytics Project

This project uses **Python regression modeling** to help a catering business **predict event revenue** based on several key factors — such as number of guests, event type, menu tier, and add-ons.  

The goal is to help sales and finance teams **accurately quote catering events** and understand which business drivers most affect profitability.

---

## 🚀 Project Overview

**Objective:**  
Build a data-driven model to predict total event revenue and uncover key factors influencing profitability.

**Key Results:**
- Achieved an **R² = 0.8345** and **Adjusted R² = 0.8315**, explaining **83% of the variation in event revenue**.  
- Identified that **number of guests, menu tier, and event type** are the strongest predictors of revenue.  
- Seasonal effects were **not statistically significant**, meaning pricing and demand remain stable throughout the year.

---

## 🛠️ Tools & Technologies

| Category | Tools |
|-----------|--------|
| **Programming** | Python |
| **Data Analysis** | Pandas, NumPy |
| **Modeling** | Statsmodels, Scikit-learn |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook, VS Code |

---

## 🧩 Project Workflow

### 1️⃣ Data Generation  
Synthetic data was generated to simulate 500 catering events, with features such as:
- `Guests` (20–500)  
- `Event_Type` (Wedding, Corporate, Birthday)  
- `Menu_Tier` (Basic, Standard, Premium)  
- `Season` (Spring, Summer, Fall, Winter)  
- `Add_Ons` (0–5 optional services)

### 2️⃣ Exploratory Data Analysis (EDA)
- Reviewed distributions, correlations, and pairplots to identify strong predictors of revenue.  
- Found strong linear relationships between revenue, guests, and menu tier.

### 3️⃣ Regression Modeling
- Built an **Ordinary Least Squares (OLS)** regression model using `statsmodels`.  
- Examined coefficients, p-values, and model assumptions.  
- Achieved strong model performance (Adjusted R² = 0.8315).

### 4️⃣ Model Interpretation
| Variable | Coefficient | P-Value | Interpretation |
|-----------|-------------|---------|----------------|
| **Guests** | 86.02 | 0.000 | Each additional guest adds ≈ **\$86** to revenue. |
| **Add_Ons** | 369.12 | 0.054 | Each add-on contributes ≈ **\$369** to revenue. (Marginal significance) |
| **Event_Type_Corporate** | 3,806 | 0.000 | Corporate events earn ≈ **\$3,800** more than birthdays. |
| **Event_Type_Wedding** | 10,560 | 0.000 | Weddings earn ≈ **\$10,500** more than birthdays. |
| **Menu_Tier_Standard** | 4,735 | 0.000 | Standard menus earn ≈ **\$4,700** more than Basic menus. |
| **Menu_Tier_Premium** | 10,240 | 0.000 | Premium menus earn ≈ **\$10,200** more than Basic menus. |
| **Season Variables** | — | >0.05 | No statistically significant effect. |

---

## 🧾 Regression Equation

**Revenue = -11,610**  
+ (86.02 × Guests)  
+ (369.12 × Add_Ons)  
+ (3,806 × Event_Type_Corporate)  
+ (10,560 × Event_Type_Wedding)  
+ (4,735 × Menu_Tier_Standard)  
+ (10,240 × Menu_Tier_Premium)
  
*(Seasonal variables excluded — not statistically significant.)*

---

## 📈 Visual Insights

| Visualization | Description |
|----------------|-------------|
| **Pairplot / Correlation Matrix** | Reveals strong linear correlation between guests, menu tier, and revenue. |
| **Predicted vs Actual Scatterplot** | Shows high model accuracy and low residual error. |
| **Feature Importance Bar Chart** | Highlights which variables contribute most to revenue. |
| **Residual Distribution Plot** | Confirms normally distributed residuals (valid regression assumptions). |

Example Plots:
```python
plt.scatter(model.fittedvalues, y, alpha=0.6)
plt.xlabel("Predicted Revenue")
plt.ylabel("Actual Revenue")
plt.title("Predicted vs Actual Revenue")
plt.show()
