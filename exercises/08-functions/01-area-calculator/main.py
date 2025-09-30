def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    return area

def calculate_circle_area(radius):
    """Calculate the area of a circle"""
    area = 3.14159 * radius ** 2
    return area

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle"""
    area = (base * height) / 2
    return area

print("=== Area Calculator ===")

# Test your functions with these values:
rectangle_area = calculate_rectangle_area(5, 3)
print(f"Rectangle (5 × 3): {rectangle_area} square units")

circle_area = calculate_circle_area(4)
print(f"Circle (radius 4): {circle_area:.2f} square units")

triangle_area = calculate_triangle_area(6, 8)
print(f"Triangle (6 × 8): {triangle_area} square units")


