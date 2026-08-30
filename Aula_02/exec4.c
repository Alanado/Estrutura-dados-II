#include <stdio.h>

int main() {
    int vetor[10];
    int i, temp;

    for(i = 0; i < 10; i++) {
        printf("Digite o valor %d: ", i + 1);
        scanf("%d", &vetor[i]);
    }

    // Inversão na mesma variável
    for(i = 0; i < 5; i++) {
        temp = vetor[i];
        vetor[i] = vetor[9 - i];
        vetor[9 - i] = temp;
    }

    printf("\nVetor invertido:\n");
    for(i = 0; i < 10; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
    return 0;
}