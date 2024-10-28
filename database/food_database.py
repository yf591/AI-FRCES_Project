import csv

def load_food_prices(csv_file):
    """CSVファイルから食品の価格データを読み込む"""
    try:
        food_prices = {}
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # ヘッダー行をスキップ
            for row in reader:
                try:
                    food_prices[row[0]] = int(row[1])
                except (ValueError, IndexError) as e:
                    print(f"Error reading CSV row: {row}, Error: {e}")
        return food_prices
    except FileNotFoundError:
        print(f"Error: CSV file not found: {csv_file}")
        return None

def get_unit_price(food_type, food_prices):
    """食材の単価を取得する"""
    return food_prices.get(food_type)