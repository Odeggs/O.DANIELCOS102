class External_Vendors:
    def menu(self):
        pass

class Cooperative_Cafeteria(External_Vendors):
    def menu(self):
        print("Cooperative Cafeteria Menu:")
        print("1. Jollof Rice and Stew - 200")
        print("2. White Rice and Stew - 200")
        print("3. Fried Rice - 200")
        print("4. Salad - 100")
        print("5. Platain - 100")

class Faith_Hostel_Cafeteria(External_Vendors):
    def menu(self):
        print("Faith Hostel Cafeteria Menu:")
        print("1. Fried Rice - 400")
        print("2. White Rice and Stew - 400")
        print("3. Jollof Rice - 400")
        print("4. Beans - 200")
        print("5. Chicken - 1000")

class Student_Centre_Cafeteria(External_Vendors):
    def menu(self):
        print("Student Centre Cafeteria Menu:")
        print("1. Chicken Fried Rice - 800")
        print("2. Pomo Sauce - 300")
        print("3. Spaghetti Jollof - 500")
        print("4. Amala/Ewedu - 500")
        print("5. Semo with Eforiro Soup - 500")

# Get user input for the desired vendor
vendor_choice = input("Enter the desired vendor (Cooperative Hostel, Faith Hostel, Student Center): ")

# Create an instance of the chosen vendor class
if vendor_choice == "Cooperative Hostel":
    vendor = Cooperative_Cafeteria()
elif vendor_choice == "Faith Hostel":
    vendor = Faith_Hostel_Cafeteria()
elif vendor_choice == "Student Center":
    vendor = Student_Centre_Cafeteria()
else:
    print("Invalid vendor choice.")
    exit()

# Call the menu method to display the vendor's menu
vendor.menu()
