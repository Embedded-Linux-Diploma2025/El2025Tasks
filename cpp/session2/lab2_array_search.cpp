#include <cassert>
#include <iostream>

int searchInArray(int arr[], int size, int target) {
  if(size == 0)
  {
    //std::cerr <<"size is invalid" << std::endl;
    return -1;
  }
  

  for(int i = 0 ;i<size; i++){
    if (arr[i]==target) return i; 
    return i;
  }
  
  
  // write your solution here...
  // Hint: Iterate through the array and compare each element with target
  // Hint: Return the index if found, return -1 if not found
  return -1;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "       ARRAY SEARCH FUNCTION\n";
  std::cout << "==============================================\n\n";

  // Test the searchInArray function
  // Test basic search cases
  {
    int arr1[] = {1, 2, 3, 4, 5};
    assert(searchInArray(arr1, 5, 3) == 2);  // Found at index 2
    assert(searchInArray(arr1, 5, 1) == 0);  // Found at index 0
    assert(searchInArray(arr1, 5, 5) == 4);  // Found at index 4
    assert(searchInArray(arr1, 5, 6) == -1); // Not found
  }

  // Test search in unsorted array
  {
    int arr2[] = {10, 5, 8, 3, 1};
    assert(searchInArray(arr2, 5, 8) == 2);  // Found at index 2
    assert(searchInArray(arr2, 5, 10) == 0); // Found at index 0
    assert(searchInArray(arr2, 5, 1) == 4);  // Found at index 4
    assert(searchInArray(arr2, 5, 7) == -1); // Not found
  }

  // Test single element array
  {
    int arr3[] = {42};
    assert(searchInArray(arr3, 1, 42) == 0);  // Found at index 0
    assert(searchInArray(arr3, 1, 43) == -1); // Not found
  }

  // Test arrays with negative numbers
  {
    int arr4[] = {-1, -2, -3, -4, -5};
    assert(searchInArray(arr4, 5, -3) == 2);  // Found at index 2
    assert(searchInArray(arr4, 5, -1) == 0);  // Found at index 0
    assert(searchInArray(arr4, 5, 0) == -1);  // Not found
  }

  // Test arrays with duplicates (should return first occurrence)
  {
    int arr5[] = {5, 3, 5, 1, 5};
    assert(searchInArray(arr5, 5, 5) == 0);  // First occurrence at index 0
    assert(searchInArray(arr5, 5, 3) == 1);  // Found at index 1
    assert(searchInArray(arr5, 5, 1) == 3);  // Found at index 3
  }

  // Test arrays with zeros
  {
    int arr6[] = {0, 1, 0, 2, 0};
    assert(searchInArray(arr6, 5, 0) == 0);  // First zero at index 0
    assert(searchInArray(arr6, 5, 1) == 1);  // Found at index 1
    assert(searchInArray(arr6, 5, 2) == 3);  // Found at index 3
  }

  // Test mixed positive and negative
  {
    int arr7[] = {-5, 0, 3, -2, 1};
    assert(searchInArray(arr7, 5, 0) == 1);   // Found at index 1
    assert(searchInArray(arr7, 5, -2) == 3);  // Found at index 3
    assert(searchInArray(arr7, 5, 10) == -1); // Not found
  }

  // Test larger array
  {
    int arr8[] = {100, 50, 200, 75, 150, 25, 300, 125};
    assert(searchInArray(arr8, 8, 200) == 2);  // Found at index 2
    assert(searchInArray(arr8, 8, 25) == 5);   // Found at index 5
    assert(searchInArray(arr8, 8, 999) == -1); // Not found
  }

  // Test empty-like case (size 0)
  {
    int arr9[] = {1, 2, 3};
    assert(searchInArray(arr9, 0, 1) == -1); // Size 0, should not find anything
  }

  std::cout << "\n\n[✓] All tests passed! Array search function works correctly.\n";
  std::cout << "Function correctly searches for elements and returns proper indices.\n";

  return 0;
}
