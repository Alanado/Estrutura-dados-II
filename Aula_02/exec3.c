#include <stdio.h>

int main() {
int numeros[20];
int qtdPares = 0, somaPares = 0;

//
 Leitura dos 20 inteiros
for(int i = 0; i < 20; i++) {
    printf("Digite o valor %d/20: ", i + 1);
    scanf("%d", &numeros[i]);
}

// Processamento
printf("\nNumeros pares encontrados: ");
for(int i = 0; i < 20; i++) {
    if(numeros[i] % 2 == 0) {
        printf("%d ", numeros[i]);
        qtdPares++;
        somaPares += numeros[i];
    }
}

// Exibição do resumo
printf("\nQuantidade de numeros pares: %d\n", qtdPares);
printf("Soma dos numeros pares: %d\n", somaPares);

return 0;


}