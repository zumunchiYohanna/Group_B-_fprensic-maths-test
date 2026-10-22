# Vehicle Collision Skid Analysis

distance = float(input("Enter the skid mark distance (feet): "))
drag_factor = float(input("Enter the drag factor: "))

# Calculate estimated speed in miles per hour
speed = (30 * distance * drag_factor) ** 0.5

print(f"The calculated speed is: {speed:.2f} mph")
