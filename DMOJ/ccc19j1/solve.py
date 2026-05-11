three_pt_a = int(input()) * 3
two_pt_a = int(input()) * 2
one_pt_a = int(input())

three_pt_b = int(input()) * 3
two_pt_b = int(input()) * 2
one_pt_b = int(input())

total_a = three_pt_a + two_pt_a + one_pt_a
total_b = three_pt_b + two_pt_b + one_pt_b

if total_a > total_b:
	print('A')
elif total_b > total_a:
	print('B')
else:
	print('T')

