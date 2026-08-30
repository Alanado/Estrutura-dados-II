#include <stdio.h>

int main() {
int numeros[10];
int maior, menor, posMaior = 0, posMenor = 0;

// Leitura dos dados
for(int i = 0; i < 10; i++) {
    printf("Digite o valor %d: ", i + 1);
    scanf("%d", &numeros[i]);

    // Inicializa maior e menor com o primeiro elemento
    if(i == 0) {
        maior = numeros[i];
        menor = numeros[i];
    } else {
        // Verifica se é o novo maior
        if(numeros[i] > maior) {
            maior = numeros[i];
            posMaior = i;
        }
        // Verifica se é o novo menor
        if(numeros[i] < menor) {
            menor = numeros[i];
            posMenor = i;
        }
    }
}

// Exibição dos resultados
printf("\nMaior valor: %d (Encontrado na posicao %d do vetor)\n", maior, posMaior);
printf("Menor valor: %d (Encontrado na posicao %d do vetor)\n", menor, posMenor);

return 0;


}