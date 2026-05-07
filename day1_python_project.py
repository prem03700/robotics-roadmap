# ROBOT IDENTITY CARD GENERATOR
# Build a program that asks for robot details and prints a card

robot_name = input("Enter robot name: ")
robot_type = input("Enter robot type (drone/arm/mobile): ")
max_speed = float(input("Enter max speed (m/s): "))
battery = int(input("Enter battery capacity (mAh): "))
autonomous = input("Is it autonomous? (yes/no): ")

# Calculate battery life (assume 500mAh used per hour)
battery_life = battery / 500

print("\n" + "="*40)
print("       ROBOT IDENTITY CARD")
print("="*40)
print(f"Name        : {robot_name.upper()}")
print(f"Type        : {robot_type.capitalize()}")
print(f"Max Speed   : {max_speed} m/s")
print(f"Battery     : {battery} mAh")
print(f"Battery Life: {battery_life:.1f} hours")
print(f"Autonomous  : {autonomous.capitalize()}")
print(f"Speed in km/h: {max_speed * 3.6:.2f}")
print("="*40)