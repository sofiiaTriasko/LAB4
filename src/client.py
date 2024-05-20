import Pyro4

def main():
    # Підключення до служби імен Pyro4
    ns = Pyro4.locateNS()
    uri = ns.lookup('store.manager')
    store_manager = Pyro4.Proxy(uri)

    response = store_manager.add_category('Beverages')
    print('Response:', response)

    response = store_manager.add_product('Apple Juice', 1, 1.5, 50)
    print('Response:', response)

    response = store_manager.find_products('Apple Juice')
    print('Response:', response)

    response = store_manager.update_product(1, price=1.75)
    print('Response:', response)

    response = store_manager.delete_product(1)
    print('Response:', response)

    response = store_manager.delete_category(1)
    print('Response:', response)

if __name__ == "__main__":
    main()
