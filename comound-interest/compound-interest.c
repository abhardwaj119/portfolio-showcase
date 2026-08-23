#include <stdio.h>
#include <math.h>

int main() {

    double principal = 0.0;
    double rate = 0.0;
    int years = 0;
    int times_compounded = 0;
    double total = 0;

    printf("Enter the principal: ");
    scanf("%lf", &principal);

    printf("Enter the rate: ");
    scanf("%lf", &rate);
    rate /= 100;

    printf("Enter the number of years: ");
    scanf("%d", &years);

    printf("Enter the number of times interest is compounded per year: ");
    scanf("%d", &times_compounded);

    total = principal * pow(1 + rate/times_compounded, times_compounded*years);

    printf("After %d years the total will be $%.2lf", years, total);

    return 0;
}