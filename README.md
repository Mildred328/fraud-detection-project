# AI for Fraud Detection

This project was developed as part of my Artificial Intelligence program with Hex Softwares.

## Project Overview
This project focuses on detecting fraudulent financial transactions using machine learning techniques.

The model learns patterns from historical transaction data and classifies transactions as either fraudulent or legitimate.


## Dataset
- 284,807 transactions  
- 31 features  
- Highly imbalanced dataset  


## Key Insights
- Fraud cases are very rare  
- Fraud is not only based on transaction amount  
- Machine learning is required to detect complex patterns  


## Model Used
- Logistic Regression  
- Class imbalance handled using class_weight='balanced'  
- Feature scaling using StandardScaler  


## Results
- Recall: **92%** (Fraud detection)
- High recall ensures most fraud cases are detected  


## Limitations
- Low precision (false positives exist)
- Model uses simplified features in demo  


## Deployment
- Built a Streamlit web app  
- Users can input transaction amount and get prediction  


## Tools Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Seaborn & Matplotlib  
- Streamlit  


## Demo
Video demonstration included showing model and app in action.


## Conclusion
This project demonstrates how machine learning can be applied to detect fraud and improve financial security.

Future improvements include:
- Advanced models (Random Forest, XGBoost)
- Real-time deployment
