#include <cassert>
#include <iostream>

void findEvenOdd(int arr[], int size, int even[], int odd[], int* evenCount, int* oddCount) {
  // write your solution here...
  // Hint: Iterate through the array and check if each number is even (num % 2 == 0) or odd
  // Hint: Add even numbers to the even array and odd numbers to the odd array
  // Hint: Update evenCount and oddCount accordingly
  unsigned int even_index{0};
  unsigned int odd_index{0};
  for(int i = 0;i < size;i++)
  {
    if(arr[i] % 2 == 0)
    {
      even[even_index++] = arr[i];
    }
    else
    {
      odd[odd_index++] = arr[i];
    }
  }
  *evenCount = even_index;
  *oddCount = odd_index;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "     EVEN AND ODD NUMBER SEPARATOR\n";
  std::cout << "==============================================\n\n";

  // Test the findEvenOdd function
  // Test basic separation
  {
    int arr[] = {1, 2, 3, 4, 5, 6};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 6, even, odd, &evenCount, &oddCount);

    assert(evenCount == 3);
    assert(oddCount == 3);

    // Even numbers should be: {2, 4, 6}
    assert(even[0] == 2);
    assert(even[1] == 4);
    assert(even[2] == 6);

    // Odd numbers should be: {1, 3, 5}
    assert(odd[0] == 1);
    assert(odd[1] == 3);
    assert(odd[2] == 5);
  }

  // Test all even numbers
  {
    int arr[] = {2, 4, 6, 8, 10};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 5, even, odd, &evenCount, &oddCount);

    assert(evenCount == 5);
    assert(oddCount == 0);

    // Even numbers should be: {2, 4, 6, 8, 10}
    assert(even[0] == 2);
    assert(even[1] == 4);
    assert(even[2] == 6);
    assert(even[3] == 8);
    assert(even[4] == 10);
  }

  // Test all odd numbers
  {
    int arr[] = {1, 3, 5, 7, 9};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 5, even, odd, &evenCount, &oddCount);

    assert(evenCount == 0);
    assert(oddCount == 5);

    // Odd numbers should be: {1, 3, 5, 7, 9}
    assert(odd[0] == 1);
    assert(odd[1] == 3);
    assert(odd[2] == 5);
    assert(odd[3] == 7);
    assert(odd[4] == 9);
  }

  // Test single element (even)
  {
    int arr[] = {4};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 1, even, odd, &evenCount, &oddCount);

    assert(evenCount == 1);
    assert(oddCount == 0);
    assert(even[0] == 4);
  }

  // Test single element (odd)
  {
    int arr[] = {7};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 1, even, odd, &evenCount, &oddCount);

    assert(evenCount == 0);
    assert(oddCount == 1);
    assert(odd[0] == 7);
  }

  // Test with zero (zero is even)
  {
    int arr[] = {0, 1, 2, 3};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 4, even, odd, &evenCount, &oddCount);

    assert(evenCount == 2);
    assert(oddCount == 2);

    // Even numbers should be: {0, 2}
    assert(even[0] == 0);
    assert(even[1] == 2);

    // Odd numbers should be: {1, 3}
    assert(odd[0] == 1);
    assert(odd[1] == 3);
  }

  // Test with negative numbers
  {
    int arr[] = {-4, -3, -2, -1, 0, 1, 2};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 7, even, odd, &evenCount, &oddCount);

    assert(evenCount == 4);
    assert(oddCount == 3);

    // Even numbers should be: {-4, -2, 0, 2}
    assert(even[0] == -4);
    assert(even[1] == -2);
    assert(even[2] == 0);
    assert(even[3] == 2);

    // Odd numbers should be: {-3, -1, 1}
    assert(odd[0] == -3);
    assert(odd[1] == -1);
    assert(odd[2] == 1);
  }

  // Test with duplicates
  {
    int arr[] = {2, 2, 3, 3, 4, 4};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 6, even, odd, &evenCount, &oddCount);

    assert(evenCount == 4);
    assert(oddCount == 2);

    // Even numbers should be: {2, 2, 4, 4}
    assert(even[0] == 2);
    assert(even[1] == 2);
    assert(even[2] == 4);
    assert(even[3] == 4);

    // Odd numbers should be: {3, 3}
    assert(odd[0] == 3);
    assert(odd[1] == 3);
  }

  // Test larger array
  {
    int arr[] = {10, 15, 20, 25, 30, 35, 40, 45, 50};
    int even[10], odd[10];
    int evenCount, oddCount;

    findEvenOdd(arr, 9, even, odd, &evenCount, &oddCount);

    assert(evenCount == 5);
    assert(oddCount == 4);

    // Even numbers should be: {10, 20, 30, 40, 50}
    assert(even[0] == 10);
    assert(even[1] == 20);
    assert(even[2] == 30);
    assert(even[3] == 40);
    assert(even[4] == 50);

    // Odd numbers should be: {15, 25, 35, 45}
    assert(odd[0] == 15);
    assert(odd[1] == 25);
    assert(odd[2] == 35);
    assert(odd[3] == 45);
  }

  std::cout << "\n\n[✓] All tests passed! Even/Odd separator works correctly.\n";
  std::cout << "Function correctly separates even and odd numbers from the array.\n";

  return 0;
}
