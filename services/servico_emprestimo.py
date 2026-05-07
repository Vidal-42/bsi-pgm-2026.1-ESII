from datetime import date
from typing import Optional, List, Tuple
from models.equipamento import Equipamento
from models.emprestimo import Emprestimo
from repositories.repositorio_equipamento import RepositorioEquipamento
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador

class ServicoEmprestimo:
    def __init__(self, repo_equip: RepositorioEquipamento, repo_emp: RepositorioEmprestimo, notificador: Notificador):
        self.repo_equip = repo_equip
        self.repo_emp = repo_emp
        self.notificador = notificador

    def registrar(self, equip_id: int, usuario_nome: str, usuario_email: str, dias: int) -> bool:
        ...

    def devolver(self, emprestimo_id: int) -> Tuple[bool, float]:
        ...

    def listar_atrasados(self) -> List[Tuple[str, int, float]]:
        ...

    def _calcular_atraso(self, data_devolucao: date, hoje: date) -> int:
        ...

    def _calcular_multa(self, tipo: str, dias_atraso: int) -> float:
        ...