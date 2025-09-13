HEAD
# PEC_TECHATHON-3.0

# Hospital Resource Optimisation

## Steps to Run

1. Generate data
```bash
python scripts/generate_synthetic_hospital_data.py
```

2. Train forecast model
```bash
python models/train_forecast_model.py
```

3. Start backend API
```bash
cd backend
uvicorn server__model:app --reload
```

4. Start dashboard
```bash
cd dashboard
streamlit run app_streamlit.py
```
9df6ece (Initial project upload)
