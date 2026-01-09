
from flask import Flask, request, render_template, send_file
import os
from core import calculate_wellness_from_csv

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCORED_FILE = os.path.join(BASE_DIR, "scored.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    df = None
    message = ""
    download_link = False

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            df = calculate_wellness_from_csv(file)
            df.to_csv(SCORED_FILE, index=False)
            message = "Wellness scores calculated successfully!"
            download_link = True

    return render_template("index.html", rows=df.to_dict(orient='records') if df is not None else None,
                           message=message, download_link=download_link)

@app.route("/download")
def download():
    if os.path.exists(SCORED_FILE):
        return send_file(SCORED_FILE, as_attachment=True)
    return "No scored file available. Please upload and calculate first."

if __name__ == "__main__":
    app.run(debug=True)
