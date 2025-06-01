# 🏅 Olympic Analysis Web App

[![Streamlit App](https://img.shields.io/badge/Streamlit-1.38.0-FF4B4B.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg)](https://python.org/)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-20BEFF.svg)](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

A comprehensive Streamlit-based web application for analyzing Olympic Games data, providing deep insights into country-wise medal tallies, athlete performance metrics, and demographic trends using the **120 Years of Olympic History dataset** from Kaggle.

LIVE DEPLOYMENT : https://olympic-analysis-webapp-model.streamlit.app/

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🚀 Installation](#-installation)
- [🎮 Usage](#-usage)
- [🛠️ Technologies Used](#️-technologies-used)

---

## 🎯 Overview

This interactive web application leverages the power of **Streamlit** to explore Olympic Games data spanning from **1896 to 2016**. The app transforms raw Olympic data into meaningful insights through interactive visualizations and comprehensive analyses.

### Key Capabilities:
- 🏆 **Medal Analysis**: Track medal tallies and performance trends over time
- 👥 **Athlete Demographics**: Explore age, height, and weight distributions
- 🌍 **Country Comparisons**: Compare performance across different nations
- 📈 **Participation Trends**: Analyze gender participation evolution
- 🎯 **Sport-Specific Insights**: Dive deep into individual sports analytics

---

## ✨ Features

### 🏛️ **Country-wise Analysis**
- Interactive medal tally visualizations over time
- Customizable country selection via dropdown menus
- Historical performance trends and comparisons

### 🏃‍♂️ **Athlete-wise Analysis**
- **Age Distribution Analysis**:
  - Overall athlete age distributions
  - Medal-specific age breakdowns (Gold, Silver, Bronze)
  - Sport-specific age analysis for gold medalists
- **Physical Characteristics**:
  - Height vs. weight scatterplots with medal differentiation
  - Gender-based physical attribute comparisons
  - Sport-specific athlete profiles

### 🏆 **Performance Analytics**
- **Top Performers**: Identify most successful athletes by:
  - Country-specific rankings
  - Sport-specific achievements
  - Medal count leaderboards
- **Participation Trends**:
  - Male vs. female participation over decades
  - Gender equality progression in Olympic sports
  - Historical participation growth patterns

### 🎛️ **Interactive Features**
- Intuitive dropdown menus for country and sport selection
- Dynamic filtering and real-time chart updates
- Responsive design for various screen sizes
- Rich tooltips and hover information

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Git (for cloning the repository)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/olympic-analysis-webapp.git
   cd olympic-analysis-webapp
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Dataset**
   - Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
   - Download `athlete_events.csv` and `noc_regions.csv`
   - Place both files in the project root directory
   - Ensure `app.py` is configured to load these files correctly

5. **Launch the Application**
   ```bash
   streamlit run app.py
   ```
   
   🎉 The app will automatically open in your browser at `http://localhost:8501`


---
## 🌟Project Snapshots
![Screenshot 2025-06-02 011546](https://github.com/user-attachments/assets/f6986869-e70a-4b06-b1dd-995c09bae96c)
![Screenshot 2025-06-02 011703](https://github.com/user-attachments/assets/c998348b-c78a-4952-9efb-498c20735f78)


---

## 🛠️ Technologies Used

### Core Framework
- **[Streamlit](https://streamlit.io/)** `1.38.0` - Web application framework
- **[Python](https://python.org/)** `3.8+` - Programming language

### Data Processing
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[NumPy](https://numpy.org/)** - Numerical computing

### Visualization
- **[Plotly](https://plotly.com/python/)** - Interactive visualizations
- **[Seaborn](https://seaborn.pydata.org/)** - Statistical data visualization
- **[Matplotlib](https://matplotlib.org/)** - Static plotting library

### Statistical Analysis
- **[SciPy](https://scipy.org/)** - Scientific computing and statistics

### Development Environment
- **[PyCharm](https://www.jetbrains.com/pycharm/)** - Integrated Development Environment

---


<div align="center">

**Built with ❤️ using Streamlit and Python**

*Dataset sourced from [Kaggle](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)*

---

⭐ **Star this repository if you found it helpful!** ⭐

</div>
