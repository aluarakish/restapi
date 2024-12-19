from flask import Flask, request, jsonify
from sql_practice import add_post, get_posts, delete_post, get_post, update_post  # Импортируем функции для работы с базой данных

app = Flask(__name__)

# Главная страница
@app.route("/")
def welcome():
    return "Это моё первое API"

# Функция для получения имени
@app.route("/name")
def get_name():
    return "Алуа"

# Функция для получения погоды по городу
@app.route("/city/<city_name>")
def weather_by_city(city_name):
    city_name = city_name.lower()
    weather_data = {
        "astana": -10.3,
        "almaty": -6.7,
        "vienna": 0
    }
    
    if city_name in weather_data:
    return jsonify({
        "message": f"Текущая погода в {city_name.capitalize()}: {weather_data[city_name]} цельсия"
    }), 200
else:
    return jsonify({
        "error": f"У меня нет информации о погоде в {city_name.capitalize()}"
    }), 404


# 1. Обработчик для создания нового поста
@app.route("/post/new", methods=["POST"])
def create_post():
    data = request.get_json()  
    title = data.get("title")
    content = data.get("content")
    
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    
    add_post(title, content)  
    return jsonify({"message": "Post created successfully"}), 201

# 2. Обработчик для получения поста по ID
@app.route("/post/<int:post_id>", methods=["GET"])
def get_single_post(post_id):
    post = get_post(post_id)  
    if post:
        return jsonify(post), 200  
    return jsonify({"error": "Post not found"}), 404  

# 3. Обработчик для обновления поста
@app.route("/post/update/<int:post_id>", methods=["PUT"])
def update_single_post(post_id):
    data = request.get_json()  
    title = data.get("title")
    content = data.get("content")
    
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    
    result = update_post(post_id, title, content)  
    if result > 0:
        return jsonify({"message": "Post updated successfully"}), 200
    return jsonify({"error": "Post not found or not updated"}), 404  

# 4. Обработчик для удаления поста
@app.route("/post/delete/<int:post_id>", methods=["DELETE"])
def delete_single_post(post_id):
    delete_post(post_id)
    return jsonify({"message": "Post deleted successfully"}), 200

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
