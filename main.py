import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras import Sequential
from tensorflow.keras.layers import (
    Input,
    RandomRotation,
    RandomTranslation,
    RandomZoom,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense
)


# ==========================================
# 1. Load MNIST dataset
# ==========================================

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("Training images:", X_train.shape)
print("Testing images:", X_test.shape)


# ==========================================
# 2. Normalize pixel values
# ==========================================

X_train = X_train / 255.0
X_test = X_test / 255.0

print(
    "Pixel range:",
    X_train.min(),
    "to",
    X_train.max()
)


# ==========================================
# 3. Reshape for CNN
# ==========================================

X_train_cnn = X_train.reshape(
    -1, 28, 28, 1
)

X_test_cnn = X_test.reshape(
    -1, 28, 28, 1
)

print(
    "CNN training shape:",
    X_train_cnn.shape
)

print(
    "CNN testing shape:",
    X_test_cnn.shape
)


# ==========================================
# 4. Build CNN with Data Augmentation
# ==========================================

cnn_model = Sequential([

    Input(shape=(28, 28, 1)),

    # Data augmentation
    RandomRotation(0.08),

    RandomTranslation(
        height_factor=0.10,
        width_factor=0.10
    ),

    RandomZoom(
        height_factor=0.10,
        width_factor=0.10
    ),

    # Feature extraction
    Conv2D(
        32,
        (3, 3),
        activation="relu"
    ),

    MaxPooling2D(
        (2, 2)
    ),

    # Convert feature maps to vector
    Flatten(),

    # Classification
    Dense(
        128,
        activation="relu"
    ),

    Dense(
        10,
        activation="softmax"
    )
])


# ==========================================
# 5. Compile model
# ==========================================

cnn_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# ==========================================
# 6. Display model architecture
# ==========================================

cnn_model.summary()


# ==========================================
# 7. Train the CNN
# ==========================================

history = cnn_model.fit(

    X_train_cnn,

    y_train,

    epochs=7,

    batch_size=64,

    validation_split=0.1
)


# ==========================================
# 8. Evaluate on test dataset
# ==========================================

test_loss, test_accuracy = cnn_model.evaluate(
    X_test_cnn,
    y_test,
    verbose=0
)

print(
    "\nTest Accuracy:",
    round(test_accuracy * 100, 2),
    "%"
)


# ==========================================
# 9. Plot training accuracy
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.title("CNN Accuracy")

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.legend()

plt.show()


# ==========================================
# 10. Plot training loss
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.title("CNN Loss")

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.legend()

plt.show()


# ==========================================
# 11. Test predictions
# ==========================================

predictions = cnn_model.predict(
    X_test_cnn,
    verbose=0
)

predicted_labels = np.argmax(
    predictions,
    axis=1
)

print("\nFirst 10 predictions:")
print(predicted_labels[:10])

print("\nActual labels:")
print(y_test[:10])


# ==========================================
# 12. Save improved model
# ==========================================

import os

os.makedirs(
    "models",
    exist_ok=True
)

cnn_model.save(
    "models/mnist_cnn.keras"
)

print(
    "\nImproved CNN model saved successfully!"
)