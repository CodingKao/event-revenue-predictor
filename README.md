# 🍽️ Catering Revenue Predictive Analysis

## 📊 Overview
This project uses **predictive analytics** to estimate catering event revenue based on various cost and event factors.  
It’s designed for catering businesses that want to **optimize pricing, improve forecasting, and evaluate profitability** across different event types such as weddings, corporate events, and networking functions.

The dataset used here is **synthetically generated using Python**, allowing full control and reproducibility.

---

## 🧠 Objective
Build a machine learning model that predicts **total event revenue** given input variables such as:
- Food cost
- Labor hours
- Guest count
- Event type (Wedding, Corporate, Networking)
- Season and location

The model aims to support **pricing decisions, cost forecasting, and revenue optimization** for catering businesses.

---

## 🧩 Project Workflow

1. **Data Generation**
   - Generate a synthetic dataset (`synthetic_catering_data.csv`) with random but realistic cost and event values.
   - Dataset includes columns such as:
     - `event_type`
     - `guest_count`
     - `food_cost`
     - `labor_hours`
     - `equipment_cost`
     - `beverage_cost`
     - `season`
     - `revenue` *(target variable)*

2. **Exploratory Data Analysis (EDA)**
   - Identify relationships between costs and revenue.
   - Visualize distributions and correlations using seaborn and matplotlib.

3. **Feature Engineering**
   - Add derived variables like `cost_per_guest` and interaction features.
   - Encode categorical features (e.g., `event_type`, `season`).

4. **Model Training**
   - Train regression models to predict revenue:
     - Linear Regression (baseline)
     - Random Forest Regressor (optimized)
   - Evaluate using MAE, RMSE, and R² metrics.

5. **Scenario Analysis**
   - Predict revenue for custom event inputs.
   - Test “what-if” scenarios (e.g., rising food cost or higher guest count).

6. **Visualization**
   - Compare predicted vs. actual revenue.
   - Create feature importance plots to identify key drivers.

---

## 🧰 Tools & Libraries
- Python 3.10+
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- Jupyter Notebook

---

## 💡 Business Application
This model can be applied by catering businesses to:
- **Estimate event pricing** before sending client quotes  
- **Forecast monthly/quarterly revenue** based on pipeline events  
- **Optimize resource allocation** (staffing, inventory, etc.)  
- **Simulate scenarios** to understand profit sensitivity to costs

---

