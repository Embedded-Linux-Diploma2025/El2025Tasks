#include <iostream>

int mergeArrays(int arr1[], int size1, int arr2[], int size2, int result[]) {
  // write your solution here...
  // Hint: Copy all elements from arr1 to result, then copy all elements from arr2
  // Hint: Return the total size of the merged array (size1 + size2)
  int newSize = 0;
  if(size1 > 0 && size2 > 0)
  {
    std::cout << "Merging two non-empty arrays.\n";
    newSize = size1 + size2;
    for(int i = 0; i < size1; i++)
    {
      result[i] = arr1[i];
    }
    for(int i = 0; i < size2; i++)
    {
      result[i+ size1] = arr2[i];
    }
    return newSize;
  }
  else if (size1 > 0 && size2 <= 0) 
  {
    std::cout << "Merging first non-empty array with an empty second array.\n";
    newSize += size1;
    for(int i = 0; i < size1; i++)
    {
      result[i] = arr1[i];
    }
    return newSize;
  }
  else if (size2 > 0 && size1 <= 0) 
  {
    std::cout << "Merging second non-empty array with an empty first array.\n";
    newSize = newSize + size2;
    for(int i = 0; i < size2; i++)
    {
      result[i] = arr2[i];
    }
    return newSize;
  }
  return 0;
}

int main() {

  int arr1[] = {};
  int arr2[] = {4, 5, 6};
  int result[10];
  int newSize = mergeArrays(arr1, 0, arr2, 3, result);

  std::cout << newSize << std::endl; // Should print 6

  return 0;
}