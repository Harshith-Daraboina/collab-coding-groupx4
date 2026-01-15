def take_order(menu):
    order = {}

    print("---------------------------Cafe menu--------------------------")

    for item, price in menu.items():
        print(f"Item: {item}, price: {price}")

    while True:
        item = input("Enter your order (or Done to finish): ")
        if item == "Done":
            break

        if item not in menu:
            print("Item not in menu")

        qty = int(input("Enter quantity: "))
        order[item] = order.get(item, 0) + qty

    print("Your order: ", order)

    return order
