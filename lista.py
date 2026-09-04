CAPACIDADE_MAXIMA = 5


# ESTRUTURA DE DADOS: FILA CIRCULAR

class Fila:
    def __init__(self, capacidade=CAPACIDADE_MAXIMA):
        self.capacidade = capacidade
        self.itens = [None] * capacidade
        self.inicio = 0
        self.fim = -1
        self.quantidade = 0

    def esta_vazia(self):
        return self.quantidade == 0

    def esta_cheia(self):
        return self.quantidade == self.capacidade

    def enfileirar(self, item):
        """Insere SEMPRE no fim da fila. Retorna False se estiver cheia."""
        if self.esta_cheia():
            return False
        self.fim = (self.fim + 1) % self.capacidade
        self.itens[self.fim] = item
        self.quantidade += 1
        return True

    def desenfileirar(self):
        """Remove SEMPRE do inicio da fila. Retorna None se estiver vazia."""
        if self.esta_vazia():
            return None
        item = self.itens[self.inicio]
        self.itens[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.quantidade -= 1
        return item

    def primeiro(self):
        """Consulta quem esta no inicio sem remover."""
        if self.esta_vazia():
            return None
        return self.itens[self.inicio]

    def listar(self):
        """Retorna os itens na ordem correta de atendimento."""
        resultado = []
        for i in range(self.quantidade):
            indice = (self.inicio + i) % self.capacidade
            resultado.append(self.itens[indice])
        return resultado

    def tamanho(self):
        return self.quantidade


# REGISTRO DE UM DOCUMENTO

class Documento:
    def __init__(self, codigo, nome, dono, paginas):
        self.codigo = codigo
        self.nome = nome
        self.dono = dono
        self.paginas = paginas

    def __str__(self):
        return "#%d | %s | dono: %s | %d pagina(s)" % (
            self.codigo,
            self.nome,
            self.dono,
            self.paginas,
        )


# O SPOOLER DA IMPRESSORA

class Spooler:
    def __init__(self, capacidade=CAPACIDADE_MAXIMA):
        self.fila = Fila(capacidade)
        self.proximo_codigo = 1
        self.total_impresso = 0

    def enviar(self, nome, dono, paginas):
        if self.fila.esta_cheia():
            print("ERRO: fila cheia (%d documentos). Tente mais tarde."
                  % self.fila.capacidade)
            return

        documento = Documento(self.proximo_codigo, nome, dono, paginas)
        self.fila.enfileirar(documento)
        self.proximo_codigo += 1
        print("OK: documento enviado -> %s" % documento)

    def imprimir(self):
        documento = self.fila.desenfileirar()

        if documento is None:
            print("ERRO: nao ha documentos aguardando impressao.")
            return

        print("IMPRIMINDO: %s" % documento)
        print("Impressao concluida.")
        self.total_impresso += 1

    def mostrar_fila(self):
        print("\n" + "-" * 55)
        print("FILA DE IMPRESSAO (%d/%d) | ja impressos: %d"
              % (self.fila.tamanho(), self.fila.capacidade, self.total_impresso))
        print("-" * 55)

        if self.fila.esta_vazia():
            print("(fila vazia)")
        else:
            posicao = 1
            for documento in self.fila.listar():
                marcador = "<== proximo" if posicao == 1 else ""
                print("%do lugar: %s %s" % (posicao, documento, marcador))
                posicao += 1
        print("-" * 55)




def menu():
    print("\n===== SISTEMA DE IMPRESSAO =====")
    print("1 - Enviar documento para a fila")
    print("2 - Imprimir proximo documento")
    print("3 - Consultar proximo da fila")
    print("0 - Sair")


def main():
    spooler = Spooler()

    while True:
        spooler.mostrar_fila()
        menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            nome = input("Nome do arquivo: ")
            dono = input("Nome do usuario: ")
            entrada = input("Numero de paginas: ")
            if entrada.isdigit() and int(entrada) > 0:
                spooler.enviar(nome, dono, int(entrada))
            else:
                print("ERRO: numero de paginas invalido.")

        elif opcao == "2":
            spooler.imprimir()

        elif opcao == "3":
            documento = spooler.fila.primeiro()
            if documento is None:
                print("A fila esta vazia.")
            else:
                print("Proximo a ser impresso: %s" % documento)

        elif opcao == "0":
            print("Encerrando o sistema.")
            break

        else:
            print("ERRO: opcao invalida.")


if __name__ == "__main__":
    main()