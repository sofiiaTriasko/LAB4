import socket
import json
from db_operations import (
    add_category, update_category, delete_category, find_categories,
    add_product, update_product, delete_product, find_products
)

def handle_request(data):
    request = json.loads(data)
    action = request.get('action')
    if action == 'add_category':
        name = request.get('name')
        add_category(name)
        return 'Category added successfully'
    elif action == 'update_category':
        category_id = request.get('category_id')
        name = request.get('name')
        update_category(category_id, name)
        return 'Category updated successfully'
    elif action == 'delete_category':
        category_id = request.get('category_id')
        delete_category(category_id)
        return 'Category deleted successfully'
    elif action == 'find_categories':
        name = request.get('name')
        categories = find_categories(name)
        return json.dumps(categories)
    elif action == 'add_product':
        name = request.get('name')
        category_id = request.get('category_id')
        price = request.get('price')
        quantity = request.get('quantity')
        add_product(name, category_id, price, quantity)
        return 'Product added successfully'
    elif action == 'update_product':
        product_id = request.get('product_id')
        name = request.get('name')
        category_id = request.get('category_id')
        price = request.get('price')
        quantity = request.get('quantity')
        update_product(product_id, name, category_id, price, quantity)
        return 'Product updated successfully'
    elif action == 'delete_product':
        product_id = request.get('product_id')
        delete_product(product_id)
        return 'Product deleted successfully'
    elif action == 'find_products':
        name = request.get('name')
        products = find_products(name)
        return json.dumps(products)
    else:
        return 'Unknown action'

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('Server started and listening on:'.format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        print('Got connection from', addr)
        data = client_socket.recv(1024).decode()
        response = handle_request(data)
        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
