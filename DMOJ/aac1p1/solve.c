#include <stdio.h>

int main() {
    int x,y;
    scanf("%d %d", &x, &y);
    
    // Areas
    int sqar = x * x;
    float ciar = (y * y) * 3.14;
    
    //Comparison
    if (sqar > ciar) {
        printf("SQUARE");
  }
    else {
        printf("CIRCLE");
  }
    return 0;
}
