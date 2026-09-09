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

*Model Configuration
| Component           | Configuration                   |
| ------------------- | ------------------------------- |
| Input Size          | 28 × 28 × 1                     |
| Convolution Filters | 32                              |
| Kernel Size         | 3 × 3                           |
| Activation          | ReLU                            |
| Pooling             | MaxPooling 2 × 2                |
| Dense Layer         | 128 neurons                     |
| Output Layer        | 10 neurons                      |
| Output Activation   | Softmax                         |
| Optimizer           | Adam                            |
| Loss Function       | Sparse Categorical Crossentropy |
| Dataset             | MNIST                           |

The trained model is stored as:
models/mnist_cnn.keras

📊 Model Performance
The CNN achieves approximately 98% test accuracy on the MNIST dataset.
The application also provides the probability assigned to each digit.
For example:
Prediction: 3
Confidence: 99.20%
0 → 0.01%
1 → 0.02%
2 → 0.10%
3 → 99.20%
4 → 0.05%
...
Note: Predictions on user-drawn digits may vary because handwritten input can differ significantly from the images used during model training.

🗂️ Dataset
This project uses the MNIST handwritten digit dataset.
MNIST contains:
60,000 training images
10,000 testing images
10 digit classes
Images of size 28 × 28 pixels
Grayscale images
Before training, pixel values are normalized from:
0–255
to:
0–1
For CNN input, images are reshaped into:
28 × 28 × 1

🔄 Application Workflow
User Draws Digit
       ↓
HTML Canvas
       ↓
JavaScript
       ↓
Image Data
       ↓
Flask Backend
       ↓
Image Preprocessing
       ↓
28 × 28 Image
       ↓
CNN Model
       ↓
Prediction
       ↓
Confidence + Probabilities
       ↓
Web Interface

🛠️ Technologies Used
Programming Languages
Python
JavaScript
HTML
CSS
Machine Learning
TensorFlow
Keras
NumPy
Scikit-learn
Backend
Flask
Image Processing
Pillow (PIL)
Data Visualization / Analysis
Pandas
Matplotlib
📁 Project Structure
MNIST Digit Classification/
│
├── models/
│   └── mnist_cnn.keras
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
└── venv/
File Description
File / Folder	Purpose
models/	Stores the trained CNN model
mnist_cnn.keras	Saved trained CNN model
static/	Contains CSS and JavaScript
script.js	Canvas drawing and frontend prediction logic
style.css	Web application styling
templates/	Contains HTML templates
index.html	Main application interface
app.py	Flask backend and prediction API
main.py	Model training and evaluation
requirements.txt	Required Python dependencies
README.md	Project documentation
venv/	Python virtual environment

⚙️ Installation
1. Clone the Repository
git clone https://github.com/Shalini20-25/mnist-digit-classification.git
Move into the project directory:
cd mnist-digit-classification

2. Create a Virtual Environment
python -m venv venv
Activate it on Windows:
venv\Scripts\activate
You should see:
(venv)
in your terminal.

3. Install Dependencies
pip install -r requirements.txt

▶️ Running the Application
Start the Flask server:
python app.py
You should see something similar to:
* Running on http://127.0.0.1:5000
Open the following address in your browser:
http://127.0.0.1:5000

✍️ How to Use
Step 1
Open the web application.

Step 2
Draw a digit between 0 and 9 on the canvas.

Step 3
Click:
Predict

Step 4
The application displays:
Predicted digit
Confidence score
Probability of each digit

Step 5
Previous predictions are automatically added to the prediction history.

Step 6
Use:
Clear
to clear the current drawing.
Use:
Clear History
to remove previous predictions.

🔍 Image Preprocessing
Before sending the image to the CNN, the application performs several preprocessing steps.

Canvas Image
     ↓
Convert to Grayscale
     ↓
Detect Digit Area
     ↓
Crop
     ↓
Add Padding
     ↓
Resize
     ↓
Center the Digit
     ↓
Normalize Pixel Values
     ↓
28 × 28 × 1
     ↓
CNN
This preprocessing helps make the user's canvas drawing more similar to the format expected by the trained MNIST model.

🛡️ Error Handling
The application includes backend and frontend validation.
Examples include:
No image data received.
Invalid image format.
Invalid or corrupted image.
Please draw a digit before predicting.
Unexpected server errors are also handled so that the application does not expose unnecessary technical details to the user.

🎯 Learning Objectives
This project demonstrates practical implementation of:
Machine Learning
Deep Learning
Convolutional Neural Networks
Image preprocessing
Model training
Model evaluation
Model saving and loading
Flask API development
Frontend-backend integration
JavaScript canvas interaction
REST-style prediction requests
Error handling
Responsive web design

🚀 Future Improvements
Possible future improvements include:
Improve recognition of difficult handwritten digits
Add more advanced CNN architectures
Add data augmentation
Display the processed 28 × 28 image
Add model comparison
Add prediction statistics
Add dark/light theme
Deploy the application online
Add support for uploaded handwritten images
Improve accessibility
Add more detailed model analytics

📌 Project Status
Status: Completed ✅
The current application supports:
✅ CNN model
✅ MNIST classification
✅ Flask backend
✅ Interactive drawing canvas
✅ Prediction
✅ Confidence score
✅ Probability visualization
✅ Prediction history
✅ Clear history
✅ Touch support
✅ Input validation
✅ Error handling
✅ Project information section

👩‍💻 Author
Shalini Kumari Singh
Computer Science & Engineering Student

📄 License
This project is created for educational and learning purposes.
```markdown
git clone https://github.com/Shalini20-25/mnist-digit-classification.git
