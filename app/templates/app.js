document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("phishingForm");

    if (form) {
        form.addEventListener("submit", async function (event) {
            event.preventDefault();
            const urlInput = document.getElementById("url").value;

            try {
                // Send the URL to the backend for prediction
                const response = await fetch("http://127.0.0.1:5000/predict", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ url: urlInput })  // Send the URL as JSON
                });

                // Check if the response was successful
                if (!response.ok) throw new Error("Network response error");

                // Get the JSON response from the backend
                const data = await response.json();

                // Redirect to the prediction result page with phishing status
                window.location.href = `prediction.html?phishing=${data.phishing}`;

            } catch (error) {
                // If there's an error, alert the user
                alert("Error: Unable to fetch prediction.");
            }
        });
    }

    // Display prediction result in the prediction.html page
    const resultText = document.getElementById("resultText");
    if (resultText) {
        const params = new URLSearchParams(window.location.search);
        const isPhishing = params.get("phishing") === "true";  // Check if phishing result is true
        resultText.textContent = isPhishing ? "⚠️ This is a phishing URL!" : "✅ This URL is safe.";
        resultText.classList.add(isPhishing ? "phishing" : "legitimate");
    }
});
