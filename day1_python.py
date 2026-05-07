print("TOPIC 1: Variables & Data Types")
# Integers — whole numbers
age = 19
year = 2026

# Floats — decimal numbers
height = 5.9
pi = 3.14159

# Strings — text
name = "Stago"
university = "Parul University"

# Boolean — True or False
is_student = True
has_drone = False

# Check the type of any variable
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>

print("TOPIC 2: Operators")
# Arithmetic operators
a = 10
b = 3

print(a + b)   # 13  — Addition
print(a - b)   # 7   — Subtraction
print(a * b)   # 30  — Multiplication
print(a / b)   # 3.33 — Division (always float)
print(a // b)  # 3   — Floor division (removes decimal)
print(a % b)   # 1   — Modulus (remainder)
print(a ** b)  # 1000 — Power (10 to the power 3)

# Comparison operators (return True or False)
print(a > b)   # True
print(a < b)   # False
print(a == b)  # False
print(a != b)  # True

# Logical operators
print(a > 5 and b < 5)   # True (both conditions true)
print(a > 5 or b > 5)    # True (at least one true)
print(not(a > 5))         # False (reverses the result)


print("TOPIC 3: Strings")
name = "Stago"

# String operations
print(len(name))           # 5 — length
print(name.upper())        # STAGO
print(name.lower())        # stago
print(name[0])             # S — first character
print(name[-1])            # o — last character
print(name[0:3])           # Sta — slicing

# String formatting (use this always)
age = 19
city = "Gujarat"
print(f"My name is {name}, I am {age} years old from {city}")

# String methods
sentence = "  hello world  "
print(sentence.strip())         # removes spaces
print(sentence.replace("hello", "hi"))
print(sentence.split())         # splits into list

# Check inside string
print("ago" in name)    # True
print("xyz" in name)    # False


print("TOPIC 4: Input & Output")
# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # convert to int
height = float(input("Enter height: "))  # convert to float

print(f"Hello {name}!")
print(f"In 10 years you will be {age + 10}")
print(f"Your height is {height:.2f} feets")  # 2 decimal places
