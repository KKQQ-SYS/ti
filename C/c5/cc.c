#include <stdio.h>
#include <string.h>
#define NAME "GIGATHINK, INC"
#define ADDRESS "101  MEGABUCK  Plaza"
#define PLACE "Megapolis,  CA  949404"
#define WIDTH  40

void starbar(void) ;
int show_n_char (char ch,int num);

int main()
{
    show_n_char('*',WIDTH);
    
    putchar('\n');

    show_n_char(" ",12);

    printf("%s\n", NAME);
    printf("%s\n", ADDRESS);
    printf("%s\n", PLACE);


    int space = (WIDTH - strlen(ADDRESS))/2;
    show_n_char(' ',space);
    printf("%s\n", ADDRESS);

    space = (WIDTH - strlen(PLACE)) / 2;
    show_n_char(' ',space);
    printf("%s\n", PLACE);
    starbar();

    return 0;
}

void starbar(void)
{
    int count;
    for(count=1; count <= WIDTH; count++)
    {
        putchar('*');
    }

    putchar('\n');

}

int show_n_char(char ch,int num)
{
    int count ;
    for(count = 1; count <= num; count++)
    {
        putchar(ch);
    }
}