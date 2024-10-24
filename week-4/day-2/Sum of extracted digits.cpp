#include <iostream>
using namespace std;

// Function to extract the second last digit
int extractSecondLastDigit(long long number) {
    // Check if the number has fewer than 2 digits
    if (number < 10) {
        return -1;  // Indicate invalid number
    }
    // Remove the last digit
    number /= 10;
    // Extract the new last digit which is the second last digit of the original number
    return number % 10;
}

int main() {
    long long num1, num2;

    // Take input from user
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    // Extract the second last digit from each number
    int digit1 = extractSecondLastDigit(num1);
    int digit2 = extractSecondLastDigit(num2);

    // Check if either of the numbers was invalid
    if (digit1 == -1 || digit2 == -1) {
        cout << "Invalid number" << endl;
    } else {
        // Print the sum of the second last digits
        cout << (digit1 + digit2) << endl;
    }

    return 0;
}
