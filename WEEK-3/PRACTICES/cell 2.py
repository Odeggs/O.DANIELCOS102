#Input form user
m = float(input("Enter mass in kg:"))

#Constant value for the speed of light  in m/s
c = 299792458

#Calculating energy using Eisten's equation
energy = m * c **2

#DISPLAYING THE RESULT
print(f"The energy equivalent to {m} kg of mass is {energy} joules.")
