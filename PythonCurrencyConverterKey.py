#Here Is An Outline To Read Over To Understand what your trying to do

# Step 1: Set up exchange rates (you can modify or expand this dictionary)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "NGN": 0.739,
    # Add more currencies and their rates as needed
}

# Step 2: Get user input
def get_user_input():
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD, EUR, NGN): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., USD, EUR, NGN): ").upper()
    return amount, from_currency, to_currency

# Step 3: Perform the conversion
def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Currency not supported.")
        return None

    from_rate = exchange_rates[from_currency]
    to_rate = exchange_rates[to_currency]
    converted_amount = (amount / from_rate) * to_rate
    return converted_amount

# Step 4: Display the result
def main():
    amount, from_currency, to_currency = get_user_input()
    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

if __name__ == "__main__":
    main()