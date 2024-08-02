#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

//Verifies if a credit car number is valid.
//Step 1: Take the sum of every other digit (that has been doubled) starting with the second last one.
//Step 2: Take the sum of every other digit starting with the last one. 
//Step 3: Add these two sums together. If the result is cleanly divisible by 10, then the credit card number is valid.
bool isValid(unsigned long long credit_number) {
    unsigned long long previous_value = 0;
    unsigned long long current_digit_s = 0;
    unsigned long long current_value = 0;
    unsigned long long i = 10;
    int total_sum = 0;
    bool even = false;

    while (previous_value != credit_number) {
          current_value = (credit_number) % i;

          current_digit_s = (current_value - previous_value);
          current_digit_s = (current_digit_s * 10) / i;
          current_digit_s *= 2;

          previous_value = current_value;

          if (even) {
               if (current_digit_s >= 10) {
                    total_sum += (1 + current_digit_s % 10);
               }
               else {
                    total_sum += current_digit_s;
               }
          }
          else {
               total_sum += (current_digit_s / 2);
          }
          i *= 10;
          even = !even;
    }

    if (total_sum % 10 == 0) {
          return true;
    }
    return false;
}

//Removes one digit at a time from "credit_number" to determine its number of digits.
int getNumDigits(unsigned long long credit_number) {
     int numDigits = 0;
     while(credit_number > 0) {
          credit_number = credit_number / 10;
          numDigits++;
     }
     return numDigits;
}

int main(void) {
     unsigned long long credit_number;

     printf("Enter a long integer: ");
     scanf("%llu", &credit_number);

     if (isValid(credit_number)) {
          int num_digits = getNumDigits(credit_number);
          int first_digit = 0;
          int first_two_digits = 0;

          for(int i = 0; i < num_digits - 2; i++) {
               credit_number = credit_number / 10;
          }
          first_digit = credit_number / 10;
          first_two_digits = credit_number;

          //Conditions for Visa: 13 or 16 digits | Begins with "4"
          if ((num_digits == 13 || num_digits == 16) && (first_digit == 4)) {
               printf("Visa credit card!");
          }
          //Conditions for MasterCard: 16 digits | Begins with "51", "52", "53", "54" or "55".
          else if ((num_digits == 16) && first_two_digits <= 55 && first_two_digits >= 51) {
                printf("MasterCard credit card!");
          }
          //Conditions for American Express: 15 digits | Begins with "34" or "37"
          else if ((num_digits == 15) && (first_two_digits == 34 || first_two_digits == 37)) {
                printf("American Express credit card!");
          }
          else {
               printf("The credit card has valid digits, but an unrecognisable provider!");
          }
     }
     else {
          printf("Invalid credit card number!");
     }
}