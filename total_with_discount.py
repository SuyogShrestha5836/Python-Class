def total_with_discount(items):
    total = sum(items.values())
    discount = total * 0.1
    total_with_discount = total - discount
    return total_with_discount