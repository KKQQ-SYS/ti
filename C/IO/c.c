#include<stdio.h>
#include<stdlib.h>

int main(int argc,char* argv[])
{
    int ch;
    FILE* fp;
    unsigned long count = 0;

    if(argc != 2)
    {
        printf("Usage: %s filename\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    if((fp = fopen(argv)))
}