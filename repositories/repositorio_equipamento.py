from typing import Optional, List
from models.equipamento import Equipamento

class RepositorioEquipamento:
    def __init__(self):
        self._equipamentos: List[Equipamento] = []

    def buscar_equipamento(self, equip_id: int) -> Optional[Equipamento]:
        ...

    def marcar_disponivel(self, equip_id: int) -> None:
        ...

    def marcar_indisponivel(self, equip_id: int) -> None:
        ...