# Diagramas – Decomposição em camadas

## Decomposição em camadas

### models/
- **Equipamento** – Localizada em `models/`, pois apresenta alta coesão: sua única responsabilidade é representar os dados de um equipamento (id, nome, tipo, disponível), ocultando seus atributos internos e sem depender de outras camadas.

- **Emprestimo** – Fica em `models/` pela mesma razão: estrutura os dados de um empréstimo (datas, usuário, equipamento) sem conter lógica de negócio, o que mantém o acoplamento baixo e facilita a manutenção.

### services/
- **ServicoEmprestimos** – Pertence a `services/` porque centraliza todas as regras de negócio (registrar empréstimo, processar devolução, calcular multa, listar atrasados), isolando essa lógica da interface e da persistência para que possa ser testada sem dependências externas.

### repositories/
- **RepositorioEquipamentos** – Mora em `repositories/` para ocultar onde os dados estão guardados (se é lista em memória, arquivo ou banco de dados), permitindo trocar a forma de persistência sem afetar os serviços e mantendo baixo acoplamento.
- **RepositorioEmprestimos** – Mesma justificativa: separa a responsabilidade de salvar, buscar e listar empréstimos, garantindo alta coesão e que a lógica de negócio não precise conhecer os detalhes de armazenamento.

### interface/
- **CLI** – Fica em `interface/` porque sua única função é interagir com o usuário pelo terminal (exibir menus, ler opções, mostrar resultados), sem conter nenhuma regra de empréstimo ou cálculo. Isso segue o princípio de separação de responsabilidades.

### main.py
- **main** – Não é uma classe, mas o ponto de entrada do programa. Sua responsabilidade é apenas criar as instâncias necessárias (repositórios, serviços, interface) e ligar tudo, injetando as dependências. Isso mantém o restante do sistema desacoplado e centraliza a configuração.