import datetime
import random
from database.food_database import load_food_prices
from data_acquisition.sensor_reader import read_sensor_data
from image_processing.image_classifier import classify_image
from data_analysis.cost_calculator import calculate_cost
from database.user_data import insert_data


def main():
    weight = read_sensor_data()
    image_path = 'images/test_image.jpg'  # ローカルの画像ファイルパス

    food_type, estimated_weight = classify_image(image_path)  # 戻り値を2つ受け取る


    csv_file_path = 'food_prices.csv'  # ローカルのCSVファイルパス
    food_prices = load_food_prices(csv_file_path)

    if food_type is not None and food_prices is not None:
        cost = calculate_cost(food_type, estimated_weight, food_prices)  # estimated_weight を使用
        if cost is not None:
            data = {"weight": estimated_weight, "food_type": food_type, "cost": cost, "timestamp": datetime.datetime.now().isoformat()}
            user_id = "test_user"  # テストユーザーID
            insert_data(user_id, food_type, estimated_weight, cost) # データベースに保存
            print(f"Data inserted into database: {food_type, estimated_weight, cost}")
    else:
        if food_type is None:
            print("Could not classify image.")
        if food_prices is None:
            print("Could not load food prices.")



if __name__ == "__main__":
    main()