import tkinter as tk

class DeliveryService:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Delivery Service")
        self.window.geometry("400x300")

        self.location_var = tk.StringVar()
        self.weight_var = tk.IntVar()

        # Corrected 'tk.label' to 'tk.Label'
        tk.Label(self.window, text="DELIVERY LOCATION:").pack()

        # Corrected 'Self.window' to 'self.window' and 'Variable=' to 'variable='
        tk.Radiobutton(self.window, text="PAU", variable=self.location_var, value="PAU").pack()
        tk.Radiobutton(self.window, text="Epe", variable=self.location_var, value="Epe").pack()

        # Corrected 'tk.label' to 'tk.Label'
        tk.Label(self.window, text="Package Weight (kg):").pack()

        # Added an Entry widget for weight input
        tk.Entry(self.window, textvariable=self.weight_var).pack()

        # Corrected 'tk.Radiobutton' to 'tk.Button' and fixed 'command='
        tk.Button(self.window, text="Calculate Cost", command=self.calculate_cost).pack()

    def calculate_cost(self):
        location = self.location_var.get()
        weight = self.weight_var.get()

        # Fixed logical and syntax errors in the condition
        if location in ["PAU", "Epe"] and weight >= 10:
            cost = 2000
        else:
            cost = 1500
            

        # Display the cost to the user
        tk.Label(self.window, text=f"Cost: {cost}").pack()

# Create an instance of the class and run the application
if __name__ == "__main__":
    app = DeliveryService()
    app.window.mainloop()
