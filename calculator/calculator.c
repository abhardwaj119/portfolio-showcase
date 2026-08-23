#include <stdio.h>

int main() {

    double num1 = 0.0;
    double num2 = 0.0;
    char op = '\0';
    double result = 0.0;

    printf("Enter a number: ");
    scanf("%lf", &num1);

    printf("Enter an operator: ");
    scanf(" %c", &op);

    printf("Enter another number: ");
    scanf("%lf", &num2);

    switch (op) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 == 0) {
                printf("Error: Division by zero!!");
                return 1;
            } else {
                result = num1 / num2;
                break;
            }
        default:
            printf("Please enter a valid operator..");
            return 1;
    }

    printf("%lf", result);

    return 0;
}