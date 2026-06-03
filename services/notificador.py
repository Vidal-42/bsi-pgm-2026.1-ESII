class SistemaNotificacoes:
    
    def enviar_aviso_emprestimo(self, destinatario: str, prazo_devolucao: str) -> None:
        ...

    def enviar_aviso_devolucao(self, destinatario: str, valor_multa: float) -> None:
        ...

    def enviar_aviso_atraso(self, destinatario: str, dias_atrasados: int, valor_multa: float) -> None:
        ...