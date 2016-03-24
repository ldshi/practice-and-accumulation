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

int main() {

  char str_0[] = "       ";
  char str_1[] = "  I am working at Singapore.    ";
  char str_2[] = " I am working at     Singapore.";
  char str_3[] = "I am working at Singapore.";

  printf("%s\n", str_trim(str_0));
  printf("%s\n", str_trim(str_1));
  printf("%s\n", str_trim(str_2));
  printf("%s\n", str_trim(str_3));

  return 0;
}


