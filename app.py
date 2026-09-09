from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import base64
from PIL import Image
import io
import binascii


app = Flask(__name__)


# ==========================================
# Load trained CNN model
# ==========================================

model = load_model("models/mnist_cnn.keras", compile=False)


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# Prediction Route
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # --------------------------------------
        # Check whether JSON data was received
        # --------------------------------------

        if not request.is_json:
            return jsonify({
                "error": "Invalid request format."
            }), 400


        data = request.get_json()


        # --------------------------------------
        # Check whether image data exists
        # --------------------------------------

        if not data or "image" not in data:
            return jsonify({
                "error": "No image data received."
            }), 400


        image_data = data["image"]


        # --------------------------------------
        # Check image data format
        # --------------------------------------

        if not isinstance(image_data, str):
            return jsonify({
                "error": "Invalid image data."
            }), 400


        if "," not in image_data:
            return jsonify({
                "error": "Invalid image format."
            }), 400


        # --------------------------------------
        # Extract Base64 image
        # --------------------------------------

        image_data = image_data.split(",", 1)[1]


        # --------------------------------------
        # Decode image
        # --------------------------------------

        try:

            image_bytes = base64.b64decode(
                image_data,
                validate=True
            )

        except (binascii.Error, ValueError):

            return jsonify({
                "error": "Unable to decode image."
            }), 400


        # --------------------------------------
        # Open image using Pillow
        # --------------------------------------

        try:

            image = Image.open(
                io.BytesIO(image_bytes)
            ).convert("L")

        except Exception:

            return jsonify({
                "error": "Invalid or corrupted image."
            }), 400


        # ======================================
        # Image Preprocessing
        # ======================================

        image_array = np.array(image)


        # --------------------------------------
        # Check whether canvas is empty
        # --------------------------------------

        coords = np.argwhere(
            image_array > 30
        )


        if coords.size == 0:

            return jsonify({
                "error": "Please draw a digit before predicting."
            }), 400


        # --------------------------------------
        # Find bounding box
        # --------------------------------------

        y_min, x_min = coords.min(axis=0)
        y_max, x_max = coords.max(axis=0)


        cropped = image.crop(
            (
                x_min,
                y_min,
                x_max + 1,
                y_max + 1
            )
        )


        # --------------------------------------
        # Add padding
        # --------------------------------------

        padding = 4


        padded = Image.new(
            "L",
            (
                cropped.width + 2 * padding,
                cropped.height + 2 * padding
            ),
            0
        )


        padded.paste(
            cropped,
            (padding, padding)
        )


        # --------------------------------------
        # Resize to MNIST-like dimensions
        # --------------------------------------

        padded.thumbnail(
            (20, 20),
            Image.Resampling.LANCZOS
        )


        final_image = Image.new(
            "L",
            (28, 28),
            0
        )


        x_position = (
            28 - padded.width
        ) // 2


        y_position = (
            28 - padded.height
        ) // 2


        final_image.paste(
            padded,
            (
                x_position,
                y_position
            )
        )


        image = np.array(final_image)


        # ======================================
        # Center Image
        # ======================================

        total = image.sum()


        if total > 0:

            y_indices, x_indices = np.indices(
                image.shape
            )


            center_x = (
                (x_indices * image).sum()
                / total
            )


            center_y = (
                (y_indices * image).sum()
                / total
            )


            target_x = 13.5
            target_y = 13.5


            shift_x = int(
                round(
                    target_x - center_x
                )
            )


            shift_y = int(
                round(
                    target_y - center_y
                )
            )


            centered = np.zeros_like(
                image
            )


            src_x_start = max(
                0,
                -shift_x
            )


            src_x_end = min(
                28,
                28 - shift_x
            )


            src_y_start = max(
                0,
                -shift_y
            )


            src_y_end = min(
                28,
                28 - shift_y
            )


            dst_x_start = max(
                0,
                shift_x
            )


            dst_x_end = (
                dst_x_start
                + (
                    src_x_end
                    - src_x_start
                )
            )


            dst_y_start = max(
                0,
                shift_y
            )


            dst_y_end = (
                dst_y_start
                + (
                    src_y_end
                    - src_y_start
                )
            )


            centered[
                dst_y_start:dst_y_end,
                dst_x_start:dst_x_end
            ] = image[
                src_y_start:src_y_end,
                src_x_start:src_x_end
            ]


            image = centered


        # ======================================
        # Normalize Image
        # ======================================

        image = image / 255.0


        # Add CNN batch and channel dimensions

        image = image.reshape(
            1,
            28,
            28,
            1
        )


        # ======================================
        # Model Prediction
        # ======================================

        prediction = model.predict(
            image,
            verbose=0
        )


        predicted_digit = int(
            np.argmax(prediction)
        )


        confidence = float(
            np.max(prediction)
        ) * 100


        probabilities = (
            prediction[0] * 100
        ).round(2).tolist()


        # ======================================
        # Return Prediction
        # ======================================

        return jsonify({

            "prediction": predicted_digit,

            "confidence": round(
                confidence,
                2
            ),

            "probabilities": probabilities

        })


    # ==========================================
    # Unexpected Errors
    # ==========================================

    except Exception as error:

        print(
            "Prediction Error:",
            error
        )


        return jsonify({

            "error":
                "Something went wrong while "
                "processing the prediction."

        }), 500


# ==========================================
# Global 404 Error
# ==========================================

@app.errorhandler(404)
def page_not_found(error):

    return jsonify({

        "error": "Page not found."

    }), 404


# ==========================================
# Global 500 Error
# ==========================================

@app.errorhandler(500)
def internal_server_error(error):

    return jsonify({

        "error":
            "Internal server error."

    }), 500


# ==========================================
# Run Flask Application
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )