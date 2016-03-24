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
#include <string.h>
#include <ctype.h>

char *str_trim(char *str) {

  char *end;

  while (isspace(*str)) {
    str++;
  }

  if (*str == '\0') {
    return str;
  }

  end = str + strlen(str) - 1;
  while (end > str && isspace(*end)) {
    end--;
  }

  *(end + 1) = '\0';

  return str;
}

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

  int total, which;

  char input[128];

  char *tmp;

  fgets(input, sizeof(input), stdin);

  tmp = str_trim(input);

  sscanf(tmp, "%d %d", &total, &which);

  if (which % 2 == 0) {
    printf("%d\n", (total + 1 - which) / 2 + 1);
  } else {
    printf("%d\n", which / 2 + 1);
  }

  return 0;
}


