price_house = 1000000  # 1 million
buyer_credits = input('Enter your "CREDIT SCORE" (good or not): ').strip().lower() #strip().lower() ensures input is case-insensitive (e.g., "Good" or " good " still work)

if buyer_credits == "good":
    down_payment = 0.1 * price_house  # 10% down payment
else:
    down_payment = 0.2 * price_house  # 20% down payment

print(f'Down payment: ${down_payment:,}')  # Format with comma separators (${down_payment:,} → $100,000.00)

