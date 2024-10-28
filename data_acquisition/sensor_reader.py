import random

def read_sensor_data():
    """センサーデータの代わりとなるランダムな重量データを返す (シミュレーション用)"""
    return random.uniform(0.1, 1.0)

# 実際のセンサーを使う場合は、以下のように置き換える
# import serial
# def read_sensor_data():
#     try:
#         ser = serial.Serial('適切なポート名', 9600)  # ポート名とボーレートを指定
#         weight_data = float(ser.readline().decode('utf-8').strip())
#         return weight_data
#     except Exception as e:
#         print(f"Error reading sensor data: {e}")
#         return None