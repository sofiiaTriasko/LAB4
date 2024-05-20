import Pyro4
from db_operations import (
    add_category, update_category, delete_category, find_categories,
    add_product, update_product, delete_product, find_products
)

@Pyro4.expose
class StoreManager:
    def add_category(self, name):
        add_category(name)
        return "Category added successfully"

    def update_category(self, category_id, name):
        update_category(category_id, name)
        return "Category updated successfully"

    def delete_category(self, category_id):
        delete_category(category_id)
        return "Category deleted successfully"

    def find_categories(self, name):
        categories = find_categories(name)
        return categories

    def add_product(self, name, category_id, price, quantity):
        add_product(name, category_id, price, quantity)
        return "Product added successfully"

    def update_product(self, product_id, name=None, category_id=None, price=None, quantity=None):
        update_product(product_id, name, category_id, price, quantity)
        return "Product updated successfully"

    def delete_product(self, product_id):
        delete_product(product_id)
        return "Product deleted successfully"

    def find_products(self, name):
        products = find_products(name)
        return products

def main():
    Pyro4.Daemon.serveSimple(
        {
            StoreManager: "store.manager"
        },
        host="localhost",
        port=9090,
        ns=True
    )

if __name__ == "__main__":
    main()
