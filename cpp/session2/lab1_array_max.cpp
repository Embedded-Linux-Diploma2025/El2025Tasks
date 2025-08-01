#include <cassert>
#include <iostream>
#include <climits>
int findMaxInArray(int arr[], int size) {
  // write your solution here...
  // Hint: Iterate through the array and keep track of the maximum value
  // Hint: Handle edge cases like empty arrays
  int max_val = INT_MIN;

  for (int i = 0; i < size; ++i) {
    max_val = std::max(arr[i], max_val);
  }
  return max_val;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "       ARRAY MAXIMUM FINDER\n";
  std::cout << "==============================================\n\n";

  // Test the findMaxInArray function
  // Test basic arrays
  {
    int arr1[] = {1, 2, 3, 4, 5};
    assert(findMaxInArray(arr1, 5) == 5);
  }

  {
    int arr2[] = {5, 4, 3, 2, 1};
    assert(findMaxInArray(arr2, 5) == 5);
  }

  {
    int arr3[] = {3, 1, 4, 1, 5, 9, 2, 6};
    assert(findMaxInArray(arr3, 8) == 9);
  }

  // Test single element array
  {
    int arr4[] = {42};
    assert(findMaxInArray(arr4, 1) == 42);
  }

  // Test arrays with negative numbers
  {
    int arr5[] = {-1, -2, -3, -4, -5};
    assert(findMaxInArray(arr5, 5) == -1);
  }

  {
    int arr6[] = {-10, -5, -8, -3, -1};
    assert(findMaxInArray(arr6, 5) == -1);
  }

  // Test arrays with mixed positive and negative
  {
    int arr7[] = {-5, 0, 3, -2, 1};
    assert(findMaxInArray(arr7, 5) == 3);
  }

  {
    int arr8[] = {-10, -20, 5, -30};
    assert(findMaxInArray(arr8, 4) == 5);
  }

  // Test arrays with duplicate maximum values
  {
    int arr9[] = {5, 3, 5, 1, 5};
    assert(findMaxInArray(arr9, 5) == 5);
  }

  {
    int arr10[] = {10, 10, 10, 10};
    assert(findMaxInArray(arr10, 4) == 10);
  }

  // Test arrays with zeros
  {
    int arr11[] = {0, 0, 0, 0};
    assert(findMaxInArray(arr11, 4) == 0);
  }

  {
    int arr12[] = {-1, 0, -2};
    assert(findMaxInArray(arr12, 3) == 0);
  }

  // Test larger arrays
  {
    int arr13[] = {100, 50, 200, 75, 150, 25, 300, 125};
    assert(findMaxInArray(arr13, 8) == 300);
  }

  std::cout << "\n\n[✓] All tests passed! Array maximum finder works correctly.\n";
  std::cout << "Function correctly finds the maximum element in arrays.\n";

  return 0;
}
