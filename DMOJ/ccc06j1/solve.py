burg_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dess_choice = int(input())

if burg_choice == 1:
	burg_choice = 461
elif burg_choice == 2:
	burg_choice = 431
elif burg_choice == 3:
	burg_choice = 420
else:
	burg_choice = 0


if side_choice == 1:
        side_choice = 100
elif side_choice == 2:
        side_choice = 57
elif side_choice == 3:
        side_choice = 70
else:
        side_choice = 0


if drink_choice == 1:
        drink_choice = 130
elif drink_choice == 2:
        drink_choice = 160
elif drink_choice == 3:
        drink_choice = 118
else:
        drink_choice = 0


if dess_choice == 1:
        dess_choice = 167
elif dess_choice == 2:
        dess_choice = 266
elif dess_choice == 3:
        dess_choice = 75
else:
        dess_choice = 0

total_cals = str(burg_choice + side_choice + drink_choice + dess_choice)
print("Your total Calorie count is " + total_cals + ".")
