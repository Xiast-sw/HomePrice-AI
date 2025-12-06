# HomePrice-AI

A machine learning desktop application that predicts house prices using Multiple Linear Regression and Random Forest algorithms.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📊 Results

### Price Distribution

![Price Distribution](results/price_distribution.png)

### Price by Number of Rooms

![Rooms vs Price](results/rooms_vs_price.png)

### Price by Building Age

![Age vs Price](results/age_vs_price.png)

### Correlation Matrix

![Correlation Matrix](results/correlation_matrix.png)

---

## 📈 Model Performance

| Metric | Linear Regression | Random Forest |
|--------|-------------------|---------------|
| **MAE** | 320,014 TL | 151,508 TL |
| **RMSE** | 422,077 TL | 213,440 TL |
| **Cross-Val MSE** | 217B | 314B |

**Winner: Random Forest** - Lower MAE and RMSE values indicate better prediction accuracy.

---

## 🏗️ Project Structure

    HomePrice-AI/
    ├── data/
    │   └── FatihEvFiyatları.csv
    ├── notebooks/
    │   └── home-price-predict-enhanced.ipynb
    ├── src/
    │   ├── preprocessing.py
    │   ├── model.py
    │   ├── train.py
    │   └── app.py
    ├── results/
    │   ├── price_distribution.png
    │   ├── rooms_vs_price.png
    │   ├── age_vs_price.png
    │   └── correlation_matrix.png
    ├── .gitignore
    ├── requirements.txt
    └── README.md

---

## 📋 Dataset

| Info | Details |
|------|---------|
| **Source** | Manually collected (Fatih, Istanbul) |
| **Records** | 39 houses |
| **Features** | Area (m²), Room Count, Building Age |
| **Target** | House Price (TL) |
| **Price Range** | 650,000 - 5,500,000 TL |

### Feature Statistics

| Feature | Min | Max | Mean |
|---------|-----|-----|------|
| Area (m²) | 22 | 197 | 95.4 |
| Room Count | 1 | 5 | 3.05 |
| Building Age | 0 | 18 | 5.05 |
| Price (TL) | 650K | 5.5M | 2.54M |

---

## 🧠 Model Architecture

### Linear Regression
- Standard multiple linear regression
- Features: Area, Room Count, Building Age

### Random Forest
- 100 decision trees (n_estimators=100)
- Additional feature: Room Count × Building Age
- random_state=42 for reproducibility

### Feature Engineering

    odasayi_binayasi = Room Count × Building Age
    log_fiyat = log(Price)

---

## 🚀 Getting Started

### 1. Clone the Repository

    git clone https://github.com/Xiast-sw/HomePrice-AI.git
    cd HomePrice-AI

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Run Training

    python src/train.py

### 4. Run Desktop App

    python src/app.py

### 5. Or Use Jupyter Notebook

    jupyter notebook notebooks/home-price-predict-enhanced.ipynb

---

## 🖥️ Desktop Application

The app allows users to input:
- **Area (m²):** Size of the house
- **Room Count:** Number of rooms
- **Building Age:** Age of the building in years

And returns the **predicted house price** using the Random Forest model.

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| **Language** | Python 3.x |
| **ML Library** | Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **GUI** | Tkinter |

---

## 📁 File Descriptions

| File | Description |
|------|-------------|
| `src/preprocessing.py` | Data loading and feature engineering |
| `src/model.py` | Model definitions (Linear Regression, Random Forest) |
| `src/train.py` | Training script with evaluation metrics |
| `src/app.py` | Tkinter desktop application |
| `notebooks/home-price-predict-enhanced.ipynb` | Interactive analysis notebook |
| `data/FatihEvFiyatları.csv` | House price dataset |

---

## 📊 Key Insights

- **Area** has the strongest correlation with price (0.94)
- **Building Age** has negative correlation with price (-0.58)
- Newer buildings are significantly more expensive
- 4-room apartments have the highest average price

---

## 👤 Author

**Adil Buğra Aytar**

[![GitHub](https://img.shields.io/badge/GitHub-Xiast--sw-black?logo=github)](https://github.com/Xiast-sw)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Adil%20Buğra%20Aytar-blue?logo=linkedin)](https://linkedin.com/in/adil-bugra-aytar-47a555224)

[![Email](https://img.shields.io/badge/Email-a.bugraaytar@gmail.com-red?logo=gmail)](mailto:a.bugraaytar@gmail.com)

---

## 📝 License

This project is licensed under the MIT License.
