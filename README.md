
<div align="center">

### 🚀 This project has evolved! Check out the production-grade MLOps version:

[![CureLoop MLOps](https://img.shields.io/badge/⚡_CureLoop--MLOps-Production_Version-00C853?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mayank-goyal09/CureLoop-MLOps)
[![Live API](https://img.shields.io/badge/🌐_Live_API-Try_Now-blue?style=for-the-badge)](https://mayankg09-cureloop-mlops.hf.space/docs)

> **What's new?** Automated CI/CD Pipeline • Docker Containerization • FastAPI REST API • Auto-Retraining on Push • Deployed on Hugging Face Spaces 🤗
>
> 📓 *This repo = Research & Notebook Phase* → 🔄 *[CureLoop-MLOps](https://github.com/mayank-goyal09/CureLoop-MLOps) = Production & Deployment Phase*

---

</div>

```
                                ╔═══════════════════════════════════════════════════════════════╗
                                ║          ⚕️ ELITE MEDICAL AI DIAGNOSTIC SYSTEM ⚕️            ║
                                ║      AI-Powered Disease Prediction & Health Recommendations   ║
                                ║              Professional ML Architecture                     ║
                                ╚═══════════════════════════════════════════════════════════════╝
```

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/ML-Decision%20Tree-green?style=for-the-badge)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-orange?style=for-the-badge&logo=plotly)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

**An enterprise-grade medical diagnostic system leveraging Decision Tree Classifier to predict diseases from symptoms and deliver personalized health recommendations through an intuitive Streamlit web interface.**

[🚀 Live Demo](https://medicine-recommendation-system-project.streamlit.app/) • [✨ Features](#-features) • [🛠️ Tech Stack](#%EF%B8%8F-tech-stack) • [⚙️ Architecture](#%EF%B8%8F-architecture) • [📦 Installation](#-installation)

---

## 🎯 Overview

**Elite Medical AI** is a portfolio-ready, production-level healthcare application built with **Machine Learning** and a robust **multi-dataset backend**. This project showcases professional software architecture, comprehensive medical intelligence, symptom-based disease prediction, and personalized health recommendations including medications, diet plans, precautions, and workout routines.

### Why Elite Medical AI?

- ✅ **Production-Ready ML System**: Enterprise-level Decision Tree model with 94.7% accuracy
- ✅ **Comprehensive Health Intelligence**: Disease descriptions, medications, diet, workouts, precautions
- ✅ **132+ Medical Conditions**: Extensive disease database covering common to complex conditions
- ✅ **Real-Time Predictions**: Instant diagnostic insights based on symptom analysis
- ✅ **Luxury UI/UX**: Premium white-gold-charcoal themed Streamlit dashboard
- ✅ **Portfolio Showcase**: Demonstrates ML engineering, data science, and full-stack deployment skills

---

## 🚀 Live Demo

🌐 **[Visit the Live Application](https://medicine-recommendation-system-project.streamlit.app/)**

Experience the full diagnostic system with:

- 🩺 AI-powered disease prediction from symptoms
- 💊 Personalized medication recommendations
- 🥗 Custom nutrition blueprints
- 🏋️ Tailored workout protocols
- 🛡️ Preventive care guidelines
- 📊 Confidence score visualization

---

## ✨ Features

### 🩺 Intelligent Disease Prediction

- Multi-symptom analysis using Decision Tree Classifier
- Predict from 132+ medical conditions
- Real-time symptom-to-disease mapping
- High accuracy diagnostic engine (94.7% precision)
- Confidence score with visual gauge

### 💊 Comprehensive Health Recommendations

- **Pharmaceutical Intelligence**: Disease-specific medication suggestions
- **Nutritional Blueprints**: Personalized diet plans for recovery
- **Preventive Protocols**: 4-step precautionary guidelines per condition
- **Performance Training**: Custom workout routines based on health status
- **Medical Descriptions**: Detailed clinical overviews for each disease

### 🎨 Premium User Experience

- Luxury white-gold-charcoal UI theme
- Responsive dashboard with Plotly visualizations
- Interactive multi-select symptom search
- Patient intake form (name, age, gender)
- Organized clinical intelligence report
- Confidence gauge with gradient indicators

### 📊 Data-Driven Insights

- Symptom severity mapping
- Disease-specific training dataset (4920+ records)
- Integrated CSV-based medical databases
- Joblib model persistence for fast loading
- Real-time confidence scoring

---

## 🛠️ Tech Stack

| Layer                | Technology          | Purpose                           |
|----------------------|---------------------|-----------------------------------|
| **Frontend**         | Streamlit           | Interactive web application       |
| **Backend**          | Python 3.8+         | Core business logic               |
| **Machine Learning** | Scikit-learn        | Decision Tree Classifier          |
| **Data Processing**  | Pandas, NumPy       | Data manipulation & vectorization |
| **Visualization**    | Plotly              | Interactive charts and gauges     |
| **Model Storage**    | Joblib              | Serialized ML model & symptoms    |
| **Database**         | CSV Files           | Medical knowledge base (5 datasets) |
| **UI Styling**       | Custom CSS          | Luxury theme with Google Fonts    |

---

## ⚙️ Architecture

```
medicine-recommendation-system/
├── app.py                       # Streamlit application & UI logic
├── main.ipynb                   # ML model training & experimentation
├── doctor_model.joblib          # Trained Decision Tree Classifier
├── symptom_list.joblib          # Serialized symptom feature list
├── Training.csv                 # ML training dataset (4920 records)
├── Symptom-severity.csv         # Symptom weight mappings
├── description.csv              # Disease clinical descriptions
├── precautions_df.csv           # Preventive care guidelines
├── medications.csv              # Pharmaceutical recommendations
├── diets.csv                    # Nutritional blueprints
├── workout_df.csv               # Exercise protocols
├── symtoms_df.csv               # Symptom-disease relationship data
├── requirements.txt             # Python dependencies
└── .gitignore                   # Version control exclusions
```

### System Workflow

```
