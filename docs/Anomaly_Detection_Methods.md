# 🧠 Anomaly Detection Methods

This guide introduces the two main anomaly detection methods considered in our project: **Isolation Forest** and **Autoencoders**.

---

## 🌲 1. Isolation Forest

**Isolation Forest** is an unsupervised algorithm specifically designed for anomaly detection.

### 🔧 How It Works:
- Randomly selects features and splits values.
- Constructs decision trees to isolate data points.
- Anomalies are easier to isolate and appear in shorter paths.

### ✅ Pros:
- Works well with **high-dimensional** data.
- **Fast** and scalable to large datasets.
- Does **not require labeled** training data.

### 📉 Use Case:
- Ideal for tabular datasets like **financial transactions**, where speed and scalability are important.

---

## 🤖 2. Autoencoders

**Autoencoders** are a type of neural network trained to reconstruct input data.

### 🔧 How It Works:
- Learns to **compress** and **rebuild** data through encoding-decoding.
- Anomalies have **higher reconstruction error**, since they deviate from learned normal patterns.

### ⚙️ Architecture:

Input → Encoder → Bottleneck → Decoder → Output


- **Loss Function**: Mean Squared Error (Input vs Output)

### ✅ Pros:
- Great for capturing **non-linear** patterns and **complex anomalies**.
- Flexible architecture for image, text, or tabular data.

---

## 📊 Summary Comparison

| Feature             | Isolation Forest                | Autoencoders                          |
|---------------------|----------------------------------|----------------------------------------|
| Type                | Tree-based algorithm             | Neural network                         |
| Learning            | Unsupervised                     | Unsupervised or semi-supervised        |
| Speed               | Fast                             | Slower (training required)             |
| Data Type           | Structured (e.g., CSV)           | Structured or unstructured             |
| Labeled Data Needed | No                               | No (but can benefit from it)           |
| Strength            | Efficient with large datasets    | Detects subtle and non-linear patterns |

---

🔍 *In this project, we implemented the **Isolation Forest** method. Autoencoders are explored as a potential future upgrade for deeper anomaly detection in complex data.*

---
