# PEC_TECHATHON-3.0

# Hospital Resource Optimisation

# 🏥 Predictive Analysis for Hospital Resource Optimisation

A real-time dashboard powered by predictive analytics to optimize critical hospital resources such as oxygen supply, bed availability, and staff allocation. Built for techathons, this project demonstrates how data science can be applied to solve real-world healthcare challenges.


## 🚀 Features

- **📊 Real-Time Dashboard:** A clean Streamlit interface displaying key hospital metrics.
- **🔮 Oxygen Usage Forecasting:** Predicts future oxygen demand using a Holt-Winters time-series model to prevent tank depletion.
- **🛏️ Bed Availability Monitoring:** Tracks total and occupied beds across multiple wards in real-time.
- **🧑‍⚕️ Staff Allocation Optimizer:** Uses Linear Programming (via PuLP) to optimally assign staff to shifts based on requirements and availability.
- **🧪 Synthetic Data Generation:** A script to simulate realistic hospital data for demonstration and testing.

## 🏗️ System Architecture

The project follows a modular microservices architecture:

1.  **Data Layer:** `synthetic_hospital_data.csv` simulates input from EHR systems and IoT sensors.
2.  **Model Layer:** Python scripts for training the forecasting model and the optimization logic.
3.  **Backend API:** A FastAPI server providing REST endpoints for predictions and optimization.
4.  **Frontend Dashboard:** A Streamlit app that consumes the API and provides the user interface.

## 📁 Project Structure

```bash
hospital-resource-optimisation/
│
├── data/
│   └── synthetic_hospital_data.csv        # Generated synthetic data
│
├── models/
│   ├── train_forecast_model.py            # Script to train the Holt-Winters model
│   └── staff_optimizer.py                 # PuLP-based staff optimization model
│
├── backend/
│   ├── serve_model.py                     # FastAPI application
│   └── requirements.txt                   # Backend dependencies (FastAPI, Uvicorn, Pandas)
│
├── dashboard/
│   ├── app_streamlit.py                   # Main Streamlit dashboard application
│   └── requirements.txt                   # Frontend dependencies (Streamlit, Requests)
│
├── scripts/
│   └── generate_synthetic_hospital_data.py# Script to generate synthetic data
│
├── architecture_diagram.png               # System architecture diagram
└── README.md


🖥️ Steps to Run

1. Generate data
python scripts/generate_synthetic_hospital_data.py

2. Train forecast model
python models/train_forecast_model.py

3. Start backend API
cd backend
uvicorn server_model:app --reload

4. Start dashboard
cd dashboard
streamlit run app_streamlit.py
