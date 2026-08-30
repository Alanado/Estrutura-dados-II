#include <stdio.h>

int main() {
    int matriz[4][4];
    int soma = 0;

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            printf("Digite o valor para [%d][%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
        }
    }

    printf("\nDiagonal Principal: ");
    for(int i = 0; i < 4; i++) {
        printf("%d ", matriz[i][i]);
        soma += matriz[i][i];
    }
    
    printf("\nSoma da diagonal: %d\n", soma);
    return 0;
}