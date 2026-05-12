input_width = int(input())
input_cheese = int(input())

if (input_width == 1 and input_cheese <= 50):
	cc_sat = 'fairly'

elif (input_width == 3 and input_cheese >= 95):
	cc_sat = 'absolutely'

else:
	cc_sat = 'very'


print('C.C. is ' + cc_sat + ' satisfied with her pizza.')


