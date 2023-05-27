from django.shortcuts import render
from django.views import View
from .models import EmissionFactor

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

def calculate_carbon_emission(distance, vehicle_type, food_items, waste_items):
    emission_transportation = distance * emission_factors[vehicle_type]

    emission_food = sum(emission_factors[food_item] for food_item in food_items)
    emission_waste = sum(emission_factors[waste_item] for waste_item in waste_items)

    total_emission = emission_transportation + emission_food + emission_waste

    return total_emission


def index(request):
    if request.method == 'POST':
        distance = float(request.POST['distance'])
        vehicle_type = request.POST['vehicle_type']
        food_items = request.POST.getlist('food_items')
        waste_items = request.POST.getlist('waste_items')

        emission_transportation = vehicle_type
        emission_food = food_items
        emission_waste = waste_items

        total_emission = calculate_carbon_emission(distance, vehicle_type, food_items, waste_items)

        recommendations_list = get_recommendations(emission_transportation, emission_food, emission_waste)

        return render(request, 'result.html', {
            'total_emission': total_emission,
            'emission_transportation': emission_transportation,
            'emission_food': emission_food,
            'emission_waste': emission_waste,
            'recommendations_list': recommendations_list
        })

    return render(request, 'index.html')

def get_recommendations(emission_transportation, emission_food, emission_waste):
    recommendations_list = []
    print(emission_transportation)
    print(emission_food)
    print(emission_waste)
    for transportation_item in emission_transportation:
        if transportation_item in recommendations["transportation"]:
            recommendations_list.append(recommendations["transportation"][transportation_item])


    for food_item in emission_food:
        if food_item in recommendations["food"]:
            recommendations_list.append(recommendations["food"][food_item])

    
    for waste_item in emission_waste:
        if waste_item in recommendations["waste"]:
            recommendations_list.append(recommendations["waste"][waste_item])

    return recommendations_list

    
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the URL name of your home page

