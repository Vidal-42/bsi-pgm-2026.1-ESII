from abc import ABC, abstractmethod

class IControleEmprestimos(ABC):

    @abstractmethod
    def obter_equipamento(self, codigo: int):
        pass

    @abstractmethod
    def registrar_emprestimo(self, emprestimo) -> None:
        pass

    @abstractmethod
    def obter_emprestimo(self, codigo: int):
        pass

    @abstractmethod
    def definir_indisponivel(self, equipamento_id: int) -> None:
        pass

    @abstractmethod
    def definir_disponivel(self, equipamento_id: int) -> None:
        pass

    @abstractmethod
    def registrar_devolucao(self, emprestimo_id: int) -> None:
        pass

    @abstractmethod
    def consultar_atrasados(self) -> list:
        pass

    @abstractmethod
    def gerar_id_emprestimo(self) -> int:
        pass