#include <stdio.h>

int main() {
    int rows, i, j, spaces;

    printf("Enter number of rows: ");
    scanf("%d", &rows);

    // Upper part of the rhombus
    for (i = 1; i <= rows; i++) {
        // Print leading spaces
        for (spaces = 1; spaces <= rows - i; spaces++) {
            printf(" ");
        }
        // Print stars
        for (j = 1; j <= rows; j++) {
            printf("* ");
        }
        printf("\n");
    }

    // Lower part of the rhombus
    for (i = rows - 1; i >= 1; i--) {
        // Print leading spaces
        for (spaces = 1; spaces <= rows - i; spaces++) {
            printf(" ");
        }
        // Print stars
        for (j = 1; j <= rows; j++) {
            printf("* ");
        }
        printf("\n");
    }

    return 0;
}
