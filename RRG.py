# Import the Flask framework for creating web applications
from flask import Flask, jsonify
# Import the random module to generate random recipes
import random

# Create an instance of the Flask app
app = Flask(__name__)

# List of example recipes
recipes = [
    "Pasta Carbonara",
    "Chicken Stir-Fry",
    "Vegetable Curry",
    "Spaghetti Bolognese",
    "Grilled Salmon",
    "Homemade Pizza",
    "Crispy Tofu Tacos",
    "Beef Stew",
    "Omelette",
    "Fruit Smoothie"
]

# Define a route for the API endpoint to generate a random recipe
@app.route('/random_recipe', methods=['GET'])
def random_recipe():
    # Choose a random recipe from the list
    random_recipe = random.choice(recipes)
    # Return the random recipe as a JSON response
    return jsonify({"recipe": random_recipe})

# Run the app when executed directly
if __name__ == '__main__':
    # Start the app on 0.0.0.0 (all available network interfaces) and port 8080
    app.run(host='0.0.0.0', port=8080)
