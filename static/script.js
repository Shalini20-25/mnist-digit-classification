const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let drawing = false;

// Prediction history
let predictionHistory = [];


// =================================
// Canvas setup
// =================================

ctx.fillStyle = "black";

ctx.fillRect(
    0,
    0,
    canvas.width,
    canvas.height
);

ctx.strokeStyle = "white";
ctx.lineWidth = 18;
ctx.lineCap = "round";
ctx.lineJoin = "round";


// =================================
// Mouse drawing
// =================================

canvas.addEventListener("mousedown", (event) => {

    drawing = true;

    draw(event);

});


canvas.addEventListener("mousemove", (event) => {

    if (drawing) {

        draw(event);

    }

});


canvas.addEventListener("mouseup", () => {

    drawing = false;

    ctx.beginPath();

});


canvas.addEventListener("mouseleave", () => {

    drawing = false;

    ctx.beginPath();

});


// =================================
// Touch drawing
// =================================

canvas.addEventListener("touchstart", (event) => {

    event.preventDefault();

    drawing = true;

    draw(event.touches[0]);

});


canvas.addEventListener("touchmove", (event) => {

    event.preventDefault();

    if (drawing) {

        draw(event.touches[0]);

    }

});


canvas.addEventListener("touchend", () => {

    drawing = false;

    ctx.beginPath();

});


// =================================
// Drawing function
// =================================

function draw(event) {

    const rect =
        canvas.getBoundingClientRect();


    const x =
        (event.clientX - rect.left) *
        (canvas.width / rect.width);


    const y =
        (event.clientY - rect.top) *
        (canvas.height / rect.height);


    ctx.lineTo(x, y);

    ctx.stroke();

    ctx.beginPath();

    ctx.moveTo(x, y);

}


// =================================
// Clear current canvas
// =================================

document.getElementById("clearBtn")
    .addEventListener("click", () => {

        ctx.fillStyle = "black";

        ctx.fillRect(
            0,
            0,
            canvas.width,
            canvas.height
        );

        ctx.beginPath();


        document.getElementById("result")
            .textContent =
            "Prediction: --";


        document.getElementById("probabilities")
            .innerHTML = "";

    });


// =================================
// Predict digit
// =================================

document.getElementById("predictBtn")
    .addEventListener("click", async () => {


        const imageData =
            canvas.toDataURL("image/png");


        document.getElementById("result")
            .textContent =
            "Predicting...";


        try {

            const response =
                await fetch("/predict", {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        image: imageData
                    })

                });


            console.log(
                "HTTP Status:",
                response.status
            );


            const result =
                await response.json();


            console.log(
                "Server Response:",
                result
            );


            // =================================
            // Handle backend errors
            // =================================

            if (!response.ok) {

                document.getElementById("result")
                    .textContent =
                    "⚠️ " +
                    (
                        result.error ||
                        "Prediction failed!"
                    );


                // Clear old probabilities
                document.getElementById(
                    "probabilities"
                ).innerHTML = "";


                return;
            }


            // =================================
            // Successful prediction
            // =================================

            document.getElementById("result")
                .textContent =
                "Prediction: " +
                result.prediction +
                " | Confidence: " +
                result.confidence +
                "%";


            // =================================
            // Add prediction to history
            // =================================

            predictionHistory.unshift({

                digit: result.prediction,

                confidence:
                    result.confidence

            });


            // =================================
            // Display prediction history
            // =================================

            const history =
                document.getElementById(
                    "history"
                );


            history.innerHTML = "";


            predictionHistory.forEach(
                (item, index) => {


                    const historyItem =
                        document.createElement(
                            "div"
                        );


                    historyItem.className =
                        "history-item";


                    historyItem.innerHTML = `

                        <span>
                            #${index + 1}
                        </span>

                        <span class="history-digit">
                            ${item.digit}
                        </span>

                        <span class="history-confidence">
                            ${Number(
                                item.confidence
                            ).toFixed(2)}%
                        </span>

                    `;


                    history.appendChild(
                        historyItem
                    );

                }
            );


            // =================================
            // Display probability bars
            // =================================

            const probabilities =
                document.getElementById(
                    "probabilities"
                );


            probabilities.innerHTML = "";


            result.probabilities.forEach(
                (probability, digit) => {


                    const row =
                        document.createElement(
                            "div"
                        );


                    row.className =
                        "probability-row";


                    row.innerHTML = `

                        <span class="digit">
                            ${digit}
                        </span>

                        <div class="bar-container">

                            <div
                                class="bar"
                                style="width: ${Number(
                                    probability
                                ).toFixed(2)}%">
                            </div>

                        </div>

                        <span class="percentage">
                            ${Number(
                                probability
                            ).toFixed(2)}%
                        </span>

                    `;


                    probabilities.appendChild(
                        row
                    );

                }
            );

        }


        // =================================
        // Network / unexpected error
        // =================================

        catch (error) {

            console.error(
                "FULL ERROR:",
                error
            );


            document.getElementById("result")
                .textContent =
                "⚠️ Unable to connect to the server.";


            document.getElementById(
                "probabilities"
            ).innerHTML = "";

        }

    });


// =================================
// Clear prediction history
// =================================

document.getElementById("clearHistoryBtn")
    .addEventListener("click", () => {

        predictionHistory = [];

        document.getElementById("history")
            .innerHTML = "";

    });