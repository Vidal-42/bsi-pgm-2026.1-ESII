# Diagramas – Decomposição em camadas

## Decomposição em camadas

## Decomposição em camadas

### models/
- **Equipamento** – Alta coesão: representa exclusivamente os dados de um equipamento, ocultando seus atributos internos e sem dependências externas.
- **Emprestimo** – Mesmo princípio: estrutura os dados do empréstimo (datas, usuário, equipamento) sem conter lógica de negócio, facilitando a manutenção.

### services/
- **ServicoEmprestimo** – Centraliza todas as regras de negócio (registrar, devolver, calcular multa, listar atrasados). Isola essas regras da interface e da persistência, permitindo testes sem dependências externas. Baixo acoplamento porque depende apenas de interfaces de repositórios e do notificador.
- **Notificador** – Responsabilidade única: enviar mensagens (e-mail) para os usuários. Ao separar esta classe, aumentamos a coesão do sistema e reduzimos o acoplamento do serviço principal.

### repositories/
- **RepositorioEquipamento** – Oculta onde os dados dos equipamentos estão armazenados (lista, arquivo, banco). Qualquer mudança na persistência fica confinada a esta classe, sem afetar os serviços.
- **RepositorioEmprestimo** – Mesma justificativa para empréstimos. Ambos repositórios garantem baixo acoplamento com a lógica de negócio.

### main.py
- **main (função principal)** – Ponto de entrada do programa. Não é uma classe, mas atua como orquestrador: cria instâncias dos repositórios, do notificador e do serviço, injeta as dependências e executa o menu CLI. Sua coesão é propositalmente baixa, pois apenas configura o sistema, separando essa responsabilidade das demais camadas.

# Diagramas de Sequência

```mermaid 
sequenceDiagram 
actor Atendente 
participant main as main.py 
participant servico as ServicoEmprestimo 
participant repo as RepositorioEmprestimo 
participant notif as Notificador 
Atendente->>main: informa equip_id, nome, email, dias 
main->>servico: registrar(equip_id, nome, email, dias) 
servico->>repo: buscar_equipamento(equip_id) 
repo-->>servico: Equipamento 
alt equipamento disponível 
servico->>repo: salvar_emprestimo(emprestimo) 
servico->>repo: marcar_indisponivel(equip_id) 
servico->>notif: notificar_emprestimo(email, data_devolucao) 
servico-->>main: True 
else equipamento indisponível 
servico-->>main: False 
end 
``` 

## Diagrama Mermaid para UC02
![Imagem do Diagrama UC02](../docs/imagens/Diagrama_2.png)


## Diagrama Mermaid para UC03
![Imagem do Diagrama UC03](../docs/imagens/Diagrama_3.png)