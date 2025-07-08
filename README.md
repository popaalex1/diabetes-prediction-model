# Diabetes Health Predictor

A modern web application that uses machine learning to predict diabetes risk based on health indicators. Built with **FastAPI** (Python) for the backend and **React** (Vite) for the frontend, with a futuristic, user-friendly interface.

---

## 🚀 Features
- **Diabetes risk prediction** using a trained XGBoost model
- Clean, responsive, and modern UI (React + Vite)
- Futuristic visuals and easy navigation
- CORS-enabled API for seamless frontend-backend communication
- HTTPS support for local development

---

## 🖼️ Preview

**Home:**
![Home Preview](https://www.tissupath.com.au//wp-content/uploads/Diabetes-Overview-1-768x768.png)

**Prediction:**
![Prediction Preview](https://cdn.analyticsvidhya.com/wp-content/uploads/2022/01/30738medtec-futuristic-650-672c56a896ab7.webp)

---

## 📦 Technologies Used
- **Backend:** Python, FastAPI, XGBoost, Pandas, Joblib
- **Frontend:** React, Vite, CSS
- **ML:** XGBoost Classifier, SMOTE (for balancing)
- **Dev Tools:** Uvicorn, npm, @vitejs/plugin-basic-ssl (for local HTTPS)

---

## ⚡ Quickstart

### 1. Clone the repository
```sh
https://github.com/popaalex1/diabetes-health-predictor.git
cd diabetes-health-predictor
```

### 2. Backend Setup (FastAPI)
- Make sure you have **Python 3.9+** installed.
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
- Train or use the provided model (`diabetes_model.joblib`).
- Start the API server:
  ```sh
  uvicorn api:app --reload
  ```
  The API will be available at `http://localhost:8000` (or `https://localhost:8000` if you configure SSL).

### 3. Frontend Setup (React + Vite)
- Go to the frontend folder:
  ```sh
  cd react_diabetes
  ```
- Install dependencies:
  ```sh
  npm install
  ```
- (Optional) For HTTPS local dev, install:
  ```sh
  npm install --save-dev @vitejs/plugin-basic-ssl
  ```
- Start the frontend:
  ```sh
  npm run dev
  ```
- Open [https://localhost:5173](https://localhost:5173) in your browser.

---

## 📝 Usage
1. Go to the **Prediction** section.
2. Fill in the health indicators in the form.
3. Click **Calculate** to get your diabetes risk prediction.
4. The result will be displayed instantly below the form.

---

## 🛠️ Project Structure
```
Proiect/
├── api.py                # FastAPI backend
├── diabetes_prediction.py # Model training and evaluation
├── diabetes_model.joblib  # Trained ML model
├── dataset/
│   └── diabetes_health_indicators.csv
├── react_diabetes/        # React frontend (Vite)
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── ...
│   └── vite.config.js
├── README.md
└── ...
```

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙋‍♂️ Contact
For questions or feedback, open an issue or contact [popaalex1 on GitHub](https://github.com/popaalex1).
