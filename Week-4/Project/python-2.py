# Define the function to calculate Annual Tax Revenue (ATR)
def calculate_annual_tax_revenue(years_of_experience, age):
    # Check the conditions and assign the ATR accordingly
    if years_of_experience > 25 and age >= 55:
        atr = "N5,600,000"
    elif years_of_experience >= 20 and age > 45:
        atr = "N4,480,000"
    elif years_of_experience > 10 and age >= 35:
        atr = "N1,500,000"
    else:
        atr = "N550,000"

    return atr

# Example usage: 
# Get input from the user for years of experience and age
years_of_experience = int(input("Enter your years of experience: "))
age = int(input("Enter your age: "))

# Call the function and print the result
atr = calculate_annual_tax_revenue(years_of_experience, age)
print(f"The Annual Tax Revenue (ATR) for the staff is {atr}.")
