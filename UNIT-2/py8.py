# Global
x = 10
def outer():
    # Nonlocal 
    y = 20

    def inner():
        # Accessing nonlocal variable
        nonlocal y
        y = y + 5
        print("Nonlocal variable:", y)

    inner()

def demo():
    # Local 
    z = 30
    print("Local variable:", z)
# Accessing global variable
print("Global variable:", x)
# Calling functions
demo()
outer()
