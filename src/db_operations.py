from db_config import get_connection

def execute_query(query, params=None):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        return cursor.fetchall()
    except Exception as e:
        connection.rollback()
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

# Операції з категоріями
def add_category(name):
    query = "INSERT INTO categories (name) VALUES (%s)"
    execute_query(query, (name,))

def update_category(category_id, name):
    query = "UPDATE categories SET name = %s WHERE id = %s"
    execute_query(query, (name, category_id))

def delete_category(category_id):
    query = "DELETE FROM categories WHERE id = %s"
    execute_query(query, (category_id,))

def find_categories(name):
    query = "SELECT * FROM categories WHERE name LIKE %s"
    return execute_query(query, ('%' + name + '%',))

# Операції з продуктами
def add_product(name, category_id, price, quantity):
    query = "INSERT INTO products (name, category_id, price, quantity) VALUES (%s, %s, %s, %s)"
    execute_query(query, (name, category_id, price, quantity))

def update_product(product_id, name=None, category_id=None, price=None, quantity=None):
    sql_parts = []
    values = []
    if name:
        sql_parts.append("name = %s")
        values.append(name)
    if category_id:
        sql_parts.append("category_id = %s")
        values.append(category_id)
    if price:
        sql_parts.append("price = %s")
        values.append(price)
    if quantity:
        sql_parts.append("quantity = %s")
        values.append(quantity)
    sql = f"UPDATE products SET {', '.join(sql_parts)} WHERE id = %s"
    values.append(product_id)
    execute_query(sql, tuple(values))

def delete_product(product_id):
    query = "DELETE FROM products WHERE id = %s"
    execute_query(query, (product_id,))

def find_products(name):
    query = "SELECT * FROM products WHERE name LIKE %s"
    return execute_query(query, ('%' + name + '%',))
