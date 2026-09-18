#include <stdio.h>

int main(void) {
  int ant, eye;
  scanf("%d %d", &ant, &eye);

  if (ant >= 3 && eye <= 4) {
    printf("TroyMartian\n");
  }

  if (ant <= 6 && eye >= 2) {
    printf("VladSaturnian\n");
  }

  if (ant <= 2 && eye <= 3) {
    printf("GraemeMercurian\n");
  }

  else {
    printf("");
  }

  return 0;
}
