#include <stdio.h>

struct Aluno {
char nome[50];
int idade;
float notas[3];
};

int main() {
struct Aluno turma[5];
int aprovados = 0, reprovados = 0, idMaiorMedia = 0;
float maiorMedia = -1;

// Cadastro da Turma
printf("--- Cadastro da Turma ---\n");
for(int i = 0; i < 5; i++) {
    printf("\nAluno %d:\n", i + 1);
    printf("Nome: ");
    scanf(" %[^\n]", turma[i].nome);
    printf("Idade: ");
    scanf("%d", &turma[i].idade);
    
    for(int j = 0; j < 3; j++) {
        printf("Nota %d: ", j + 1);
        scanf("%f", &turma[i].notas[j]);
    }
}

printf("\n--- Classificacao Final ---\n");
for(int i = 0; i < 5; i++) {
    // Cálculo da média
    float media = (turma[i].notas[0] + turma[i].notas[1] + turma[i].notas[2]) / 3.0;
    
    printf("Aluno: %s | Media: %.2f | Status: ", turma[i].nome, media);
    
    if(media >= 7.0) {
        printf("Aprovado\n");
        aprovados++;
    } else {
        printf("Reprovado\n");
        reprovados++;
    }

    // Verifica a maior média
    if(media > maiorMedia) {
        maiorMedia = media;
        idMaiorMedia = i;
    }
}

// Relatório final
printf("\n--- Resumo ---\n");
printf("Total de Aprovados: %d\n", aprovados);
printf("Total de Reprovados: %d\n", reprovados);
printf("Aluno com a Maior Media: %s (Media: %.2f)\n", turma[idMaiorMedia].nome, maiorMedia);

return 0;


}