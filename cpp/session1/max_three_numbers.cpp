#include <cassert>
#include <iostream>


int getMaximum(int a, int b, int c) {
  // write your solution here...
  int max=a;
  if (b > max) max = b;
  if (c > max) max = c;
  return max;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "     MAXIMUM OF THREE NUMBERS FINDER\n";
  std::cout << "==============================================\n\n";

  // Test the getMaximum function
  // Test basic cases
  assert(getMaximum(1, 2, 3) == 3);
  assert(getMaximum(3, 2, 1) == 3);
  assert(getMaximum(2, 3, 1) == 3);

  // Test with equal values
  assert(getMaximum(5, 5, 5) == 5);
  assert(getMaximum(10, 10, 8) == 10);
  assert(getMaximum(7, 9, 9) == 9);
  assert(getMaximum(12, 8, 12) == 12);

  // Test with negative numbers
  assert(getMaximum(-1, -2, -3) == -1);
  assert(getMaximum(-10, -5, -8) == -5);
  assert(getMaximum(-1, 0, 1) == 1);

  // Test with zero
  assert(getMaximum(0, 0, 0) == 0);
  assert(getMaximum(-1, 0, 1) == 1);
  assert(getMaximum(5, 0, 3) == 5);

  // Test with larger numbers
  assert(getMaximum(100, 200, 150) == 200);
  assert(getMaximum(999, 1000, 998) == 1000);

  // Test edge cases
  assert(getMaximum(1, 1, 2) == 2);
  assert(getMaximum(2, 1, 1) == 2);
  assert(getMaximum(1, 2, 1) == 2);

  std::cout << "\n\n[✓] All tests passed! Maximum function works correctly.\n";
  std::cout << "Function correctly finds the maximum of three numbers.\n";

  return 0;
}
