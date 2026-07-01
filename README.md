# 🎓 Student Performance Prediction System

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?style=flat&logo=flask)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

> A Machine Learning web application that predicts a student's performance based on key academic and behavioral indicators.

🔗 **Live Demo:** [https://student-performance-prediction-puuj.onrender.com](https://student-performance-prediction-puuj.onrender.com)

---

## 📌 Table of Contents

- [Objective](#-objective)
- [Dataset](#-dataset)
- [ML Lifecycle](#-ml-lifecycle)
- [Models Used](#-models-used)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How to Run Locally](#-how-to-run-locally)
- [Results](#-results)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Objective

To predict a student's academic performance grade using machine learning by analyzing factors such as:
- Academic percentage & GPA
- Weekly study hours
- Class absences
- Parental education & support level
- Extracurricular involvement
- Tutoring status

---

## 📦 Dataset

| Property | Details |
|---|---|
| **Source** | Kaggle — Students Performance Dataset |
| **Author** | Rabie El Kharoua |
| **Records** | 2,392 students |
| **Features** | 15 attributes |
| **Target** | GradeClass (A / B / C / D / F) |

**Key Features Used:**
- `GPA` — Grade Point Average
- `Absences` — Number of classes missed
- `StudyTimeWeekly` — Weekly study hours
- `ParentalSupport` — Level of parental support (0–4)
- `ParentalEducation` — Education level of parents
- `Tutoring` — Whether student receives private tutoring
- `Extracurricular`, `Sports`, `Music`, `Volunteering` — Activity involvement

---

## 🔄 ML Lifecycle

The project follows the complete Machine Learning lifecycle:

| Phase | Description |
|---|---|
| **Phase 1** | Problem Understanding & Objective Definition |
| **Phase 2** | Data Collection from Kaggle |
| **Phase 3** | Data Preprocessing — missing values, duplicates, outliers, normalization |
| **Phase 4** | Exploratory Data Analysis — histograms, heatmaps, scatter plots, boxplots |
| **Phase 5** | Feature Engineering — Engagement Ratio, Activity Score, Support Index |
| **Phase 6** | Model Building — 3 ML models trained |
| **Phase 7** | Model Evaluation — Accuracy, F1, ROC-AUC, Confusion Matrix |
| **Phase 8** | Deployment — Flask app deployed on Render |

---

## 🤖 Models Used

| Model | Accuracy |
|---|---|
| Logistic Regression | ~82% |
| Random Forest | ~92% |
| **XGBoost (Best)** | **~93%** |

**Evaluation Metrics:** Accuracy, Precision, Recall, F1 Score, ROC-AUC

**Best Model:** XGBoost — saved as `Model/xgboost.pkl`

---
<a name="-tech-stack"></a>
## 🛠️ Tech Stack



| Category | Tools |
|---|---|
| **Language** | Python 3.13 |
| **ML Libraries** | Scikit-learn, XGBoost, Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Web Framework** | Flask |
| **Frontend** | HTML, CSS (Glassmorphism UI) |
| **Deployment** | Render (Free Tier) |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```text
Student_Performance_Prediction/
│
├── Dataset/
│   ├── student_performance.csv       # Raw dataset
│   ├── cleaned_data.csv              # After preprocessing
│   └── final_data.csv                # After feature engineering
│
├── Notebook/
│   ├── 01_preprocessing.ipynb        # Data cleaning & encoding
│   ├── 02_eda.ipynb                  # Exploratory Data Analysis
│   ├── 03_feature_engineering.ipynb  # Feature creation & selection
│   ├── 04_model_building.ipynb       # Model training & comparison
│   └── 05_evaluation.ipynb           # Metrics & confusion matrix
│
├── Model/
│   ├── xgboost.pkl                   # Best trained model
│   ├── random_forest.pkl             # Random Forest model
│   ├── logistic_regression.pkl       # Logistic Regression model
│   └── feature_names.pkl             # Feature list for prediction
│
├── Flask_App/
│   ├── app.py                        # Flask application
│   └── templates/
│       ├── index.html                # Input form (Glassmorphism UI)
│       └── result.html               # Prediction result page
│
├── Documentation/
│   ├── histograms.png                # Univariate analysis
│   ├── heatmap.png                   # Correlation heatmap
│   ├── scatter_plots.png             # Bivariate analysis
│   ├── confusion_matrices.png        # Model evaluation
│   ├── feature_importance.png        # Top features
│   └── model_metrics.csv             # All model scores
│
├── Procfile                          # Render deployment config
├── gunicorn_config.py                # Gunicorn server config
├── requirements.txt                  # All dependencies
├── .gitignore                        # Ignored files
└── README.md                         # Project documentation
```

---


<a name="-how-to-run-locally"></a>
## ▶️ How to Run Locally


### 1. Clone the repository
```bash
git clone https://github.com/shrutim2804/Student_Performance_Prediction.git
cd Student_Performance_Prediction
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
cd Flask_App
python app.py

```

### 5. Open in browser
http://127.0.0.1:5000

---

## 📊 Results

### Model Comparison

| Model | Accuracy | F1 Score | ROC-AUC |
|---|---|---|---|
| Logistic Regression | ~82% | ~81% | ~91% |
| Random Forest | ~92% | ~92% | ~98% |
| XGBoost | ~93% | ~93% | ~99% |

### Key Findings from EDA
- Students who study **15+ hours/week** consistently achieve Grade A
- **Absences** have the strongest negative correlation with GPA
- **Parental support** significantly improves student outcomes
- Students with **tutoring** perform on average one grade higher

---


<a name="-author"></a>
## 👩‍💻 Author


**Shruti Mishra** ||
B.Tech CSE || Student 

🔗 LinkedIn: [Shruti Mishra](https://www.linkedin.com/in/shruti-mishra-5020s)
 GitHub: [github.com/shrutim2804](https://github.com/shrutim2804)

---

## 📄 License

This project is for academic purposes.

