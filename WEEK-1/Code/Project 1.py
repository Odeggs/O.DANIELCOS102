def simple_interest():
    P = float(input("Enter the principal amount (P): "))
    T = float(input("Enter the time in years (T): "))
    R = float(input("Enter the annual interest rate (R) as a decimal: "))
    A = P * (1 + R*T)
    print(f"The simple interest is: {A}")

def compound_interest():
    P = float(input("Enter the principal amount (P): "))
    T = float(input("Enter the time in years (T): "))
    R = float(input("Enter the annual interest rate (R) as a decimal: "))
    A = P * (1 + R/100)**T
    print(f"The compound interest is: {A}")

def annuity_plan():
    PMT = float(input("Enter the annuity payment (PMT): "))
    R = float(input("Enter the annual interest rate (R) as a decimal: "))
    n = float(input("Enter the number of times the interest is compounded per year (n): "))
    t = float(input("Enter the time in years (t): "))
    A = PMT * (((1 + R/n)**(n*t))-1) / (R/n)
    print(f"The future value of the annuity is: {A}")

print("Select a problem to solve:")
print("1. Simple Interest")
print("2. Compound Interest")
print("3. Annuity Plan")

problem = int(input("Enter the number of the problem you want to solve: "))

if problem == 1:
    simple_interest()
elif problem == 2:
    compound_interest()
elif problem == 3:
    annuity_plan()
else:
    print("Invalid problem number.")