#include <stdio.h>

main()
{
    int i, j;
    char x[10], y[10], s;

    do
    {
        printf("Digite uma palavra: ");
        scanf("%s", &x);
        getchar();

        printf("Digite outra palavra: ");
        scanf("%s", &y);
        getchar();

        for (i = 0; x[i] != '\0' || y[i] != '\0'; i++)
        {
            if(x[i] != y[i])
            {
                printf("\nDiferentes\n");
                break;
            }
        }

        if(x[i] == y[i] && x[i] == '\0')
        {
            printf("\nIguais\n");
        }

        printf("\nDeseja continuar (s/n)? ");
        scanf("%c", &s);
        getchar();
        printf("\n");
    } while(s == 's' || s == 'S');
}
