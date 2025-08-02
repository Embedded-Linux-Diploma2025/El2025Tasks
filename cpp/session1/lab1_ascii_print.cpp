#include <cassert>
#include <iomanip>
#include <iostream>
#include <string>

int getASCIIValue(char character) {
  int ascii = static_cast<int>(character); 
  return ascii;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "        ASCII TABLE GENERATOR\n";
  std::cout << "==============================================\n\n";

  // Test the createASCIITable function
  // Test basic ASCII values
  assert(getASCIIValue('A') == 65);
  assert(getASCIIValue('a') == 97);
  assert(getASCIIValue('0') == 48);
  assert(getASCIIValue(' ') == 32);
  assert(getASCIIValue('~') == 126);

  // Test special characters
  assert(getASCIIValue('!') == 33);
  assert(getASCIIValue('@') == 64);
  assert(getASCIIValue('#') == 35);
  assert(getASCIIValue('$') == 36);
  assert(getASCIIValue('%') == 37);

  // Test numbers
  assert(getASCIIValue('1') == 49);
  assert(getASCIIValue('9') == 57);

  // Test uppercase letters
  assert(getASCIIValue('Z') == 90);
  assert(getASCIIValue('B') == 66);

  // Test lowercase letters
  assert(getASCIIValue('z') == 122);
  assert(getASCIIValue('b') == 98);
  std::cout << "\n\n[✓] All tests passed! ASCII values should be correct.\n";

  return 0;
}