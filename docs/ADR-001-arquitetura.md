# ADR-001: Escolha da Arquitetura do Sistema de Biblioteca

**Status:** Proposed
**Data:** 2026-05-02

## Contexto

O sistema de gerenciamento de empréstimos (v1.0) foi desenvolvido como um script único (`emprestimos.py`). Com a necessidade de evolução para v2.0, surgiram dois problemas claros:

- Adicionar um novo tipo de equipamento (ex.: tablet) exige abrir o script e modificar múltiplos blocos `if/elif` (dentro de `devolver` e `listar_atrasados`).
- Não é possível testar as regras de negócio (cálculo de multa, devolução) sem depender da data atual do computador, de `print` na tela e de entrada manual do usuário.

Esses problemas violam os requisitos não funcionais RNF03 (manutenibilidade) e RNF04 (testabilidade) definidos no `docs/requisitos.md`.

## Opções consideradas 
| Estilo | Atende RNF03? | Atende RNF04? | Adequado para CLI? | Familiar para iniciantes? | Decisão |
|--------|--------------|--------------|--------------------|--------------------------|----------|
| Arquivo único | Não - Toda a estrutura do código está misturada | Não - seria dependente de variaveis, funções globais, data atual e print | Sim - sistema simples, próprio para aprendizagem | Sim - funciona bem em terminal | Descartado |
| Em camadas | Sim - responsabilidades separadas em módulos distintos | Sim - regras isoladas, testáveis comdata injetada e sem print | Sim - funciona bem em terminal | Média | Escolhido |
| MVC | Sim - separação cara entre Model, View e Controller | Sim - regras no Model, testável | Não - foi criado para interfaces gráficas, gera complexidade desnecessária no terminal | Baixo - Complexidade amior para iniciantes | Descartado |

- **Arquivo único:** descartado — os dois problemas persistem (mesmo código precisa ser alterado em dois lugares; regras acopladas à data atual e à saída no console).
- **MVC:** descartado — adequado para interfaces gráficas; o sistema usa CLI (terminal) e não justifica a separação View/Controller, adicionando complexidade desnecessária para a equipe iniciante.
- **Em camadas:** resolve os dois problemas com complexidade proporcional ao tamanho da equipe (estudantes em disciplina de graduação).

## Decisão

| Diretório| Responsabilidade |
|-------|------------------|
| `models/` | Representação dos dados: classes `Equipamento`, `Emprestimo`. Apenas atributos e métodos internos (sem regras de negócio complexas). |
| `services/` | Regras de negócio: cálculo de multa, registro de empréstimo, devolução. Isolado de interface, persistência e notificação. |
| `repository/` | Acesso a dados: operações de buscar, salvar, listar equipamentos e empréstimos (inicialmente em memória). |
| `interface/` | Interface com o usuário (CLI): menus, entrada/saída de texto. Não contém regras de negócio. |
| `main.py` | Ponto de entrada: cria instâncias (repository, services, interface) e inicia o programa. |

## Consequências

- **Adicionar novo tipo de equipamento** = criar uma nova classe em `models/` (ex.: `Tablet`) e, se necessário, ajustar a lógica de multa em `services/` – sem modificar `interface/` ou `repository/`.

- **Testabilidade** – as regras de negócio em `services/` podem ser testadas com data fixa (passada por parâmetro), utilizando um `repository` falso (em memória) e sem dependência de `print` ou entrada do usuário.

- **Troca de notificação** (e-mail → SMS) – como a notificação está dentro de `services/` (por simplicidade), a mudança exigirá alteração apenas nessa camada. Caso no futuro queira desacoplar totalmente, pode-se extrair para um módulo separado.

- **Persistência** – se for necessário trocar de listas em memória para arquivo ou banco de dados, as mudanças ficam isoladas em `repository/`.

- **Interface** – o menu em `interface/` pode ser substituído por outro tipo de interface (ex.: API web) sem afetar `services/` ou `repository/`.

- O código original `emprestimos.py` permanece intacto como referência durante a refatoração.