#include <stdio.h>
#include <math.h>

int main(void) {
  int x;
  scanf("%d", &x);

  int square = sqrt(x);
  printf("The largest square has side length %d.", square);

  return 0;
}
