# Data from the image for boys
boys_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boys_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boys_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

# Data from the image for girls
girls_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_ages = [18, 17, 19, 16, 20, 18, 17, 19, 16, 20]
girls_heights = [5.6, 5.8, 5.7, 5.9, 5.5, 5.6, 5.7, 5.8, 5.9, 5.5]
girls_scores = [88, 92, 71, 83, 77, 85, 90, 76, 79, 84]

# Function to print data in tabular form and check scores
def print_table_and_check_scores(names, ages, heights, scores):
    # Header
    print(f"{'Name':<10} {'Age':<5} {'Height':<7} {'Score':<6}")
    print("-" * 40)
    
    # Rows and check scores
    for i in range(len(names)):
        print(f"{names[i]:<10} {ages[i]:<5} {heights[i]:<7} {scores[i]:<6}")
        if scores[i] > 80:
            print(f"{names[i]} scored above 80.")

# Call the function to print the table and check scores for boys
print("Boys:")
print_table_and_check_scores(boys_names, boys_ages, boys_heights, boys_scores)

# Call the function to print the table and check scores for girls
print("\nGirls:")
print_table_and_check_scores(girls_names, girls_ages, girls_heights, girls_scores)
