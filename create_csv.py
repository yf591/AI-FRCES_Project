# csvファイル作成
import csv

food_prices = {
    "person": 100,
    "bottle": 200,
    "banana": 200,
    "broccoli": 250,
    "orange": 150,
    "sandwich": 350,
    "tomato": 100,
    "apple": 120,
    "avocado": 250,
    "bacon": 400,
    "bagel": 200,
    "beef": 600,
    "blueberry": 300,
    "bread": 250,
    "burger": 500,
    "butter": 200,
    "cake": 400,
    "candy": 150,
    "carrot": 80,
    "celery": 100,
    "cheese": 350,
    "chicken": 550,
    "chocolate": 200,
    "coffee": 250,
    "cookie": 100,
    "corn": 150,
    "cucumber": 80,
    "donut": 180,
    "egg": 200,
    "fish": 650,
    "fries": 300,
    "grape": 280,
    "grapefruit": 150,
    "ham": 450,
    "hot dog": 300,
    "ice cream": 250,
    "juice": 200,
    "kiwi": 120,
    "lemon": 100,
    "lettuce": 150,
    "lime": 90,
    "lobster": 1200,
    "mango": 200,
    "melon": 180,
    "milk": 150,
    "muffin": 220,
    "mushroom": 200,
    "noodle": 250,
    "onion": 80,
    "pancake": 250,
    "pasta": 300,
    "peach": 150,
    "pear": 130,
    "pepper": 100,
    "pie": 400,
    "pineapple": 250,
    "pizza": 600,
    "pork": 500,
    "potato": 100,
    "pretzel": 150,
    "pudding": 200,
    "radish": 90,
    "raspberry": 350,
    "rice": 120,
    "salad": 350,
    "salmon": 700,
    "sausage": 400,
    "shrimp": 750,
    "soup": 300,
    "steak": 800,
    "strawberry": 300,
    "sushi": 500,
    "taco": 350,
    "tea": 200,
    "toast": 150,
    "waffle": 280,
    "watermelon": 200,
    "wine": 500,
    "yogurt": 180,
     # ... その他の食材
}

try:
    with open('food_prices.csv', 'w', newline='', encoding='utf-8') as csvfile: # encodingを指定
        fieldnames = ['food_name', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for food_name, price in food_prices.items():
            writer.writerow({'food_name': food_name, 'price': price})
    print(f"CSV file 'food_prices.csv' created successfully.")

except Exception as e:
    print(f"An error occurred while creating the CSV file: {e}")