bowl_one = int(input())
bowl_two = int(input())
bowl_three = int(input())

if ((bowl_one < bowl_two < bowl_three) or
    (bowl_three < bowl_two < bowl_one)):
	print(bowl_two)

elif ((bowl_one < bowl_three < bowl_two) or
      (bowl_two < bowl_three < bowl_one)):
	print(bowl_three)

else:
	print(bowl_one)
