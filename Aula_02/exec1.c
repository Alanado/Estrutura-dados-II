#include <stdio.h>

int main() {
int numeros[10];
int soma = 0;

/* STREAMING_CHUNK:Lendo os dados e calculando a soma... */
printf("--- Exercicio 1: Soma e Media ---\n");
for(int i = 0; i < 10; i++) {
    printf("Digite o %do numero: ", i + 1);
    scanf("%d", &numeros[i]);
    soma += numeros[i];
}

/* STREAMING_CHUNK:Imprimindo os numeros digitados... */
printf("\nNumeros digitados: ");
for(int i = 0; i < 10; i++) {
    printf("%d ", numeros[i]);
}

/* STREAMING_CHUNK:Imprimindo a soma e calculando/imprimindo a media... */
printf("\nSoma total: %d", soma);
// Dividimos por 10.0 para garantir que o resultado seja float (com casas decimais)
printf("\nMedia dos valores: %.2f\n", soma / 10.0);

return 0;


}