from dataclasses import dataclass

@dataclass
class Equipamento:
    id: int
    nome: str
    tipo: str       # "notebook", "projetor", "cabo", etc.
    disponivel: bool = True