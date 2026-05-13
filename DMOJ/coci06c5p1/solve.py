cups = input()
b_ball = 1

for c_swaps in cups:
	if c_swaps == 'A' and b_ball == 1:
		b_ball = 2
	elif c_swaps == 'A' and b_ball == 2:
		b_ball = 1
	elif c_swaps == 'B' and b_ball == 2:
		b_ball = 3
	elif c_swaps == 'B' and b_ball == 3:
		b_ball = 2
	elif c_swaps == 'C' and b_ball == 1:
		b_ball = 3
	elif c_swaps == 'C' and b_ball == 3:
		b_ball = 1

print(b_ball)
