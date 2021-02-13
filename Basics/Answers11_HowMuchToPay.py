name = input("Enter full name:")
length_of_wall = float(input("Enter length of wall in meters:"))
widith_of_wall = float(input("Enter widith of wall in meters:"))
length_of_window = float(input("Enter length of window  in meters:"))
widith_of_window = float(input("Enter widith of window in meters:"))
area_of_wall = length_of_wall * widith_of_wall
area_of_window = length_of_window * widith_of_window
wall_that_is_not_window = area_of_wall - area_of_window
gallons_of_paint = wall_that_is_not_window / 3
cost = gallons_of_paint * 20

print(f"""
{name}
You have bought:
{gallons_of_paint} gallons of paint.
The cost is:
${cost}
""")