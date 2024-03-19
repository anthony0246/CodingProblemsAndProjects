#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool checkSum(credit_number);

int main(void)
{
    int credit_number;
    do
    {
          credit_number = get_long("What is your credit card number: \n");
    }
    while (credit_number >= 1*pow(10,17) && credit_number <= 1*pow(10,13));  //get user's credit card number

    if (CheckSum(credit_number))
    {
    long american_express_digits = 100000000000000;
    long mastercard_digits = 1000000000000000;
    long visa_digits = 1000000000000;
    long calculation_american_express = credit_number - (credit_number % (american_express_digits/10));
    long calculation_mastercard = credit_number - (credit_number % (mastercard_digits/10));
        //check which provider the credit car number belongs too, based on length:
        //(mastercard = 16 digits, beginning with a 5), 
        //(american express = 14 digits, beginning with a 34 or 37),
        //(visa = 15 digits, beginning with a 4)
        if (calculation_mastercard == 5.1*(pow(10, 15)) || calculation_mastercard == 5.2*(pow(10, 15)) || calculation_mastercard == 5.3*(pow(10, 15)) || calculation_mastercard == 5.4*(pow(10, 15)) || calculation_mastercard == 5.5*(pow(10, 15)))
          {
          if (credit_number % (mastercard_digits/10) < 1.0000000000000001*pow(10,16) || credit_number % (mastercard_digits/10) > 0.9999999999999999*pow(10,15))
               {
                    printf("You have a mastercard credit card.\n");
               }
          }
         else if (calculation_american_express == 3.4*pow(10,14)|| calculation_american_express == 3.7*pow(10,14))
          {
               if (credit_number % american_express_digits < 1.000000000000001*pow(10,15) || credit_number % american_express_digits > 0.99999999999999*pow(10,14))
               {
               printf("You have an american express credit card.\n");
               }
          }
         else if (credit_number - (credit_number % (visa_digits*1000)) == 4*pow(10,15) || credit_number - (credit_number % (visa_digits*100)) == 4*pow(10,15) || credit_number - (credit_number % (visa_digits*10)) == 4*pow(10,15) || credit_number - (credit_number % (visa_digits)) == 4*pow(10,15))
               {
                    printf("You have a visa credit card.\n");
               }
         else
               {
                    printf("Invalid credit card number.\n");
               }
     }
     else
     {
          printf("Invalid credit card number.\n");
     }
}

bool CheckSum(credit_number) 
//verifies if a credit car number is valid,
//Step 1: Take the sum of all the even digits, which have been doubled | sum1
//Step 2: Take the sum of all the odd digits (untouched) | sum2
//Step 3: Take the sum of sum1 and sum2 and see if it is cleanly divisible by 10
{
    int iteration_count = 0;
    int iteration_count2 = 0;
    int first_sum = 0;
    int second_sum = 0;
    for(long i = 100; i < credit_number*10; i *= 100) //Step 1
    {
       long separated_numbers = credit_number % i;
       for(long j = 10; j < credit_number*10; j *= 100)
          {
               j = 10 *(pow(100,iteration_count));
               if (j == 0)
               {
                    j = 10;
               }
               long remainder = separated_numbers % j;
               int individual_numbers = (separated_numbers - remainder) / j;
               individual_numbers *= 2;
               int remainder_sum1 = individual_numbers % 10;
               int first_digit_individual_numbers = individual_numbers/10;
               first_sum += first_digit_individual_numbers + remainder_sum1;
               iteration_count++;
               break;
          }
   }
   for(long s = 10; s < credit_number*10; s *= 100) //Step 2
     {
          long separated_numbers2 = credit_number % s;
          for(long a = 10; a < credit_number*10; a *= 100)
          {
               a = 1*(pow(100, iteration_count2));
               long remainder2 = separated_numbers2 % a;
               if (separated_numbers2 % a == separated_numbers2)
               {
                    remainder2 = 0;
               }
               int individual_numbers2 = (separated_numbers2 - remainder2) / a;
               if (individual_numbers2 < 1)
                    {
                         individual_numbers2 *= 10;
                    }
               second_sum += individual_numbers2;
               iteration_count2++;
               break;
          }
   }
   int final_sum = first_sum + second_sum; //Step 3
    if (final_sum % 10 == 0)
    {
        return true;
    }
    else {
        return false;
    }
}
