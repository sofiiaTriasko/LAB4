import unittest
from src.db_operations import (
    add_category, update_category, delete_category, find_categories,
    add_product, update_product, delete_product, find_products
)

class TestDBOperations(unittest.TestCase):

    def test_add_category(self):
        add_category('Test Category')
        result = find_categories('Test Category')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Test Category')

    def test_update_category(self):
        add_category('Update Test Category')
        result = find_categories('Update Test Category')
        self.assertEqual(len(result), 1)
        category_id = result[0][0]
        update_category(category_id, 'Updated Category')
        result = find_categories('Updated Category')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Updated Category')

    def test_delete_category(self):
        add_category('Delete Test Category')
        result = find_categories('Delete Test Category')
        self.assertEqual(len(result), 1)
        category_id = result[0][0]
        delete_category(category_id)
        result = find_categories('Delete Test Category')
        self.assertEqual(len(result), 0)

    def test_add_product(self):
        add_category('Product Test Category')
        category = find_categories('Product Test Category')[0]
        add_product('Test Product', category[0], 10.0, 100)
        result = find_products('Test Product')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][2], 'Test Product')

    def test_update_product(self):
        add_category('Product Update Category')
        category = find_categories('Product Update Category')[0]
        add_product('Update Product', category[0], 10.0, 100)
        product = find_products('Update Product')[0]
        update_product(product[0], price=20.0)
        result = find_products('Update Product')
        self.assertEqual(result[0][3], 20.0)

    def test_delete_product(self):
        add_category('Product Delete Category')
        category = find_categories('Product Delete Category')[0]
        add_product('Delete Product', category[0], 10.0, 100)
        product = find_products('Delete Product')[0]
        delete_product(product[0])
        result = find_products('Delete Product')
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
