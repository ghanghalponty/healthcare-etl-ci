def process_claim(amount):
    if amount < 0:
        raise ValueError("Invalid claim amount")
    return amount * 0.9
