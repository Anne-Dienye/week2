#coding
students = int(input("How many students? "))
group_size = int(input("Required group size? "))

groups = students // group_size
leftover = students % group_size

# Grammar adjustment for singular/plural leftovers
leftover_word = "student" if leftover == 1 else "students"

print(f"There will be {groups} groups with {leftover} {leftover_word} left over.")