import sqlite3
from config import DB_PATH


# Функция для добавления нового поста
def add_post(title: str, content: str) -> None:
    add_post_query = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(add_post_query, (title, content))
    connection.commit()
    connection.close()

    print("Пост добавлен")


# Функция для получения всех постов
def get_posts():
    get_posts_query = """
    SELECT * FROM posts;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_posts_query)

    posts = cursor.fetchall()

    connection.close()

    print("Вот посты:", posts)


# Функция для удаления поста
def delete_post(post_id: int) -> None:
    delete_post_query = """
    DELETE FROM posts WHERE post_id = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(delete_post_query, (post_id,))
    connection.commit()
    connection.close()

    print(f"Удалено постов: {cursor.rowcount}")


# Функция для получения одного поста по ID
def get_post(post_id: int):
    get_post_query = """
    SELECT * FROM posts WHERE post_id = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_post_query, (post_id,))
    
    post = cursor.fetchone() 
    connection.close()

    if post:
        return {"post_id": post[0], "title": post[1], "content": post[2]}
    else:
        return None


# Функция для обновления поста по ID
def update_post(post_id: int, new_title: str, new_content: str) -> bool:
    update_post_query = """
    UPDATE posts SET title = ?, content = ? WHERE post_id = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(update_post_query, (new_title, new_content, post_id))
    connection.commit()

    if cursor.rowcount > 0:  
        connection.close()
        return True  
    else:
        connection.close()
        return False  
