<<<<<<< HEAD
import cmath

def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    root1 = (-b - cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)
    return root1, root2

def solve_cubic(a, b, c, d):
    q = (3*a*c - b**2) / (9 * a**2)
    r = (9*a*b*c - 27*a**2*d - 2*b**3) / (54*a**3)
    delta = q**3 + r**2
    
    if delta < 0:
        rho = (-q**3) ** 0.5
        s_real = rho ** (1./3.)
        t_real = rho ** (1./3.)
        x1 = s_real + t_real - b / (3. * a)
        return x1
    else:
        return None

# Get user input for equation type
equation_type = input("Enter the type of equation to solve (cubic/quadratic): ").lower()

if equation_type == "quadratic":
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    root1, root2 = solve_quadratic(a, b, c)
    
    print(f"The roots are {root1} and {root2}")
elif equation_type == "cubic":
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))
    
    cubic_root = solve_cubic(a, b, c, d)
    
    if cubic_root is not None:
        print(f"The cubic root is {cubic_root:.6f}")
    else:
        print("No real roots for the given coefficients.")
else:
    print("Invalid equation type. Please choose 'cubic' or 'quadratic'.")
=======
import cmath

def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    root1 = (-b - cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)
    return root1, root2

def solve_cubic(a, b, c, d):
    q = (3*a*c - b**2) / (9 * a**2)
    r = (9*a*b*c - 27*a**2*d - 2*b**3) / (54*a**3)
    delta = q**3 + r**2
    
    if delta < 0:
        rho = (-q**3) ** 0.5
        s_real = rho ** (1./3.)
        t_real = rho ** (1./3.)
        x1 = s_real + t_real - b / (3. * a)
        return x1
    else:
        return None

# Get user input for equation type
equation_type = input("Enter the type of equation to solve (cubic/quadratic): ").lower()

if equation_type == "quadratic":
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    root1, root2 = solve_quadratic(a, b, c)
    
    print(f"The roots are {root1} and {root2}")
elif equation_type == "cubic":
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))
    
    cubic_root = solve_cubic(a, b, c, d)
    
    if cubic_root is not None:
        print(f"The cubic root is {cubic_root:.6f}")
    else:
        print("No real roots for the given coefficients.")
else:
    print("Invalid equation type. Please choose 'cubic' or 'quadratic'.")
>>>>>>> 1bdbe693d7d1bdb899c76fa386e59a27bbaec618
