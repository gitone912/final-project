from flask import Flask, render_template, request


app = Flask(__name__)


# Emission factors in kg CO2 per unit
emission_factors = {
    "car": 0.2,
    "motorcycle": 0.1,
    "bus": 0.3,
    "beef": 27.0,
    "chicken": 6.9,
    "pork": 5.8,
    "vegetables": 2.0,
    "fruits": 1.4,
    "plastic": 3.0,
    "paper": 1.0,
    "glass": 2.0
}

# Recommendations based on emissions
recommendations = {
    "transportation": {
        "car": "Consider carpooling or using public transportation to reduce emissions.",
        "motorcycle": "Consider using alternative transportation modes like cycling or walking.",
        "bus": "Using public transportation is a great choice for reducing carbon emissions."
    },
    "food": {
        "beef": "Reduce consumption of beef as it has a high carbon footprint. Choose more plant-based alternatives.",
        "chicken": "Choose chicken as a lower carbon footprint alternative to beef.",
        "pork": "Opt for pork as a lower carbon footprint alternative to beef.",
        "vegetables": "Include more vegetables in your diet. They have a lower carbon footprint compared to meat.",
        "fruits": "Include more fruits in your diet. They have a lower carbon footprint compared to meat."
    },
    "waste": {
        "plastic": "Reduce the use of plastic and opt for reusable or biodegradable alternatives.",
        "paper": "Recycle paper and choose recycled paper products.",
        "glass": "Recycle glass bottles and jars to reduce waste and conserve resources."
    }
}

@app.route('/index', methods=['GET', 'POST'])


def calculate_carbon_emission(distance, vehicle_type):
    # Calculate carbon emissions from transportation
    
    emission_transportation = distance * emission_factors.get(vehicle_type, 0)

    # Calculate carbon emissions from food and waste
    emission_food = 0
    emission_waste = 0

    food_items = request.form.getlist('food_items')
    for food_item in food_items:
        emission_food += emission_factors.get(food_item, 0)

    waste_items = request.form.getlist('waste_items')
    for waste_item in waste_items:
        emission_waste += emission_factors.get(waste_item, 0)

    # Calculate total emissions
    total_emission = emission_transportation + emission_food + emission_waste

    return total_emission


def get_recommendations(emission_transportation, emission_food, emission_waste):
    recommendations_list = []

    # Add transportation recommendation
    recommendations_list.append(recommendations["transportation"].get(emission_transportation, ""))

    # Add food recommendations
    recommendations_list.append(recommendations["food"].get(emission_food, ""))

    # Add waste recommendations
    recommendations_list.append(recommendations["waste"].get(emission_waste, ""))

    return recommendations_list


@app.route('/result', methods=['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        distance = float(request.form['distance'])
        vehicle_type = request.form['vehicle_type']

        total_emission = calculate_carbon_emission(distance, vehicle_type)

        emission_transportation = "transportation: " + str(distance) + " km by " + vehicle_type
        emission_food = "food: " + ", ".join(request.form.getlist('food_items'))
        emission_waste = "waste: " + ", ".join(request.form.getlist('waste_items'))

        recommendations_list = get_recommendations(emission_transportation, emission_food, emission_waste)

        return render_template('result.html', total_emission=total_emission,
                               emission_transportation=emission_transportation,
                               emission_food=emission_food, emission_waste=emission_waste,
                               recommendations_list=recommendations_list)

    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
