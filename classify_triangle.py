def classify_triangle(a, b, c):
    # Ensure that the inputs are positive and form a valid triangle
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid Triangle: Sides should be greater than 0"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid Triangle: Sides do not form a valid triangle"
    
    # Check if it is an equilateral triangle
    if a == b == c:
        return "Equilateral Triangle"
    
    # Check if it is a right triangle
    if (round(a**2 + b**2, 5) == round(c**2, 5)) or (round(a**2 + c**2, 5) == round(b**2, 5)) or (round(b**2 + c**2, 5) == round(a**2, 5)):
        if a == b or b == c or a == c:
            return "Isosceles Right Triangle"
        return "Scalene Right Triangle"

    # Check for isosceles triangle
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    
    # Otherwise, it's a scalene triangle
    return "Scalene Triangle"
