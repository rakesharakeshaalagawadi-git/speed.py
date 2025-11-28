# speed.py

def calculate_speed(d, t):
    if t == 0:
        return "Time cannot be zero"
    return d / t

# Optional manual run
if _name_ == "_main_":
    d = float(input("Enter distance (d): "))
    t = float(input("Enter time (t): "))
    print("Speed =", calculate_speed(d, t))