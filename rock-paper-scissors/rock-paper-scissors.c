#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

int getUserChoice();
int getComputerChoice();
void checkWinner(int, int);

int main() {

    srand(time(NULL));

    printf("Welcome to Rock-Paper-Scissors!!\n");

    int userChoice = getUserChoice();
    int computerChoice = getComputerChoice();

    checkWinner(userChoice, computerChoice);

    return 0;
}

int getUserChoice() {
    int ch = 0;

    do {
        printf("1. Rock\n");
        printf("2. Paper\n");
        printf("3. Scisors\n");

        printf("Enter your choice: ");
        scanf("%d", &ch);
    } while (ch < 1 || ch > 3);

    switch (ch)
    {
    case 1:
        printf("You chose Rock!\n");
        break;
    
    case 2:
        printf("You chose Paper!\n");
        break;

    case 3:
        printf("You chose Scissors!\n");
        break;
    }

    return ch;
}

int getComputerChoice() {
    int ch = (rand() % 3) + 1;

    switch (ch)
    {
    case 1:
        printf("Computer chose Rock!\n");
        break;
    
    case 2:
        printf("Computer chose Paper!\n");
        break;

    case 3:
        printf("Computer chose Scissors!\n");
        break;
    }

    return ch;
}

void checkWinner(int userChoice, int computerChoice) {

    bool win = (userChoice == 1 && computerChoice == 3) || (userChoice == 2 && computerChoice == 1) || (userChoice == 3 && computerChoice == 2);
    
    if (userChoice == computerChoice) {
        printf("It's a draw..");
    } else if (win) {
        printf("You won!!");
    } else {
        printf("You lost :(");
    }

}