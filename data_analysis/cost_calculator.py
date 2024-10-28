from database.food_database import load_food_prices, get_unit_price # 相対パスでインポート

def calculate_cost(food_type, weight, food_prices): # food_pricesを引数に追加
    """食材の種類と重量から金額を計算する。"""
    unit_price = get_unit_price(food_type, food_prices)
    if unit_price is None:
        print(f"Warning: Price not found for {food_type}")
        return None
    cost = unit_price * weight
    return cost