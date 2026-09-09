# MNIST Digit Classifier 🧠

A web-based handwritten digit recognition application built using a **Convolutional Neural Network (CNN)** and **Flask**.

The application allows users to draw a handwritten digit from **0 to 9** on a canvas and uses a trained CNN model to predict the digit along with its confidence and probability distribution.

---

## 📌 Project Overview

Handwritten digit recognition is a classic machine learning and computer vision problem.

This project demonstrates how a **Convolutional Neural Network** can learn visual patterns from handwritten digits and classify them into one of ten classes:

**0, 1, 2, 3, 4, 5, 6, 7, 8, 9**

The trained model is integrated into a Flask web application, allowing users to interact with the machine learning model through a simple web interface.

---

## ✨ Features

- ✍️ Draw digits directly on a digital canvas
- 🤖 CNN-based handwritten digit classification
- 🎯 Prediction of digits from 0–9
- 📊 Probability distribution for all 10 digits
- 📈 Prediction confidence score
- 📝 Prediction history
- 🗑️ Clear canvas functionality
- 🧹 Clear prediction history
- 📱 Mouse and touch support
- ⚠️ Input validation and error handling
- 📚 Built-in project information section
- 🌐 Flask-based web interface

---

## 🧠 Machine Learning Model

The project uses a **Convolutional Neural Network (CNN)** trained on the MNIST handwritten digit dataset.

### CNN Architecture

```text
Input Image
    ↓
28 × 28 × 1
    ↓
Convolutional Layer
32 Filters
    ↓
ReLU Activation
    ↓
Max Pooling
    ↓
Flatten
    ↓
Dense Layer
128 Neurons
    ↓
ReLU Activation
    ↓
Output Layer
10 Neurons
    ↓
Softmax
    ↓
Predicted Digit