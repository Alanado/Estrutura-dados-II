#include <stdio.h>

int main() {
// 4 alunos, 3 notas cada
float notas[4][3];
float soma;

// Leitura dos dados
for(int i = 0; i < 4; i++) {
    printf("\n--- Notas do Aluno %d ---\n", i + 1);
    for(int j = 0; j < 3; j++) {
        printf("Digite a Nota P%d: ", j + 1);
        scanf("%f", &notas[i][j]);
    }
}

// Calculando e apresentando as médias
printf("\n--- Medias Finais ---\n");
for(int i = 0; i < 4; i++) {
    soma = 0;
    for(int j = 0; j < 3; j++) {
        soma += notas[i][j];
    }
    printf("Aluno %d: Media = %.2f\n", i + 1, soma / 3.0);
}

return 0;


}