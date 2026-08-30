#include <stdio.h>
#include <string.h>

struct Funcionario {
    char nome[50];
    int idade;
    char cargo[50];
    float salario;
};

int main() {
    struct Funcionario funcs[10];
    int opcao, totalCadastrados = 0;
    float somaSalarios = 0, mediaSalarial = 0;

    do {
        printf("\n=================================\n");
        printf("       SISTEMA DE FUNCIONARIOS\n");
        printf("=================================\n");
        printf("1 - Cadastrar funcionarios (Total: %d/10)\n", totalCadastrados);
        printf("2 - Listar funcionarios\n");
        printf("3 - Maior salario\n");
        printf("4 - Media salarial\n");
        printf("5 - Salarios acima da media\n");
        printf("0 - Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        if(opcao == 1 && totalCadastrados < 10) {
            printf("Nome: ");
            scanf(" %[^\n]s", funcs[totalCadastrados].nome);
            printf("Idade: ");
            scanf("%d", &funcs[totalCadastrados].idade);
            printf("Cargo: ");
            scanf(" %[^\n]s", funcs[totalCadastrados].cargo);
            printf("Salario: ");
            scanf("%f", &funcs[totalCadastrados].salario);
            totalCadastrados++;
            printf("Cadastrado com sucesso!\n");
        } 
        else if (opcao == 2) {
            for(int i = 0; i < totalCadastrados; i++) {
                printf("\nNome: %s | Cargo: %s | Salario: R$%.2f", funcs[i].nome, funcs[i].cargo, funcs[i].salario);
            }
        }
        else if (opcao == 3) {
            if(totalCadastrados == 0) continue;
            int idMaior = 0;
            for(int i = 1; i < totalCadastrados; i++) {
                if(funcs[i].salario > funcs[idMaior].salario) idMaior = i;
            }
            printf("\nMaior salario: %s (R$%.2f)\n", funcs[idMaior].nome, funcs[idMaior].salario);
        }
        else if (opcao == 4) {
            if(totalCadastrados == 0) continue;
            somaSalarios = 0;
            for(int i = 0; i < totalCadastrados; i++) somaSalarios += funcs[i].salario;
            mediaSalarial = somaSalarios / totalCadastrados;
            printf("\nMedia salarial geral: R$%.2f\n", mediaSalarial);
        }
        else if (opcao == 5) {
            if(totalCadastrados == 0) continue;
            somaSalarios = 0;
            for(int i = 0; i < totalCadastrados; i++) somaSalarios += funcs[i].salario;
            mediaSalarial = somaSalarios / totalCadastrados;
            
            printf("\nFuncionarios acima da media (R$%.2f):\n", mediaSalarial);
            for(int i = 0; i < totalCadastrados; i++) {
                if(funcs[i].salario > mediaSalarial) {
                    printf("- %s (R$%.2f)\n", funcs[i].nome, funcs[i].salario);
                }
            }
        }
    } while(opcao != 0);

    return 0;
}