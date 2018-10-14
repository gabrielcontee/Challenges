#include <stdio.h>
// #include <strings.h>
#include <string.h>

int main ()
{
    char nome[10000][21];
    int lower[10000];
    int higher[10000];
    int testes;
    int database;
    int query;
    int precos;
    int conta_carro = 0;
    int i = 0;
    int ador = 0;
    int soma_query;
    char saida[100100][25];

    scanf("%d", &testes);


    while (testes != 0)
    {
        scanf("%d", &database);
        for (int cont = 0; cont < database; cont++)
        {
            scanf ("%s %d %d", &nome[cont], &lower[cont], &higher[cont]);
        }
        //printf("\n");
        scanf("%d", &query);
        soma_query += query;

        for (i = 0; i < query; i++)
        {
            scanf("%d", &precos);

            for (int cont = 0; cont < database; cont++)
            {
                if (lower[cont] <= precos && higher[cont] >= precos)
                {
                    conta_carro++;
                    strcpy(saida[ador], nome[cont]);


                    if (conta_carro == 2)
                    {
                        cont = 99999;
                        strcpy(saida[ador], "UNDETERMINED");
                    }
                }
            }
            if (conta_carro == 0)
            strcpy(saida[ador], "UNDETERMINED");

            conta_carro = 0;
            ador++;
            if (i == query - 1)
            {
                ador++;
                strcpy(saida[ador], "BARRAENEQUEBRADELINHA");
                soma_query++;
            }
            
        }

        
        
        testes--;
    }

    for (int cont = 0; cont < soma_query; cont++)
        {
            if (strcmp (saida[cont], "BARRAENEQUEBRADELINHA") == 0) {
                printf("\n");
            }else{
                if (cont == (soma_query - 1)){
                    printf("%s", saida[cont]);
                }else{
                    printf("%s\n", saida[cont]);
                }
                
            }
        }

    return 0;

}
