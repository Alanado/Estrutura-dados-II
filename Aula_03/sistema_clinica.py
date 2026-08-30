# ==============================================================================
# ESTRUTURA DE DADOS II - AULA 03
# Sistema de Fila Dinâmica para Clínica (com regra de prioridade)
# ==============================================================================

class Paciente:
    """Classe responsável por armazenar as informações de cada paciente."""
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        # Define se é prioritário com base na idade (Desafio da aula)
        self.eh_prioritario = idade >= 60

    def __repr__(self):
        status = "PRIORITÁRIO" if self.eh_prioritario else "NORMAL"
        return f"[{self.nome}, {self.idade} anos - {status}]"


class Node:
    """A estrutura básica de um Nó dinâmico contendo o dado e a referência do próximo."""
    def __init__(self, paciente: Paciente):
        self.dado = paciente
        self.proximo = None


class FilaClinica:
    """Gerenciador da Fila de Pacientes."""
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        """Verifica se a fila possui pacientes."""
        return self.inicio is None

    def adicionar(self, nome: str, idade: int):
        """
        Adiciona um paciente respeitando as regras de prioridade:
        - Prioritários entram antes dos normais, respeitando a ordem de chegada.
        """
        novo_paciente = Paciente(nome, idade)
        novo_no = Node(novo_paciente)

        # Caso 1: Fila vazia
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
            self._tamanho += 1
            print(f"-> Paciente {novo_paciente.nome} adicionado como o primeiro da fila.")
            return

        # Caso 2: Paciente é prioritário
        if novo_paciente.eh_prioritario:
            # Se o primeiro já é normal, o prioritário entra no início absoluto
            if not self.inicio.dado.eh_prioritario:
                novo_no.proximo = self.inicio
                self.inicio = novo_no
            else:
                # Percorre para encontrar o último prioritário na fila
                atual = self.inicio
                while atual.proximo is not None and atual.proximo.dado.eh_prioritario:
                    atual = atual.proximo

                # Encaixa o nó prioritário logo após o último prioritário encontrado
                novo_no.proximo = atual.proximo
                atual.proximo = novo_no

                # Atualiza o fim se inseriu na última posição
                if novo_no.proximo is None:
                    self.fim = novo_no

        # Caso 3: Paciente Normal (Sempre no final)
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

        self._tamanho += 1
        print(f"-> Paciente {novo_paciente.nome} ({novo_paciente.idade} anos) adicionado à fila.")

    def atender(self):
        """Remove e retorna o primeiro paciente da fila."""
        if self.esta_vazia():
            print("\n⚠️ A fila está vazia! Nenhum paciente para atender.")
            return None

        paciente_atendido = self.inicio.dado
        self.inicio = self.inicio.proximo
        self._tamanho -= 1

        if self.inicio is None:
            self.fim = None

        print(f"\n✅ Atendendo: {paciente_atendido.nome}")
        return paciente_atendido

    def listar_espera(self):
        """Exibe todos os pacientes aguardando (Evita laço infinito atualizando o ponteiro)."""
        print("\n--- 📋 FILA DE ESPERA ATUAL ---")
        if self.esta_vazia():
            print("Nenhum paciente aguardando.")
            print("-------------------------------\n")
            return

        atual = self.inicio
        posicao = 1

        while atual is not None:
            print(f"{posicao}º -> {atual.dado}")
            atual = atual.proximo # Correção do laço infinito ensinada na aula
            posicao += 1
        print(f"Total na fila: {self._tamanho}")
        print("-------------------------------\n")


# === TESTANDO O SISTEMA (Main) ===
if __name__ == "__main__":
    clinica = FilaClinica()

    print("=== 1. CHEGADA DE PACIENTES ===")
    clinica.adicionar("Ana", 32)      # Normal
    clinica.adicionar("Bruno", 70)    # Prioritário (Vai p/ frente)
    clinica.adicionar("Carlos", 45)   # Normal
    clinica.adicionar("Dona Benta", 80) # Prioritário (Fica atrás do Bruno, mas antes dos normais)
    
    clinica.listar_espera()

    print("=== 2. ATENDIMENTOS ===")
    clinica.atender() # Atende Bruno
    clinica.atender() # Atende Dona Benta
    
    clinica.listar_espera()