user_input = input()

if (user_input.count(':-)') == 0 and  user_input.count(':-(') == 0):
        print('none')

elif (user_input.count(':-)') > user_input.count(':-(')):
	print('happy')

elif (user_input.count(':-)') <  user_input.count(':-(')):
	print('sad')

elif (user_input.count(':-)') == user_input.count(':-(')):
	print('unsure')

else:
	print('none')
