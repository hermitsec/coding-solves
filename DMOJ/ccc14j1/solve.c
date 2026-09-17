#include <stdio.h>

int main () {
  int a,b,c;
  scanf("%d %d %d", &a, &b, &c);


  if (a == b && b == c && a + b + c == 180) {
    printf("Equilateral");
  }

  else if (a+b+c==180) {
    if (a==b || b==c || c==a) {
      printf("Isosceles");
    }
    else {
      printf("Scalene");
    }
  }

  else {
    printf("Error");
  }
  return 0;
}
