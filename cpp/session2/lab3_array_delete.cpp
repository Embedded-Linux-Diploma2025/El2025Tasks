#include <cassert>
#include <iostream>

int deleteFromArray(int arr[], int size, int target) {
  // write your solution here...
  // Hint: Find  first occurance of the target element and shift all elements after it to the left
  // Hint: Return the new size of the array after deletion
  // Hint: If target not found, return original size
  if (size <= 0) {
    std::cerr << "Error: Array is empty.\n";   
  }
  else
  {
    int i = 0;
    while (i < size) {
      if (arr[i] == target) {
        // Shift elements to the left
        for (int j = i; j < size - 1; ++j) {
          arr[j] = arr[j + 1];
        }
        --size; // Decrease size
        //continue; // Stay at the same index
        break;
      }
      ++i;
    }
  }  
  return size;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "       ARRAY DELETE FUNCTION\n";
  std::cout << "==============================================\n\n";

  // Test the deleteFromArray function
  // Test basic deletion
  {
    int arr1[] = {1, 2, 3, 4, 5};
    int newSize = deleteFromArray(arr1, 5, 3);
    assert(newSize == 4);
    // Array should now be: {1, 2, 4, 5}
    assert(arr1[0] == 1);
    assert(arr1[1] == 2);
    assert(arr1[2] == 4);
    assert(arr1[3] == 5);
  }

  // Test deleting first element
  {
    int arr2[] = {10, 20, 30, 40};
    int newSize = deleteFromArray(arr2, 4, 10);
    assert(newSize == 3);
    // Array should now be: {20, 30, 40}
    assert(arr2[0] == 20);
    assert(arr2[1] == 30);
    assert(arr2[2] == 40);
  }

  // Test deleting last element
  {
    int arr3[] = {5, 10, 15, 20};
    int newSize = deleteFromArray(arr3, 4, 20);
    assert(newSize == 3);
    // Array should now be: {5, 10, 15}
    assert(arr3[0] == 5);
    assert(arr3[1] == 10);
    assert(arr3[2] == 15);
  }

  // Test deleting from single element array
  {
    int arr4[] = {42};
    int newSize = deleteFromArray(arr4, 1, 42);
    assert(newSize == 0);
    // Array is now empty
  }

  // Test element not found
  {
    int arr5[] = {1, 2, 3, 4, 5};
    int original[] = {1, 2, 3, 4, 5}; // Keep original for comparison
    int newSize = deleteFromArray(arr5, 5, 10);
    assert(newSize == 5); // Size should remain the same
    // Array should remain unchanged
    for (int i = 0; i < 5; i++) {
      assert(arr5[i] == original[i]);
    }
  }

  // Test deleting from array with duplicates (should delete first occurrence)
  {
    int arr6[] = {5, 3, 5, 1, 5};
    int newSize = deleteFromArray(arr6, 5, 5);
    assert(newSize == 4);
    // Array should now be: {3, 5, 1, 5} (first 5 removed)
    assert(arr6[0] == 3);
    assert(arr6[1] == 5);
    assert(arr6[2] == 1);
    assert(arr6[3] == 5);
  }

  // Test deleting negative numbers
  {
    int arr7[] = {-1, -2, -3, -4};
    int newSize = deleteFromArray(arr7, 4, -2);
    assert(newSize == 3);
    // Array should now be: {-1, -3, -4}
    assert(arr7[0] == -1);
    assert(arr7[1] == -3);
    assert(arr7[2] == -4);
  }

  // Test deleting zero
  {
    int arr8[] = {0, 1, 0, 2, 0};
    int newSize = deleteFromArray(arr8, 5, 0);
    assert(newSize == 4);
    // Array should now be: {1, 0, 2, 0} (first 0 removed)
    assert(arr8[0] == 1);
    assert(arr8[1] == 0);
    assert(arr8[2] == 2);
    assert(arr8[3] == 0);
  }

  // Test deleting from larger array
  {
    int arr9[] = {100, 50, 200, 75, 150, 25};
    int newSize = deleteFromArray(arr9, 6, 75);
    assert(newSize == 5);
    // Array should now be: {100, 50, 200, 150, 25}
    assert(arr9[0] == 100);
    assert(arr9[1] == 50);
    assert(arr9[2] == 200);
    assert(arr9[3] == 150);
    assert(arr9[4] == 25);
  }

  std::cout << "\n\n[✓] All tests passed! Array delete function works correctly.\n";
  std::cout << "Function correctly removes elements and shifts remaining elements.\n";

  return 0;
}
