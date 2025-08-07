#include <cassert>
#include <iostream>

int mergeArrays(int arr1[], int size1, int arr2[], int size2, int result[]) {
  // if(size1==0 || size2==0){
  //   return -1 ;
  // }
  int index=0;

  for (index ; index<size1;index++){
    result[index] = arr1[index];
  }
  for (int i=0;i<size2;i++){
    result[index]=arr2[i];
    index++;
  }
 
  // write your solution here...
  // Hint: Copy all elements from arr1 to result, then copy all elements from arr2
  // Hint: Return the total size of the merged array (size1 + size2)
  return size1+size2;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "       ARRAY MERGE FUNCTION\n";
  std::cout << "==============================================\n\n";

  // Test the mergeArrays function
  // Test basic merge
  {
    int arr1[] = {1, 2, 3};
    int arr2[] = {4, 5, 6};
    int result[10];
    int newSize = mergeArrays(arr1, 3, arr2, 3, result);
    assert(newSize == 6);
    // Result should be: {1, 2, 3, 4, 5, 6}
    assert(result[0] == 1);
    assert(result[1] == 2);
    assert(result[2] == 3);
    assert(result[3] == 4);
    assert(result[4] == 5);
    assert(result[5] == 6);
  }

  // Test merging arrays of different sizes
  {
    int arr1[] = {10, 20};
    int arr2[] = {30, 40, 50, 60};
    int result[10];
    int newSize = mergeArrays(arr1, 2, arr2, 4, result);
    assert(newSize == 6);
    // Result should be: {10, 20, 30, 40, 50, 60}
    assert(result[0] == 10);
    assert(result[1] == 20);
    assert(result[2] == 30);
    assert(result[3] == 40);
    assert(result[4] == 50);
    assert(result[5] == 60);
  }

  // Test merging with empty first array
  {
    int arr1[] = {};
    int arr2[] = {1, 2, 3};
    int result[10];
    int newSize = mergeArrays(arr1, 0, arr2, 3, result);
    assert(newSize == 3);
    // Result should be: {1, 2, 3}
    assert(result[0] == 1);
    assert(result[1] == 2);
    assert(result[2] == 3);
  }

  // Test merging with empty second array
  {
    int arr1[] = {5, 10, 15};
    int arr2[] = {};
    int result[10];
    int newSize = mergeArrays(arr1, 3, arr2, 0, result);
    assert(newSize == 3);
    // Result should be: {5, 10, 15}
    assert(result[0] == 5);
    assert(result[1] == 10);
    assert(result[2] == 15);
  }

  // Test merging single element arrays
  {
    int arr1[] = {100};
    int arr2[] = {200};
    int result[10];
    int newSize = mergeArrays(arr1, 1, arr2, 1, result);
    assert(newSize == 2);
    // Result should be: {100, 200}
    assert(result[0] == 100);
    assert(result[1] == 200);
  }

  // Test merging arrays with negative numbers
  {
    int arr1[] = {-1, -2};
    int arr2[] = {-3, -4, -5};
    int result[10];
    int newSize = mergeArrays(arr1, 2, arr2, 3, result);
    assert(newSize == 5);
    // Result should be: {-1, -2, -3, -4, -5}
    assert(result[0] == -1);
    assert(result[1] == -2);
    assert(result[2] == -3);
    assert(result[3] == -4);
    assert(result[4] == -5);
  }

  // Test merging arrays with mixed positive and negative
  {
    int arr1[] = {-5, 0, 5};
    int arr2[] = {-10, 10};
    int result[10];
    int newSize = mergeArrays(arr1, 3, arr2, 2, result);
    assert(newSize == 5);
    // Result should be: {-5, 0, 5, -10, 10}
    assert(result[0] == -5);
    assert(result[1] == 0);
    assert(result[2] == 5);
    assert(result[3] == -10);
    assert(result[4] == 10);
  }

  // Test merging arrays with duplicates
  {
    int arr1[] = {1, 2, 2};
    int arr2[] = {2, 3, 3};
    int result[10];
    int newSize = mergeArrays(arr1, 3, arr2, 3, result);
    assert(newSize == 6);
    // Result should be: {1, 2, 2, 2, 3, 3}
    assert(result[0] == 1);
    assert(result[1] == 2);
    assert(result[2] == 2);
    assert(result[3] == 2);
    assert(result[4] == 3);
    assert(result[5] == 3);
  }

  // Test merging both empty arrays
  {
    int arr1[] = {};
    int arr2[] = {};
    int result[10];
    int newSize = mergeArrays(arr1, 0, arr2, 0, result);
    assert(newSize == 0);
    // Result should be empty
  }

  std::cout << "\n\n[✓] All tests passed! Array merge function works correctly.\n";
  std::cout << "Function correctly merges two arrays into one.\n";

  return 0;
}