#include <cassert>
#include <iostream>
#include <algorithm>
#include <string>
#include <cctype>

bool isVowel(char letter) {
  // Professional C++ solution using std::find and std::tolower
  static const std::string vowels = "aeiou";
  return std::find(vowels.begin(), vowels.end(), std::tolower(letter)) != vowels.end();
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "         VOWEL CHECKER\n";
  std::cout << "==============================================\n\n";

  // Test the isVowel function
  // Test lowercase vowels
  assert(isVowel('a') == true);
  assert(isVowel('e') == true);
  assert(isVowel('i') == true);
  assert(isVowel('o') == true);
  assert(isVowel('u') == true);

  // Test uppercase vowels
  assert(isVowel('A') == true);
  assert(isVowel('E') == true);
  assert(isVowel('I') == true);
  assert(isVowel('O') == true);
  assert(isVowel('U') == true);

  // Test lowercase consonants
  assert(isVowel('b') == false);
  assert(isVowel('c') == false);
  assert(isVowel('d') == false);
  assert(isVowel('f') == false);
  assert(isVowel('g') == false);
  assert(isVowel('h') == false);
  assert(isVowel('j') == false);
  assert(isVowel('k') == false);
  assert(isVowel('l') == false);
  assert(isVowel('m') == false);
  assert(isVowel('n') == false);
  assert(isVowel('p') == false);
  assert(isVowel('q') == false);
  assert(isVowel('r') == false);
  assert(isVowel('s') == false);
  assert(isVowel('t') == false);
  assert(isVowel('v') == false);
  assert(isVowel('w') == false);
  assert(isVowel('x') == false);
  assert(isVowel('y') == false);
  assert(isVowel('z') == false);

  // Test uppercase consonants
  assert(isVowel('B') == false);
  assert(isVowel('C') == false);
  assert(isVowel('D') == false);
  assert(isVowel('F') == false);
  assert(isVowel('G') == false);
  assert(isVowel('H') == false);
  assert(isVowel('J') == false);
  assert(isVowel('K') == false);
  assert(isVowel('L') == false);
  assert(isVowel('M') == false);
  assert(isVowel('N') == false);
  assert(isVowel('P') == false);
  assert(isVowel('Q') == false);
  assert(isVowel('R') == false);
  assert(isVowel('S') == false);
  assert(isVowel('T') == false);
  assert(isVowel('V') == false);
  assert(isVowel('W') == false);
  assert(isVowel('X') == false);
  assert(isVowel('Y') == false);
  assert(isVowel('Z') == false);

  // Test non-letter characters
  assert(isVowel('1') == false);
  assert(isVowel('2') == false);
  assert(isVowel('!') == false);
  assert(isVowel('@') == false);
  assert(isVowel('#') == false);
  assert(isVowel(' ') == false);
  assert(isVowel('.') == false);
  assert(isVowel(',') == false);

  std::cout << "\n\n[✓] All tests passed! Vowel checker works correctly.\n";
  std::cout << "Function correctly identifies vowels (a, e, i, o, u) in both "
               "uppercase and lowercase.\n";

  return 0;
}
