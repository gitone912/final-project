from flask import Flask, render_template, request

from project import calculate_carbon_footprint, get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    miles = float(request.form['miles'])
    electricity = float(request.form['electricity'])

    footprint = calculate_carbon_footprint(miles, electricity)
    recommendations = get_recommendations(footprint)

    return render_template('result.html', footprint=footprint, recommendations=recommendations)

if __name__ == '__main__':
    app.run()
