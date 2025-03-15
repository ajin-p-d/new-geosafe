from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load CSV file
csv_file = "data/forecasted_values.csv"
df = pd.read_csv(csv_file)

# Define the required columns
selected_columns = {
    "NAME":"NAME",
    "PREDICTED PRECIPITATION RATE": "Predicted Precipitation Rate",
    "PREDICTED SOIL MOISTURE": "Predicted Soil Moisture",
    "PREDICTED WIND SPEED": "Predicted Wind Speed",
    "PREDICTED SURFACE TEMPERATURE": "Predicted Surface Temperature",
    "PREDICTED DEEP SOIL TEMPERATURE": "Predicted Deep Soil Temperature"
}

@app.route('/', methods=['GET', 'POST'])
def search():
    result = None
    error = None

    if request.method == 'POST':
        try:
            name_value = float(request.form.get('name'))  # Convert input to float

            # Find the row where NAME matches the user input
            matching_row = df[df["NAME"] == name_value]

            if matching_row.empty:
                error = "No matching data found."
            else:
                # Select only the required columns
                result = {label: matching_row.iloc[0][col] for col, label in selected_columns.items()}

        except ValueError:
            error = "Invalid input. Please enter a valid float number for NAME."

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
