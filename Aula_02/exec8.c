#include <stdio.h>

struct Produto {
char nome[50];
int codigo;
float preco;
int quantidade;
};

int main() {
struct Produto produtos[5];
float maiorValorEstoque = -1;
int idMaiorEstoque = 0;

// Cadastro de produtos
printf("--- Cadastro de Produtos ---\n");
for(int i = 0; i < 5; i++) {
    printf("\nProduto %d:\n", i + 1);
    printf("Nome: ");
    scanf(" %[^\n]", produtos[i].nome); // O espaço antes de % resolve problemas do buffer do scanf
    printf("Codigo: ");
    scanf("%d", &produtos[i].codigo);
    printf("Preco Unitario: ");
    scanf("%f", &produtos[i].preco);
    printf("Quantidade em Estoque: ");
    scanf("%d", &produtos[i].quantidade);
}

printf("\n--- Relatorio de Estoque ---\n");
for(int i = 0; i < 5; i++) {
    float valorTotal = produtos[i].preco * produtos[i].quantidade;
    
    printf("Produto: %s | Cod: %d | Estoque Total: R$ %.2f\n", 
           produtos[i].nome, produtos[i].codigo, valorTotal);

    // Verifica se é o maior valor em estoque
    if(valorTotal > maiorValorEstoque) {
        maiorValorEstoque = valorTotal;
        idMaiorEstoque = i;
    }
}

printf("\nProduto com MAIOR valor em estoque: %s (R$ %.2f)\n", 
       produtos[idMaiorEstoque].nome, maiorValorEstoque);

return 0;


}