""" from predefined_prices import prices

def get_items_prices(items):
    #return the items of each items found in a list
    all_prices = [[] for _ in range(len(items))]
    for i, item in enumerate(items):
        for price in prices:
            if item.lower() in price['name'].lower():
                all_prices[i].append(price)
    return all_prices """