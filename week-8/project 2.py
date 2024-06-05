import pandas as pd

# Define the data for the DataFrame
data = {
    'Product': ['Cocoa Butter', 'Cocoa Liquor', 'Cocoa Cake', 'Cocoa Powder', 'Bournvita', 'Hot Chocolate', 'Tom Tom', 'Buttermint'],
    'Export': ['International', 'International', 'Local', 'International & Local', 'Local', 'Local', 'Local', 'Local'],
    'Segment': ['Intermediate Cocoa Products', 'Intermediate Cocoa Products', 'Intermediate Cocoa Products', 'Intermediate Cocoa Products', 'Refreshment Beverages', 'Refreshment Beverages', 'Confectionery', 'Confectionery'],
    'Brand': ['CADBURY', 'CADBURY', 'CADBURY', 'CADBURY', 'CADBURY', 'CADBURY', 'TOMTOM', 'BUTTERMINT']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('cadbury_market.csv', index=False)

print("DataFrame saved to cadbury_market.csv")
