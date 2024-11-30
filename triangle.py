
side1=int(input("Enter the side 1"))
side2=int(input("Enter the side 2"))
side3=int(input("Enter the side 3"))
def is_right_angled_triangle(side1,side2,side3):
    side=[side1,side2,side3]
    side.sort()
    if side[2]**2==side[0]**2+side[1]**2:
      return True
    return False
if is_right_angled_triangle(side1,side2,side3):
    print(f"The sides are the part of the right angled triangle")
else:
    print(f"the sides are not part of the right angled triangle")
is_right_angled_triangle(side1,side2,side3)