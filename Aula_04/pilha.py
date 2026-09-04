CAPACIDADE_MAXIMA = 50

# ESTRUTURA DE DADOS: PILHA

class Pilha:
    def __init__(self, capacidade=CAPACIDADE_MAXIMA):
        self.capacidade = capacidade
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def esta_cheia(self):
        return len(self.itens) == self.capacidade

    def empilhar(self, item):
        """Insere no topo da pilha."""
        if self.esta_cheia():
            # Descarta a acao mais antiga para abrir espaco (historico limitado)
            self.itens.pop(0)
        self.itens.append(item)

    def desempilhar(self):
        """Remove e retorna o item do topo. Retorna None se a pilha estiver vazia."""
        if self.esta_vazia():
            return None
        return self.itens.pop()

    def topo(self):
        """Consulta o item do topo sem remover."""
        if self.esta_vazia():
            return None
        return self.itens[-1]

    def tamanho(self):
        return len(self.itens)



# REGISTRO DE UMA ACAO

class Acao:

    def __init__(self, tipo, posicao, texto_novo="", texto_antigo=""):
        self.tipo = tipo
        self.posicao = posicao
        self.texto_novo = texto_novo
        self.texto_antigo = texto_antigo

    def __str__(self):
        if self.tipo == "digitar":
            return "digitar '%s' na posicao %d" % (self.texto_novo, self.posicao)
        if self.tipo == "apagar":
            return "apagar '%s' da posicao %d" % (self.texto_antigo, self.posicao)
        return "substituir '%s' por '%s' na posicao %d" % (
            self.texto_antigo,
            self.texto_novo,
            self.posicao,
        )



# O EDITOR DE TEXTO

class Editor:
    def __init__(self):
        self.texto = ""
        self.historico = Pilha()

    def digitar(self, novo_texto):
        """Insere texto no final do documento."""
        posicao = len(self.texto)
        self.texto = self.texto + novo_texto
        self.historico.empilhar(Acao("digitar", posicao, texto_novo=novo_texto))
        print("OK: texto inserido.")

    def apagar(self, quantidade):
        """Apaga os ultimos N caracteres do documento."""
        if quantidade <= 0:
            print("ERRO: quantidade invalida.")
            return
        if quantidade > len(self.texto):
            print("ERRO: o texto tem apenas %d caractere(s)." % len(self.texto))
            return

        posicao = len(self.texto) - quantidade
        removido = self.texto[posicao:]          # guarda o que sera perdido
        self.texto = self.texto[:posicao]
        self.historico.empilhar(Acao("apagar", posicao, texto_antigo=removido))
        print("OK: '%s' apagado." % removido)

    def substituir(self, antigo, novo):
        """Substitui a primeira ocorrencia de uma palavra."""
        posicao = self.texto.find(antigo)
        if posicao == -1:
            print("ERRO: '%s' nao encontrado no texto." % antigo)
            return

        fim = posicao + len(antigo)
        self.texto = self.texto[:posicao] + novo + self.texto[fim:]
        self.historico.empilhar(
            Acao("substituir", posicao, texto_novo=novo, texto_antigo=antigo)
        )
        print("OK: '%s' substituido por '%s'." % (antigo, novo))

    def desfazer(self):
        """Remove a acao do topo da pilha e aplica a operacao inversa."""
        acao = self.historico.desempilhar()

        if acao is None:
            print("ERRO: nao ha nada para desfazer (historico vazio).")
            return

        if acao.tipo == "digitar":
            # inverso de inserir = remover
            fim = acao.posicao + len(acao.texto_novo)
            self.texto = self.texto[:acao.posicao] + self.texto[fim:]

        elif acao.tipo == "apagar":
            # inverso de remover = reinserir
            self.texto = (
                self.texto[:acao.posicao]
                + acao.texto_antigo
                + self.texto[acao.posicao:]
            )

        elif acao.tipo == "substituir":
            # inverso de substituir = trocar de volta
            fim = acao.posicao + len(acao.texto_novo)
            self.texto = (
                self.texto[:acao.posicao] + acao.texto_antigo + self.texto[fim:]
            )

        print("DESFEITO: %s" % acao)

    def mostrar_estado(self):
        print("\n" + "-" * 55)
        print("TEXTO ATUAL: [%s]" % self.texto)
        print("Acoes no historico: %d" % self.historico.tamanho())
        proxima = self.historico.topo()
        if proxima is not None:
            print("Proximo desfazer: %s" % proxima)
        print("-" * 55)



# PROGRAMA PRINCIPAL

def menu():
    print("\n===== EDITOR DE TEXTO =====")
    print("1 - Digitar")
    print("2 - Apagar")
    print("3 - Substituir")
    print("4 - Desfazer")
    print("0 - Sair")


def main():
    editor = Editor()

    while True:
        editor.mostrar_estado()
        menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            texto = input("Texto a digitar: ")
            editor.digitar(texto)

        elif opcao == "2":
            entrada = input("Quantos caracteres apagar? ")
            if entrada.isdigit():
                editor.apagar(int(entrada))
            else:
                print("ERRO: digite um numero inteiro.")

        elif opcao == "3":
            antigo = input("Palavra a substituir: ")
            novo = input("Nova palavra: ")
            editor.substituir(antigo, novo)

        elif opcao == "4":
            editor.desfazer()

        elif opcao == "0":
            print("Encerrando o editor.")
            break

        else:
            print("ERRO: opcao invalida.")


if __name__ == "__main__":
    main()
