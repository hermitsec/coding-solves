first_dig = int(input())
second_dig = int(input())
third_dig = int(input())
fourth_dig = int(input())

if ((first_dig == 8 or first_dig == 9) and
	(fourth_dig == 8 or fourth_dig == 9) and
	(second_dig == third_dig)):
	print('ignore')
else:
	print('answer')
