# 💸 AI-Powered Anomaly Detection in Financial Transactions

This project uses machine learning models to identify anomalous (potentially fraudulent) financial transactions in structured tabular data. Built with Streamlit, the app enables users to upload datasets, select features, and visually inspect anomalies using two powerful models: Isolation Forest and Autoencoder (PyTorch).

🔗 Live Demo: (optional – add link if deployed)

📁 Sample dataset: sample.csv

## 🧠 Table of Contents

- Overview
- Features
- Technologies Used
- How It Works
- Setup & Installation
- Folder Structure
- Sample Dataset Format
- Screenshots
- Limitations & Future Work
- License

## 📌 Overview

This project helps detect suspicious financial transactions by learning typical patterns in numeric features and flagging outliers. It allows users to:
- Upload labeled or unlabeled datasets.
- Choose relevant features for anomaly detection.
- Apply machine learning models to detect anomalies.
- Visualize results using scatter plots, bar charts, time series, and box plots.
- View model performance metrics if ground-truth labels are available.

## ✨ Features

- Interactive Web Interface with Streamlit
- Supports CSV Uploads or Built-in Sample Dataset
- Two Anomaly Detection Models:
  - Isolation Forest (unsupervised)
  - Autoencoder Neural Network (deep learning)
- Supports labeled and unlabeled datasets
- Visualizations:
  - Anomaly scatter plot
  - Bar chart for anomaly counts
  - Line chart for time series
  - Box plot for feature distribution
- Performance metrics: Accuracy, Precision, Recall, F1 Score (if labels are provided)
- Summary of detected anomalies

## 🛠 Technologies Used

- Python
- Streamlit (web interface)
- Scikit-learn (Isolation Forest, metrics)
- PyTorch (Autoencoder neural network)
- Pandas (data handling)
- Plotly (visualizations)
- NumPy, Matplotlib (supporting libraries)

## ⚙️ How It Works

1. The user uploads a CSV file or uses the sample.
2. They select relevant numeric features.
3. They choose an anomaly detection model.
4. The app trains the model and assigns anomaly scores.
5. Anomalies are visualized and tabulated.
6. If the dataset includes true labels (column named true_label), metrics are displayed.

## 🚀 Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/anomaly-detection-app.git
cd anomaly-detection-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```
