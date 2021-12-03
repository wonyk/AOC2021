#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Code mainly from the main Linux Man page
int main(void)
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    const int SIZE = 12;
    int binary[SIZE];
    char result[SIZE];

    for (int i = 0; i < SIZE; i++)
    {
        binary[i] = 0;
    }

    fp = fopen("input.txt", "r");
    if (fp == NULL)
    {
        exit(EXIT_FAILURE);
    }

    while ((read = getline(&line, &len, fp)) != -1)
    {
        for (int i = 0; i < strlen(line); i++)
        {
            if (line[i] == '1')
            {
                binary[i]++;
                continue;
            }
            binary[i]--;
        }
    }

    for (int i = 0; i < SIZE; i++)
    {
        if (binary[i] < 0)
        {
            result[i] = '0';
        }
        else
        {
            result[i] = '1';
        }
    }

    int gamma = 0;
    int epsilon = 0;

    for (int i = SIZE - 1; i >= 0; i--)
    {
        if (result[i] == '1')
        {
            gamma += pow(2, SIZE - i - 1);
        }
        else
        {
            epsilon += pow(2, SIZE - i - 1);
        }
    }

    printf("Gamma: %d, Epsilon: %d, Final result: %d", gamma, epsilon, gamma * epsilon);

    free(line);
    exit(EXIT_SUCCESS);
}