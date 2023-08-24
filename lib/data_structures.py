spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    return total_heat // num_foods if num_foods > 0 else 0

# Call the functions and print the results
names = get_names(spicy_foods)
print("Names:", names)

spiciest_foods = get_spiciest_foods(spicy_foods)
print("Spiciest Foods:", spiciest_foods)

print("All Spicy Foods:")
print_spicy_foods(spicy_foods)

american_food = get_spicy_food_by_cuisine(spicy_foods, "American")
print("American Food:", american_food)

print("Spiciest Foods:")
print_spiciest_foods(spicy_foods)

average_heat = get_average_heat_level(spicy_foods)
print("Average Heat Level:", average_heat)

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()  # Create a copy to avoid modifying the original list
    new_spicy_foods.append(spicy_food)    # Add the new spicy_food dictionary
    return new_spicy_foods
