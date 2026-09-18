#include <stdio.h>

int main(void) {
  int sp_limit,od_speed;
  scanf("%d %d", &sp_limit, &od_speed);
  int sp_diff = od_speed - sp_limit;

  if (sp_diff <= 20 && sp_diff > 0 ) {
    printf("You are speeding and your fine is $100.");
  }

  else if (sp_diff >= 21 && sp_diff <= 30) {
    printf("You are speeding and your fine is $270.");
  }

  else if (sp_diff >= 31) {
    printf("You are speeding and your fine is $500.");
  }

  else {
    printf("Congratulations, you are within the speed limit!");
  }

  return 0;
}
