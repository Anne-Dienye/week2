#coding
sweets = int(input("How many sweets are in the tub? "))
pupils = int(input("How many pupils are attending? "))

sweets_per_pupil = sweets // pupils
leftover_sweets = sweets % pupils

# Grammar adjustment for singular/plural pupils
pupil_word = "pupil" if pupils == 1 else "pupils"

print(f"Each {pupil_word} will receive {sweets_per_pupil} sweets, with {leftover_sweets} sweet(s) left over.")