value_p = int(input())
value_b = int(input())
value_d = int(input())

badge_money = int((value_p / value_b)) * value_d
paint_money = value_p % value_b
total_money = badge_money + paint_money

print (total_money)
