from flask import Flask, jsonify, render_template
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Load and preprocess data
file_path = "data/TalukWiseListDigitisedVillagesKerala.csv"
df = pd.read_csv(file_path)
df.columns = ["Index", "District", "District_Malayalam", "Taluk_Malayalam", "Taluk", "Village_Malayalam", "Village"]

df = df[["District", "Taluk", "Village"]].dropna()

districts = sorted(df["District"].unique())

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/districts')
def get_districts():
    return jsonify(districts)

@app.route('/taluks/<district>')
def get_taluks(district):
    taluks = sorted(df[df["District"] == district]["Taluk"].unique())
    return jsonify(taluks)

@app.route('/villages/<taluk>')
def get_villages(taluk):
    villages = sorted(df[df["Taluk"] == taluk]["Village"].unique())
    return jsonify(villages)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
