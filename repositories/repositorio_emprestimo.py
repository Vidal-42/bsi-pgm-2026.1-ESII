from typing import Optional, List
from models.emprestimo import Emprestimo

class RepositorioEmprestimo:
    def __init__(self):
        self._emprestimos: List[Emprestimo] = []

    def salvar_emprestimo(self, emprestimo: Emprestimo) -> None:
        ...

    def buscar_emprestimo(self, emprestimo_id: int) -> Optional[Emprestimo]:
        ...

    def listar_emprestimos_nao_devolvidos(self) -> List[Emprestimo]:
        ...

    def marcar_devolvido(self, emprestimo_id: int) -> None:
        ...