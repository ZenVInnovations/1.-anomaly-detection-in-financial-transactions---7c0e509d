# AI-Powered Anomaly Detection in Financial Transactions

## Overview

This application identifies anomalies in financial transactions using machine learning techniques such as Isolation Forest and Autoencoder. It features a modern and interactive web interface built with Streamlit, allowing users to upload data, choose models, and visualize anomalies effectively.

## Design Objectives

- Enable fast and intuitive anomaly detection for both labeled and unlabeled datasets.
- Provide clear visualization and feedback on detected anomalies.
- Ensure modular code organization for easy maintenance and model switching.
- Support future expansion (e.g., new models or datasets).

## Models Used

### 1. Isolation Forest
- **Algorithm**: Ensemble of decision trees to isolate outliers.
- **Strengths**: Fast, unsupervised, works well with high-dimensional data.
- **Parameters**:
  - contamination: 0.05
  - n_estimators: 100
  - random_state: 42

### 2. Autoencoder (PyTorch)
- **Architecture**:
  - Input → Linear(16) → ReLU → Linear(8) → Linear(16) → ReLU → Output
- **Loss**: MSE (Mean Squared Error)
- **Thresholding** used to detect reconstruction error-based anomalies.
- **Epochs**: 30
- **Optimizer**: Adam

## UI/UX Design

- Built with **Streamlit** for fast and interactive prototyping.
- **Sidebar** for model selection.
- Clear sectioning: upload → feature selection → model run → output.
- **Visualizations**:
  - **Scatter Plot** for anomalies
  - **Bar Plot** for count
  - **Line Chart** for temporal trends
  - **Box Plot** for outlier distribution
  - **Performance metrics** rendered in an attractive table using HTML/CSS.

## Visual Output Examples

- **Normal vs Anomalous transactions** highlighted using colors.
- **Line chart**: Feature trend over time with anomalies highlighted.
- **Box plot**: Visual distribution and outliers.
- **Tabulated performance metrics** (Precision, Recall, F1 Score, Accuracy).

## Modularity & Extensibility

- Easily switch or add models by adding functions in the `models/` folder.
- The UI auto-adapts to model outputs.
- Clean separation between **model logic** and **UI logic**.

## Error Handling & Edge Cases

- Handles missing values and non-numeric columns gracefully.
- Ensures proper conversion of date columns.
- Automatically checks for the presence of true labels for metric computation.
