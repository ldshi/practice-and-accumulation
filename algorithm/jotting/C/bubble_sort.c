#include <stdio.h>

int main() {

  int arr[11] = {94, 54, 67, 76, 32, 23, 8, 65, 90, 8, 6};

  int i, j;
  for (i = 0; i < 10; i++) {
    for (j = i + 1; j < 11; j++) {
      if (arr[i] > arr[j]) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
      }
    }
  }

  for (i = 0; i < 11; i++) {
    printf("%d\n", arr[i]);
  }

  return 0;
}


