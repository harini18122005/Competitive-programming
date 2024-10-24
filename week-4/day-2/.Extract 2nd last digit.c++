#include <iostream>
using namespace std;

int main() {
    long long number;
    
    // Take input from user
    cout << "Enter a number: ";
    cin >> number;
    
    // Check if the number has fewer than 2 digits
    if (number < 10) {
        cout << "Invalid number" << endl;
    } else {
        // Extract the second last digit
        // Get the last digit by taking modulo 10
        int lastDigit = number % 10;
        // Remove the last digit by integer division
        number /= 10;
        // The new last digit is the second last digit of the original number
        int secondLastDigit = number % 10;
        
        cout << secondLastDigit << endl;
    }
    
    return 0;
}
