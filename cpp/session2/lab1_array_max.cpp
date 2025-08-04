#include <cassert>
#include <iostream>

int findMaxInArray(int arr[], int size) 
{

  int max_value = arr[0];
  if (size <= 0) {
    return -1; // Return -1 for empty array
  } else if (size == 1) {
    return arr[0]; // If only one element, return it as max
  } else if (size == 2) {
    return (arr[0] > arr[1]) ? arr[0] : arr[1]; // Compare two elements
  } else {
    for (int i = 1; i < size; ++i) {
      if (arr[i] > max_value) {
        max_value = arr[i];
      }
    }
  }
  return max_value;
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
