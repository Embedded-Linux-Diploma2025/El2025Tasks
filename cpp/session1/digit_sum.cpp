#include <cassert>
#include <iostream>

int sumDigits(int number) {
  // write your solution here...
  // Hint: Use modulo (%) to get last digit and division (/) to remove last
  // digit Hint: Handle negative numbers appropriately
  int sum{0};
  number = std::abs(number);
  while(number != 0)
  {
    int lastDigit{0};
    lastDigit = number % 10;
    number /= 10;
    sum += lastDigit;
  }
  return sum;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "       DIGIT SUMMATION CALCULATOR\n";
  std::cout << "==============================================\n\n";

  // Test the sumDigits function
  // Test single digit numbers
  assert(sumDigits(0) == 0);
  assert(sumDigits(1) == 1);
  assert(sumDigits(5) == 5);
  assert(sumDigits(9) == 9);

  // Test two digit numbers
  assert(sumDigits(12) == 3);  // 1 + 2 = 3
  assert(sumDigits(23) == 5);  // 2 + 3 = 5
  assert(sumDigits(45) == 9);  // 4 + 5 = 9
  assert(sumDigits(99) == 18); // 9 + 9 = 18

  // Test three digit numbers
  assert(sumDigits(123) == 6);  // 1 + 2 + 3 = 6
  assert(sumDigits(456) == 15); // 4 + 5 + 6 = 15
  assert(sumDigits(789) == 24); // 7 + 8 + 9 = 24
  assert(sumDigits(999) == 27); // 9 + 9 + 9 = 27

  // Test larger numbers
  assert(sumDigits(1234) == 10);  // 1 + 2 + 3 + 4 = 10
  assert(sumDigits(5678) == 26);  // 5 + 6 + 7 + 8 = 26
  assert(sumDigits(12345) == 15); // 1 + 2 + 3 + 4 + 5 = 15
  assert(sumDigits(98765) == 35); // 9 + 8 + 7 + 6 + 5 = 35

  // Test numbers with zeros
  assert(sumDigits(101) == 2);  // 1 + 0 + 1 = 2
  assert(sumDigits(1001) == 2); // 1 + 0 + 0 + 1 = 2
  assert(sumDigits(2050) == 7); // 2 + 0 + 5 + 0 = 7

  // Test negative numbers (should work with absolute value)
  assert(sumDigits(-123) == 6);  // |-123| = 123, 1 + 2 + 3 = 6
  assert(sumDigits(-456) == 15); // |-456| = 456, 4 + 5 + 6 = 15
  assert(sumDigits(-9) == 9);    // |-9| = 9
  assert(sumDigits(-1001) == 2); // |-1001| = 1001, 1 + 0 + 0 + 1 = 2

  // Test edge cases
  assert(sumDigits(1000000) == 1);    // 1 + 0 + 0 + 0 + 0 + 0 + 0 = 1
  assert(sumDigits(111111) == 6);     // 1 + 1 + 1 + 1 + 1 + 1 = 6
  assert(sumDigits(987654321) == 45); // 9+8+7+6+5+4+3+2+1 = 45

  std::cout << "\n\n[✓] All tests passed! Digit summation calculator works "
               "correctly.\n";
  std::cout
      << "Function correctly calculates the sum of all digits in a number.\n";

  return 0;
}
