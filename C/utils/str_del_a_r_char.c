/*
 * This method is for deleting the specified repeated adjacent character INSIDE a string(only keep one).
 */

/*
 * Compiler info given out by 'gcc --version':
 *   Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
 *   Apple LLVM version 7.0.2 (clang-700.1.81)
 *   Target: x86_64-apple-darwin15.0.0
 *   Thread model: posix
 */

#include <stdio.h>

int str_del_a_r_char(char *str, char ch) {

  char *p = str, *q = str;

  int counter = 0, tmp = 0;

  while (*q) {
    if (*q != ch) {
      *p++ = *q;
      tmp = 0;
    } else if (*q == ch) {
      if (tmp == 0) {
        tmp++;
        *p++ = *q;
      } else {
        counter++;
      }
    } else {
      counter++;
    }
    q++;
  }

  *p = '\0';

  return counter;
}

int main() {

  char str_0[] = "I am working at    Singapore.";

  str_del_a_r_char(str_0, ' ');

  printf("%s\n", str_0);

}


