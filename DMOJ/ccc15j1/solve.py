user_month = int(input())
user_day = int(input())

ccc_month = 2
ccc_day = 18

if ((0 < user_month < 13) and
    (0 < user_day < 32) and
    (user_month == ccc_month and user_day < ccc_day) or
    (user_month < ccc_month)):
	print('Before')

elif ((0 < user_month < 13) and
      (0 < user_day < 32) and
      (user_month == ccc_month and user_day > ccc_day) or
      (user_month > ccc_month)):
	print('After')

elif ((user_month == ccc_month) and
      (user_day == ccc_day)):
	print('Special')

else:
	print('Invalid')
