def calculate_total(items, discount_percent=0, promo=None):
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be in [0, 100]")
    
    total = 0.0
    for item in items:
        price = item["price"]
        qty = item["qty"]
        if price <= 0 or qty < 1:
            raise ValueError("invalid item")
        total += price * qty
        
    if promo == "SALE10":
        discount_percent += 10
        
    # Внимание: здесь кроется учебный дефект (скидка может превысить 100%)
    return round(total * (1 - discount_percent / 100), 2)