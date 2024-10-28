# Flaskを使ったAPIの例。クラウド関数にデプロイする必要があります

from flask import Flask, request, jsonify
from database.user_data import insert_data, get_data #修正

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        food_type = data.get('food_type')
        weight = data.get('weight')
        cost = data.get('cost')

        if not all([user_id, food_type, weight, cost]):
          return jsonify({"message": "Missing required data."}), 400
        
        insert_data(user_id, food_type, weight, cost)

        return jsonify({"message": "Data uploaded successfully."}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {e}"}), 500

@app.route('/data/<user_id>', methods=['GET'])
def get_user_data(user_id):
  try:
    data = get_data(user_id)
    return jsonify(data), 200
  except Exception as e:
    return jsonify({"message": f"An error occurred: {e}"}), 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) #ローカルテスト用