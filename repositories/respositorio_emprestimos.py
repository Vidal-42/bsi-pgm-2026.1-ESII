# Armazenamento dos dados de empréstimos
from repositórios.interfaces import IControleEmprestimos

class GerenciadorEmprestimos(IControleEmprestimos):
    def __init__(self):
        # Dados simulados em memória
        self.lista_equipamentos = [
            {"id": 1, "nome": "Notebook Dell", "categoria": "Notebook", "disponivel": True},
            {"id": 2, "nome": "Projetor Epson", "categoria": "Projetor", "disponivel": True}
        ]
        self.registros_emprestimos = []

    def obter_por_id(self, codigo: int):
        return next(
            (equip for equip in self.lista_equipamentos if equip["id"] == codigo),
            None
        )

    def adicionar_registro(self, item):
        self.registros_emprestimos.append(item)

    def exibir_registros(self):
        return self.registros_emprestimos